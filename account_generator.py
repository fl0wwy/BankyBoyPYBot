import datetime
from typing import Union,Optional

class Account:
    def __init__(self,id: int,balance: Optional[Union[int,float]]=None ,salary: Optional[Union[int,float]]=None) -> None:
        self.id = id
        self.date = ''
        self.balance = balance
        self.expenses = {}
        self.deposits = {}
        self.salary = salary
    def expense(self,amount: Union[int,float,str],place: str,products : str):
        if type(amount) == str:
            if amount.isdecimal():
                amount = float(amount)
            else:
                raise TypeError("Expense amount must be a decimal value!")        
        self.expenses[place] = {'Place': place,'Amount' : amount, 'Products Purchased': products or None, 'Time' : datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}
        self.balance -= amount
        return self.expenses[place]
    def deposition(self,amount: Union[int,float,str],sender: str, reason: str = None):
        if type(amount) == str:
            if amount.isdecimal():
                amount = float(amount)
            else:
                raise TypeError("Expense amount must be a decimal value!") 
        self.deposits[sender] = {'Sender': sender,'Amount' : amount, 'Reason': reason, 'Time': datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}
        self.balance += amount
        return self.deposits[sender]
    def __str__(self):
        return f'Account Balance: {self.balance}'








        
