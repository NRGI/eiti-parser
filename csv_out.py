"""reads in eiti json and output csv"""
import json
import csv

def main(json_data):
    """main body"""
    header = ['name', 'year', 'commodity', 'code', 'subtotal']

    # Create new CSV archive file for input month
    csv_out = open('output/eiti.csv', 'wb')
    csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csv_writer.writerow(header)
    for record in json_data:
        outrow = []
        outrow.append(record['name'])
        outrow.append(record['commodity'])
        outrow.append(record['code'])
        outrow.append(record['year'])
        outrow.append(record['subtotal'])
        csv_writer.writerow(outrow)

    csv_out.close()


    # for record in json:

        # print len(json_data)




	# {
 #        "code":"gov_total2007all",
 #        "1145E":{
 #            "included":"na",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Taxes on use of goods/permission to use goods or perform activities",
 #            "payment":"na"
 #        },
 #        "114522E":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Emission and pollution taxes",
 #            "payment":"na"
 #        },
 #        "1212E":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Social security employer contributions",
 #            "payment":"na"
 #        },
 #        "141E":{
 #            "included":"na",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Property income",
 #            "payment":"na"
 #        },
 #        "1143E":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Profits of natural resource fiscal monopolies",
 #            "payment":"na"
 #        },
 #        "143E":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Fines, penalties, and forfeits",
 #            "payment":"na"
 #        },
 #        "1141E":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"General taxes on goods and services (VAT, sales tax, turnover tax)",
 #            "payment":"na"
 #        },
 #        "year":"2007",
 #        "1151E":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Customs and other import duties",
 #            "payment":"na"
 #        },
 #        "1415E31":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Delivered/paid directly to government",
 #            "payment":"na"
 #        },
 #        "1415E32":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Delivered/paid to state-owned enterprise(s)",
 #            "payment":"na"
 #        },
 #        "12E":{
 #            "included":"na",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Social contributions",
 #            "payment":"na"
 #        },
 #        "1153E1":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Profits of natural resource export monopolies",
 #            "payment":"na"
 #        },
 #        "11451E":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Motor vehicle taxes",
 #            "payment":"na"
 #        },
 #        "1421E":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Sales of goods and services by government units",
 #            "payment":"na"
 #        },
 #        "144E1":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Voluntary transfers to government (donations)",
 #            "payment":"na"
 #        },
 #        "14E":{
 #            "included":"na",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Other revenue",
 #            "payment":"na"
 #        },
 #        "115E":{
 #            "included":"na",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Taxes on international trade and transactions",
 #            "payment":"na"
 #        },
 #        "1412E":{
 #            "included":"na",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Dividends",
 #            "payment":"na"
 #        },
 #        "113E":{
 #            "included":"Included",
 #            "name_of_recieving_agency":"District Assembly / Municipality",
 #            "name_of_str_in_country":"Property Rate",
 #            "name":"Taxes on property",
 #            "payment":884811.0
 #        },
 #        "114521E":{
 #            "included":"Included",
 #            "name_of_recieving_agency":"Minerals Commission",
 #            "name_of_str_in_country":"Mineral Right Licence",
 #            "name":"Licence fees",
 #            "payment":0.0
 #        },
 #        "111E":{
 #            "included":"na",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Taxes on income, profits and capital gains",
 #            "payment":"na"
 #        },
 #        "1415E1":{
 #            "included":"Included",
 #            "name_of_recieving_agency":"Internal Revenue Service",
 #            "name_of_str_in_country":"Mineral Royalty",
 #            "name":"Royalties",
 #            "payment":40836760.0
 #        },
 #        "142E":{
 #            "included":"na",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Sales of goods and services",
 #            "payment":"na"
 #        },
 #        "1412E2":{
 #            "included":"Included",
 #            "name_of_recieving_agency":"Non Tax Revenue Unit (Ministry of Finance & Economic Planning)",
 #            "name_of_str_in_country":"Dividend",
 #            "name":"From government participation (equity)",
 #            "payment":3853442.0
 #        },
 #        "1412E1":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"From state-owned enterprises",
 #            "payment":"na"
 #        },
 #        "1142E":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Excise taxes",
 #            "payment":"na"
 #        },
 #        "1112E2":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Extraordinary taxes on income, profits and capital gains",
 #            "payment":"na"
 #        },
 #        "1112E1":{
 #            "included":"Included",
 #            "name_of_recieving_agency":"Internal Revenue Service",
 #            "name_of_str_in_country":"Corporate Tax",
 #            "name":"Ordinary taxes on income, profits and capital gains",
 #            "payment":15573250.0
 #        },
 #        "subtotal":61149888.0,
 #        "11E":{
 #            "included":"na",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Taxes",
 #            "payment":"na"
 #        },
 #        "1152E":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Taxes on exports",
 #            "payment":"na"
 #        },
 #        "name":"Government Total",
 #        "commodity":"all",
 #        "1415E":{
 #            "included":"na",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Production entitlements (in-kind or cash)",
 #            "payment":"na"
 #        },
 #        "1413E":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Withdrawals from income of quasi-corporations",
 #            "payment":"na"
 #        },
 #        "116E":{
 #            "included":"Included",
 #            "name_of_recieving_agency":"Office of the Administrator of Stool Lands",
 #            "name_of_str_in_country":"Ground Rent",
 #            "name":"Other taxes payable by natural resource companies",
 #            "payment":1625.0
 #        },
 #        "1422E":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Administrative fees for government services",
 #            "payment":"na"
 #        },
 #        "114E":{
 #            "included":"na",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Taxes on goods and services",
 #            "payment":"na"
 #        },
 #        "1415E4":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Compulsory transfers to government (infrastructure and other)",
 #            "payment":"na"
 #        },
 #        "1415E5":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Other rent payments",
 #            "payment":"na"
 #        },
 #        "112E":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Taxes on payroll and workforce",
 #            "payment":"na"
 #        },
 #        "1415E2":{
 #            "included":"Not included",
 #            "name_of_recieving_agency":"na",
 #            "name_of_str_in_country":"na",
 #            "name":"Bonuses",
 #            "payment":"na"
 #        }
 #    },