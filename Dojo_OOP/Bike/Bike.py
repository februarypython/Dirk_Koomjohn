
# declare a class and give it name User
class Bike(object):
    # the __init__ method is called every time a new object is created
    def __init__(self, price, maxspeed):
        # set some instance variables
        self.price = price
        self.maxspeed = maxspeed
        self.miles = 0
    def displayinfo(self):
        print "bike price: ${p}, maxspeed: {ms}mph, milage: {m}".format(p=self.price, ms=self.maxspeed, m=self.miles)
        return self
    def ride(self):
        self.miles += 10
        print "Riding - bike milage: {ms}".format(ms=self.miles)
        return self 
    def reversing(self):
        if self.miles > 5:
            self.miles = self.miles -5
        else:
            self.miles = 0
        print "Reversing - bike milage: {m}".format(m=self.miles)
        return self
        
Bike(222,22).displayinfo().ride().ride().ride().reversing().displayinfo()
Bike(222,22).displayinfo().ride().ride().reversing().reversing().displayinfo()
Bike(222,22).displayinfo().reversing().reversing().reversing().displayinfo()

