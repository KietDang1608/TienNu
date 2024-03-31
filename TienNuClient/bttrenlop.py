def print_args(*args):
    for arg in args:
        print(arg)

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"key:{key} , value: {value}")
        
def printboth(*args,**kwargs):
    for arg in args:
        print(arg)
    for key,value in kwargs.items():
        print(f"key:{key} , value: {value}")
        
printboth(1, 'two', third=3,fourth = 'IV')
def my_decor(func):
    def wrapper():
        print("cai qq j do truoc khi goi ham")
        func()
        print("Cai qq j do sau khi goi ham")
    return wrapper
@my_decor
def say_hello():
    print("Xin chao")

say_hello()