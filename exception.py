while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again   ")

'''
def this_fails():
        x = 1/0
try:
        this_fails()
except ZeroDivisionError as err:
        print('Handling run-time error:', err)


try:
        raise NameError('Hi There!')
except NameError:
        print('An exception flew by!')
        raise

'''
# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except (ValueError) as Argument:
        print ("参数没有包含数字\n", Argument)

# 调用函数
temp_convert("xyz");
