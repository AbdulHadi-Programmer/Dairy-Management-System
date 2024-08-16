# Dairy Shop inventory management system

class product:
    def __init__(self, Name, Quantity, Base_Price):
        self.name = Name.title()
        self.quantity = Quantity
        self.__buyprice = Base_Price

    def productInfo(self):
        print(f"\nProduct: {self.name}\nBase Price: {self.__buyprice}\nQuantity: {self.quantity}")

milk = product("Milk", "5 litres", "170 Rupees/litre")
yogurt = product("Yogurt", "5 Kg", "200/kg") # 200 rs/kg as we buy it for 320-300rs/kg

class Inventory():    # --> Inventories
    def __init__(self, ID, Product_List): # The reason for inventory name/ID is to keep an identification of inventories when working with multiple.
        self.invID = ID
        self.prdList = Product_List     # Taking a list of product objects

        # Checks if the "Product_List" is given a list datatype as input or not.
        if not isinstance(Product_List, list):
            raise TypeError("Error: Product List is supposed to be some sort of list.")
        
        # Checks if all the elements in the list are objects of "Product()" class or not.
        for prd in self.prdList:
            if not isinstance(prd, product):
                print("Error: Only objects of class product are applicable, item was not added.")
                self.prdList.remove(prd)

        self.prdListInfo = {}
        for prds in self.prdList:
            self.prdListInfo[prds.name] = [prds.quantity, prds._product__buyprice]

    def addProduct(self, Product): # Adds a product(object) to the inventory
        if not isinstance(Product, product):
            print("Error: Only objects of class product are applicable.")
        elif Product in self.prdList:
            print("Product is already present in the inventory.")
        else:
            self.prdList.append(Product)
            self.prdListInfo[Product.name] = [Product.quantity, Product._product__buyprice]
            print(f"{Product.name} has been added to the inventory.")

    def remProduct(self, Product): # Removes a product from the inventory
        if not isinstance(Product, product):
            print("Error: Only objects of class product are applicable.")
        elif Product in self.prdList:
            self.prdList.remove(Product)
            self.prdListInfo.pop(Product.name)
            print(f"{Product.name} has been deleted from the inventory.")
        else:
            print("The given product is not present in the inventory.")

    def invInfo(self):
        print(f"Inventory ID: {self.invID}\nProducts:\n{self.prdListInfo}")

    def updateProduct(self, Product, New_Buy_Price): # Updates the info of the product (C.P, )
        if not isinstance(Product, product):
            print("Error: Only objects of class product are applicable.")
        elif Product in self.prdList:
            print(f"The Cost Price of {Product.name} has been changed from {Product._product__buyprice} to {New_Buy_Price}")
            Product._product__buyprice = New_Buy_Price
            self.prdListInfo[Product.name][1] = New_Buy_Price
        else:
            print("Product is not present in the inventory.")


# Testing
inv = Inventory(4002, [milk,yogurt])
inv.invInfo()
inv.remProduct(yogurt)
# inv.invInfo()
inv.addProduct(yogurt)
# inv.invInfo()
inv.updateProduct(milk, "200 Rupees/litre")
# inv.addProduct()
inv.invInfo()
