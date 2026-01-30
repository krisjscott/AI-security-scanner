import psycopg2

DATABASE_PASSWORD = "supersecret123"
API_KEY = "sk-1234567890abcdef"
def connect_db():
    return psycopg2.connect(
        host="localhost",
        password=DATABASE_PASSWORD
    )