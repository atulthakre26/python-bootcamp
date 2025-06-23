class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real, "i +", self.img, "j")
    
num1 = ComplexNumber(1,2)
num1.showNumber()

     
             