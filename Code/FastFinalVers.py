#import_librairies
from tkinter import *
from tkinter.messagebox import *
import sys
import os
#window
window = Tk()
window.title("MUN Enigma Machine")
window.configure(background='white')

#logo and title
image = PhotoImage(file="muneng.gif")
Label(window, image=image, background='white').pack(padx=10, pady=10, side=TOP)
Label(window, text="Enigma Machine Simulator", font=("times new roman", 25), background='white').pack(padx=10, pady=10, side=TOP)

#frame
frame1 = Frame(window, borderwidth=0, relief=FLAT, background='white')
frame1.pack(side=TOP, padx=10, pady=10)

#slider updates
def update1(x):
    x = int(x)
    alphabetList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lab1.configure(text='position : {}'.format(alphabetList[x]))
def update2(x):
    x = int(x)
    alphabetList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lab2.configure(text='position : {}'.format(alphabetList[x]))
def update3(x):
    x = int(x)
    alphabetList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lab3.configure(text='position : {}'.format(alphabetList[x]))

#rotor labels
rotor1lab = Label(frame1, text='Rotor I', padx=10, pady=5, borderwidth=0, background='white')
rotor1lab.grid(row=0, column=0)
rotor2lab = Label(frame1, text='Rotor II', padx=10, pady=5, borderwidth=0, background='white')
rotor2lab.grid(row=0, column=1)
rotor3lab = Label(frame1, text='Rotor III', padx=10, pady=5, borderwidth=0, background='white')
rotor3lab.grid(row=0, column=2)


#sliders
rotor1_var = DoubleVar()
scale1 = Scale(frame1, from_=0, to=25, variable = rotor1_var, showvalue=0, command=update1, length= 150, background='white')
scale1.grid(row=1, column=0, padx=60, pady=10)
rotor2_var = DoubleVar()
scale2 = Scale(frame1, from_=0, to=25, variable = rotor2_var, showvalue=0, command=update2, length= 150, background='white')
scale2.grid(row=1, column=1, padx=60, pady=10)
rotor3_var = DoubleVar()
scale3 = Scale(frame1, from_=0, to=25, variable = rotor3_var, showvalue=0, command=update3, length= 150, background='white')
scale3.grid(row=1, column=2, padx=60, pady=10)


#labels for sliders
lab1 = Label(frame1, background='white')
lab1.grid(row=2, column=0)
lab2 = Label(frame1, background='white')
lab2.grid(row=2, column=1)
lab3 = Label(frame1, background='white')
lab3.grid(row=2, column=2)

lab1.configure(text='position : A')
lab2.configure(text='position : A')
lab3.configure(text='position : A')

#from engi1020.arduino import *
#These are the 1930 rotor specs from Enigma I, prototype in initial AAZ config
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
rotor1listTemp = []
rotor2listTemp = []
rotor3listTemp = []
reflectorBlist=['Y','R','U','H','Q','S','L','D','P','X','N',
            'G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T']
 dfltPB1=['G','V','U','R','P',
          'S','L','W','I','H']
dfltPB2=['A','C','D','X','N',
         'T','F','M','B','O']
dfltPB1=['A','C','D','X','N',
         'T','F','M','B','O']
reverse=False
countf=0
countm=0
countf1=0
countm1=0
counts1=0
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
    global rotor1list,rotor1listTemp,rotor2list,rotor2listTemp,rotor3list,rotor3listTemp, countf1, countm1, counts1
    countf1=int(rotor3_var.get())
    countm1=int(rotor2_var.get())
    counts1=int(rotor1_var.get())
    for e in range(l-1):
        rotor1list.append(rotor1list[0])
        del rotor1list[0]
    rotor1listTemp = rotor1list
    rotor1list=['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y',
            'H','X','U','S','P','A','I','B','R','C','J']
    for f in range(m-1):
        rotor2list.append(rotor2list[0])
        del rotor2list[0]
    rotor2listTemp = rotor2list
    rotor2list = ['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M',
            'C','Q','G','Z','N','P','Y','F','V','O','E']
    for g in range(n-1):
        rotor3list.append(rotor3list[0])
        del rotor3list[0]   
    rotor3listTemp = rotor3list
    rotor3list=['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y',
            'E','I','W','G','A','K','M','U','S','Q','O']
def shift():
    global countf,countm,countf1, countm1, counts1, rotor1listTemp,rotor2listTemp,rotor3listTemp
    #always change fast rotor so no if condition needed, increase countf
    rotor3listTemp.append(rotor3listTemp[0])
    del rotor3listTemp[0]
    countf+=1
   
    countf1+=1
    if countf1 == 26:
        scale3.set(0)
        countf1 = 0
        countm1 += 1
        if countm1 == 26:
            scale2.set(0)
            countm1 = 0
            counts1+=1
            if counts1 == 26:
                scale1.set(0)
                counts1 = 0
            else:
                scale1.set(counts1)
        else:
            scale2.set(countm1)
    else:
        scale3.set(countf1)
        
                
    if countf%26==0:
        #change middle rotor and increase count m
        rotor2listTemp.append(rotor2listTemp[0])
        del rotor2listTemp[0]
        
    if countm%26==0 and countm!=0:
        #change slow rotor
        rotor1listTemp.append(rotor1listTemp[0])
        del rotor1listTemp[0]

def reflector(mssg,reflect=reflectorBlist):
    postref=[]
    
    for char in mssg:
        if char in alphabetlist:
            changedletter=reflect[alphabetlist.index(char)]
            postref.append(changedletter)
    rotor1(postref)

def rotor1(mssg):
    global reverse
    postr1=[]
    
    if reverse==False:
        for char in mssg:
            
            if char in alphabetlist:
                changedletter=rotor1listTemp[alphabetlist.index(char)]
                postr1.append(changedletter)   
                 
        reverse=True
        reflector(postr1)        
    else:
        for char in mssg:
        
            if char in alphabetlist:
                changedletter=alphabetlist[rotor1listTemp.index(char)]
                postr1.append(changedletter)
        rotor2(postr1)
        
def rotor2(mssg):
    global reverse
    postr2=[]
    
    if reverse==False:
        for char in mssg:
            
            if char in alphabetlist:
                changedletter=rotor2listTemp[alphabetlist.index(char)]
                postr2.append(changedletter)   
        rotor1(postr2)        
    else:
        for char in mssg:
        
            if char in alphabetlist:
                changedletter=alphabetlist[rotor2listTemp.index(char)]
                postr2.append(changedletter)
        rotor3(postr2)

def rotor3(mssg):
    global reverse
    postr3=[]
    
    if reverse==False:
        for char in mssg:
            test=[]
            if char in alphabetlist:
                changedletter=rotor3listTemp[alphabetlist.index(char)]
                postr3.append(changedletter)
                #rotor2 needs to be called here but that will only send one character first, then both on 2nd run
                test.append(postr3[-1])
                rotor2(test)
                shift()
                     
    else:
        for char in mssg:
        
            if char in alphabetlist:
                changedletter=alphabetlist[rotor3listTemp.index(char)]
                postr3.append(changedletter)
                #shift(), letter still has to come back through same config  
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
        rotor3(postPB)
    else:
        finalmsg.append(postPB)
        #print("PB",postPB)
        #set everything to initial position so it works again for next character in for loop in rotor 3
        reverse=False

def code():
    global finalmsg, countf, countm
    #rotorinput=list(input("Enter initial rotor settings for rotors-L,M and R:"))
    omssg= entryvar.get()
    rotorsetting(int(rotor1_var.get()) + 1,int(rotor2_var.get()) + 1,int(rotor3_var.get()) + 1)
    # print(rotor1listTemp)
    # print(rotor2listTemp)
    # print(rotor3listTemp)
    mssglst=list(omssg)
    plugboard(mssglst)
    flat_list = [item for sublist in finalmsg for item in sublist]
    fnlMsg=''.join(flat_list)
       
    flat_list = []
    finalmsg = []
    countf = 0
    countm = 0
    #output result
    value = StringVar()
    value.set(fnlMsg)
    output.insert(END, value.get())
    output.see("end")

#text entry label
textLabel = Label(window, text = "Enter the message to be decrypted/encrypted", background='white')
textLabel.pack()

#text entry
entryvar = StringVar()
entry = Entry(window, textvariable = entryvar, width=50, background='white')
entry.focus_set()
entry.bind("<Return>", code)
entry.pack(padx=10, pady=10)

#functions for buttons
def clear():
    output.delete(0, END)
    entry.delete(0, END)
def export():
    file = open("export.txt", "a") 
    value = output.get(0, END)
    file.write(value) 
    file.close() 
def _help():
    print("Hi")
#button to run
runButton = Button(window, text="Run", width=10, command=code, background='white')
runButton.pack()

#output result
frame2 = Frame(window, borderwidth=0, relief=FLAT, background='white')
frame2.pack(pady = 5)
output = Listbox(frame2, height=5, width=50, borderwidth=0, background='white')
output.pack(side = LEFT, fill = Y, padx=5, pady=5)


#frame for clear and export buttons layout
frame3 = Frame(window, borderwidth=0, relief=FLAT, background='white')
frame3.pack(side=TOP, padx=10, pady=0)
clearButton = Button(frame3, text="Clear", width=10, command=clear, background='white')
clearButton.pack(side = LEFT, padx=5, pady=5)
exportButton = Button(frame3, text="Export", width=10, command=export, background='white')
exportButton.pack(side = LEFT, padx=5, pady=5)

#frame for help and quit buttons layout
frame4 = Frame(window, borderwidth=0, relief=FLAT, background='white')
frame4.pack(side=TOP, padx=10, pady=0)
helpButton = Button(frame4, text="Help", width=10, command=_help, background='white')
helpButton.pack(side = LEFT, padx=5, pady=5)
quitButton = Button(frame4, text="Quit", width=10, command=window.destroy, background='white')
quitButton.pack(side = LEFT, padx=5, pady=5)

#credits
_credits = Label(window, text = "ENGI 1020 project by Krishnaraj Pandya", background='white')
_credits.pack(side = BOTTOM, padx=10, pady=10)

window.mainloop()
