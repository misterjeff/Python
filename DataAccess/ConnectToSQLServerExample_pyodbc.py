import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
		      'Server=EODB;'
		      'Database=ERM;'
		      'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('SELECT TOP 100 * FROM FrontOffice.TradeLog;')

for row in cursor:
    print(row)
