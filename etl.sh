#!/bin/bash

declare -a arr=(
	"etl_scripts.oltp.create_tables"
	"etl_scripts.oltp.component_type"
	"etl_scripts.oltp.type"
	"etl_scripts.oltp.outside_shape"
	"etl_scripts.oltp.base_type"
	"etl_scripts.oltp.connection_type"
	"etl_scripts.oltp.tube_assembly"
	"etl_scripts.oltp.component"
	"etl_scripts.oltp.bill_of_materials"
	"etl_scripts.oltp.supplier"
	"etl_scripts.oltp.price_quote"
	);

for i in "${arr[@]}"
do
   python3 -m "$i"
   # or do whatever with individual element of the array
done