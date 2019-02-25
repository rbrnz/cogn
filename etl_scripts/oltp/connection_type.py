import pandas as pd
from sqlalchemy.orm import sessionmaker

from .create_tables import ConnectionType
from etl_scripts.config import CSV_PATH, oltp_engine


def get_unique_connection_types():
	comp_boss = pd.read_csv(CSV_PATH + 'comp_boss.csv')
	connection_types = comp_boss['connection_type_id'].unique().tolist()

	connection_type_unique_ids = []

	for connection_type in connection_types:
		connection_type_unique_ids.append({
			'connection_type_id': connection_type
			})

	return connection_type_unique_ids

def add_to_table(session):
	connection_type_unique_ids = get_unique_connection_types()

	for connection_type in connection_type_unique_ids:
		row = ConnectionType(**connection_type)
		session.add(row)

if __name__ == "__main__":
	Session = sessionmaker(bind = oltp_engine)
	session = Session()

	add_to_table(session)
	session.commit()

	print("Success on connection_type!")