
class Person:
    def __init__(self,name):
        self.name = name #public accessable outside of class
        self._salary = 4000 #private, only in class
    
    @property #salary turned from method to PROPERTY, getter
    def salary(self):
        return round(self._salary)  
    
    @salary.setter
    def salary(self,salary):
        if salary < 0:
            raise ValueError('No')
        self._salary = salary
           

p = Person('Ahmed')
p.salary = 420

#OLD way 

class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0

    def get_balance(self):
        return round(self._balance)

    def set_balance(self, balance):
#Javascript: if( type(balance) !== Numbre || float )
        if type(balance) not in [int, float]:
            return

        if  balance < 0 or balance >= 100000:
              return
        
        self._balance= balance
        
#NEW WAY

