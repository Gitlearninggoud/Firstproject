class computerA :

    def __init__(self,name,age) :
        self.name=name
        self.age=age
        
    def configB(self) :
        print("this is i5A processor \n")
class computerB (computerA) :
    def __init__(self,name,age) :
        self.name=name
        self.age=age
     
    def configB(self,name) :
        print("this is i5B processor \n"+self.name)        

        
com1=computerB("Don",40)
com1.configB()

