from Calculator import addition, division, subtraction, multiplication

def dataParse(data):
    line = str(data)
    temp = []

    for el in line:
        if el == "+":
            temp=line.split("+")
            print(temp)
            calculator = addition(int(temp[0]), int(temp[1]))
            return calculator
        
        if el == "-":
            temp=line.split("-")
            print(temp)
            calculator = subtraction(int(temp[0]), int(temp[1]))
            return calculator
        
        if el == "*":
            temp=line.split("*")
            print(temp)
            calculator = multiplication(int(temp[0]), int(temp[1]))
            return calculator
        
        if el == "/":
            temp=line.split("/")
            print(temp)
            calculator = division(int(temp[0]), int(temp[1]))
            return calculator