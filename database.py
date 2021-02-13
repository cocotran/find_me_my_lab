import mysql.connector
import config


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

    def create_table(self, table:str) -> None:
        self.mycursor.execute("CREATE TABLE " + table)

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

    def get_lab_room_by_software(self, table:str, software:str):
        sql = ("SELECT * FROM " + table + " WHERE " + software + "=%s")
        adr = ("True", )
        self.mycursor.execute(sql, adr)
        result = self.mycursor.fetchall()
        return result
