import pandas as pd
from sqlalchemy.orm import sessionmaker

from .create_tables import BaseType
from etl_scripts.config import CSV_PATH, oltp_engine


def get_unique_base_types():
	comp_boss = pd.read_csv(CSV_PATH + 'comp_boss.csv')
	comp_boss_base_types = comp_boss['base_type'].dropna() \
							 .drop_duplicates() \
							 .reset_index(drop=True) \
							 .reset_index() \
							 .to_dict('records')

	base_types = []

	for base_type in comp_boss_base_types:
		base_types.append({
			'base_type_id': "BT00" + str(base_type['index'] + 1),
			'base_type'   : base_type['base_type']
			})

	return base_types

def add_to_table(session):
	base_type_unique_ids = get_unique_base_types()

	for base_type in base_type_unique_ids:
		row = BaseType(**base_type)
		session.add(row)

if __name__ == "__main__":
	Session = sessionmaker(bind = oltp_engine)
	session = Session()

	add_to_table(session)
	session.commit()

	print("Success on base_type!")