import pymysql

try:
    con=pymysql.connect(host='localhost',user='root',password='',database='stdDb')
except Exception as e:
    print(e)

cr= con.cursor()

blntblcre=False
try:
    tblCre="create table stdReg(Regid integer primary key auto_increment,name text,city text)"
    cr.execute(tblCre)
    blntblcre=True
except Exception as e:
    print(e)

try:
    if blntblcre:
        for ind in range(0,5):
            name=input(f"Enter Student {ind+1} Name:")
            city=input(f"Enter Student {ind+1} City:")

            insert_qry="insert into stdReg(name,city) values('" + name + "','"+city+"')"
            cr.execute(insert_qry)
            con.commit()
except Exception as e:
    print(e)

try:
    sel_qry="SELECT * FROM stdreg ORDER BY NAME"
    cr.execute(sel_qry)
    stdlist=cr.fetchall()

    for i in stdlist:
        print(f"id:{i[0]} | Name:{i[1]}  | City:{i[2]}")

except Exception as e:
    print(e)

try:
    upd_qry="UPDATE STDREG SET NAME='Jalpeshbhai' where name='Jalpesh'"
    cr.execute(upd_qry)
    con.commit()
except Exception as e:
    print(e)

try:
    del_qry="DELETE FROM STDREG WHERE NAME='JalpeshBhai'"
    cr.execute(del_qry)
    con.commit()
except Exception as e:
    print(e)

try:
    altQry="ALTER TABLE STDREG ADD COLUMN lastname TEXT"
    cr.execute(del_qry)
    con.commit()
except Exception as e:
    print(e)

