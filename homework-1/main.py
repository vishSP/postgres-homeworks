"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

customers_row = []
employees_row = []
orders_row = []

with open('north_data/customers_data.csv') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for row in csv_reader:
        customer_id, company_name, contact_name = row
        customers_row.append(row)

with open('north_data/employees_data.csv') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for row in csv_reader:
        first_name, last_name, title, birth_date, notes = row
        employees_row.append(row)

with open('north_data/orders_data.csv') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for row in csv_reader:
        order_id, customer_id, employee_id, order_date, ship_city = row
        orders_row.append(row)

with psycopg2.connect(host='localhost', database='north', user='postgres', password='1620') as conn:
    with conn.cursor() as cur:
        for employee in employees_row:
            cur.execute('INSERT INTO employees (last_name, first_name, title , birth_date ,notes)'
                        'VALUES (%s, %s, %s, %s, %s)', employee)
            conn.commit()
        for customer in customers_row:
            cur.execute("INSERT INTO customers VALUES (%s,%s,%s)", customer)
            conn.commit()

        for order in orders_row:
            cur.execute("INSERT INTO orders VALUES (%s,%s,%s,%s,%s)", order)

conn.close()
