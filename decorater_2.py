from functools import wraps

def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):#<--------------
        if not can_run:#                           |
            return "Function will not run" #       |
        return f(*args, **kwargs)#先返回被装饰函数 |
    return decorated #再返回-----------------------

#先返回被装饰函数（带参数），再逐层从内到外返回函数（不带参数。？）



@decorator_name
def func():
    return("Function is running")
 
can_run = True
print(func())
# Output: Function is running
 
can_run = False
print(func())
