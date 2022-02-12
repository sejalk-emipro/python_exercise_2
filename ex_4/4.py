from ufw.util import valid_address


class InventoryManagement:
    '''Create class of InventoryManagement
       Create constractor of the class with parameter
       define Empty dictionary
       purchase_product(): Get two input from the user and add purchase product details to dictionary
       display_product_stock(): display product stock
       sales_processes():get input from the user and update quantity of the product
    '''

    def __init__(self):
        self.mainDict = {}
        self.index=0

    def purchase_product(self):
        self.index += 1
        product_price = int(input("Enter price of product :"))
        product_quantity = int(input("Enter quantity of product :"))
        self.mainDict[self.index] = {'price': product_price, 'quantity': product_quantity,
                                 'subtotal': (product_price * product_quantity)}

        self.display_product_stock()

    def display_product_stock(self):
        print("{:<10} {:<10} {:<10} {:<10}".format('key', 'price', 'quantity', 'subtotal'))
        for key, value in self.mainDict.items():
            print("{:<10} {:<10} {:<10} {:<10}".format(key, value['price'], value['quantity'], value['subtotal']))

    def sales_processes(self):
        sales_product = int(input("Enter the qty of sell: "))
        sum_quantity = 0

        delete_key=[]
        sum_quantity = sum(d['quantity'] for d in self.mainDict.values() if d)
        # for key, value in self.mainDict.items():
        #     sum_quantity += sum([(v) for k, v in value.items() if k == 'quantity'])

        for key, value in self.mainDict.items():
            if sales_product > sum_quantity:
                print("Sorry, not enough quantity.\nStart the purchase order procedure please!\n")
                break
            else:
                    tmp_quantity=0
                    quantity = value['quantity']
                    if sales_product>=quantity:
                        tmp_quantity=quantity
                        sales_product=sales_product-tmp_quantity
                    else:
                        tmp_quantity=sales_product
                        sales_product=0

                    value['quantity'] = value['quantity'] - tmp_quantity
                    value['subtotal'] = (value['quantity'] * value['price'])
                    self.mainDict[key] = value

                    if value['quantity']==0:
                        delete_key.append(key)

        # new_dict = {key: val for key, val in self.mainDict.items() if val['quantity'] != 0}
        for delete in delete_key:
            del self.mainDict[delete]
        # self.mainDict = new_dict
        self.display_product_stock()



    def display_valuation(self):
        sub_total = 0
        sum_quantity = 0
        for k, value in self.mainDict.items():
            sub_total += sum([(v) for k, v in value.items() if k == 'subtotal'])
            sum_quantity += sum([(v) for k, v in value.items() if k == 'quantity'])

        print("valuation of product : ", (sub_total / sum_quantity))


inventoryManagement = InventoryManagement()

print("Menu Driven Program")
print("1.Purchase Product")
print("2.Sale Product")
print("3.View Available Product Quantities")
print("4.Show Valuation")
print("5.Exit")

while True:
    choice = int(input('Enter your choice: '))
    if choice == 1:
        inventoryManagement.purchase_product()
    elif choice == 2:
        inventoryManagement.sales_processes()
    elif choice == 3:
        inventoryManagement.display_product_stock()
    elif choice == 4:
        inventoryManagement.display_valuation()
    else:
        exit(0)
