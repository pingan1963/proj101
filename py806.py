class DefaultInit(object):
      
      def __init__(self):
        print('我是不带参数的__init__构建方法')
      def __init__(self,param):
        print('我是带参数的__init__构建方法,参数值为：{param}')     

DefaultInit('hello')
print('类实例化结束')
# test.show()