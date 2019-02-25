import pandas as pd
from sqlalchemy.orm import sessionmaker

from .create_tables import Type
from etl_scripts.config import CSV_PATH, oltp_engine


def get_unique_types():
	comp_boss = pd.read_csv(CSV_PATH + 'comp_boss.csv')
	comp_boss_types = comp_boss['type'].dropna() \
							 .drop_duplicates() \
							 .reset_index(drop=True) \
							 .reset_index() \
							 .to_dict('records')

	types = []

	for type in comp_boss_types:
		types.append({
			'type_id': "T00" + str(type['index'] + 1),
			'type'   : type['type']
			})

	return types

def add_to_table(session):
	type_unique_ids = get_unique_types()

	for type in type_unique_ids:
		row = Type(**type)
		session.add(row)

if __name__ == "__main__":
	Session = sessionmaker(bind = oltp_engine)
	session = Session()

	add_to_table(session)
	session.commit()

	print("Success on type!")