import csv
from datetime import datetime 

from sqlalchemy.orm import sessionmaker
from .create_tables import PriceQuote
from etl_scripts.config import CSV_PATH, oltp_engine


def get_processed_data():

	with open(CSV_PATH + 'price_quote.csv', 'r') as file:
		reader = csv.DictReader(file, delimiter=',')

		rows = []

		for row in reader:
			if row['bracket_pricing'] == 'Yes':
				min_order_quantity = row['quantity'] if row['min_order_quantity'] == '0' else row['min_order_quantity']
			else:
				min_order_quantity = row['min_order_quantity']

			rows.append({
				'tube_assembly_id': row['tube_assembly_id'],
				'supplier_id': row['supplier'],
				'annual_usage': row['annual_usage'],
				'quote_date': datetime.strptime(row['quote_date'], '%Y-%m-%d'),
				'min_order_quantity': int(min_order_quantity),
				'cost': float(row['cost'])
				})

	return rows


def add_to_table(session):
	rows = get_processed_data()

	for row in rows:
		data = PriceQuote(**row)
		session.add(data)

if __name__ == "__main__":
	Session = sessionmaker(bind = oltp_engine)
	session = Session()

	add_to_table(session)
	session.commit()

	print("Success on component!")