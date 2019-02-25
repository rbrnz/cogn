import configparser
from sqlalchemy import *

config = configparser.ConfigParser()
config.read('./etl_scripts/config.ini')

# DB connections
oltp_engine = create_engine(f"postgresql+psycopg2://{config['OLTP']['USER']}:{config['OLTP']['PASSWORD']}@{config['OLTP']['DATABASE']}:5432/{config['OLTP']['SCHEMA']}")

CSV_PATH = './input/'