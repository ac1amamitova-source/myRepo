class Money:
    def __init__(self,amount,currency):
        self.amount=amount
        self.currency=currency

#стоковые представления
    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __repr__(self):
        return f"{self.amount} {self.currency}" 

#оперативные сравнения
    def __eq__(self,other):
        if isinstance(other,Money):
            return self.amount==other.amount 

    def __lt__(self,other):
        if isinstance(other,Money):
            return self.amount<other.amount 

    def __gt__(self,other):
        if isinstance(other,Money):
            return self.amount>other.amount 

#Арифметические операции

    def __add__(self):
        return Money(self.amount+other.amount,self.currency)
    def __sub__(self):
        return Money(self.amount-other.amount,self.currency)
    def __mul__(self):
        return Money(self.amount*other.amount,self.currency)

print("Hello world")   