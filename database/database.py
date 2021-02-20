import mysql.connector
import config

TABLE_HOST = "labhost"

class DatababseHelper:

    def __init__(self) -> None:
        HOST = config.URL
        USER = config.USER
        PASSWORD = config.PASSWORD
        DATABASE = config.DATABASE
        db = None
        mycursor = None

    def connect(self) -> None:
        # Connect to database
        self.db = mysql.connector.connect(
            host=self.HOST,
            user=self.USER,
            password=self.PASSWORD,
            database=self.DATABASE
        )
        # initialize cursor
        self.mycursor = self.db.cursor()

    def create_table(self, table=TABLE_HOST) -> None:
        self.mycursor.execute("CREATE TABLE " + table + " (id INT AUTO_INCREMENT PRIMARY KEY, host VARCHAR(255), os VARCHAR(255))")

    def add_column(self, table:str, column:str, column_type:str) -> None:
        self.mycursor.execute("ALTER TABLE " + table + " ADD COLUMN " + column + " " + column_type)

    def insert(self, table:str, input_list:list) -> None:
        query = "("
        value = "("
        val = "("
        for i in input_list:
            query = query + " " + str(input_list[i]) + ","
            value = value + " " + "%s" + ","
            val = val + " True," 
        query = query[:-1] + ")"
        value = value[:-1] + ")"
        val = val[:-1] + ")"
        sql = "INSERT INTO " +  table + " " + query + " VALUES " + value
        self.mycursor.execute(sql, val)
        self.db.commit()

    def insert(self, host:str, os:str, table=TABLE_HOST):
        sql = "INSERT INTO " + table + " (host, os) VALUES (%s, %s)"
        val = (host, os)
        self.mycursor.execute(sql, val)
        self.db.commit()

    def get_lab_room_by_software(self, table:str, software:str):
        sql = ("SELECT * FROM " + table + " WHERE " + software + "=%s")
        adr = ("True", )
        self.mycursor.execute(sql, adr)
        result = self.mycursor.fetchall()
        return result

    def get_all_host(self, table=TABLE_HOST):
        self.mycursor.execute("SELECT * FROM " + table)
        all_host = self.mycursor.fetchall()
        return all_host

    def get_host_by_room(self, software:str, table=TABLE_HOST):
        sql = "SELECT * FROM " + table + " WHERE address ='Park Lane 38'"
