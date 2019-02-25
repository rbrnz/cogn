import csv
from sqlalchemy.orm import sessionmaker
from .create_tables import BillOfMaterials
from etl_scripts.config import oltp_engine, CSV_PATH

def get_processed_data():
	with open(CSV_PATH + 'bill_of_materials.csv', 'r') as file:
		reader = csv.DictReader(file)

		rows = []
		
		for row in reader:
			tube_assembly_id = row['tube_assembly_id']

			for i in range(1,9):

				if row[f'component_id_{i}'] != 'NA':
					component_id = row[f'component_id_{i}']
					quantity 	 = int(row[f'quantity_{i}'])

					rows.append({
						'tube_assembly_id' : tube_assembly_id,
						'component_id' 	   : component_id,
						'quantity'         : quantity
						})
				else:
					pass
						
	return rows


def add_to_table(session):
	bill_of_materials = get_processed_data()

	for bill_of_material in bill_of_materials:
		row = BillOfMaterials(**bill_of_material)
		session.add(row)

if __name__ == '__main__':
	Session = sessionmaker(bind = oltp_engine)
	session = Session()

	add_to_table(session)
	session.commit()

	print("Success on bill_of_material!")