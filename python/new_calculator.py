"""         Coded by @CoderX on telegram!         """
import os
import time

class Calculator:
    def __init__(self):
        self.guide='''"+" for Addition (Default)
"-" for  substraction
"*", "×", "x" for multiplication
"/", "÷" for  division
"//" for floor division
"%" for remainder (Modulus)
\n\n'''
        print(self.guide)
        self.result="Unable to calculate..."
        self.fnum="0"
        self.Snum="0"
        self.oprt=""
        self.opr="+"
        self.multi_result=""
        self.__main__()
        os.system("clear")
        if self.multi_result:
            print("Answer is: ", "\033[1m" + "\033[32m" + str(self.multi_result) + "\033[33m")
        else:
            print("\033[1m" + "\033[32m" + f"{self.fnum} {self.opr} {self.Snum} = {self.result}" + "\033[33m")
        
    def __main__(self):
        self.__input()
        if self.opr=="+":
            self.result=self.fnum+self.Snum
        elif self.opr=="-":
            self.result=self.fnum-self.Snum
        elif self.opr=="/" or self.opr=="÷":
            self.tres=f"{self.fnum/self.Snum}"
            self.result=self.tres
            if ".0" in self.tres:
                Lastres=self.tres.replace(".0", "")
                self.result=Lastres
            else:
                self.result=self.tres
        elif self.opr=="//":
            self.result=self.fnum//self.Snum
        elif self.opr=="%":
            self.result=self.fnum%self.Snum
        elif self.opr=="*" or self.opr=="×" or self.opr=="x":
            self.result=self.fnum*self.Snum
        else:
            print("Operation not supported ;(")

    def __input(self):
        fcheck=int(input("""Will you enter numbers like this : 
        a+b or a+b+c? 
        enter 1 if a+b
        else enter 2
 
Enter a valid option: """))
        os.system("clear")
        if fcheck!=1 and fcheck!=2:
            for _ in range(9):
                print(f"\033[3{_}m"+"Please enter a valid input." + "\033[0m",end="\r") 
                time.sleep(1)
            os.system("clear")
            self.__input()
        if fcheck==2:
            self.__multiple_cal()
        else:
            print(self.guide)
            try:
                self.fnum=eval(input("Enter the first number: "))
                self.Snum=eval(input("Enter the second number: "))
            except Exception:
                for _ in range(9):
                    print(f"\033[3{_}m"+"Please enter a valid number." + "\033[0m",end="\r") 
                    time.sleep(1)
                os.system("clear")
                self.__main__()
 
     # Operation 
            self.oprt=input("What operation you want to perform?: ")
            self.__opr_check(self.oprt,self.__input)
        if not self.opr:
            print("No operation given using default operation \"+\"")
            time.sleep(5)
            os.system("clear")
            self.__main__()
        else:
            self.opr=self.oprt

    @classmethod
    def __opr_check(cls,i,obj_to_pass):
        if i!="+" and i!="-" and i!="*" and i!="×" and i!="x" and i!="÷" and i!="/" and i!="//" and i!="%":
            os.system("clear")
            print("Operation not supported I'm really sorry..")
            time.sleep(6)
            os.system("clear")
            obj_to_pass()
        else:
            pass

    def __multiple_cal(self):
        print(self.guide)
        try:
            nums=eval(input("Enter the numbers with operation (everything together): "))
        except ValueError:
            print("Enter a valid number")
            time.sleep(5)
            os.system("clear")
        else:
            if nums=="":
                print("Kindly enter a valid input")
                time.sleep(5)
                os.system("clear")
            else:
                self.multi_result=nums

if __name__ == "__main__":
    Calculator()
 
