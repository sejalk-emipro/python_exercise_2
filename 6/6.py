import csv
# Open csv file

def get_country(country):
    dict_country = {'AU': 'Australia', 'USA': 'United States of America', 'IT': 'Italy', 'ES': 'Spain', 'DE': 'Germany',
               'UK': 'United Kingdom'}
    return dict_country.get(country)

result = {}
with open('Sales Order.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    next(reader)
    for row in reader:
        key = row['Order No']
        if key in result:
            # implement your duplicate row handling here
            subDict={'sku':row['SKU'],'price':row['Price'],'qty':row['Qty']}
            result[key]['orderlines'].append(subDict)
            pass
        else:
            result[key]={'customer': {'name':row['Customer'],'address 1' : row['Address1'],'address 2': row['Address2'], 'city' :row['City'], 'country': get_country(row['Country']),'zipcode':row['Zipcode']},
                       'orderlines':[{'sku':row['SKU'],'price':row['Price'],'qty':row['Qty']}]}

    infile.close() #Close file
print(result)



