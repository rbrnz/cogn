import csv
import pandas as pd
from sqlalchemy.orm import sessionmaker
from .create_tables import Component
from etl_scripts.config import CSV_PATH, oltp_engine
from . import type, outside_shape, base_type


def get_processed_data():

	types = pd.DataFrame(type.get_unique_types()) \
						.set_index("type") \
						.to_dict("index")

	outside_shapes = pd.DataFrame(outside_shape.get_unique_outside_shapes()) \
						.set_index("outside_shape") \
						.to_dict("index")

	base_types = pd.DataFrame(base_type.get_unique_base_types()) \
						.set_index("base_type") \
						.to_dict("index")

	with open(CSV_PATH + 'comp_boss.csv', 'r') as file:
		reader = csv.DictReader(file, delimiter=',')

		rows = []

		for row in reader:
			rows.append({
				'component_id': row['component_id'],
				'component_type_id': row['component_type_id'],
				'connection_type_id': row['connection_type_id'],
				'type_id': types[row['type']]['type_id'] if row['type'] != 'NA' else None,
				'outside_shape_id': outside_shapes[row['outside_shape']]['outside_shape_id'] if row['outside_shape'] != 'NA' else None,
				'base_type_id': base_types[row['base_type']]['base_type_id'] if row['base_type'] != 'NA' else None,
				'height_over_tube': row['height_over_tube'],
				'bolt_pattern_long': row['bolt_pattern_long'] if row['bolt_pattern_long'] != 'NA' else None,
				'bolt_pattern_wide': row['bolt_pattern_wide'] if row['bolt_pattern_wide'] != 'NA' else None,
				'groove': True if row['groove'] == 'Yes' else False,
				'base_diameter': row['base_diameter'] if row['base_diameter'] != 'NA' else None,
				'shoulder_diameter': row['shoulder_diameter'] if row['shoulder_diameter'] != 'NA' else None,
				'unique_feature': True if row['shoulder_diameter'] == 'Yes' else False,
				'orientation': True if row['orientation'] == 'Yes' else False,
				'weight': row['weight'] if row['weight'] != 'NA' else None
				})

	return rows


def add_to_table(session):
	rows = get_processed_data()

	for row in rows:
		data = Component(**row)
		session.add(data)

if __name__ == "__main__":
	Session = sessionmaker(bind = oltp_engine)
	session = Session()

	add_to_table(session)
	session.commit()

	print("Success on component!")