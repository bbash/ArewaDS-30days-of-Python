import math

"""_
    Exercises: Level 1
"""
# Question 1: create a class called Statistics and create
# all the functions that do statistical calculations as methods 
# for the Statistics class. Check the output below.

class Statistics:
   
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)
    
    def sum(self):
        sum = 0
        for num in self.data:
            sum += num
        return sum
    
    def min(self):
        self.data.sort()
        return self.data[0]


    def max(self):
        self.data.sort()
        return self.data[-1]


    def range(self):
        return (self.max() - self.min())
      
    def mean(self):
        return round(self.sum() / self.count())
    
    def median(self):
        self.data.sort()
        if self.count() % 2 == 0:
            midpoint = self.count() // 2
            return (self.data[midpoint] + self.data[midpoint + 1]) // 2
        else:
            midpoint = self.count() // 2
            return self.data[midpoint]

    def mode(self):
        dic = {}
        for num in self.data:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        list = [(v, k) for k, v in dic.items()]
        list.sort()
        mode, count = list[-1]
        return (count, mode)

    def std(self):
        
        u = self.mean()
        result = 0
        for number in self.data:
            m = (number - u) ** 2
            result += m
        
        return result / self.count()


    def var(self):
        u = self.mean()
        result = 0
        for number in self.data:
            m = (number - u) ** 2
            result += m
        
        return f"{math.sqrt(result / self.count()):.2f}"
        
    def freq_dis(self):
        dic = {}
        for num in self.data:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        list = [(k, v) for k, v in dic.items()]
        list.sort()
        return list
    
    
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print(data.count())
print(data.sum())
print(data.min())
print(data.max())
print(data.range())
print(data.mean())
print(data.median())
print(data.mode())
print(data.std())
print(data.var())
print(data.freq_dis())
print()

class PersonAccount:
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []
        
    def add_incomes(self, amount):
        self.incomes.append(amount)
    
    def add_expenses(self, amount):
        self.expenses.append(amount)
    
    def total_incomes(self):
        return sum(self.incomes)
    
    def total_expense(self):
        return sum(self.expenses)
    
    def account_balance(self):
        return self.total_incomes() - self.total_expense()
    
    def account_info(self):
        return print(f"{self.firstname} {self.lastname}, you total incomes {self.total_incomes()}, total expense {self.total_expense()} and account balance: {self.account_balance()}")
        

person = PersonAccount("UMAR", "USMAN ADAMU")
person.add_incomes(10)
person.add_incomes(10)
person.add_expenses(5)
person.add_expenses(5)
person.account_info()
person.add_expenses(5)
person.add_expenses(5)
person.account_info()






