def hello():
    print("This is my my first function")
hello()
def calculate():
    x=30
    y=50
    print(x*y)
calculate()
def majina(fname,lname):
    print(fname+" "+lname)
majina("eric","were")
majina("hesbon","maina")
majina("lamech" ,"mwangi")
majina("meshack","koech")

def greetings (name, greetings="hello"):
    print(greetings + " "+name)
greetings("Eric")
greetings("joan","niaje")


def list (item, price="price  is "):
        print(item +" "+ price)
        price("100")

def maxvalu(a, b, c, d, e, f):
    return max(a,b,c,d,e,f)
results=maxvalu(7,9,1,8,17,45)
print(results)
def minvalu(z,f,g,h,k,y):
    return min(z,f,g,k,y)
results=minvalu(6,40,90,34,20,60)
print(results)
def sort_list (list):
    return sorted(list)
answer =sort_list([3,9,0,2,7,1,5,6,4,2])
print(answer)
def print_numbers(n):
    for i in range (n):
        print(i)
print_numbers(5)