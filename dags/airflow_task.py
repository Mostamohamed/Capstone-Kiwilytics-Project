from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
from airflow.hooks.postgres_hook import PostgresHook
import pandas as pd
from matplotlib import pyplot as plt


PG_CONN_ID='postgres_conn'

default_args = {
    'owner':'mostafa',
    'retries' : 1,
    'retry_delay': timedelta(minutes=2),
}
#task 1 Get date
def fetch_order_data():
    hook=PostgresHook(postgres_conn_id=PG_CONN_ID)
    conn=hook.get_conn()

    query= '''
        SELECT 
            o.OrderDate::date AS sales_date,
            od.ProductID,
            p.ProductName,
            od.Quantity,
            p.Price
        FROM orders o
        JOIN order_details od on o.OrderID =od.OrderID
        JOIN products p on od.ProductID =p.ProductID
    '''

    df=pd.read_sql(query,conn)
    df.to_csv('/home/kiwilytics/mostafa/daily_sales_data.csv',index=False)



#task 2 process total daily revenue

def process_daily_revenue():
    df=pd.read_csv('/home/kiwilytics/mostafa/daily_sales_data.csv')
    df['total_revenue']=df['quantity'] * df['price']

    revenue_per_day=df.groupby('sales_date').agg(total_revenue=('total_revenue','sum')).reset_index()
    revenue_per_day.to_csv('/home/kiwilytics/mostafa/daily_revenue.csv',index=False)


#task 3 visualization
def visualization():
    df=pd.read_csv('/home/kiwilytics/mostafa/daily_revenue.csv')
    df['sales_date']=pd.to_datetime(df['sales_date'])

    output_path = '/home/kiwilytics/mostafa/daily_revenue_plot.png'

    plt.figure(figsize=(12,6))
    plt.plot(df['sales_date'],df['total_revenue'],marker='o',linestyle='-')
    plt.title("Daily total Sales Revenue")
    plt.xlabel('Date')
    plt.ylabel('Total Revenue')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()
    print(f"Revenue chart saved to {output_path}")


#define DAG
with DAG(
    dag_id='daily_revenue_sales_analysis',
    default_args=default_args,
    start_date=days_ago(1),
    schedule_interval='@daily',
    catchup=False,
    description='compute and vis daily revenue using pandas and matplotlib in airflow'
) as dag:
    task_fetch_data = PythonOperator(
        task_id='fetch_order_data',
        python_callable=fetch_order_data
    )

    task_process_revenue = PythonOperator(
        task_id='process_daily_revenue',
        python_callable=process_daily_revenue
    )

    task_plot_revenue = PythonOperator(
        task_id='plot_daily_revenue',
        python_callable=visualization
    )


    task_fetch_data >> task_process_revenue >> task_plot_revenue




