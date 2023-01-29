class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        raise NotImplementedError('younhave to define this method in subclasses ')
class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return 'bow bow'


class Cat(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        return 'meow meow'


doggy=Dog('boony','pug')
print(doggy.sound())
