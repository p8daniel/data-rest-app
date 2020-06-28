from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'techtest_db',
    user='techtest_db',
    password='techtest_db',
    host='localhost', port=5432,
    autorollback=True
)
