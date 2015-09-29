# COT 4930  Python Programming
# name: Diego Pinto
# id  : Z23162468
# lab : 03
import sys
def eratos(number):
    list=[]
    for i  in range (2,number+1):
        list.append(i)
    
    for i in list:
        for j in list:
            if(j % i == 0 and i!=j):
                list.remove(j)
    return list

def print_primes(list):
    for i in range(len(list)):
         if (i % 11 == 0 and i !=0 ):
            print()
         print('%5s' %list[i],end = " ")

def main():
    
    number = eval(input("Please insert a range between 2 - 300:"))
    if(number > 300 or number < 2):
        sys.exit("Out of Range, will now terminate")
    list = eratos(number)
    print_primes(list)
    print()

main()
                       
