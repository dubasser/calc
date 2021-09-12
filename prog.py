def add(x,y):
    return float(x)+float(y)

def subtract(x,y):
    return float(x)-float(y)

def abs_average(x,y):
    return (abs(float(x))+abs(float(y)))/2

x=input()
y=input()
print("Summa:"+str(add(x,y))+"   Raznost:"+str(subtract(x,y))+"   Srednee modylei:"+str(abs_average(x,y)))
input()
