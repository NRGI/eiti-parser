"""reads in eiti json and output csv"""

import csv

def main(json_data):
    """main body"""
    # Create new CSV archive file for input month
    csv_out = open('output/eiti.csv', 'wb')
    csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csv_header = ['name', 'year', 'commodity', 'code', 'subtotal', 'companyID', 'file_name', '1145E', '114522E', '1212E', '141E', '1143E', '143E', '1141E', '1151E', '1415E31', '1415E32', '12E', '1153E1', '11451E', '1421E', '144E1', '14E', '115E', '1412E', '113E', '114521E', '111E', '1415E1', '142E', '1412E2', '1412E1', '1142E', '1112E2', '1112E1', '11E', '1152E', '1415E', '1413E', '116E', '1422E', '114E', '1415E4', '1415E5', '112E', '1415E2']

    csv_writer.writerow(csv_header)
    for record in json_data:
        outrow = []
        outrow.append(record['name'])
        outrow.append(record['year'])
        outrow.append(record['commodity'])
        outrow.append(record['code'])
        outrow.append(record['subtotal'])
        outrow.append(record['id'])
        outrow.append(record['file_name'])

        outrow.append(record['1145E']['payment'])
        outrow.append(record['114522E']['payment'])
        outrow.append(record['1212E']['payment'])
        outrow.append(record['141E']['payment'])
        outrow.append(record['1143E']['payment'])
        outrow.append(record['143E']['payment'])
        outrow.append(record['1141E']['payment'])
        outrow.append(record['1151E']['payment'])
        outrow.append(record['1415E31']['payment'])
        outrow.append(record['1415E32']['payment'])
        outrow.append(record['12E']['payment'])
        outrow.append(record['1153E1']['payment'])
        outrow.append(record['11451E']['payment'])
        outrow.append(record['1421E']['payment'])
        outrow.append(record['144E1']['payment'])
        outrow.append(record['14E']['payment'])
        outrow.append(record['115E']['payment'])
        outrow.append(record['1412E']['payment'])
        outrow.append(record['113E']['payment'])
        outrow.append(record['114521E']['payment'])
        outrow.append(record['111E']['payment'])
        outrow.append(record['1415E1']['payment'])
        outrow.append(record['142E']['payment'])
        outrow.append(record['1412E2']['payment'])
        outrow.append(record['1412E1']['payment'])
        outrow.append(record['1142E']['payment'])
        outrow.append(record['1112E2']['payment'])
        outrow.append(record['1112E1']['payment'])
        outrow.append(record['11E']['payment'])
        outrow.append(record['1152E']['payment'])
        outrow.append(record['1415E']['payment'])
        outrow.append(record['1413E']['payment'])
        outrow.append(record['116E']['payment'])
        outrow.append(record['1422E']['payment'])
        outrow.append(record['114E']['payment'])
        outrow.append(record['1415E4']['payment'])
        outrow.append(record['1415E5']['payment'])
        outrow.append(record['112E']['payment'])
        outrow.append(record['1415E2']['payment'])

        csv_writer.writerow(outrow)

    csv_out.close()

    gfs_csv_out = open('output/gfs.csv', 'wb')
    gfs_csv_writer = csv.writer(gfs_csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    file_names = []
    gfs_header = ['year', 'ref', 'id', 'name', 'included', 'name_of_recieving_agency', 'name_of_str_in_country']

    gfs_csv_writer.writerow(gfs_header)

    for record in json_data:
        if record['file_name'] in file_names:
            pass
        else:
            outrow = []
            outrow.append(record['year'])
            outrow.append(record['file_name'])
            for key in record:
                if key in ('code', 'subtotal', 'commodity', 'name', 'file_name', 'id', 'year'):
                    pass
                else:
                    outrow.append(key)
                    outrow.append(record[key]['name'])
                    outrow.append(record[key]['included'])
                    outrow.append(record[key]['name_of_recieving_agency'])
                    outrow.append(record[key]['name_of_str_in_country'])
            gfs_csv_writer.writerow(outrow)
            file_names.append(record['file_name'])
