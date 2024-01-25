class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self,x):
        print("Bark! Bark!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# 创建实例并调用方法
animal = Animal()
animal.make_sound()  # 输出: Some generic sound

dog = Dog()
dog.make_sound(1)  # 输出: Bark! Bark!

cat = Cat()
cat.make_sound()  # 输出: Meow!
