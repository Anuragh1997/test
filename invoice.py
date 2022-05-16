class invoice:
    def __init__(self,partnumber,partdescription,quantity,price):
        self.partno=partnumber
        self.partdesc=partdescription
        self.qnt=quantity
        self.itemprice=price
    def getinvoice(self):
        result=0
        print(self.partno)
        print(self.partdesc)
        print(self.qnt)
        print(self.itemprice)
        result=self.qnt*self.itemprice
        if self.qnt<0:
            result=0*self.itemprice
        if self.itemprice<0:
            result=self.qnt*0.0
        print(result)
inv=invoice(1,"demo",10,-20)
inv.getinvoice()
