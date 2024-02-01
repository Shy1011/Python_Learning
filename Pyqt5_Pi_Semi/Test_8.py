"""
解释了pyhton的命名空间问题


"""
class Test_1():
    test = 1

    def printf(self):
        test = 2
        print("self.text" + str(self.test))
        print("test" + str(test))


x = Test_1()
x.printf()