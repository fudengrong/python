# name = input('Please enter you name：');
# # print("My name is :"+name+",你好")

# print('I\'am \"ok\";')

# print('I \'am \"OK\" ,\nLearning Python');


# 'My name %s,I \'am %d years '%  ('fudengrong',20)
# List = ['Mack','jekk','Tke']
# len(List)

# age = 3
# if age >= 18:
#       print('your age is', age)
#       print('adult')
# else:
#       print('your age is', age)
#       print('teenager')

def My_test(x):
      if not isinstance(x,(int,float)):
            raise TypeError("bad operand type")
      if x >=0:
            return x
      else:
            return -x

My_test(1)