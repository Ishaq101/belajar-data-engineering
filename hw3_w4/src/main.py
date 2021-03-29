import plusone, square, fibonaci

plusone = plusone.plus_one
square = square.square
fibonaci = fibonaci.fibonaci

class The_function:
    def __init__(self,start,end,function):
        self.start = start
        self.end = end
        function(self.start,self.end)


test_plusone = The_function(2,29,plusone)
test_square = The_function(2,29,square)
test_fibonaci = The_function(2,29,fibonaci)