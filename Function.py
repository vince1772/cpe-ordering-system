import csv
import uuid
import datetime


class Food:
    foodList = []
    optionList = []

    foodSelected = []
    queueFood = []
    queueCount = 0

    def __init__(self):
        # list of food you want to add
        with open("data/food.csv", 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                # print(dict(row))
                self.foodList.append(dict(row))
        # list of option you want to add
        with open("data/option.csv", 'r') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                # print(dict(row))
                self.optionList.append(dict(row))

    def showFoodList(self):
        
        return ['{0} {1} Php'.format(i['Name'], i['Price']) for i in self.foodList]

    def showOptionList(self):
        
        return ['{0} {1} Php'.format(i['Name'], i['Price']) for i in self.optionList]

    def addFood(self, food, option={'Name': '', 'Price': 0}):
        
        foodOptionSelected = {
            'foodName': food['Name'],
            'foodOption': option['Name'],
            'sumPrice': food['Price'] + option['Price']
        }
        self.foodSelected.append(foodOptionSelected)

    def showFoodSelected(self):
        
        return ['{0} {1} {2} Php'.format(
                i['foodName'], i['foodOption'], i['sumPrice']) for i in self.foodSelected]

    def cancelFoodSelected(self, food):
        
        self.foodSelected.remove(food)

    def addQueueFood(self, table, foodSelectedList):
        """
        add a queue and table number on the selected food
        model data
        {
            'queue':1,
            'table':1,
            'foodSelectedList':[
                {'foodName': 'Food B', 'foodOption': '', 'total': 35},
                {'foodName': 'Food A', 'foodOption': '', 'total': 20}]
        }
        """
        self.queueCount += 1
        value = {'queue': self.queueCount,
                 'table': table, 'foodSelectedList': foodSelectedList}
        self.queueFood.append(value)
        self.foodSelected = []  # reset food selected list

    def clearQueueFood(self, queue):
        # remove queue with selected
        self.queueFood.remove(queue)

    def getAllQueue(self):
        return self.queueFood

    def getDetailQueue(self, queueNumber):
        for i in self.queueFood:
            if (i['queue'] == queueNumber):  # find detail
                return i

    def saveToDb(self, queue):
        """
        model queue
        {
            'queue':1, 
            'foodSelectedList':[
                {'name': 'Food B', 'price': 35},
                {'name': 'Food A', 'price': 20}]
        }
        """
        total = 0  # total price
        for food in queue['foodSelectedList']:
            total += food['total']

        genFoodId = str(uuid.uuid4())  # generate foodId for two files csv

        with open('data/db.csv', mode='w') as csvFile:
            fieldnames = ['Date', 'FoodId','FoodName', 'Total']
            writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'Date': str(datetime.datetime.now()),
                             'FoodId': genFoodId,
                             'Total': total
                             })

        with open('data/foodDb.csv', mode='w') as csvFile:
            fieldnames = ['FoodId', 'FoodName']
            writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
            writer.writeheader()

            for food in queue['foodSelectedList']:
                writer.writerow({'FoodId': genFoodId,  # generate unique id
                                 'FoodName': food['foodName']
                                 })

        self.queueFood.remove(queue)  # remove this queue from queue food


if __name__ == "__main__":
    x = Food()
    x.addFood({'Name': 'Food A', 'Price': 10}, {
              'Name': 'Option B', 'Price': 10})
    x.addFood({'Name': 'Food B', 'Price': 20})
    x.addQueueFood(5, x.foodSelected)
    x.saveToDb(x.queueFood[0])
