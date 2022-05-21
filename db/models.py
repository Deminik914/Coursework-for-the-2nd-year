# models.py
from peewee import *
import datetime


'''
# Connect to a MySQL database on network.
mysql_db = MySQLDatabase('my_app', user='app', password='db_password',
                         host='ip_addres', port=3306)'''

'''#Connect to a Postgres database.
pg_db = PostgresqlDatabase('my_app', user='postgres', password='secret',
                           host='ip_addres', port=5432)'''
# Подключение БД
database = SqliteDatabase('db_bot.db')


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = database
        order_by = 'id'


# Описание таблицы Record
class Record(BaseModel):
    user_id = CharField(max_length=16)
    date_create = DateTimeField(default=datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
    body = CharField(max_length=64)
    reminder_date = DateTimeField(formats='%d-%m-%Y')
    notification = BitField()

    class Meta:
        db_table = "record"

# atabase.drop_tables([Record], safe=True)
database.create_tables([Record], safe=True)
