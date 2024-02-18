class MyClass:
    def __init__(self):
        self._value = None
        self._callback = None

    def set_callback(self, callback):
        self._callback = callback

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if self._value != new_value:
            self._value = new_value
            if self._callback:
                self._callback()

def callback_function():
    print("Value has changed!")

# 创建 MyClass 实例
obj = MyClass()

# 设置回调函数
obj.set_callback(callback_function)

# 修改 value 属性的值
obj.value = 10  # 这将触发回调函数

# 再次修改 value 属性的值
obj.value = 20  # 这也将触发回调函数
