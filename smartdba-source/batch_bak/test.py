import pymysql
from pprint import pprint
from collections import defaultdict


def makeDictFactory(cursor):
    columnNames = [d[0] for d in cursor.description]

    def createRow(*args):
        return dict(zip(columnNames, args))

    return createRow



 
# MySQL Connection 연결
conn = pymysql.connect(host='10.52.124.77', user='root', password='Gs#ora!@34',
                       db='smartdba', charset='utf8')
 
# Connection 으로부터 Cursor 생성
cursor = conn.cursor()


sql = """
SELECT B.TABLE_NAME, C.COLUMN_NAME
FROM CUST_DB_LIST A,
     CUST_TABLE_LIST B,
     CUST_COLUMN_LIST C,
     CUST_DOMAIN_LIST D
WHERE A.ID = B.ID_DBLIST
  AND B.ID = C.ID_TABLELIST
  AND D.ID = B.ID_DOMAINLIST
  AND D.DOMAIN_NAME = '상품'
  -- AND B.data_search_psbl_yn = 1
  AND B.TABLE_NAME IN ('PRD_ATTR_PRD_M','PRD_BRAND_M');     
"""

cursor.execute(sql)
dataset = cursor.fetchall()

dataset_dict = defaultdict(list) 

for key, val in dataset: 
    dataset_dict[key].append(val) 	
  
print(dataset)
print(dataset_dict) 