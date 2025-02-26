import pandas as pd
import mysql.connector


excel_file = "Emp_data.xlsx"
sheet_name = "Sheet1"     
df = pd.read_excel(excel_file, sheet_name=sheet_name)


df = df.where(pd.notnull(df), None)


db_config = {
    "host": "localhost",
    "user": "dev_root_user_daemon",
    "password": "dev_root_password_daemon",
    "database": "timesheet_master_database_development",
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()


table_name = "employees"


insert_query = f"""
INSERT INTO {table_name} (employee_id, employee_name, employee_department, employee_job_title, employee_branch)
VALUES (%s, %s, %s, %s, %s);
"""


data_to_insert = [tuple(row) for row in df.to_numpy()]


cursor.executemany(insert_query, data_to_insert)


connection.commit()


cursor.close()
connection.close()

print("Data imported successfully!")