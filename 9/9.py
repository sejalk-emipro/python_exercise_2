from builtins import set


class SalesManagment:
    def __init__(self):
        self.product_details = {}
        self.product_stock_details={}
        self.product_index=0
    def manage_product(self):
        product_values=self.prepared_product()
        self.create_product(product_values)

    def prepared_product(self):
        name=input("Enter product name : ")
        product_unit_price=int(input("Enter product unit price : "))
        product_price=int(input("Enter product price: "))
        product_stock=int(input("Enter product stock : "))
        return {'name':name,'product_unit_price':product_unit_price,'product_cost_price':product_price,'product_stock':product_stock}

    def create_product(self,product_values):
        self.product_index +=1
        product_sku='PRD'+str((self.product_index))
        self.product_details.update({product_sku:{'name':product_values.get('name'),'product_unit_price':product_values.get('product_unit_price')
                                                  ,'product_cost_price':product_values.get('product_cost_price')}})

        self.product_stock_details.update({product_sku:product_values.get('product_stock')})
        return product_sku

    def update_product_stock(self):
        self.display_product_stock()
        product_name = input("Enter product sku:")
        if product_name in self.product_stock_details:
            product_stock = int(input("Enter updated stock of product:"))
            current_stock = self.product_stock_details[product_name]
            self.product_stock_details[product_name] += product_stock
            # self.product_stock_details.update(product_name=(product_stock+current_stock))
        else:
            print("1.Do you want to retry.")
            print("2.Exit")
            while True:
                choice = int(input('Enter your choice: '))
                if choice == 1:
                    self.display_product_stock()
                else:
                    False

    def display_product_stock(self):
        for key, value in self.product_details.items():
            print("Product SKU ID :{:<10}".format(key))

class Customer:
    def __init__(self):
        self.customer_details = {}
        self.customer_other_details={}
        self.product_index=0







sales = SalesManagment()

print("Menu Driven Program")
print("1.Add Product")
print("2.Update Product Stock")
print("3.View Available Product Quantities")
print("4.Show Valuation")
print("5.Exit")

while True:
    choice = int(input('Enter your choice: '))
    if choice == 1:
        sales.manage_product()
    elif choice == 2:
        sales.update_product_stock()
    elif choice == 3:
        sales.display_product_stock()
    elif choice == 4:
        sales.display_product_stock()
    else:
        exit(0)
