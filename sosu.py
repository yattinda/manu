def sosu(max):
    num = 2
    while(num <= max):
        prime = True
        for i in range(2,num):
            if (num % i == 0):
                prime = False
                break
        if prime:yield num
        num += 1

a = sosu(int(input("number")))

for i in a:
    print(i,end=",")
