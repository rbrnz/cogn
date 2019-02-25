import pandas as pd
from sqlalchemy.orm import sessionmaker

from .create_tables import TubeAssembly
from etl_scripts.config import CSV_PATH, oltp_engine


def get_unique_tube_assembly_ids():
	# Tube assembly IDs are present both in `bill_of_materials.csv` and `price_quote.csv`,
	# so we have to load both in order to get all unique IDS

	bill_of_materials = pd.read_csv(CSV_PATH + 'bill_of_materials.csv')
	price_quote = pd.read_csv(CSV_PATH + 'price_quote.csv')

	bill_of_materials = bill_of_materials['tube_assembly_id'].unique().tolist()
	price_quote = price_quote['tube_assembly_id'].unique().tolist()

	unique_ids = []

	unique_ids.extend(bill_of_materials)
	unique_ids.extend(price_quote)

	tube_assembly_ids = []

	for tube_assembly in set(unique_ids):
		tube_assembly_ids.append({
			'tube_assembly_id': tube_assembly
			})

	return tube_assembly_ids

def add_to_table(session):
	tube_assembly_ids = get_unique_tube_assembly_ids()

	for tube_assembly in tube_assembly_ids:
		row = TubeAssembly(**tube_assembly)
		session.add(row)

if __name__ == "__main__":
	Session = sessionmaker(bind = oltp_engine)
	session = Session()

	add_to_table(session)
	session.commit()

	print("Success on tube_assembly!")