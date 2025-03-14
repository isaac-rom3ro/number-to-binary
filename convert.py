class Binary:
    def __init__(self, number: int): 
        self.number = number

    def convertNumberToBinary(self):
        dividend = self.number
        divisor = 2
        quocient = 0
        binaryNumber = []

        while(dividend > 1):
            rest = int(dividend % divisor)
            quocient = int(dividend / divisor)
            dividend = quocient

            binaryNumber.append(rest)

            
        binaryNumber.append(quocient)

        return binaryNumber
