class Fudengrong:
    #构造函数并初始化，
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
    #定义一个SayHi的方法
    def SayHi(self):
        print('Hi my name is %s,I am %s years old '%(self.Name,self.Age))
        #self.__talk()

    #私有属性
    #def __talk(self):
    #    print('I am private')

    #定义一个析构函数,程序结束后释放内存
    def __del__(self):
        print('Say godbye %s'%(self.Name))



p = Fudengrong('ale',32)
p.SayHi()

#del p

#print('##'*40)
#p2 = Fudengrong('syde',45)
#p2.SayHi()