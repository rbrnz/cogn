import pandas as pd
from sqlalchemy.orm import sessionmaker

from .create_tables import OutsideShape
from etl_scripts.config import CSV_PATH, oltp_engine


def get_unique_outside_shapes():
	comp_boss = pd.read_csv(CSV_PATH + 'comp_boss.csv')
	comp_boss_outside_shapes = comp_boss['outside_shape'].dropna() \
							 .drop_duplicates() \
							 .reset_index(drop=True) \
							 .reset_index() \
							 .to_dict('records')

	outside_shapes = []

	for outside_shape in comp_boss_outside_shapes:
		outside_shapes.append({
			'outside_shape_id': "OS00" + str(outside_shape['index'] + 1),
			'outside_shape'   : outside_shape['outside_shape']
			})

	return outside_shapes

def add_to_table(session):
	outside_shape_unique_ids = get_unique_outside_shapes()

	for outside_shape in outside_shape_unique_ids:
		row = OutsideShape(**outside_shape)
		session.add(row)

if __name__ == "__main__":
	Session = sessionmaker(bind = oltp_engine)
	session = Session()

	add_to_table(session)
	session.commit()

	print("Success on outside_shape!")