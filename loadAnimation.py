from time import sleep

def loader(iteration,total):
    percentage = 100 * iteration/float(total)
    
    print("["+"*"*int(percentage)+"-"*int(100-percentage)+"]"+str(percentage)+"%",end='\r')

for i in range(1,11):
    loader(i,10)
    sleep(0.5)
print()
