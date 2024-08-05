def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
def fibonacci_series(n):
    series = []
    for i in range(1,n+1):
        series.append(fibonacci(i))
    return series 
list=(fibonacci_series(10))
print(list)


