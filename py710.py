def exp(p1,p2,df=0,*vart,**kw):
    print(f'参数1：{p1},参数2：{p2},默认参数：{df},可变参数：{vart},关键字参数：{kw}')

exp(1,2)
exp(1,2,c=3)
exp(1,2,3,'a','b')
exp(1,2,3,'abc','x=9')
 