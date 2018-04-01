class Products(object):         
    def __init__(self, price, item, wt, brand, tax_rate, ret_reason):
        # set some instance variables
        self.price = price
        self.item = item
        self.wt = wt
        self.brand = brand
        self.status = "for sale"
        self.tax_rate = tax_rate
        self.ret_reason = ret_reason
    def Sell(self):
        self.status = "sold"
        return self
    def Prodreturn(self):
        if self.ret_reason == "def":
            self.price = 0
            self.status = "defective"
        elif self.ret_reason == "new":
            self.status = "for sale"
        elif self.ret_reason == "open":
            self.status = "used"
            self.price = self.price * .8
        return self
    def Addtax(self):
        print "initial price: ${p}".format(p=self.price)
        print "tax rate: ${p}".format(p=self.tax_rate)
        plustax = self.price * (self.tax_rate + 1)
        return plustax
    def display_all(self):
        print "price: ${p}".format(p=self.price)
        print "item: {ms}".format(ms=self.item)
        print "wt: {ml}".format(ml=self.wt)
        print "brand: {f}".format(f=self.brand)
        print "status: {st}".format(st=self.status)
        print "tax_rate: {tr}".format(tr=self.tax_rate)
        print "reason for return: {rr}".format(rr=self.ret_reason)
        print " "

print " enter a couple product ================================================== "
Products(20,"shoes","4 lbs","Converse","","").display_all()
Products(20,"shoes","4.5 lbs","Nike","","").Sell().display_all()

print "return a price after adding sales tax =========================================="
pricewithtax = Products(20,"shoes","4 lbs","Converse",.10,"").Addtax()
print  "price with tax: {pt}".format(pt=pricewithtax)
print " "

print "return some products ========================================="
Products(20,"shoes","4 lbs","Converse",0,"def").Prodreturn().display_all()
Products(20,"shoes","4.4 lbs","Addidas",0,"open").Prodreturn().display_all()
Products(20,"shoes","4 lbs","Converse",0,"new").Prodreturn().display_all()
