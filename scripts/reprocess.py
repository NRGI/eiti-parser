#!/usr/bin/env python

import unicodecsv

INFILE = "output/eiti.csv"
GFSFILE = "output/gfs.csv"
OUTFILE = "../data/eiti_normalised.csv"

HEADERS = ['name', 'year', 'commodity', 'code', 'companyID',
'file_name', 'gfs_code', 'gfs_name', 'value']

def get_gfs():
    """Get GFS codes, names from GFS file - names specific to each year"""
    codes = {}
    with open(GFSFILE, "r") as f_gfsfile:
        csv_gfsfile = unicodecsv.DictReader(f_gfsfile)
        for row in csv_gfsfile:
            year = row["year"]
            gfs_id = row["gfsID"]
            gfs_name = row["name"]
            
            codes[year] = {gfs_id: gfs_name}
            gfsd = row.items()
            
            # Use counter to cycle through columns
            count = 0
            for i, v in enumerate(gfsd[7][1]):
                if count == 0: 
                    gfs_id = v
                if count == 1: 
                    gfs_name = v
                    codes[year][gfs_id] = gfs_name
                count += 1
                if count == 5: count = 0
    return codes

def reprocess(gfscodes):
    """Make one row per GFS code per row"""
    with open(INFILE, "r") as f_infile:
        csv_infile = unicodecsv.DictReader(f_infile)
        f_outfile = open(OUTFILE, "wb")
        csv_outfile = unicodecsv.DictWriter(f_outfile, fieldnames=HEADERS)
        
        csv_outfile.writeheader()
        for row in csv_infile:
            if row['commodity'] == "all": continue
            year = row["year"]
            
            # For each existing row, write one row per GFS code
            for gfscode, gfsname in gfscodes[year].items():
                value = row[gfscode]
                if value == "na": continue
                csv_outfile.writerow({
                    "name": row["name"],
                    "year": row["year"],
                    "commodity": row["commodity"],
                    "code": row["code"],
                    "companyID": row["companyID"],
                    "file_name": row["file_name"],
                    "gfs_code": gfscode,
                    "gfs_name": gfsname,
                    "value": value,
                })
    
if __name__ == "__main__":
    gfscodes = get_gfs()
    reprocess(gfscodes)