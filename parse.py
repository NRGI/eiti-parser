"""functions for parsing excel"""
import xlrd
from xlrd import open_workbook
import sys


def excel_read(file_name):
    """reades in excel workbook and checks for revenue sheet"""
    workbook = open_workbook(file_name)

    sheet_name = '3. Revenues'
    # check to see if revenu sheet exists
    try:
        sheet = workbook.sheet_by_name(sheet_name)
    except xlrd.biffh.XLRDError:
        print 'No \"3. Revenues\" sheet in ' + file_name
        sys.exit()

    return sheet

def parse_sheet(sheet, json_data, year):
    """parses incoming excel into json"""
    # (row,col)
    json_data.append({
        'name':'total',
        'year': year,
        sheet.cell_value(2,2):
        })
    # print sheet.cell_value(2,1)
    # for row in sheet.nrows:
    # 	print row
    
    # return labels


def main(file_name, json_data):
    """main body"""
    sheet = excel_read(file_name)
    parse_sheet(sheet, json_data, file_name[0:4])
    print json_data

