def fibonacci(n):
    if type(n)==str or n<0:
        return 'invalid input'

    elif n==0:
        return 0

    elif n==1:
        return 1

    else:
        return fibonacci(n-1)+fibonacci(n-2)    





def lucas(n):
    if type(n)==str or n<0:
        return 'invalid input'
    elif n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)            



def sum_series(n,firt=0,second=1):
    if firt==0 and second==1:
        return fibonacci(n)
    elif first==2 and second==1: 
        return lucas(n)
    else:
        if type(n)==str or n<0:
            return 'invalid input'
        elif n==1:
            return second
        elif n==0:
            return first    

        else:
            return sum_series(n-1,first,second)+sum_series(n-2,first,second)    

    


