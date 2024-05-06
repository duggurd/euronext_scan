from sqlalchemy import create_engine

def get_conn_sqlite():
    DB_PATH="ingestion.db"
    return create_engine(f"sqlite:///{DB_PATH}")

def get_conn_pg():
    DB_USER="postgres"
    DB_PASSWORD="postgres"
    DB_HOST="localhost"
    DB_PORT="5432"
    DB_NAME="ingestion"
    return create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

if __name__ == "__main__":
    conn = get_conn_pg().connect()