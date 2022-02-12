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
            subDict = {'sku': row['SKU'], 'price': row['Price'], 'qty': row['Qty']}
            result[key]['orderlines'].append(subDict)
            pass
        else:
            result[key] = {
                'customer': {'name': row['Customer'], 'address 1': row['Address1'], 'address 2': row['Address2'],
                             'city': row['City'], 'country': get_country(row['Country']), 'zipcode': row['Zipcode']},
                'orderlines': [{'sku': row['SKU'], 'price': row['Price'], 'qty': row['Qty']}]}

    infile.close()
csv_columns = ['Order No', 'Customer', 'SKU', 'Qty', 'Price', 'Address1', 'Address2', 'Zipcode', 'City', 'Country']

with open('demo.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for key,value in result.items():
        for n in value.get('orderlines'):
            writer.writerow({'Order No':key,'Customer':value.get('customer').get('name'),
                       'SKU':n.get('sku'),'Qty':n.get('qty'),'Price':n.get('price'),
                       'Address1' :  value.get('customer').get('address 1'),
                       'Address2': value.get('customer').get('address 2'),
                       'Zipcode': value.get('customer').get('zipcode'),
                        'City' :value.get('customer').get('city'),'Country': value.get('customer').get('country')})

    csvfile.close()

