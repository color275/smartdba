import pymysql


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
SELECT ID id, TABLE_NAME table_name
FROM CUST_TABLE_LIST
WHERE 1=1
-- AND DATA_SEARCH_PSBL_YN = 1
-- AND TABLE_NAME = 'STG_PRD_PRD_M'
AND ID IN 
(
96250,
96256,
96258,
96424,
178189
)
"""

cursor.execute(sql)

columnNames = [d[0] for d in cursor.description]
dataset_target = [dict(zip(columnNames, row)) for row in cursor]


for target in dataset_target :

	sql = """
	SELECT sql_exp_column,
	       pk_column,
	       id_tablelist_parent_table
	FROM CUST_TABLE_LIST B
	          INNER JOIN CUST_DB_LIST A
	          ON A.ID = B.ID_DBLIST
	WHERE B.ID = {id}
	""".format(id=target['id'])

	cursor.execute(sql)

	columnNames = [d[0] for d in cursor.description]
	dataset = [dict(zip(columnNames, row)) for row in cursor]
	# print(dataset)

	str_sql_exp_column = dataset[0]['sql_exp_column']
	str_pk_column = dataset[0]['pk_column']
	parent_table_id = dataset[0]['id_tablelist_parent_table']

	if parent_table_id == None :
		parent_table_id = -1

	sql = """
	SELECT sql_exp_column,
	       pk_column,
	       table_name
	FROM CUST_TABLE_LIST A
	WHERE A.ID = {parent_table_id}
	""".format(parent_table_id=parent_table_id)


	cursor.execute(sql)


	columnNames = [d[0] for d in cursor.description]
	dataset = [dict(zip(columnNames, row)) for row in cursor]

	parent_have_yn = ""
	str_sql_exp_column_parent = ""
	str_pk_column_parent = ""
	sql_table_parent = ""
	table_parent = ""

	# print(dataset)

	if dataset  :
		str_sql_exp_column_parent = dataset[0]['sql_exp_column']
		str_pk_column_parent = dataset[0]['pk_column']
		sql_table_parent = '\t, {table_name} B\n'.format(table_name=dataset[0]['table_name'])
		table_parent = dataset[0]['table_name']
		parent_have_yn = "Y"
	else :
		parent_have_yn = "N"
		sql_table_parent = ""
		table_parent = ""



	#############################################
	## 검색 테이블 노출 컬럼 가공 시작
	#############################################

	str_sql_exp_column = str_sql_exp_column.replace(" ","")

	# print(str_sql_exp_column)

	list_sql_exp_column = str_sql_exp_column.split(',')

	# print(list_sql_exp_column)

	str_sql_exp_column = ""

	for col in list_sql_exp_column :
		str_sql_exp_column = str_sql_exp_column + "'"+ col + "',"


	str_sql_exp_column = str_sql_exp_column.rstrip(",")

	# print(str_sql_exp_column)

	sql = """
	SELECT column_name, col_comments
	FROM CUST_COLUMN_LIST C INNER JOIN CUST_TABLE_LIST B
	                          ON B.ID = C.ID_TABLELIST
	                          INNER JOIN CUST_DB_LIST A
	                          ON A.ID = B.ID_DBLIST
	WHERE B.ID = {id}
	  AND C.COLUMN_NAME IN ({str_sql_exp_column})
	ORDER BY C.COLUMN_ID
	""".format(
				str_sql_exp_column=str_sql_exp_column,
				id=target['id'],)

	# print(sql)

	cursor.execute(sql)

	columnNames = [d[0] for d in cursor.description]
	dataset_exp_column_name = [dict(zip(columnNames, row)) for row in cursor]
	# print(dataset)

	sql_exp_column = ""

	for data in dataset_exp_column_name :

		sql_exp_column = sql_exp_column + \
		              """\t, A.{column_name} "{col_comments}"\n""".format(column_name=data['column_name'],
																	   col_comments=data['col_comments'])

	# sql_exp_column = sql_exp_column.rstrip("\n")

	#############################################
	## 검색 테이블 노출 컬럼 가공 끝
	#############################################


	#############################################
	## 검색 테이블 PK COLUMN 가공 시작
	#############################################

	str_pk_column = str_pk_column.replace(" ","")

	# print(str_pk_column)

	list_sql_exp_column = str_pk_column.split(',')

	# print(list_sql_exp_column)

	str_pk_column = ""

	for col in list_sql_exp_column :
		str_pk_column = str_pk_column + "'"+ col + "',"


	str_pk_column = str_pk_column.rstrip(",")

	# print(str_pk_column)

	sql = """
	SELECT column_name, col_comments
	FROM CUST_COLUMN_LIST C INNER JOIN CUST_TABLE_LIST B
	                          ON B.ID = C.ID_TABLELIST
	                          INNER JOIN CUST_DB_LIST A
	                          ON A.ID = B.ID_DBLIST
	WHERE B.ID = {id}
	  AND C.COLUMN_NAME IN ({str_pk_column})
	ORDER BY C.COLUMN_ID
	""".format( str_pk_column=str_pk_column,
				id=target['id'],)

	# print(sql)

	cursor.execute(sql)

	columnNames = [d[0] for d in cursor.description]
	dataset = [dict(zip(columnNames, row)) for row in cursor]
	# print(dataset)

	sql_pk_select = ""
	sql_pk_where = ""

	for data in dataset :

		sql_pk_select = sql_pk_select + \
		              """\tA.{column_name} "{col_comments}",\n""".format(column_name=data['column_name'],
																	   col_comments=data['col_comments'])
		sql_pk_where = sql_pk_where + \
					  """\tAND A.{column_name1} =  :{column_name2}\n""".format(column_name1=data['column_name'],
					  	                                                       column_name2=data['column_name'].lower())


	# sql_pk_select = sql_pk_select.rstrip("\n")
	# sql_pk_where = sql_pk_where.rstrip("\n")

	#############################################
	## 검색 테이블 PK COLUMN 가공 끝
	#############################################

	# str_sql_exp_column_parent = dataset[0]['sql_exp_column']
	# str_pk_column_parent = dataset[0]['pk_column']

	sql_select_parent = ""
	sql_pk_select_parent = ""
	sql_pk_where_parent = ""

	if parent_have_yn == "Y" and str_sql_exp_column_parent != None:


		#############################################
		## 부모 테이블 검색 테이블 노출 컬럼 가공 시작
		#############################################

		str_sql_exp_column_parent = str_sql_exp_column_parent.replace(" ","")

		# print(str_sql_exp_column_parent)

		list_sql_exp_column = str_sql_exp_column_parent.split(',')

		# print(list_sql_exp_column)

		str_sql_exp_column_parent = ""

		for col in list_sql_exp_column :
			str_sql_exp_column_parent = str_sql_exp_column_parent + "'"+ col + "',"


		str_sql_exp_column_parent = str_sql_exp_column_parent.rstrip(",")

		# print(str_sql_exp_column_parent)

		sql = """
		SELECT column_name, col_comments
		FROM CUST_COLUMN_LIST C INNER JOIN CUST_TABLE_LIST B
		                          ON B.ID = C.ID_TABLELIST
		                          INNER JOIN CUST_DB_LIST A
		                          ON A.ID = B.ID_DBLIST
		WHERE B.ID = {parent_table_id}
		  AND C.COLUMN_NAME IN ({str_sql_exp_column_parent})
		ORDER BY C.COLUMN_ID
		""".format( str_sql_exp_column_parent=str_sql_exp_column_parent,
					parent_table_id=parent_table_id,)

		# print(sql)

		cursor.execute(sql)

		columnNames = [d[0] for d in cursor.description]
		dataset = [dict(zip(columnNames, row)) for row in cursor]
		# print(dataset)



		sql_select_parent = ""

		for data in dataset :

			sql_select_parent = sql_select_parent + \
			              """\t, B.{column_name} "{col_comments}"\n""".format(column_name=data['column_name'],
																		   col_comments=data['col_comments'])

		# sql_select_parent = sql_select_parent.rstrip("\n")

		# print("#" + sql_select_parent)

		#############################################
		## 부모 테이블 검색 테이블 노출 컬럼 가공 끝
		#############################################


		#############################################
		## 부모 테이블 검색 테이블 PK COLUMN 가공 시작
		#############################################

		str_pk_column_parent = str_pk_column_parent.replace(" ","")

		# print(str_pk_column_parent)

		list_sql_exp_column = str_pk_column_parent.split(',')

		# print(list_sql_exp_column)

		str_pk_column_parent = ""

		for col in list_sql_exp_column :
			str_pk_column_parent = str_pk_column_parent + "'"+ col + "',"


		str_pk_column_parent = str_pk_column_parent.rstrip(",")

		# print(str_pk_column_parent)

		sql = """
		SELECT column_name, col_comments
		FROM CUST_COLUMN_LIST C INNER JOIN CUST_TABLE_LIST B
		                          ON B.ID = C.ID_TABLELIST
		                          INNER JOIN CUST_DB_LIST A
		                          ON A.ID = B.ID_DBLIST
		WHERE B.ID = {parent_table_id}
		  AND C.COLUMN_NAME IN ({str_pk_column_parent})
		ORDER BY C.COLUMN_ID
		""".format( parent_table_id=parent_table_id,
					str_pk_column_parent=str_pk_column_parent)

		# print(sql)

		cursor.execute(sql)

		columnNames = [d[0] for d in cursor.description]
		dataset = [dict(zip(columnNames, row)) for row in cursor]
		# print(dataset)

		sql_pk_select_parent = ""
		sql_pk_where_parent = ""

		for data in dataset :

			sql_pk_select_parent = sql_pk_select_parent + \
			              """\tA.{column_name} "{col_comments}",\n""".format(column_name=data['column_name'],
																		   col_comments=data['col_comments'])
			sql_pk_where_parent = sql_pk_where_parent + \
						  """\tAND A.{column_name} =  B.{column_name}\n""".format(column_name=data['column_name'])


		# sql_pk_select_parent = sql_pk_select_parent.rstrip("\n")
		# sql_pk_where_parent = sql_pk_where_parent.rstrip("\n")
	else :
		sql_select_parent = ""
		sql_pk_select_parent = ""
		sql_pk_where_parent = ""

	#############################################
	## 부모 테이블 검색 테이블 PK COLUMN 가공 끝
	#############################################
	# print(sql_exp_column+"\n")
	# print(sql_pk_select+"\n")
	# print(sql_select_parent+"\n")
	# print(sql_pk_select_parent+"\n")
	# print(sql_pk_where_parent+"\n")

	# print(db_nm)
	# print(table_name)

	sql = """
	SELECT c.column_name,
	       IF(c.col_comments is null,c.column_name,c.col_comments) col_comments,
	       b.table_name,
	       b.pk_column,
	       c.column_type,
	       c.code_key,
	       id_tablelist_code_table,
	       (select bb.table_name
	        from   cust_table_list bb
	        where  bb.id = c.id_tablelist_code_table ) code_table,
	       (select bb.sql_exp_column
	        from   cust_table_list bb
	        where  bb.id = c.id_tablelist_code_table ) code_table_exp_column


	FROM CUST_COLUMN_LIST C   INNER JOIN CUST_TABLE_LIST B
	                          ON B.ID = C.ID_TABLELIST
	                          INNER JOIN CUST_DB_LIST A
	                          ON A.ID = B.ID_DBLIST
	WHERE B.ID = {id}
	ORDER BY C.COLUMN_ID
	""".format(id=target['id'])

	cursor.execute(sql)


	columnNames = [d[0] for d in cursor.description]
	dataset = [dict(zip(columnNames, row)) for row in cursor]
	# print(dataset)




	sql_exp_column_org = sql_exp_column

	for data in dataset :

		compelte_sql = ""
		sql_cmm_table = ""
		sql_cmm_column  = ""
		sql_code_column = ""
		sql_code_table = ""
		sql_code_table_exp_select = ""

		sql_exp_column = sql_exp_column_org

		# print(data['column_name'])
		sql_column_name = "\t  A." + data['column_name'] + ' "' + data['col_comments'] + '"' + "\n"
		sql_table_name = "\t  " + data['table_name'] + " A" + "\n"


		# SELECT 컬럼 중복 제거
		for dt in dataset_exp_column_name :
			if dt['column_name'] == data['column_name'] :
				# print("#"+'\t '+sql_exp_column[2:])
				sql_column_name = ""
				sql_exp_column = '\t '+sql_exp_column[2:]
				# sql_exp_column = (sql_exp_column+"|").replace(",\n|","\n")


		compelte_sql = """SELECT\n""" + \
					   """{sql_column_name}""" + \
					   """{exp_column}""" + \
		               """{sql_select_parent}""" + \
					   """{sql_code_table_exp_select}""" + \
					   """FROM\n""" + \
					   """{sql_table_name}""" + \
					   """{sql_table_parent}""" + \
					   """{sql_cmm_table}""" + \
					   """{sql_code_table}""" + \
					   """WHERE 1 = 1\n""" + \
					   """{sql_pk_where_parent}""" + \
					   """{sql_pk_where}""" + \
					   """{sql_code_column}""" + \
					   """{sql_cmm_column}"""



		if data['column_type'] == "0" :
			pass
	# 		compelte_sql = """SELECT
	# {sql_select_parent}
	# {exp_column}
	# \tA.{column_name} "{col_comments}"
	# FROM
	# \t{table_name} A
	# {sql_table_parent}
	# WHERE 1=1
	# {sql_pk_where_parent}
	# {sql_pk_where};""".format(exp_column=sql_exp_column,
	# 		                                column_name=data['column_name'],
	# 		                                col_comments=data['col_comments'],
	# 		                                table_name=data['table_name'],
	# 		                                sql_pk_where=sql_pk_where,
	# 		                                sql_select_parent=sql_select_parent,
	# 		                                sql_pk_where_parent=sql_pk_where_parent,
	# 		                                sql_table_parent=sql_table_parent,
	# 		                                )

		elif data['column_type'] == "1" :

			sql_cmm_table = "\t, CMM_CMM_C CCC" + "\n"
			sql_cmm_column = "\tAND A." + data['column_name'] + " = CCC.CMM_CD(+)" + "\n" \
							 "\tAND CCC.CMM_GRP_CD(+) = '"+ data['code_key'] + "'" + "\n"

			# compelte_sql = compelte_sql.format( exp_column=sql_exp_column,
			# 	                                sql_column_name=sql_column_name,
			# 	                                sql_table_name=sql_table_name,
			# 	                                sql_pk_where=sql_pk_where,
			# 	                                sql_select_parent=sql_select_parent,
			# 	                                sql_pk_where_parent=sql_pk_where_parent,
			# 	                                sql_table_parent=sql_table_parent,
			# 	                                sql_cmm_table=sql_cmm_table,
			# 	                                sql_cmm_column=sql_cmm_column,
			# 	                                sql_code_table=sql_code_table,
			# 	                                sql_code_column=sql_code_column,
			# 	                                )

	# 		compelte_sql = """SELECT
	# {sql_select_parent}
	# {exp_column}
	# \tA.{column_name} "{col_comments}",
	# \tCCC.CD_VAL "{col_comments}값"
	# FROM
	# \t{table_name} A
	# {sql_table_parent}
	# \t, CMM_CMM_C CCC
	# WHERE 1=1
	# {sql_pk_where_parent}
	# {sql_pk_where}
	# \tAND A.{column_name} = CCC.CMM_CD(+)
	# \tAND CCC.CMM_GRP_CD(+) = '{code_key}';""".format(exp_column=sql_exp_column,
	# 		                                column_name=data['column_name'],
	# 		                                col_comments=data['col_comments'],
	# 		                                table_name=data['table_name'],
	# 		                                sql_pk_where=sql_pk_where,
	# 		                                code_key=data['code_key'],
	# 		                                sql_select_parent=sql_select_parent,
	# 		                                sql_pk_where_parent=sql_pk_where_parent,
	# 		                                sql_table_parent=sql_table_parent,
	# 		                                )

		elif data['column_type'] == "2" :

			if data['code_table'] != None :
				sql_code_column = "\tAND A." + data['column_name'] + " = C." + data['column_name'] + " /* 또는 " + data['code_table'] +" 테이블의 PK 속성 */" + "\n"
				sql_code_table = "\t, " + data['code_table'] + " C" + "\n"

			#############################################
			## 개별 테이블 검색 노출 컬럼 가공 시작
			#############################################


			if data['code_table_exp_column'] != None :
				str_sql_code_table_exp_column_parent = data['code_table_exp_column']

				str_sql_code_table_exp_column_parent = str_sql_code_table_exp_column_parent.replace(" ","")

				# print(str_sql_code_table_exp_column_parent)

				list_sql_exp_column = str_sql_code_table_exp_column_parent.split(',')

				# print(list_sql_exp_column)

				str_sql_code_table_exp_column_parent = ""

				for col in list_sql_exp_column :
					str_sql_code_table_exp_column_parent = str_sql_code_table_exp_column_parent + "'"+ col + "',"


				str_sql_code_table_exp_column_parent = str_sql_code_table_exp_column_parent.rstrip(",")

				# print(str_sql_code_table_exp_column_parent)

				sql = """
				SELECT column_name, col_comments
				FROM CUST_COLUMN_LIST C INNER JOIN CUST_TABLE_LIST B
				                          ON B.ID = C.ID_TABLELIST
				                          INNER JOIN CUST_DB_LIST A
				                          ON A.ID = B.ID_DBLIST
				WHERE B.ID = {id_tablelist_code_table}
				  AND C.COLUMN_NAME IN ({str_sql_code_table_exp_column_parent})
				ORDER BY C.COLUMN_ID
				""".format(id_tablelist_code_table=data['id_tablelist_code_table'],
						   str_sql_code_table_exp_column_parent=str_sql_code_table_exp_column_parent)

				# print(sql)

				cursor.execute(sql)

				columnNames = [d[0] for d in cursor.description]
				dataset = [dict(zip(columnNames, row)) for row in cursor]
				# print(dataset)



				sql_code_table_exp_select = ""

				for dt in dataset :

					sql_code_table_exp_select = sql_code_table_exp_select + \
					              """\t, C.{column_name} "{col_comments}"\n""".format(column_name=dt['column_name'],
																				   col_comments=dt['col_comments'])

				# sql_code_table_exp_select = sql_code_table_exp_select.replace(",\n","\n")



		compelte_sql = compelte_sql.format( exp_column=sql_exp_column,
			                                sql_column_name=sql_column_name,
			                                sql_table_name=sql_table_name,
			                                sql_pk_where=sql_pk_where,
			                                sql_select_parent=sql_select_parent,
			                                sql_pk_where_parent=sql_pk_where_parent,
			                                sql_table_parent=sql_table_parent,
			                                sql_cmm_table=sql_cmm_table,
			                                sql_cmm_column=sql_cmm_column,
			                                sql_code_table=sql_code_table,
			                                sql_code_column=sql_code_column,
			                                sql_code_table_exp_select=sql_code_table_exp_select,
			                                )

		# print(compelte_sql)

	# 		compelte_sql = """SELECT
	# {sql_select_parent}
	# {exp_column}
	# \tA.{column_name} "{col_comments}"
	# FROM
	# \t{table_name} A
	# {sql_table_parent}
	# \t, {code_table} C
	# WHERE 1=1
	# {sql_pk_where_parent}
	# {sql_pk_where}
	# \tAND A.{column_name} = C.({code_table}테이블의 PK COLUMN);""".format(exp_column=sql_select,
	# 		                                column_name=data['column_name'],
	# 		                                col_comments=data['col_comments'],
	# 		                                table_name=data['table_name'],
	# 		                                sql_pk_where=sql_pk_where,
	# 		                                code_table=data['code_table'],
	# 		                                sql_select_parent=sql_select_parent,
	# 		                                sql_pk_where_parent=sql_pk_where_parent,
	# 		                                sql_table_parent=sql_table_parent,
	# 		                                )


		# print(compelte_sql)
		compelte_sql = compelte_sql.replace("'","''")
		update_sql ="""UPDATE CUST_COLUMN_LIST C INNER JOIN CUST_TABLE_LIST B
	                          ON B.ID = C.ID_TABLELIST
	                          INNER JOIN CUST_DB_LIST A
	                          ON A.ID = B.ID_DBLIST
	SET C.SQL_text = '{compelte_sql}'
	WHERE B.ID = {id}
	  AND C.COLUMN_NAME = '{column_name}'""".format(compelte_sql=compelte_sql,
	  												id=target['id'],
	  												column_name=data['column_name']
	  												)

		# print(update_sql)
		cursor.execute(update_sql)
		conn.commit()

	print('## {0} 완료'.format(target['table_name']))




# 전체 rows
# # print(rows[0])  # 첫번째 row: (1, '김정수', 1, '서울')
# # print(rows[1])  # 두번째 row: (2, '강수정', 2, '서울')

# Connection 닫기
conn.close()


# print("================================================================================")


