import pyodbc

server = 'localhost'
database = 'Hospital'
username = 'sa'
password = 'Password01.'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

count = cursor.execute("""
UPDATE TipoExame SET Nome = ?, Descricao = ? WHERE Id = 2002""",
'Feminino2', 'Exames femininos2.').rowcount

conn.commit()
print(f'Rows updated: {count}')
