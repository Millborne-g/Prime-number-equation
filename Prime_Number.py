def factors(x):
    print("\nThe factors of",x,"are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

def equation():
    print("\nUsing Y=8X^2+1 equation:")
    for i in range(-5,5):
        y=8*(pow(i,2))+1
        print("\ny =","8(",i,")^2 +1")
        print("y =",y)
    

X = int(input("Input the value X: "))         
PrimeNumber = False

if X > 1:
    n = int(X/2)+1
    for i in range(2,n):
        if (X % i) == 0:
            print("The value",X, "is not a prime number")
            PrimeNumber = True
            break
    else:
        print("The value",X, "is a prime number")

else:
    print("The value",X, "is not a prime number")
    PrimeNumber = True

    

if PrimeNumber == True:
    factors(X)
    
equation()
