import pandas as pd
from sqlalchemy.orm import sessionmaker

from .create_tables import ComponentType
from etl_scripts.config import CSV_PATH, oltp_engine


def get_unique_component_types():
	comp_boss = pd.read_csv(CSV_PATH + 'comp_boss.csv')
	component_types = comp_boss['component_type_id'].unique().tolist()

	component_type_unique_ids = []

	for component_type in component_types:
		component_type_unique_ids.append({
			'component_type_id': component_type
			})

	return component_type_unique_ids

def add_to_table(session):
	component_type_unique_ids = get_unique_component_types()

	for component_type in component_type_unique_ids:
		row = ComponentType(**component_type)
		session.add(row)

if __name__ == "__main__":
	Session = sessionmaker(bind = oltp_engine)
	session = Session()

	add_to_table(session)
	session.commit()

	print("Success on component_type!")