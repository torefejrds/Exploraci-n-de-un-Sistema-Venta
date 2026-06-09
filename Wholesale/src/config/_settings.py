from dotenv import load_dotenv
import os

#carga del enviroment
load_dotenv()

class Settings:
    DB_SERVER = os.getenv("DB_SERVER")
    DB_DATABASE = os.getenv("DB_DATABASE")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DATABASE_URL = (
        f"mssql+pyodbc://"
        f"{DB_USERNAME}:"
        f"{DB_PASSWORD}@"
        f"{DB_SERVER}/"
        f"{DB_DATABASE}"
        "?drive=ODBC+Driver+18+For+SQL+Server"
        "&TrustServerCertificate=yes"
         
    )
    Settings = Settings()