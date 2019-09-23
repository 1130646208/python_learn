class people:
    name=''
    age=0

    #def private var
    __weight=0
    #def construction method

    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.weight=w

    def speak(self):
        print("{} says:I'm {}years old.（people class）".format(self.name,self.age))

wsx=people('wsx',16,56)
wsx.speak()

fy=people('fy',16,50)
fy.speak()

#单继承范例

class student(people):
    grade=''
    def __init__(self,n,a,w,g):
        #use father class cons method
        people.__init__(self,n,a,w)
        self.grade=g
    #override father speak method
    def speak(self):
        print("{} says:I'm a student of {},I'm {}years old.(student class)".format(self.name,self.grade,self.age))


wsx=student('wsx',20,56,'grade 6')
wsx.speak()

#student 是子类，现在调用父类方法

child=student('child',20,56,'grade 6')

child.speak()#调用子类方法
super(student,child).speak()#调用父类方法


