# main code (only main menu,flow. Allocate functions in func folder  ) 
import os
import time
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
        print("Not a valid number, returning to menu...")
        time.sleep(1)
        return
    

    


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
            except ValueError:
                clearConsole()
                pr.mainMenu()
                print("Invalid option")
                opt = -1

        if(opt == 5):
            # (todo) complete print last conv
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