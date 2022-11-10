import pymysql
import os

db = pymysql.connect(
        host='localhost',
        user='root',
        password='123456789',
        port=3306,
        db='z_lib_new'
    )

cur = db.cursor()

files = os.listdir('.')
for filename in files:
    portion = os.path.splitext(filename)

    if portion[1] != ".py":
        cur.execute("SELECT extension FROM books WHERE zlibrary_id = " + portion[0])
        res = cur.fetchone()[0]
        print(res)
        newname = portion[0] + "." + res  
        os.rename(filename,newname)