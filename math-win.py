import os
import time
from sys import stderr
import sys
import functionmath



Bl='\033[30m' # VARIABLE BUAT WARNA CUYY
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'


def autoketik(x): 
    for y in x + "\n":
        sys.stdout.write(y)
        sys.stdout.flush()
        time.sleep(0.030)

def banner():  
    stderr.writelines(f"""
    {Re}╔═╗ ┌─┐ ┬     ╔╦╗ ┌─┐ ┌┬┐ ┬ ┬
    {Wh}║   ├─┤ │ ─── ║║║ ├─┤  │  ├─┤
    {Re}╚═╝ ┴ ┴ ┴─┘   ╩ ╩ ┴ ┴  ┴  ┴ ┴
    {Wh}<<--TOOLS CALCULATOR MATH-->>
    {Re} <>{Wh}from HunX and Telejoker{Re}<>\n
""")
banner()

def Select_menu():
    print(f'    {Re}[{Wh}1{Re}] {Wh}STAR CALCULATOR')
    print(f'    {Re}[{Wh}2{Re}] {Wh}EXIT\n')
Select_menu()

user = ""
user = input(f'    {Wh}User@Cal-Math : {Re}')


while user != "exit":
        if user == "1":
            num1 = input(f'{Wh}Enter the first number  : {Re}')
            num2 = input(f'{Wh}Enter the second number : {Re}')
            num1 = int(num1)
            num2 = int(num2)
            math = input(f'{Wh}input options [+][-][*][/] : {Re}')
            #pemilihan + - * / dan function nya
            if math == '+':
                time.sleep(0.3)
                autoketik(f'\n{Wh}RESULTS CALCULATOR :\n')
                Hasil = {functionmath.tambah(a=num1,b=num2)}
            elif math == '-':
                time.sleep(0.3)
                autoketik(f'\n{Wh}RESULTS CALCULATOR :\n')
                Hasil = {functionmath.kurang(a=num1,b=num2)}
                
            elif math == '*':
                time.sleep(0.3)
                autoketik(f'\n{Wh}RESULTS CALCULATOR : \n')
                Hasil = {functionmath.kali(a=num1,b=num2)}
                
            elif math == '/':
                time.sleep(0.3)
                autoketik(f'\n{Wh}RESULTS CALCULATOR : \n')
                Hasil = {functionmath.bagi(a=num1,b=num2)}
            else:
                print(f"{Wh}[!] Invalid Input, Plese Select +-*/") 
                continue   
            print(f"Result : {Hasil}")

            clearcode = ""
            clearcode = input("Do You want Clear terminal Y/n or Back To Home {y/n/back} : ")
            if clearcode == "y" or clearcode == "Y":
                os.system("cls")
                user
                math
            elif clearcode == "N" or clearcode == "n":
                print("Okay SIR")
                continue
            elif clearcode == "back" or clearcode == "BACK":
                os.system("cls")
                banner()
                Select_menu()
                user = input(f'    {Wh}User@Cal-Math : {Re}')
                
        if user == "2":
            time.sleep(0.3)
            autoketik(f'\n{Wh}THANK FOR USING MY TOOL\n')
            break