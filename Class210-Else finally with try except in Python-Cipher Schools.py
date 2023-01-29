while True:
    try:
        number=int(input('enter a number: '))
    except ValueError:
        print("you didn\'t entered integer")
    except:
        print('unexpected error')
    else:
        print(f"user input {number}")
        break
    finally:
        print('finally blocks......')
