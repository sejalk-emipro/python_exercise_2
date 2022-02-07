from mock.mock import mock_open


class Manufacturing:
    '''Create class of manufacturing
            Create constractor with parameter
            raw_material:It is use to store name of raw materials
            raw_material_ratio_qty:It is use of storing raw materials ratio
            finished_product:It is storing how many product finished in stock
            raw_material_qty:it's store raw materials quantity
            finished_product_qty:it's stroring total finished product quantity

            purchase_raw_material: get input from the user and diaplsy Total raw materials
            produce:get input from the user and if raw material Not enough raw of product  then display msg
            other wise dicrese the raw materials and add finished product.

            display_raw_material_stock:It's display total raw material stack
            display_final_product_stock:It's display total finished product stack
        '''

    def __init__(self, raw_material, raw_material_ratio_qty, finished_product):
        self.raw_material = raw_material
        self.raw_material_ratio_qty = raw_material_ratio_qty
        self.finished_product = finished_product
        self.raw_material_qty = 0
        self.finished_product_qty = 0

    def purchase_raw_material(self, raw_materials):
        self.raw_material_qty += raw_materials

    def produce(self, finished_product):
        if (finished_product * self.raw_material_ratio_qty > self.raw_material_qty):
            print(
                "Not enough raw material available to produce the product, please do the purchase.\n Available raw material is: ",
                self.raw_material_qty)
        else:
            self.raw_material_qty -= finished_product * self.raw_material_ratio_qty
            self.finished_product_qty += finished_product

    def display_raw_material_stock(self):
        print('Total raw material stock :', self.raw_material_qty)

    def display_final_product_stock(self):
        print('Total of final products stock :', self.finished_product_qty)


obj = Manufacturing("2 wheel", 2, 0)
print("Menu Driven Program")
print("1.Purchase Raw Material Product")
print("2.Manufacture Finish Product")
print("3.Show Raw Material Quantity")
print("4.Show Actual Product Quantity")
print("5.Exit")
while True:

    choice = int(input("Enter your choice:"))

    if choice == 1:
        raw_materials = int(input("Enter raw materials quantity :"))
        obj.purchase_raw_material(raw_materials)
        obj.display_raw_material_stock()
        obj.display_final_product_stock()
    elif choice == 2:
        finished_product = int(input("Enter quantity of finished product:"))
        obj.produce(finished_product)
        obj.display_raw_material_stock()
        obj.display_final_product_stock()
    elif choice == 3:
        obj.display_raw_material_stock()
    elif choice == 4:
        obj.display_final_product_stock()
    else:
        exit(0)
