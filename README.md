#  EITI parser
Python parser reads in excel EITI reports and writes out formatted json and csv to output folder.

To see formated outputs click [here for csv](https://github.com/NRGI/eiti-parser/blob/master/scripts/output/eiti.csv) and [here for json](https://github.com/NRGI/eiti-parser/blob/master/scripts/output/eiti.json).

Also see [here for normalised CSV file](https://github.com/NRGI/eiti-parser/blob/master/data/eiti_normalised.csv), disaggregated by company, commodity, year, and GFS (revenue type) code. NB that there are some (relatively small - about 5%) discrepancies between these numbers and the total numbers available in the source data, because not all rows are fully disaggregated by GFS code.

###Instructions
To rerun, open terminal and type in the following commands
	
	git clone https://github.com/NRGI/eiti-parser
	cd eiti-parser/scripts
	python main.py

