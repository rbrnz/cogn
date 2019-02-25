import pandas as pd
from sqlalchemy.orm import sessionmaker

from .create_tables import Supplier
from etl_scripts.config import CSV_PATH, oltp_engine


def get_unique_suppliers():
	price_quote = pd.read_csv(CSV_PATH + 'price_quote.csv')
	price_quote_suppliers = price_quote['supplier'].unique().tolist()

	suppliers = []

	for supplier in price_quote_suppliers:
		suppliers.append({
			'supplier_id': supplier
			})

	return suppliers

def add_to_table(session):
	supplier_unique_ids = get_unique_suppliers()

	for supplier in supplier_unique_ids:
		row = Supplier(**supplier)
		session.add(row)

if __name__ == "__main__":
	Session = sessionmaker(bind = oltp_engine)
	session = Session()

	add_to_table(session)
	session.commit()

	print("Success on supplier!")