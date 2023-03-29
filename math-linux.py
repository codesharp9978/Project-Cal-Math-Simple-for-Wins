import os
import time
from sys import stderr
import sys

Bl='\033[30m' # VARIABLE BUAT WARNA CUYY
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'


def autoketik(x): # AUTOKETIK CUY!!
    for y in x + "\n":
        sys.stdout.write(y)
        sys.stdout.flush()
        time.sleep(0.030)

def banner(): # BANNER 
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

user = input(f'    {Wh}User@Cal-Math : {Re}')

try:
    def User_choose(): #USER_INPUT
        if user == '1':
            os.system('clear')
            num1 = int(input(f' {Wh}Enter the first number  : {Re}'))
            num2 = int(input(f' {Wh}Enter the second number : {Re}'))
            math = input(f' {Wh}input options [+][-][x][:] : {Re}')
            if math == '+': # TAMBAHAN
                time.sleep(0.3)
                autoketik(f'\n {Wh}RESULTS CALCULATOR :\n')
                hitung = num1 + num2
                print(f' The result is = {Re}{hitung}')
                while True:
                    time.sleep(0.3)
                    hasil = input(f'\n {Wh}Do you want to count again {Gr}Y/N : ')
                    if hasil in ['Y','y']:
                        User_choose()
                    elif hasil in ['N','n']:
                        print(f' {Re}Exit Tools...')
                        time.sleep(0.3)
                        os.system('exit')
                    break
            elif math == '-': #PENGURANGAN
                time.sleep(0.3)
                autoketik(f'\n {Wh}RESULTS CALCULATOR :\n')
                hitung = num1 - num2
                print(f' The result is = {Re}{hitung}')
                while True:
                    time.sleep(0.3)
                    hasil = input(f'\n {Wh}Do you want to count again {Gr}Y/N : ')
                    if hasil in ['Y','y']:
                        User_choose()
                    elif hasil in ['N','n']:
                        print(f' {Re}Exit Tool...')
                        time.sleep(0.3)
                        os.system('exit')
                    break
            elif math == 'x': # PERKALIAN
                time.sleep(0.3)
                autoketik(f'\n {Wh}RESULTS CALCULATOR :\n')
                hitung = num1 * num2
                print(f' The result is = {Re}{hitung}')
                while True:
                    time.sleep(0.3)
                    hasil = input(f'\n {Wh}Do you want to count again {Gr}Y/N : {Wh}')
                    if hasil in ['Y','y']:
                        User_choose()
                    elif hasil in ['N','n']:
                        print(f' {Re}Exit Tool...')
                        time.sleep(0.3)
                        os.system('exit')
                    break
            elif math == ':': # PEMBAGIAN
                time.sleep(0.3)
                autoketik(f'\n {Wh}RESULTS CALCULATOR :\n')
                hitung = num1 / num2
                print(f' The result is = {Re}{hitung}')
                while True:
                    time.sleep(0.3)
                    hasil = input(f'\n {Wh}Do you want to count again {Gr}Y/N : {Wh}')
                    if hasil in ['Y','y']:
                        User_choose()
                    elif hasil in ['N','n']:
                        print(f' {Re}Exit Tool...')
                        time.sleep(0.3)
                        os.system('exit')
                    break
        elif user == '2': # EXIT!!
            time.sleep(0.3)
            print(f'    {Re}Exit tool..')
            os.system('exit')
        else:
            print(f'{Wh}[!] Invalid Input')
except KeyboardInterrupt:
    print(f"{White} stopped Program...")

if __name__ == "__main__":
    User_choose()