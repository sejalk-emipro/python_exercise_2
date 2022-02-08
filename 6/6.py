import csv
# Open csv file

def get_country(country):
    dict_country = {'AU': 'Australia', 'USA': 'United States of America', 'IT': 'Italy', 'ES': 'Spain', 'DE': 'Germany',
               'UK': 'United Kingdom'}
    return dict_country.get(country)

result = {}
with open('Sales Order.csv', mode='r') as infile:
    reader = csv.reader(infile)
    next(reader)
    for row in reader:
        key = row[0]
        if key in result:
            # implement your duplicate row handling here
            subDict={'sku':row[2],'price':row[4],'qty':row[3]}
            result[key]['orderlines'].append(subDict)
            pass
        else:
            result[key]={'customer': {'name':row[1],'address 1' : row[5],'address 2': row[6], 'city' :row[8], 'country': get_country(row[9]),'zipcode':row[7]},
                       'orderlines':[{'sku':row[2],'price':row[4],'qty':row[3]}]}

    infile.close() #Close file
print(result)



