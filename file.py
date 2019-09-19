f=open("foo.txt", "w")

num=f.write("Python is very niub!\nYES!!!!\n")
print('写入了{}个字符,当前指针{}'.format(num,f.tell()))


f.close()


f=open("foo.txt", "r")
str=f.read()
print(str)
f.close()


f=open("foo.txt", "r")
str = f.readlines()
print(str)
for line in f:
    print(line, end='')

f.close()


'''
f.seek()

如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。

from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：

    seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
    seek(x,1) ： 表示从当前位置往后移动x个字符
    seek(-x,2)：表示从文件的结尾往前移动x个字符 
'''


with open('foo.txt', 'r') as f:
     read_data = f.read()
     
from urllib import request

response = request.urlopen("http://www.baidu.com/")  # 打开网站
fi = open("project.txt", 'w')                        # open一个txt文件
page = fi.write(str(response))                # 网站代码写入
fi.close()                                           # 关闭txt文件
