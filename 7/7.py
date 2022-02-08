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

    infile.close()

csv_columns = ['Order No','Customer','SKU','Qty','Price','Address1','Address2','Zipcode','City','Country']
list=[]
for key,value in result.items():
    for n in value.get('orderlines'):
        list.append({'Order No':key,'Customer':value.get('customer').get('name'),
                   'SKU':n.get('sku'),
                   'Qty':n.get('qty'),
                   'Price':n.get('price'),
                   'Address1' :  value.get('customer').get('address 1'),
                   'Address2': value.get('customer').get('address 2'),
                   'Zipcode': value.get('customer').get('zipcode'),
                   'City' :value.get('customer').get('city'),
                   'Country': value.get('customer').get('country')})
with open('demo.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in list:
        writer.writerow(data)
    # writer.writerow(list)
    csvfile.close()

