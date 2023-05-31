from time import sleep
for i in range(5):
    print(i)
    sleep(0.5)
    
    for i in 'abc':
        print(i)
        for i in'abc':
            print(i,end=",")
            
           