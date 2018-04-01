class Animals(object):         
    def __init__(self, name, health):
        # set some instance variables
        self.name = name
        self.health = health
    def Walk(self):
        self.health -= 1
        return self
    def Run(self):
        self.health -= 5
        return self
    def Display_h(self):
        print "name: {n}".format(n=self.name)
        print "health: {h}".format(h=self.health)
        return self
class Dog(Animals):
    def __init__(self, name, health=150):
        super(Dog, self).__init__(name, health)
    def pet(self):
        self.health += 5
        return self
class Dragon(Animals):
    def __init__(self, name, health=170):
        super(Dragon, self).__init__(name, health)
    def fly(self):
        self.health += 10
        return self
    def display_dh(self):
        super(Dragon, self).display_dh()
        print "I am a Dragon!"
        return self

print " enter a couple animals ================================================== "
rat = Animals("rat",30).Display_h().Walk().Walk().Walk().Run().Run().Display_h()
print " "
dog = Animals('dog, 40)
dog.Display_h().Walk().Walk().Walk().Run().Run().Pet().Display_h()
print " "
cat = Animal('cat', 20)
print cat.name
cat.walk().walk().walk().run().run().display_health() 
print " "
dragon1 = Dragon('PUFF')
print dragon1.name
dragon1.walk().run().fly().display_dh()
