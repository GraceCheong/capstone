# DB 연결 및 관리 함수
import sys, os
import pymysql

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from app.initDB import initDB
from app.dbInfo import dbInfo

def getDBdata():

    count:int = 0

    dblist = initDB()

    for db in dblist :
        now = dblist[count]
        count += 1
        if (now.name == 'capstonedb') :
            return now.Init()



hostdb = getDBdata()

conn = pymysql.connect(host=hostdb.host, port=3306, user=hostdb.user, password=hostdb.pw, db=hostdb.name)
#host = DB주소(localhost 또는 ip주소), user = DB id, password = DB password, db = DB명
curs = conn.cursor()

sql = "SELECT * FROM main" # 실행 할 쿼리문 입력
curs.execute(sql) # 쿼리문 실행


