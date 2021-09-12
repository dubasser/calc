def add(x,y):
    return float(x)+float(y)

def subtract(x,y):
    return float(x)-float(y)

def abs_average(x,y):
    return (abs(float(x))+abs(float(y)))/2

def multiplicate(x,y):
    return float(x)*float(y)

def divide(x,y):
    return float(x)/float(y)
print("Vvedite x:")
x=input()
print("Vvedite y:")
y=input()
print("Summa:"+str(add(x,y))+"   Raznost:"+str(subtract(x,y))+"   Srednee modylei:"+str(abs_average(x,y)))
print("Proizvedenie:"+str(multiplicate(x,y))+"   Chastnoe:"+str(divide(x,y)))
input()
