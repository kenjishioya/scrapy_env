import pymysql.cursors
import os

class MySQLConnector():

    def __init__(self):
        self.conn = pymysql.connect(host='scrapy_mysql',
                                user=os.environ.get('MYSQL_DB_USER'),
                                password=os.environ.get('MYSQL_DB_PASS'),
                                database=os.environ.get('MYSQL_DB_NAME'),
                                cursorclass=pymysql.cursors.DictCursor)

    def execute_sql(self, sql, parameters=None):
        with self.conn.cursor() as cursor:
            cursor.execute(sql, parameters)
        self.conn.commit()

    def close(self):
        self.conn.close()

    def execute_sqlfile(self, file_name, parameters=None):
        file_path = os.path.join(os.path.dirname(__file__), f'./sql/{file_name}')
        if os.path.isfile(file_path) is False:
            raise FileExistsError(f'{file_path} does not exists')
        
        with open(file_path, 'r') as sql_file:
            sql = sql_file.read()
            with self.conn.cursor() as cursor:
                cursor.execute(sql, parameters)
            self.conn.commit()

