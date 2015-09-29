# COT 4930  Python Programming
# name: Diego Pinto
# id  : Z23162468
# lab : 05

Cmd = {}
Cmd["\\A"] = "author"
Cmd["\\Y"] = "Year"
Cmd["\\B"] = "Book"
Cmd["\\P"] = "Publisher"
Cmd["\\B"] = "Book"
Cmd["\\R"] = "Article"
Cmd["\\J"] = "Journal" 
Cmd["\\bibitem"] = "doi"      


def commands( line ):
    #(cmd,newline) =  line.split("{")
    line = line.strip()
    if(line.find('{') ==8):
        (cmd,tmp) = line.split("{") 
        print ("<", Cmd[cmd], ">", sep="")
    elif(line == ""):
        print ("</", Cmd["\\bibitem"], ">", sep="")

    else:
        known = False
        (Newcmd,Newline) = line.split(' ',1)    
        Newline = Newline.strip(".")
        Newline = Newline.strip(",")
        for x in Cmd:
           if( x == Newcmd):
                known = True
                break
            
        if(known):
             print ("<", Cmd[Newcmd], ">", sep="",end="")
             print(Newline,end="")
             print ("</", Cmd[Newcmd], ">", sep="")   
        else:
            print("+++ Unknown",Newcmd, " Invalid command here",sep="")
          

       
def main():
     infile = open('bib.txt','r')
     for line in infile:
            line = line.rstrip()#will remove the new line
            commands(line)
         
main()
