import pyodbc

server = 'localhost'
database = 'Hospital'
username = 'sa'
password = 'Password01.'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

cursor.execute('SELECT * FROM TipoExame')

for i in cursor:
    print(i)