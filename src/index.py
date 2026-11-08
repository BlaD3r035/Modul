# main code (only main menu,flow. Allocate functions in func folder  ) 
import os
import time
from func.conversions import conversions
from func.prints import prints as pr
from func.verify import verify
conv = [] # (decimal,binary,octal,hexadecimal)

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate(base: int):
    clearConsole()
    print("Write your number below")
    str_num = input()
    
    if(not verify.verifyNumType(str_num,base)):
        clearConsole()
        print("Not a valid number...")
        time.sleep(1)
        return calculate(base)
    decimal = (int(str_num) if base == 10 else conversions.toDecimal(str_num,base)[0])
    if(decimal > 1000000):
        print("number is bigger than 1.000.000 (decimal), try again...")
        time.sleep(1)
        return calculate(base)
    binary = conversions.decimalTo(decimal,2)[0]
    octal = conversions.decimalTo(decimal,8)[0]
    hexa = conversions.decimalTo(decimal,16)[0]
    print(
f"""
Decimal = {decimal}
Binary = {binary}
Octal = {octal}
Hexadecimal = {hexa}
""")
    print()
    r = ""
    while (r.upper() != "Y" and r.upper() != "N"):
        r = input("would you like to review all steps from decimal to binary? (y,n)")

    if(r == "N"): return

    steps, rSteps = conversions.decimalTo(decimal,2)[1:]
    print(f"{decimal} to Binary:")
    print()
    for step in steps:
        print(step)

    print()
    print(" - ".join(rSteps))
    print("Result: " + binary)

    input("Press enter to continue...")
    conv.append((decimal,binary,octal,hexa))

    


# main menu and program root
def init():
    while(True):
        clearConsole()
        pr.logo()
        pr.mainMenu()
        opt =-1
        while(opt<1 or opt>5):
            try:
                opt = int(input("option:"))

                if(opt<1 or opt>5):
                    clearConsole()
                    pr.mainMenu()
                    print("Invalid option")
                    opt = -1

            except ValueError:
                clearConsole()
                pr.mainMenu()
                print("Invalid option")
                opt = -1

        if(opt == 5):
            clearConsole()
            print("Last conversions:")
            for conversion in conv:
                print()
                print(
f"""
Decimal = {conversion[0]}
Binary = {conversion[1]}
Octal = {conversion[2]}
Hexadecimal = {conversion[3]}
""")
            print()
            input("Press enter to close...")
            os._exit(0)
        else: 
            match opt:
                case 1:
                    calculate(10)
                case 2:
                    calculate(2)
                case 3:
                    calculate(8)
                case 4:
                    calculate(16)

            




if(__name__ == "__main__"):
    init()