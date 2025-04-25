# -*- coding: utf-8 -*-

import pymysql   # 導入python鏈接mysql的包
from tabulate import tabulate
from pymysql.cursors import DictCursor


conn = None
cursor = None

try:
    # 創建python與mysql的鏈接
    conn = pymysql.connect(
        host="localhost",   # 主機名稱
        user="root",        # mysql的用戶名
        password="666666",  # mysql的root用戶密碼
        database="world",   # 指定連接的數據庫
        charset="utf8mb4"   # 設定編碼，以免錯誤和亂碼
    )

    # 創建游標
    # cursor = conn.cursor()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    print("\n顯示所有的數據庫：")
    # 需要執行的sql命令
    cursor.execute("show databases;")
    # 通過db遍歷cursor.fetchall()獲取的數據
    for db in cursor.fetchall():    # fetchall獲取所有的數據，返回的是一個二級元組列表
        # print(f" - {db[0]}")                # 通過索引獲取數據庫并且輸出
        print(f" - {db['Database']}")

    print("\n查詢world中的所有表：")
    cursor.execute("show tables;")
    for tables in cursor.fetchall():
        # print(f" - {tables[0]}")
        print(f"  - {tables['Tables_in_world']}")

    print("\n查詢country中的field：")
    # cursor.execute("select * from country limit 3;")
    # for fields in cursor.fetchall():
    #     print(f" - {fields}")
    #     print(fields["Name"], fields["Region"])
    cursor.execute("select Name, Region from country limit 3;")
    rows = cursor.fetchall()
    print(tabulate(rows, headers="keys", tablefmt="pretty"))

except pymysql.MySQLError as err:
    print(f"鏈接mysql或者查詢發生錯誤：{err}")

finally:
    if cursor:
        cursor.close()  # 關閉游標cursor
    if conn:
        conn.close()    # 關閉鏈接conn
