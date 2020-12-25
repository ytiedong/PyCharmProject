import pyodbc
import ibm_db


def as400connection():
    connectionAAA = pyodbc.connect(
        driver='{iSeries Access ODBC Driver}',
        system='192.168.0.5',
        uid='YANG',
        pwd='YANG')
    c1 = connectionAAA.cursor()

    return c1


def db2connection():
    # connectionBBB = pyodbc.connect('DSN=SOO;UID=db2adminyang;PWD=Alan5799')
    # connectionBBB = pyodbc.connect('DSN = SO;UID = db2adminyang;PWD = Alan5799')

    # connectionBBB = pyodbc.connect('Provider=IBMOLEDB.DB2COPY1;Info=TRUE;ID=db2adminyang;Password=Alan5799;Source = SOGDB')

    # connectionBBB = pyodbc.connect('DRIVER={IBM DB2 ODBC DRIVER - DB2COPY1};SERVER=127.0.0.0;DATABASE=SOGDB;UID=db2adminyang;PWD=Alan5799')

    # connectionBBB = pyodbc.connect(
    #     DRIVER='{ODBC}',
    #     server='localhost',
    #     DATABASE='SOO',
    #     uid='db2adminyang',
    #     pwd='Alan5799')


    conn = ibm_db.pconnect(
        "DATABASE=SOGDB;HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;UID=db2adminyang;PWD=Alan5799", "", "")
    sql = "SELECT * from DB2ADMINYANG.MST_CUSTOMER"
    stmt = ibm_db.exec_immediate(conn, sql)
    c2 = ibm_db.fetch_both(stmt)
    # while dictionary != False:
    #     print
    #     "The ID is : ", dictionary["EMPNO"]
    #     print
    #     "The Name is : ", dictionary[1]
    #     dictionary = ibm_db.fetch_both(stmt)


    # c2 = connectionBBB.cursor()

    return c2
