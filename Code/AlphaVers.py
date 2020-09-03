#from engi1020.arduino import *
#Archive this and move to Beta version of code
#These are the 1930 rotor specs from Enigma I, prototype in AAZ config
#Exact inputs and outputs from historic documents may not match since the Enigma
#went through several iterations and the version of the Enigma,version of rotors,
#version of reflector etc. must match the document's years exactly for it to work
#in the same way. This is however, an accurate representation of the effective
#algorithm a typical Enigma machine would implement.
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

#TODO
#funcs. for rotor 4 and 5,
#implement such that the order and selection of rotors is implemented
#combine all rotor functions into one with an integer argument to decide which
#rotor stepping according to ring setting,
#take and delete last value of list-add it to the beginning
#custom input of connections for plugboard function
#except default the other reflector lists
#function strings and comments
def shift():
    global count,rotor1list,rotor2list,rotor3list
    #always change fast rotor so no if condition needed, increase countf
    #algorithm-rotorlist.append(list[0])
    #del list[0]
    if countf%26==0:
        pass
        #change middle rotor and increase count m
    if countm%26==0:
        pass
        #change slow rotor

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
            
            if char in alphabetlist:
                changedletter=rotor3list[alphabetlist.index(char)]
                postr3.append(changedletter)   
                 
        print("r3",postr3)
        rotor2(postr3)        
    else:
        for char in mssg:
        
            if char in alphabetlist:
                changedletter=alphabetlist[rotor3list.index(char)]
                postr3.append(changedletter)
        print("r3",postr3)    
        plugboard(postr3)

def plugboard(mssg,lstplugboard1=dfltPB1,lstplugboard2=dfltPB2):
    global reverse
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
        print("PB",postPB)
        #for every character encrypted first count must be increased
        #then shift() must be called
    
omssg=input("Enter message:")
mssglst=list(omssg)
plugboard(mssglst)
#reverse=False
#so you can run program for multiple messages when you implement that functionality


            
        
            
        
    
        
        
    



