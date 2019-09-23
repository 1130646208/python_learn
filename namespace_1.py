#Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
#其它的代码块（如 if/elif/else/、try/except、for/while等）
#是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，如下代码：
if True:
    msg = 'I am from Runoob'

print(msg)#正常输出

def test():
    msg_inner = 'I am from Runoob'

try:
    print(msg_inner)
except NameError as err:
    print('不能访问局部变量，发生异常。',err)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'msg_inner' is not defined


'''************************************'''

total = 0 # 这是一个全局变量

def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total
 
#调用sum函数
sum( 10, 20 )
print ("函数外是全局变量 : ", total)


'''************************************************'''
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num) 
    num = 123
    print(num)
fun1()
print(num)
print('***********************')
'''******************************'''
#如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）
#中的变量则需要 nonlocal 关键字了，如下实例：

def outer():
    num=1
    
    def inner():
        nonlocal num#use nonlocal to convert to outer 'num'
        num=20
        print(num)
    inner()
    
    print(num)
outer()




