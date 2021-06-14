# Python解释器会自动检查参数个数
# 内置函数abs()有参数检查，自定义函数my_abs()没有，完善函数定义，只允许整数和浮点数：
def my_abs(x):
   if not isinstance(x, (int, float)):    #函数isinstance(object, classinfo)判断对象object是否为已知类型classinfo
       raise TypeError('bad operand type')    #如满足条件则抛出错误
   if x >= 0:
       return x
   else:
       return -x

# 测试git
# the first change
# the secound change
# the third change
