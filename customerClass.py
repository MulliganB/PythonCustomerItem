class itemClass():
    name = ""
    price = 0
    description = ""

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
    
    def getName(self):
        return self.name
    def getPrice(self):
        return self.price
    def getDescription(self):
        return self.description
    
    def setName(self, name):
        self.name = name
    def setAge(self, price):
        self.price = price
    def setDescription(self, description):
        self.description = description

class listOfItems():
    itemList = []

    def addItem(self, newItem):
        self.itemList.append(newItem)
    
    def deleteItem(self, itemName):
        for i in self.itemList :
            if (i.getName() == itemName):
                del i

    def getItems(self):
        return self.itemList

    def getItem(self, index):
        return self.itemList[index]

    def getItemByName(self, name):
        for i in self.itemList :
            if i[0] == name :
                return i

class customerClass():
    name = ""
    age = 0
    address = ""
    telephone = ""
    itemList = listOfItems()

    def __init__(self, name, age, address, telephone):
        self.name = name
        self.age = age
        self.address = address
        self.telephone = telephone
    
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getAddress(self):
        return self.address
    def getTelephone(self):
        return self.telephone
    
    def setName(self, name):
        self.name = name
    def setAge(self, age):
        self.age = age
    def setAddress(self, address):
        self.address = address
    def setTelephone(self, telephone):
        self.telephone = telephone

    def displayContents(self):
        contents = "Name: ", self.name, " Age: ", self.age, " Address: ", self.address, " Telephone Number: ", self.telephone
        return contents

    def displayContactInfo(self):
        contents = "Name: ", self.name, " Address: ", self.address, " Telephone Number: ", self.telephone
        return contents

    def displayList(self):
        return self.itemList.getItems()

    def displayListItem(self, index):
        return self.itemList.getItem(index)

    def searchList(self, itemName):
        return self.itemList.getItemByName(itemName)

    def addItem(self, newItem):
        self.itemList.addItem(newItem)
    
    def deleteItem(self, itemName):
        self.itemList.deleteItem(itemName)

def createCustomerList():
    customer1 = customerClass("John Goodman", 55, "123 Place Street", "12335 098678")
    customer2 = customerClass("Jane Goods", 25, "23 Nothing Lane", "22335 098678")
    customer3 = customerClass("Henry Smith", 35, "1 Anotherplace Avenue", "12345 098678")
    customer4 = customerClass("Eve Doe", 21, "95 Place Street", "23335 098678")

    customerList = [customer1, customer2, customer3, customer4]

    return customerList

def mainfunction():
    aList = createCustomerList()
    newItem = ("Item 1", 100, "A description of an item.")
    aList[0].addItem(newItem)
    print("")
    print ("Name of First Item (search by index): ", aList[0].displayListItem(0)[0])
    print ("Price of First Item (search by index): ", aList[0].displayListItem(0)[1])
    print ("Description of First Item (search by index): ", aList[0].displayListItem(0)[2])
    print("")
    print ("Name of First Item (search by name): ", aList[0].searchList("Item 1")[0])
    print ("Price of First Item (search by name): ", aList[0].searchList("Item 1")[1])
    print ("Description of First Item (search by name): ", aList[0].searchList("Item 1")[2])
        
    print("")
    print ("**-----All Contents-----**")
    for i in aList :
        print (i.displayContents())

    print("")

    print ("**-----Contact Information-----**")
    for i in aList :
        print (i.displayContactInfo())
    
    print("")

    print ("**-----Over 35 Contact Information-----**")
    for i in aList :
        if(i.getAge() >= 35):
            print (i.displayContactInfo())
    print("")
mainfunction()