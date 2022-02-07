class InventoryManagement:
    '''Create InventoryManagement class
     Create constructor with parameter
     finished_product: It's use to storing product
     finished_product_qty :It's use to storing finished product quantity

     purchase_product():Get input by user,how many product purchase,And add purchases quantity to finished product Qty

     display_product_stock(): display stock of product

     sales_product():get input by user and check sales product available or not.
     if not then display massage :"Not enough product quantities to sell, available quantity is"
     otherwise decrease the finished product quantity
     '''

    def __init__(self, product):
        self.finished_product = product
        self.finished_product_qty = 0

    def purchase_product(self, purchase_quantity):
        self.finished_product_qty += purchase_quantity

    def display_product_stock(self):
        print('Stock of ', self.finished_product, 'is: ', self.finished_product_qty)

    def sales_product(self, sales_quantity):

        if sales_quantity > self.finished_product_qty:
            print('Not enough product quantities to sell, available quantity is ', self.finished_product_qty)
        else:
            self.finished_product_qty -= sales_quantity
            print('Available quantity after sales: ', self.finished_product_qty)


obj = InventoryManagement('pen')
print("Menu Driven Program")
print("1.Purchase Product")
print("2.Sale Product")
print("3.View Available Product Quantities")
print("4.Exit")

while True:
    choice = int(input('Enter your choice: '))
    if choice == 1:
        purchase_quantity = int(input("Enter a quantity of purchase: "))
        obj.purchase_product(purchase_quantity)
    elif choice == 2:
        sales_quantity = int(input('Enter a quantity of sales: '))
        obj.sales_product(sales_quantity)
    elif choice == 3:
        obj.display_product_stock()
    else:
        exit(0)
