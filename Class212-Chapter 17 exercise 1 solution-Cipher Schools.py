def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('you cannot divide by zero')
    except TypeError:
        print('numbers must be int or float')
    except:
        print('unexpected error')
    
print(divide(10,0))
