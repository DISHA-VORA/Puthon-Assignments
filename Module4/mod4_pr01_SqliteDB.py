import sqlite3


try:
    con=sqlite3.connect("StdDb.db")
except Exception as e:
    print(e)

blntblcre=False
try:
    tblCre="create table stdReg(Regid integer primary key autoincrement,name text,city text)"
    con.execute(tblCre)
    blntblcre=True
except Exception as e:
    print(e)

try:
    if blntblcre:
        for ind in range(0,5):
            name=input(f"Enter Student {ind+1} Name:")
            city=input(f"Enter Student {ind+1} City:")

            insert_qry="insert into stdReg(name,city) values('" + name + "','"+city+"')"
            con.execute(insert_qry)
            con.commit()
except Exception as e:
    print(e)

cur=con.cursor()
try:
    sel_qry="SELECT * FROM stdreg ORDER BY NAME"
    cur.execute(sel_qry)
    stdlist=cur.fetchall()

    for i in stdlist:
        print(f"id:{i[0]} | Name:{i[1]}  | City:{i[2]}")

except Exception as e:
    print(e)

try:
    upd_qry="UPDATE STDREG SET NAME='AakashBhai' where name='AAkash'"
    con.execute(upd_qry)
    con.commit()
except Exception as e:
    print(e)

try:
    del_qry="DELETE FROM STDREG WHERE NAME='AakashBhai'"
    con.execute(del_qry)
    con.commit()
except Exception as e:
    print(e)

try:
    altQry="ALTER TABLE STDREG ADD COLUMN lastname TEXT"
    con.execute(del_qry)
    con.commit()
except Exception as e:
    print(e)