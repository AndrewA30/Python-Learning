import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=ssg-oldbinusmaya.binus.db;"
                        "Database=LMS_DB;"
                        "uid=danielwail;pwd=12345678")

cursor = cnxn.cursor()
cursor.execute('SELECT * FROM MsOnsiteRegistrationDate')

for row in cursor:
    print('row = %r' % (row,))