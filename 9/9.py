import datetime


class SalesManagment:
    def __init__(self):
        self.product_details = {}
        self.product_stock_details={}
        self.product_index=0
        self.customer_details={}
        self.customer_address_details={}
        self.customer_index=0
        self.order_details = {}
        self.order_index=0
        self.order_total_amount=0
        self.state_draft='Draft'
        self.state_confirm = 'Confirm'
        self.stage_cancel = 'Cancel'
        self.state_done = 'Done'

    def manage_product(self):
        product_values=self.prepared_product()
        self.create_product(product_values)

    def prepared_product(self):
        name=input("Enter product name : ")
        product_unit_price=int(input("Enter product unit price : "))
        product_price=int(input("Enter product price: "))
        product_type = input("Enter product type:(stockable, consumable, service) : ")
        product_stock=int(input("Enter product stock : "))

        return {'name':name,'product_unit_price':product_unit_price,'product_cost_price':product_price,'product_type':product_type,'product_stock':product_stock}

    def create_product(self,product_values):
        self.product_index +=1
        product_sku='PRD'+str((self.product_index))
        self.product_details.update({product_sku:{'name':product_values.get('name'),
                                                  'product_unit_price':product_values.get('product_unit_price'),
                                                  'product_cost_price':product_values.get('product_cost_price'),
                                                  'product_type':product_values.get('product_type')}})

        self.product_stock_details.update({product_sku:product_values.get('product_stock')})
        return product_sku

    def update_product_stock(self):
        self.display_product_details()
        product_name = input("Enter product sku:")
        if product_name in self.product_stock_details:
            product_stock = int(input("Enter updated stock of product:"))
            current_stock = self.product_stock_details[product_name]
            self.product_stock_details[product_name] += product_stock
            # self.product_stock_details.update(product_name=(product_stock+current_stock))
        else:
            print("1.You are enter wrong product")

    def display_product_details(self):
        i = 0
        for product_key, product_value in self.product_details.items():
            print("{:<5} '[{}] - {}'".format(i+1,product_key,product_value['name']))
    '''Customer Details:'''
    def manage_customer(self):
        customer_values=self.prepared_customer()
        self.create_customer_details(customer_values)

    def prepared_customer(self):
        name = input("Enter customer name : ")
        email = input("Enter customer email : ")
        phone = input("Enter customer phone number : ")
        address1 = input("Enter customer address1 : ")
        address2 = input("Enter customer address2 : ")
        city = input("Enter customer city : ")
        state = input("Enter customer state : ")
        country = input("Enter customer country : ")
        zipcode = input("Enter customer zipcode : ")
        return {'name': name, 'email': email, 'phone_no': phone,'address1': address1,'address2': address2,'city': city,'state':state,'country': country,'zipcode': zipcode}

    def create_customer_details(self,customer_values):
        self.customer_index+=1
        customer_code = 'cust_' + str((self.customer_index))
        self.customer_details.update({customer_code:{'name':customer_values.get('name'),'email':customer_values.get('email'),
                                                     'phone':customer_values.get('phone_no')}})

        self.customer_address_details.update({customer_code:{'address1':customer_values.get('address1'),
                                                             'address2':customer_values.get('address2')
                                                             ,'city':customer_values.get('city')
                                                             ,'state':customer_values.get('state')
                                                             ,'country':customer_values.get('country')
                                                             ,'zipcode':customer_values.get('zipcode')}})
        return customer_code

    def generate_sales_order(self):
        order_values=self.prepare_sales_order()
        if order_values is None:
            pass
        else:
            self.create_sales_order(order_values)

    def prepare_sales_order(self):
        # display customer Details
        i=0
        for customer_key, customer_value in self.customer_details.items():
            print("{:<5} '[{}] - {}'".format(i+1,customer_key,customer_value['name']))
        customer_code=input("Enter Customer Code : ")

        if customer_code in self.customer_details:
            self.display_product_details() #Display product details
            order_date=datetime.datetime.today()
            return_data={'customer':customer_code,'order_lines':[],'order_date':order_date.strftime('%m-%d-%Y'),'state':'Draft','order_total_amount':0}
            self.add_product_line_item(return_data)
            while True:
                print("1.Do You want to add more product")
                print("2.exit")
                choice1=int(input('Enter your choice :'))
                if choice1==1:
                    self.add_product_line_item(return_data)
                elif choice1 == 2:
                    break
            return_data['order_total_amount']=self.order_total_amount
            self.order_total_amount=0
            return return_data
        else:
            print("Sorry!,{} customer code dose not exist".format(customer_code))
            while True:
                print("1.Do You want to retry")
                print("2.exit")
                choice1=int(input('Enter your choice :'))
                if choice1==1:
                    self.prepare_sales_order()
                elif choice1 == 2:
                    break

    def add_product_line_item(self,return_data):
        product_code = input("Enter product code : ")
        if product_code in self.product_details:
            product_quantity = int(input("Enter order quantity : "))
            product_detail = self.product_details.get(product_code)
            product_stock = self.product_stock_details.get(product_code)

            product_keys=[sub['product_sku'] for sub in return_data.get('order_lines')]
            if product_code in product_keys:
                same_product=[sub for sub in return_data.get('order_lines') if sub['product_sku']==product_code]
                res = same_product
                res[0]['quantity'] += product_quantity
                res[0]['subtotal'] = (res[0]['quantity'] * product_detail.get('product_unit_price'))
                index = next((index for (index, d) in enumerate(return_data.get('order_lines')) if
                              d["product_sku"] == product_code), None)
                return_data.get('order_lines')[index]=res[0]
            else:
                if product_quantity < product_stock:
                    subtotal = (product_detail.get('product_unit_price') * product_quantity)
                    return_data.get('order_lines').append({'product_sku': product_code,
                                                           'unit_price': product_detail.get('product_unit_price'),
                                                           'quantity': product_quantity,
                                                           'subtotal': subtotal,
                                                           'state': 'Draft'})
                else:
                    print("Not enough product quantities to sell")
        else:
            print("Sorry!,{} product code dose not exist".format(product_code))


    def create_sales_order(self,order_values):
        self.order_index += 1
        order_code = 'SO' + str(self.order_index)
        self.order_details.update({order_code:order_values})

    def change_order_state(self,order_code,from_stage,to_stage):
        self.order_details.get(order_code)['state'] = to_stage
        product_details=[]
        for product_detail in self.order_details.get(order_code)['order_lines']:
            product_detail['state']=to_stage
            product_details.append(product_detail)

            if self.state_done == to_stage:
                # deduct product stock
                product_stock=self.product_stock_details[product_detail.get('product_sku')]-product_detail.get('quantity')
                self.product_stock_details[product_detail.get('product_sku')] = product_stock

        self.order_details.get(order_code)['order_lines'] = product_details
        print("Order {} stage change to {}".format(order_code, to_stage))


    def set_order_to_draft(self):
        self.display_sales_order()
        order_code = input('Enter order ID :')
        if order_code in self.order_details:
            order_stage=self.order_details.get(order_code)['state']
            if self.state_draft == order_stage:
                print("Order stage already draft.")
            elif self.state_confirm == order_stage:
                print("Order is confirm stage.First cancel the order then move to draft stage.")
            elif self.state_done == order_stage:
                print("Order is done.Don't change the stage of the order. ")
            else:
                self.change_order_state(self.stage_cancel,self.state_draft)
        else:
            print("Order not exist")

    def set_order_to_confirm(self):
        self.display_sales_order()
        order_code = input('Enter order ID :')
        if order_code in self.order_details:
            order_stage = self.order_details.get(order_code)['state']
            if self.state_draft == order_stage:
                self.change_order_state(self.state_draft, self.state_confirm)
            elif self.state_confirm == order_stage:
                print("Order is already confirm.")
            elif self.state_done == order_stage:
                print("Order is done.Don't change the state of the order. ")
            else:
                print("Order is cancel stage.First draft the order then move to confirm stage.")
        else:
            print("Order not exist")

    def set_order_to_done(self):
        self.display_sales_order()
        order_code = input('Enter order ID :')
        if order_code in self.order_details:
            order_stage = self.order_details.get(order_code)['state']
            if self.state_draft == order_stage:
                print("Order is draft stage.First confirm the order then move to done stage.")
            elif self.state_confirm == order_stage:
                self.change_order_state(self.state_confirm, self.state_done)
            elif self.state_done == order_stage:
                print("Order is already done.")
            else:
                print("Order is cancel stage.")
        else:
            print("Order not exist")

    def set_order_to_cancel(self):
        self.display_sales_order()
        order_code = input('Enter order ID :')
        if order_code in self.order_details:
            order_stage = self.order_details.get(order_code)['state']
            if self.state_draft == order_stage:
                self.change_order_state(self.state_draft, self.stage_cancel)
            elif self.state_confirm == order_stage:
                self.change_order_state(self.state_confirm, self.stage_cancel)
            elif self.state_done == order_stage:
                print("Order is done.Don't change the state of the order.")
            else:
                print("Order is already cancel")
        else:
            print("Order not exist")

    def display_sales_order(self):
        i = 0
        for order_key, order_value in self.order_details.items():
            print("{:<5} '[{}] - {}'".format(i + 1, order_key, order_value['customer']))

    def print_sales_order(self):
        self.display_sales_order()
        order_id = input('Enter confirm order ID :')
        if order_id in self.order_details:
            print("   {}".format("______________________________Receipt______________________________"))
            print("{:>11}:{} {:>45}:{}".format("Order No", order_id, "Order Date",
                                               self.order_details.get(order_id)['order_date']))
            print("{:>14}:{}".format("Order State", self.order_details.get(order_id)['state']))

            customer_details = self.customer_details.get(self.order_details.get(order_id)['customer'])
            customer_address_details = self.customer_address_details.get(self.order_details.get(order_id)['customer'])

            print("   Customer :{},{} {:>31}:{}".format(self.order_details.get(order_id)['customer'],
                                                        customer_details.get('name'), "Address",
                                                        customer_address_details.get('address1')))
            print("{:>25} {:>35}".format(customer_details.get('email'), customer_address_details.get('address2')))
            print("{:>25} {:>38},{}".format(customer_details.get('phone'), customer_address_details.get('city'),
                                            customer_address_details.get('state')))
            print(" {:>63},{}".format(customer_address_details.get('zipcode'), customer_address_details.get('country')))
            print("\n")
            print("{:>15} {:>20} {:>20} {:>12}".format('Product Name', 'Product Price', 'Product Quantity', 'Subtotal'))
            print("   {}".format("====================================================================="))
            for product_detail in self.order_details.get(order_id)['order_lines']:
                product_details = self.product_details.get(product_detail.get('product_sku'))
                print(
                    "{:>15} {:>20} {:>20} {:>12}".format(product_details.get('name'), product_detail.get('unit_price'),
                                                         product_detail.get('quantity'),
                                                         product_detail.get('subtotal')))
            print("   {}".format("====================================================================="))
            total = "Order Total"
            print("{:>62} :{:>6}".format(total, self.order_details.get(order_id)['order_total_amount']))

        else:
            print("Order not exist")


sales = SalesManagment()

# print("Menu Driven Program")
# print("1.Add Product")
# print("2.Update Product Stock")
# print("3.Add Customer")
# print("4.Generate Sales Order")
# print("5.Set Order to Draft")
# print("6.Set Order to Confirm")
# print("7.Set Order to Done")
# print("8.Set Order to Cancel")
# print("9.Print Order Receipt")
# print("10.Exit")
while True:
    print("Menu Driven Program")
    print("1.Add Product")
    print("2.Update Product Stock")
    print("3.Add Customer")
    print("4.Generate Sales Order")
    print("5.Set to Draft")
    print("6.Confirm Order")
    print("7.Done Order")
    print("8.Set to Cancel")
    print("9.Print Order Receipt")
    print("10.Exit")

    choice = int(input('Enter your choice: '))
    if choice == 1:
        sales.manage_product()
    elif choice == 2:
        sales.update_product_stock()
    elif choice == 3:
        sales.manage_customer()
    elif choice == 4:
        sales.generate_sales_order()
    elif choice == 5:
        sales.set_order_to_draft()
    elif choice == 6:
        sales.set_order_to_confirm()
    elif choice == 7:
        sales.set_order_to_done()
    elif choice == 8:
        sales.set_order_to_cancel()
    elif choice == 9:
        sales.print_sales_order()
    elif choice == 10:
        exit(0)
    else:
       break
