def outer():
    i = 10
    def inner():
        nonlocal i  # 先声明i是nonlocal变量
        i = 20  # 然后对i进行赋值
    inner()
    print(i)  # 输出20，说明外层的i被内层函数修改了

outer()