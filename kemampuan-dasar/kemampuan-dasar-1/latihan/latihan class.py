class Person:
    def __init__(self, name):
        self.name = name
        self.alamat = alamat
        self.nohp = nohp
        

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()