class Car(object):         
    # the __init__ method is called every time a new object is created
    def __init__(self, price, speed, fuel, mileage):
        # set some instance variables
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.taxrate = .15
        else:
            self.taxrate = .12 
    def display_all(self):
        print "price: ${p}".format(p=self.price)
        print "speed: {ms}mph".format(ms=self.speed)
        print "fuel: {f}".format(f=self.fuel)
        print "mileage: {ml}mpg".format(ml=self.mileage)
        print "taxrate: {tx}".format(tx=self.taxrate)
        print " "
        return self

Car(2000,35,"FULL",15).display_all()
       
Car(2000,5,"NOT FULL",105).display_all()

Car(2000,15,"KIND OF FULL",95).display_all()

Car(2000,25,"FULL",25).display_all()

Car(2000,45,"EMPTY",15).display_all()

Car(2000000,35,"EMPTY",15).display_all()