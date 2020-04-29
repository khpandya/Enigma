from engi1020.arduino import *
from time import sleep
#These are the 1930 rotor specs from Enigma I, prototype in initial AAZ config
#Exact inputs and outputs from historic documents may not match since the Enigma
#went through several iterations and the version of the Enigma,version of rotors,
#version of reflector etc. must match the document's years exactly for it to work
#in the same way. This is however, an accurate representation of the effective
#algorithm a typical Enigma machine would implement.
#It works perfectly fine in terms of converting the encrypt to decrypt and vice-versa
#however there may be a bug in rotor3 where both reverse false and true blocks are accessed
#etc but it doesnt affect the final results for a demo
alphabetlist=['A','B','C','D','E','F','G','H','I','J','K','L',
              'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rotor1list=['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y',
            'H','X','U','S','P','A','I','B','R','C','J']
rotor2list=['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M',
            'C','Q','G','Z','N','P','Y','F','V','O','E']
rotor3list=['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y',
            'E','I','W','G','A','K','M','U','S','Q','O']
reflectorBlist=['Y','R','U','H','Q','S','L','D','P','X','N',
            'G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T']
# dfltPB1=['G','V','U','R','P',
#          'S','L','W','I','H']
#uncomment after you aren't testing
dfltPB2=['A','C','D','X','N',
         'T','F','M','B','O']
dfltPB1=['A','C','D','X','N',
         'T','F','M','B','O']
reverse=False
countf=0
countm=0
finalmsg=[]
#TODO
#shift to a characte based model?
#funcs. for rotor 4 and 5
#implement such that the order and selection of rotors is implemented
#combine all rotor functions into one with an integer argument to decide which
#rotor stepping according to historically accurate notch
#custom input of connections for plugboard function
#except default the other reflector lists
#function strings and comments
def rotorsetting(l,m,n):
    #this implementation is what's referred to as ring setting
    global rotor1list,rotor2list,rotor3list
    
    for e in range(l-1):
        rotor1list.append(rotor1list[0])
        del rotor1list[0]
        print("I ran")
        
    for f in range(m-1):
        rotor2list.append(rotor2list[0])
        del rotor2list[0]
        
    for g in range(n-1):
        rotor3list.append(rotor3list[0])
        del rotor3list[0]   
    

def shift():
    global countf,countm,rotor1list,rotor2list,rotor3list
    #always change fast rotor so no if condition needed, increase countf
    rotor3list.append(rotor3list[0])
    del rotor3list[0]
    countf+=1
    
    if countf%26==0:
        #change middle rotor and increase count m
        rotor2list.append(rotor2list[0])
        del rotor2list[0]
        countm+=1
        
    if countm%26==0 and countm!=0:
        #change slow rotor
        rotor1list.append(rotor1list[0])
        del rotor1list[0]

def reflector(mssg,reflect=reflectorBlist):
    postref=[]
    
    for char in mssg:
        if char in alphabetlist:
            changedletter=reflect[alphabetlist.index(char)]
            postref.append(changedletter)
    print("ref",postref)
    rotor1(postref)

def rotor1(mssg):
    global reverse
    postr1=[]
    
    if reverse==False:
        for char in mssg:
            
            if char in alphabetlist:
                changedletter=rotor1list[alphabetlist.index(char)]
                postr1.append(changedletter)   
                 
        reverse=True
        print("r1",postr1)
        reflector(postr1)        
    else:
        for char in mssg:
        
            if char in alphabetlist:
                changedletter=alphabetlist[rotor1list.index(char)]
                postr1.append(changedletter)
        print("r1",postr1)    
        rotor2(postr1)

def rotor2(mssg):
    global reverse
    postr2=[]
    
    if reverse==False:
        for char in mssg:
            
            if char in alphabetlist:
                changedletter=rotor2list[alphabetlist.index(char)]
                postr2.append(changedletter)   
                 
        print("r2",postr2)
        rotor1(postr2)        
    else:
        for char in mssg:
        
            if char in alphabetlist:
                changedletter=alphabetlist[rotor2list.index(char)]
                postr2.append(changedletter)
        print("r2",postr2)    
        rotor3(postr2)

def rotor3(mssg):
    global reverse
    postr3=[]
    
    if reverse==False:
        for char in mssg:
            test=[]
            if char in alphabetlist:
                changedletter=rotor3list[alphabetlist.index(char)]
                postr3.append(changedletter)
                #rotor2 needs to be called here but that will only send one character first, then both on 2nd run
                test.append(postr3[-1])
                print("r3inloop postr3andTest",postr3,test)
                print("r3list is now",rotor3list)
                rotor2(test)
                shift()
                     
        #print("r3 (rev F) Finally (except running PB-the mssg is)",postr3)
        #rotor2(postr3)        
    
    else:
        for char in mssg:
        
            if char in alphabetlist:
                changedletter=alphabetlist[rotor3list.index(char)]
                postr3.append(changedletter)
                #shift(), letter still has to come back through same config
        print("r3 (rev T)",postr3)    
        plugboard(postr3)

def plugboard(mssg,lstplugboard1=dfltPB1,lstplugboard2=dfltPB2):
    global reverse, finalmsg
    postPB=[]
    
    for char in mssg:
        
        if char in alphabetlist:
            
            if char in lstplugboard1:
                changedletter=lstplugboard2[lstplugboard1.index(char)]
                postPB.append(changedletter)
            
            elif char in lstplugboard2:
                changedletter=lstplugboard1[lstplugboard2.index(char)]
                postPB.append(changedletter)
            
            else:
                postPB.append(char)
                
    
    if reverse==False:
        print("PB",postPB)
        rotor3(postPB)
    else:
        finalmsg.append(postPB)
        #print("PB",postPB)
        #set everything to initial position so it works again for next character in for loop in rotor 3
        reverse=False

choice=int(input("""Enter number:
                    1. Console Mode
                    2. Arduino Mode
                    3. Bank Encryption Mode
                    
                    """))
if choice==1:
           
    rotorinput=list(input("Enter initial rotor settings for rotors-L,M and R:"))
    omssg=input("Enter message:")
    rotorsetting(int(rotorinput[0]),int(rotorinput[1]),int(rotorinput[2]))
    # print(rotor1list)
    # print(rotor2list)
    # print(rotor3list)
    mssglst=list(omssg)
    plugboard(mssglst)
    flat_list = [item for sublist in finalmsg for item in sublist]
    fnlMsg=''.join(flat_list)
    print("final message", fnlMsg)

if choice==2:
    
    lcd_clear()
    def rotaryToAlphabet(rotaryPin, buttonPin):
         '''
        Assumes rotaryPin and buttonPin are integers corresponding to the pin
        the rotary dial and button are plugged into, respectively
        Converts analog input to a string containing a letter
        '''
         while digital_read(buttonPin)==0:
             
             index = int((analog_read(rotaryPin) + 10) * (25 / 1023))
             # 10 added because rotary dial output doesn't remain constantly at 1024
             #lcd_print(" " + alphabetlist[index])             
             letter = alphabetlist[index]
             #print(letter)
             lcd_clear()
             lcd_print(letter)

         return letter
    
    x=rotaryToAlphabet(0,2)
    l=alphabetlist.index(x)
    lcd_clear()
    lcd_print("R1 is:")
    lcd_print(x)
    sleep(0.8)
    
    y=rotaryToAlphabet(0,2)
    m=alphabetlist.index(y)
    lcd_clear()
    lcd_print("R2 is:")
    lcd_print(y)
    sleep(0.8)
    
    z=rotaryToAlphabet(0,2)
    n=alphabetlist.index(z)
    lcd_clear()
    lcd_print("R3 is:")
    lcd_print(z)
    sleep(0.8)
    lcd_clear()
    
    rotorinput=[l,m,n]
    omssg=input("Enter message:")
    rotorsetting(int(rotorinput[0]),int(rotorinput[1]),int(rotorinput[2]))
    # print(rotor1list)
    # print(rotor2list)
    # print(rotor3list)
    mssglst=list(omssg)
    plugboard(mssglst)
    flat_list = [item for sublist in finalmsg for item in sublist]
    fnlMsg=''.join(flat_list)
    lcd_print(fnlMsg)
    #lcd_print("appended"), appends lcd_clear() clears

if choice==3:
    path = 'C:\TURBOC3\BIN\MESSAGE.TXT'
    with open(path,'r') as f:
        for x in f:
            mssg=list(x)
            print(mssg)
            plugboard(mssg)
            flat_list1 = [item for sublist in finalmsg for item in sublist]
            fnlMsg=''.join(flat_list)
        print(fnlMsg)
    
    
    
        
    
           


            
        
            
        
    
        
        
    





