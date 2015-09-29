# COT 4930  Python Programming
# name: Diego Pinto
# id  : Z23162468
# lab : 04


import operator
Location = {}

def make_dict():
    infile = open('fl_cities.txt','r')
    for line in infile:
            line = line.rstrip()#will remove the new line
            #print("\t", line)
            (Zip,City) = line.split(":")
            Location[City] = Zip
        
    infile.close()
   
def command(Command,arguement,arguement2):
    if Command == 'p':
        if(arguement =='cities'):
            #Sort_Cities = sorted(Location.items(), key=operator.itemgetter(0))
             Sort_key = sorted(Location.keys())
             for i in range (len(Sort_key)):
                 print('%-20s' %Sort_key[i], '%-20s' %Location.get(Sort_key[i]),sep= " ")
             print()   
        
    elif(Command == 'f'):
             print('%-20s' %arguement,'%-20s' %Location.get(arguement ,"No zip found"))
             print()             
    elif(Command == 'c'):
            if arguement2 in Location.keys():
                Location[arguement2] = arguement
              
            else:
                print(arguement2, "\t City not found")
                print() 
    else:
        print("Unknown command\n")
def test_dict():
    inCommand = open('fl_maint.txt','r')
    arguement2 = " "
    for line in inCommand:
        print(line)
        line = line.rstrip()
        Command,arguement= line.split("-")
        if ":" in arguement:
            arguement,arguement2 = arguement.split(":")
        command(Command,arguement,arguement2)
    print(Command)
    inCommand.close()
   



def main():
    make_dict()
    test_dict()

main()