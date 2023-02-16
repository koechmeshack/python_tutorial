class EmobilisStudent:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def hello_me(self):
        print(f"My Name  is {self.name} and im {self.age} years old")
    #creating an object
myobj=EmobilisStudent("Eric",30)

myobj.hello_me()
#create a class call magari , it should have mode,make ,year properties
#create min of three objects

class Magari:
    def __init__(self, mode,model, year):
        self.mode=mode
        self.model=model
        self.year=year
    def my_vehicles(self):
        print(self.mode , self.model ,self.year)
myobj=Magari("Nissan","toyota",2000)
myobj.my_vehicles()

class Workers:
    def __int__(self,name,Living,DOB):
        self.name=name
        self.living=living
        self.DOB=DOB
    def my_workers(self):
        print(self.name,self.living,self.DOB)
myobj=Workers("meshack","kitengela",2005)
myobj.my_workers()
