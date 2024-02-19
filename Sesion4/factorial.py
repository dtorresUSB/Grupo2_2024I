
def fcnFactorial(n):
    value=1
    for i in range(n):
        value*=i+1
    return value


if __name__=="__main__":
    print(fcnFactorial(5))