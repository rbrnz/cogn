from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import *
from etl_scripts.config import oltp_engine

engine = oltp_engine

Base = declarative_base()

class BillOfMaterials(Base):
	__tablename__ = "bill_of_materials"

	bill_of_materials_id = Column(Integer, primary_key = True, nullable = False)
	tube_assembly_id = Column(ForeignKey("tube_assembly.tube_assembly_id"), nullable = False)
	component_id = Column(String, nullable = False)
	quantity = Column (Integer, nullable = False)

class Component(Base):
	__tablename__ = "component"

	component_id = Column(String, primary_key = True, nullable = False)
	component_type_id = Column(ForeignKey("component_type.component_type_id"), nullable = False)
	connection_type_id = Column(ForeignKey("connection_type.connection_type_id"), nullable = False)
	type_id = Column(ForeignKey("type.type_id"))
	outside_shape_id = Column(ForeignKey("outside_shape.outside_shape_id"))
	base_type_id = Column(ForeignKey("base_type.base_type_id"))
	height_over_tube = Column(Float, nullable = False)
	bolt_pattern_long = Column(Float)
	bolt_pattern_wide = Column(Float)
	groove = Column(Boolean, nullable = False)
	base_diameter = Column(Float)
	shoulder_diameter = Column(Float)
	unique_feature = Column(Boolean, nullable = False)
	orientation = Column(Boolean, nullable = False)
	weight = Column(Float)

class ComponentType(Base):
	__tablename__ = "component_type"

	component_type_id = Column(String, primary_key = True, nullable = False)

class Type(Base):
	__tablename__ = "type"

	type_id = Column(String, primary_key = True, nullable = False)
	type = Column(String, nullable = False)

class OutsideShape(Base):
	__tablename__ = "outside_shape"

	outside_shape_id = Column(String, primary_key = True, nullable = False)
	outside_shape = Column(String, nullable = False)

class BaseType(Base):
	__tablename__ = "base_type"

	base_type_id = Column(String, primary_key = True, nullable = False)
	base_type = Column(String, nullable = False)

class ConnectionType(Base):
	__tablename__ = "connection_type"

	connection_type_id = Column(String, primary_key = True, nullable = False)

class PriceQuote(Base):
	__tablename__ = "price_quote"

	price_quote_id = Column(Integer, primary_key = True, nullable = False, autoincrement = True)
	tube_assembly_id = Column(ForeignKey("tube_assembly.tube_assembly_id"), nullable = False)
	supplier_id = Column(ForeignKey("supplier.supplier_id"), nullable = False)
	annual_usage = Column(Integer, nullable = False)
	quote_date = Column(Date, nullable = False)
	min_order_quantity = Column(Integer, nullable = False)
	cost = Column(Float, nullable = False)

class Supplier(Base):
	__tablename__ = "supplier"

	supplier_id = Column(String, primary_key = True, nullable = False)

class TubeAssembly(Base):
	__tablename__ = "tube_assembly"

	tube_assembly_id = Column(String, primary_key = True, nullable = False)
	

if __name__ == '__main__':
	Base.metadata.drop_all(bind=engine)
	Base.metadata.create_all(bind=engine)
	
	print("Sucess! Tables created.")