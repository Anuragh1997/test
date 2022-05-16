class calculator:
    def add(self,a,b):
       c=a+b
       print(c)
    def subtract(self,a,b):
       c=a-b
       print(c)
    def multiply(self,a,b):
       c=a*b
       print(c)
    def divide(self,a,b):
       c=a/b
       print(c)
class usecalculator(calculator):
    object=calculator()
    object.add(10,20)
    object.subtract(10,20)
    object.multiply(10,20)
    object.divide(10,20)
