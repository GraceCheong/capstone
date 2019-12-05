# DB 연결 및 관리 함수
import sys, os
import pymysql

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)



# returns DB data
def getDBdata():

    count:int = 0
    dblist = initDB()
    #print(dblist[0].name)

    for now in dblist :
        count += 1
        if (now.name == 'capstonedb') :
            #print(now.name)
            return now

# return pymysql.connect
def connect_to_DB():
    hostdb: dbInfo = getDBdata()
    conn = pymysql.connect(host=hostdb.host, port=3306, user=hostdb.user, password=hostdb.pw, db='wine_db')
    # host = DB주소(localhost 또는 ip주소), user = DB id, password = DB password, db = DB명

    return conn


# insert wine data to database table
def insert_wine(name:str):
    try:
        id = check_count('wine') + 1

        conn = connect_to_DB()
        curs = conn.cursor()

        sql = """INSERT INTO main(id, wine_name) 
        VALUES(%s, %s)"""
        curs.execute(sql, (id, name))
        conn.commit()
        check_main()

        conn.close()
    except Exception as e:
        print(e)

    return


# insert review data to database table
def insert_rev(wine_id, review):
    conn = connect_to_DB()
    curs = conn.cursor()

    review_id = check_count('rev') + 1

    try:
        sql = """INSERT INTO review(review_id, wine_id, review) 
            VALUES(%s, %s, %s)"""
        curs.execute(sql, (review_id, wine_id, review))
        conn.commit()
        check_rev()

        conn.close()

    except Exception as e:
        print(e)

    return

# search specific wine id
def select_wine(wine:str):
    conn = connect_to_DB()
    curs = conn.cursor()

    sql = "SELECT id FROM main WHERE wine_name = '{}'".format(wine)  # 실행 할 쿼리문 입력
    curs.execute(sql)  # 쿼리문 실행

    result = curs.fetchall()
    for item in result:
        id = item[0]
        print(id)

    conn.close()
    return id



# search specific review of wine by id
def select_rev(wine_id:int):
    conn = connect_to_DB()
    curs = conn.cursor()

    sql = "SELECT review FROM review WHERE wine_id = '{}'".format(wine_id)  # 실행 할 쿼리문 입력
    curs.execute(sql)  # 쿼리문 실행

    result = curs.fetchall()
    for item in result:
        id = item[0]
        print(id)

    conn.close()
    return id


#
def check_count(type:str):

    conn = connect_to_DB()
    curs = conn.cursor()

    if(type == "wine"):
        sql = "SELECT COUNT(*) as cnt FROM main"  # 실행 할 쿼리문 입력
        curs.execute(sql)  # 쿼리문 실행

        res = curs.fetchall()
        count = res[0][0]
        print(count)
    elif (type == 'rev'):
        sql = "SELECT COUNT(*) as cnt FROM review"  # 실행 할 쿼리문 입력
        curs.execute(sql)  # 쿼리문 실행

        res = curs.fetchall()
        count = res[0][0]
        print(count)

    conn.close()

    return count

# check main table
def check_main():
    conn = connect_to_DB()
    curs = conn.cursor()

    sql = "SELECT * FROM main" # 실행 할 쿼리문 입력
    curs.execute(sql)  # 쿼리문 실행

    rows = curs.fetchall()
    print(rows)

    conn.close()
    return

def check_rev():
    conn = connect_to_DB()
    curs = conn.cursor()

    sql = "SELECT * FROM review" # 실행 할 쿼리문 입력
    curs.execute(sql)  # 쿼리문 실행

    rows = curs.fetchall()
    print(rows)

    conn.close()
    return

'''c = check_count('wine')+1
insert_wine(id=c, name='wine{}'.format(c))'''

'''rc = check_count('rev')+1
insert_rev(review_id=rc, wine_id=3, review="best wine ever {}".format(rc))'''
