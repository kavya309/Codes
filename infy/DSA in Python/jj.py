def check(list1,name):
    try:
        tot=0
        for ele in list1:
            tot+=ele
        avg=tot_val//len(list1)
        pwd=avg+name
        return int(pwd)
    except valueError:
        print('Value error in check')
    except TypeError:
        print('Type error in check')
    except NameError:
        print('Name error in check')
    finally:
        print('Finally in check')
list1=[10,20,30,40,50]
try:
     check(list1,'Tara')
except NameError:
    print('Name error in main')
finally:
    print('finallyin main')
