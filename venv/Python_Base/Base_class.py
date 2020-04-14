
class DuolaAmeng:
    #定义一个初始化函数，将类中的属性进行初始化
    def __init__(self,name):
        self.name = name
        print('我叫'+self.name)
        #self.ages = ages
        #print('我今年'+self.ages+'岁了')
    #
    def getzuoqingting(self):
        print('给'+self.name+',一只蜻蜓来玩！')

class DuolaBmeng(DuolaAmeng):
    def getZhuayu(self):
        print('给'+self.name+',一只鱼来吃！')




duolaB = DuolaBmeng('Bmeng')
duolaB.getzuoqingting()
duolaB.getZhuayu()

duolaA = DuolaAmeng('Ameng')
duolaA.getZhuayu()



