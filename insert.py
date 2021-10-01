import pyodbc

server = 'localhost'
database = 'Hospital'
username = 'sa'
password = 'Password01.'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

count = cursor.execute("""
INSERT INTO TipoExame (Nome, Descricao) 
VALUES (?,?)""",
'Feminino', 'Exames femininos.').rowcount

conn.commit()
print(f'Rows inserted: {count}')
