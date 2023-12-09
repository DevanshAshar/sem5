class BaseError(Exception):pass
class HighValueError(Exception):pass
class LowValueError(Exception):pass
value = 18
while(1):
    try:
        n=int(input("Enter number:"))
        m=int(input("Enter number to check 0 div err"))
        a=n/m # div by 0 err
        di={'1':'one','2':'two'}
        li=[1,2,3]
        print(li[5]) #index err
        a,b=li #value err
        print(di['3']) #key err
        if n> value:
            raise HighValueError
        elif n < value:
            raise LowValueError
        else:
            print("Nice!Correct answer")
            break
    except LowValueError:
        print("Very Low Value, Give input again")
    except HighValueError:
        print("Very High value , give input again")
    except KeyError:
        print("in key error")
    except ZeroDivisionError:
        print("not allowed to divide by zero")
    except IndexError:
        print('index err')
    except LookupError:
        print('lookup err caught')
    except ValueError:
        print('Val err')
    except KeyboardInterrupt:
        print('keyboard intr err')
        break
    except:
        print('unknown err')
