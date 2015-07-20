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

def insert_object(row, sheet):
    """factory to create basis for json record of excel line"""
    output = {'name': sheet.cell_value(row, 2).encode('utf-8').lstrip()}
    if sheet.cell_value(row, 3) == '':
        output['included'] = 'na'
    else:
        output['included'] = sheet.cell_value(row, 3).encode('utf-8').strip()
    if sheet.cell_value(row, 5) == '':
        output['name_of_str_in_country'] = 'na'
    else:
        output['name_of_str_in_country'] = sheet.cell_value(row, 5).encode('utf-8').strip()
    if sheet.cell_value(row, 6) == '':
        output['name_of_recieving_agency'] = 'na'
    else:
        output['name_of_recieving_agency'] = sheet.cell_value(row, 6).encode('utf-8').strip()
    return output

def json_constructor(sheet, json_data, file_name):
    """parses incoming excel into json"""
    year = file_name[0:4]
    # nrows = sheet.nrows
    nrows = sheet.nrows
    ncols = sheet.ncols

    # track indexes and company names
    index_tracker = {'index': {}, 'names': {}}

    # create total records
    json_data.append({
        'code': 'gov_total' + year + 'all',
        'name':'Government Total',
        'year': year,
        'commodity': 'all',
        'companyID': 'governments',
        'file_name': file_name
        })
    index_tracker['index']['gov_total'] = len(json_data) - 1
    index_tracker['names'][len(json_data) - 1] = 'gov_total'
    json_data.append({
        'code': 'co_total' + year + 'all',
        'name':'Companies Subtotal',
        'year': year,
        'commodity': 'all',
        'companyID': 'companies',
        'file_name': file_name
        })
    index_tracker['index']['co_total'] = len(json_data) - 1
    index_tracker['names'][len(json_data) - 1] = 'co_total'

    # create comapny records
    for col in range(10, ncols):
        json_data.append({
            'code': sheet.cell_value(3, col).encode('utf-8').lower().replace(' ', '_') \
            + year \
            + sheet.cell_value(5, col).encode('utf-8').lower().replace(' ', '_'),
            'name': sheet.cell_value(3, col).encode('utf-8'),
            'year': year,
            'commodity': sheet.cell_value(5, col).encode('utf-8'),
            'subtotal': sheet.cell_value(7, col),
            'file_name': file_name
            })
        if sheet.cell_value(4, col) == '':
            json_data[-1]['companyID'] = 'na'
        else:
            json_data[-1]['companyID'] = sheet.cell_value(4, col)
        index_tracker['index'][sheet.cell_value(3, col)] = len(json_data) - 1
        index_tracker['names'][len(json_data) - 1] = sheet.cell_value(3, col)

    for row in range(8, nrows):
        indexer = index_tracker['index']
        # namer =  index_tracker['names']

        # create record to insert into company records
        if sheet.cell_value(row, 1) == '':
            pass
        elif sheet.cell_value(row, 1) == 'E. Notes':
        	subtotal_row = row
        else:
            # country totals
            json_data[indexer['gov_total']][sheet.cell_value(row, 1).encode('utf-8')] = insert_object(row, sheet)
            total_record = json_data[indexer['gov_total']][sheet.cell_value(row, 1).encode('utf-8')]
            if sheet.cell_value(row, 7) == '':
                total_record['payment'] = 'na'
            else:
                total_record['payment'] = sheet.cell_value(row, 7)

            # company totals
            json_data[indexer['co_total']][sheet.cell_value(row, 1).encode('utf-8')] = insert_object(row, sheet)
            companies_record = json_data[indexer['co_total']][sheet.cell_value(row, 1).encode('utf-8')]
            if sheet.cell_value(row, 9) == 0 or sheet.cell_value(row, 9) == '':
                companies_record['payment'] = 'na'
            else:
                companies_record['payment'] = sheet.cell_value(row, 9)

            # add to company records
            for col in range(10, ncols):
                json_data[indexer[sheet.cell_value(3, col)]][sheet.cell_value(row, 1).encode('utf-8')] = insert_object(row, sheet)
                if sheet.cell_value(row, 9) == 0 or sheet.cell_value(row, col) == '':
                    json_data[indexer[sheet.cell_value(3, col)]][sheet.cell_value(row, 1).encode('utf-8')]['payment'] = 'na'
                else:
                    json_data[indexer[sheet.cell_value(3, col)]][sheet.cell_value(row, 1).encode('utf-8')]['payment'] = sheet.cell_value(row, col)

    json_data[indexer['gov_total']]['subtotal'] = sheet.cell_value(subtotal_row, 7)
    json_data[indexer['co_total']]['subtotal'] = sheet.cell_value(subtotal_row, 9)


def main(file_name, json_data):
    """main body"""
    sheet = excel_read(file_name)
    json_constructor(sheet, json_data, file_name)
