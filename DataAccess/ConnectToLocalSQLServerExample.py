import pyodbc

conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
		      'Server=(LocalDB)\\v11.0;'
		      'Database=Sandbox;'
		      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('SELECT TOP 100 * FROM [Sandbox].[dbo].[StackDetailExample];')

for row in cursor:
    print(row)
