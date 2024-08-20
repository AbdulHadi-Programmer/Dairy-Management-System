print("Dairy Management System")
# Bro if anyone Come to my file and see the code then welcome but this is note for the collaborator that is make an other file and write changes in that and also write a heading and para what did you change and defined all above and also what did you remove and why also give the reasons.

class Profit_Management:
    def calculate_profit_percentages_and_add_to_price(self, price):
        # global product_specific_category
        # try :
        #     product_specific_category = int(input("\nSelect the Product to Caculate the Profit: \n1. Milk Shakes \n2. Cold Items (Pakola, Rooh Afza, lassi, milk bottle, cold milk) \n3. Boiled Milk \n4. Milk \n-- Enter the Option: "))
            
        # except Exception as e :
        #     print(e)
        #     self.profit_percentages(price)      

        product_specific_category = int(input("\nSelect the Product to Caculate the Profit: \n1. Milk Shakes \n2. Cold Items (Pakola, Rooh Afza, lassi, milk bottle, cold milk) \n3. Boiled Milk \n4. Yogurt \n5. Milk \n-- Enter the Option: "))
        
        match product_specific_category:
            case 1:  # Milk Shakes
                milkshakes = int((price / 100 ) * 50) # 50 percent profit
                # This function can now return the exact selling price because it add the profit percentage to that 
                return milkshakes + price
            
            case 2:  # Cold Items list
                cold_items_lst = ['Pakola Milk', 'Rooh Afza Milk', 'Cold Ice Milk', 'Lassi', 'Bottle Milk']
                cold_item = (price / 100) * 35 # 35 is the profit percentage to calculate and this only calculate the profit not add in the price.
                return cold_item + price
            
            case 3: # Boiled Milk
                boiled_milk = (price/ 100) * 30
                return boiled_milk + price
            
            case 4: # Yougurt 
                yogurt = (price /100) * 45
                return yogurt  + price 

            case 5: # Milk
                milk = (price/100) * 50 # last arg is profit percentage nn
                return milk + price

    def products_list(self):
        cold_items_lst = ['Milk', 'Pakola Milk', 'Rooh Afza Milk', 'Cold Ice Milk', 'Lassi']
        items = ['Chocolate Milkshake', 'Strawberry Milkshake', "Banana Shake", 'Bottle Milk']
        cold_items_lst.extend(items)
        # print(cold_items_lst)
        print("\nThe List of Product List: \n", "-"*25)
        for i, j in enumerate(cold_items_lst, start=1):
            print(f"{i}. {j}")
        print()

    

p = Profit_Management()
print(p.profit_percentages(400))
p.profit_percentages(400)
p.products_list()