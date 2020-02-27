from tkinter import *
import pyodbc

window = Tk()
window.title("Tkinter Example")
window.geometry("420x360")
headerLbl = Label(window, text="Enter SQL Server info below and click 'Run' to get back the top 10 rows.")
serverLbl = Label(window, text="Server Name: ")
serverTxt = Entry(window, width=24)
databaseLbl = Label(window, text="Database Name: ")
databaseTxt = Entry(window, width=24)
tableLbl = Label(window, text="Table Name: ")
tableTxt = Entry(window, width=24)
resultsLbl = Label(window, text="")

def execQuery():
    srv = serverTxt.get()
    db = databaseTxt.get()
    tbl = tableTxt.get()
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=' + srv + ';'
                          'Database=' + db + ';'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    queryStr = "SELECT TOP 10 * FROM " + tbl + ";"
    results = cursor.execute(queryStr).fetchall()
    resultsLbl.configure(text=results)

runBtn = Button(window, text="Run", command=execQuery)

headerLbl.grid(column=0, row=0)
serverLbl.grid(column=0, row=1)
serverTxt.grid(column=1, row=1)
databaseLbl.grid(column=0, row=2)
databaseTxt.grid(column=1, row=2)
tableLbl.grid(column=0, row=3)
tableTxt.grid(column=1, row=3)
runBtn.grid(column=0, row=4)
resultsLbl.grid(column=0, row=6)

window.mainloop()
