class Test:
    def prt(self):
        print(self)
        print(self.__class__)


if __name__=='__main__':
    t= Test()
    t.prt()
