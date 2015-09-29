# COT 4930  Python Programming
# name: Diego Pinto
# id  : Z23162468
# lab : 02
def FibSequence(Number):
    Seq =[]					
    Seq.append(0)
    Seq.append(1) 
    for i in range(0,Number):
       Seq.append(Seq[i]+Seq[i+1])
       #print (Seq[i], end =" ")
    Lenght = len(Seq)
    for i in range(Lenght):
         if (i % 6 == 0 and i !=0 ):
            print()
         print('%5s' %Seq[i],end="\t")

def GetName():
    Number = eval (input("How many numbers to generate?:  "))
    return Number

def main():
    Number = GetName()
    FibSequence(Number)
    print()

main()
         
