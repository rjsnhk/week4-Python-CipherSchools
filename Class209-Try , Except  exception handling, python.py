while True:
    try:
        age = int(input('enter your age: '))
        break
    except ValueError:
        print('maybe you entered string instead of number,try again')
    except:
        print('unexpected error')
if age<18:
    print('you can\'t play this game')
else:
    print('you can play this game')
