import pyodbc 
from pandas import DataFrame

#print(pyodbc.drivers())


# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server   = "WECTOADB01"
database = "FIDATAMART"
username = 'sys_DB20_rpa' 
password = 'Edw!20220617+Oe' 
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};;TrustServerCertificate=yes;SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()


SQL = """
       select  Fin_Statements_TYPE , Quarter_Month , count(*) As CNT
         from tblFinancial_Statements_All
        Where  Fin_Statements_TYPE in ('Revenue_US','IS_US' , 'BS_US' , 'CF_US' )
        group by Fin_Statements_TYPE,Quarter_Month
      """


#Sample select query
cursor.execute(SQL) 
row = cursor.fetchone() 

#columns = [column[0] for column in cursor.description]

#print(columns)

#for colname in cursor.description:
#    print(colname[0])

for row in cursor:
   print(row[0] + "  "+ row[1]  + "  "+  str(row[2])  )

#while row: 
#    print(row["Fin_Statements_TYPE"] + "  "+ row["Quarter_Month"]  + "  "+  row["CNT"]  )
#    row = cursor.fetchone()