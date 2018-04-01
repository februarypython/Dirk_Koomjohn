class MathDojo(object):
    def __init__(self):
        self.result = 0
    
    def add(self, *args):
        if not args:
            print "Nothing to add"

        sum = 0
        elif type(arg) == list: 
             for idx in range(len(arg)):
                sum += arg[idx]      #add up the numbers passed in
             arg = argsum            #arg is now the sum of all values in list
        elif type(arg) == tuple:     #handle tuples
             for val in arg:
                sum += val #add values in tuples
        self.result += sum
        return self

    def subtract(self, *args):
        if not args:
            print "Nothing to subtract"

        total = 0
        elif type(arg) == list:      #dealing with list
             for idx in range(len(arg)):
                total += arg[idx]    #add all input args to get a total to subtract
        elif type(arg) == tuple:     #handle tuple
             for val in arg:
                total += val         #sum up all values in tuple
        self.result -= total
        return self



md = MathDojo()
# print md.add(2).add(2,5).subtract(3,2).result  #returns 4
# print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result  #returns 28.15
