#!/usr/bin/python3
from module import module_1 # 引入模块1 module_1
from module.module_2 import printx # 只是从module2导入其中一个函数/class
# from module.module_2 import * # 从module中引入所有

dog = module_1.Animal()

print(module_1.a)# 这个在引用模块的 变量/函数/类时 就需要加上模块名
printx()# 不需要加上模块名