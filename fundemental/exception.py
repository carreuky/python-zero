#try is hen the code is run,
try:
    int('hello')
except ValueError as e:
    # error will be printed out instead of a massive error message
    print('exception', e)
except ZeroDivisionError as e:
    #error regarding divived by zero
    print('wrong', e)
except Exception as e:
    #takes both types of exception like the prevous two
    print('third excecption', e)
finally:
    print('last time to run')
print('done')

#bring an error on unique cirustances

# raise Exception('this is error')
num= ' narberal gamma'
if not num.isdigit():
    raise Exception('no a number')

 