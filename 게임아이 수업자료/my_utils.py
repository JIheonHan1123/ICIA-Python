import cx_Oracle
import pandas as pd
import requests

seoul_api_key = '78654862626d6f7436394273514669'

dsn = cx_Oracle.makedsn( '192.168.0.230', 1521, 'xe')


def df_creater(url):
    url = url.replace('(인증키)', seoul_api_key).replace('xml', 'json')
    res = requests.get(url).json()
    key = list(res.keys())[0]
    data = res[key]['row']
    df = pd.DataFrame(data)
    return df


def db_open():
    global db  # 전역변수로 설정하면 같은 파일 내에서 다 쓸 수 있다
    global cursor
    db = cx_Oracle.connect(user='c##finalproject', password='1234', dsn=dsn)
    cursor = db.cursor()


def sql_execute(query):
    global db
    global cursor

    try:
        # select일 경우에만 -> pd.read_sql
        # 나머지는          -> cursor.excute
        if 'select' in query or 'SELECT' in query:
            df = pd.read_sql(sql=query, con=db)
            return df  # 함수는 return이 되면 그 함수가 끝나버림
        # 그래서 이 뒤에 else를 쓸 필요가 없다
        cursor.execute(query)
        print('oracle 쿼리 성공')
    except Exception as e:  # 모든 에러에 대해서 출력
        print(e)


def db_close():
    global db
    global cursor

    try:
        db.commit()
        cursor.close()
        db.close()
        print('오라클 정상적으로 닫힘')
    except Exception as e:
        print(e)
