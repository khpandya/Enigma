#import_librairies
from tkinter import *
from tkinter.messagebox import *
import webbrowser
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
helpText = """
This is a simplified recreation of the World War II Enigma Machine used by German soldiers to encrypt messages in wartime. 

To learn how the Enigma Machine works and what exactly the rotors or plugboard settings are and how they operate, click the
"Learn More" button at the bottom of this window.

To begin encrypting a message, choose the initial rotor positions by dragging the sliders labelled under 'Rotor I', 'II' and'III'.
Record this 3-letter combination either manually or by clicking Export after clicking Run. For example, if you set the Rotor I
slider to 'C', the Rotor II slider to 'A' and the Rotor III slider to 'T', record CAT.

Now, enter the message to be encrypted in CAPITAL LETTERS in the first text-box (with an X to represent spaces, ZZ to represent
commas and FRAQ to represent a question mark) under the rotor sliders and click run. (Historically, the Enigma Machine only took
in capital letters like a typewriter with a capital X to represent spaces and had no options for more elaborate writing, the
decrypted message would just include the X, ZZ or FRAQ which was manually understood by soldiers on the other end). The encrypted
message will be shown in the second text box under the Run button. Also note that there is no cause to be alarmed over the rotor
sliders changing position, this is a base functionality of the Enigma machine.

To save this encrypted text (the same is true for decrypted text) or if the text is too long too be displayed in the text-box,
click export to save it in a .txt file named "message" in the same directory where the program is. The message will be followed
by a record of the initial rotor settings you used while encrypting/decrypting in the exported txt file.

Click Clear to refresh both text-boxes and start encrypting or decrypting a new message. Be aware that the initial rotor positions
you recorded for your last message have changed to something else now and if you want to keep using the same recorded combination
as earlier, you will have to drag the sliders back to the settings you want to use. If you want to continuously encrypt messages
while still keeping track of the initial settings being used-you can click run to encrypt multiple times and click export at the
end to have a list of messages followed by their initial settings recorded in the txt file.

To let a friend on another end decrypt your message, send him the three letter combination you recorded earlier+your encrypted
message or just your exported txt file, also don't forget a download link to (or your copy of) the Enigma Simulator. 

To decrypt a message you have received, set the sliders according to the three letter combination (e.g C, A and T for the
combination 'CAT'), enter the encrypted message in the first textbox and click Run. Everything is exactly the same for both
processes except a random combination cannot be chosen while decrypting and the inputs and outputs for the text are inverted.

Click Quit if you're done with your super-cool secret communication and sleep in peace knowing your communication is safe
(unless the person trying to eavesdrop on it is Alan Turing) 
"""


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
countf1=0
countm1=0
counts1=0
exportCounter=0
exportRotors=[]
helpStatus = False
finalmsg=[]
countshift = 0

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
        print("I ran", e)
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
    print("ref",postref)
    rotor1(postref)

def rotor1(mssg):
    global reverse
    postr1=[]
    
    if reverse==False:
        for char in mssg:
            
            if char in alphabetlist:
                changedletter=rotor1listTemp[(alphabetlist.index(char) - abs(counts1 - countm1)) % 26]
                postr1.append(changedletter)   
                 
        reverse=True
        print("r1",postr1)
        reflector(postr1)        
    else:
        for char in mssg:
        
            if char in alphabetlist:
                changedletter=alphabetlist[(rotor1listTemp.index(char) + abs(counts1 - countm1)) % 26]
                postr1.append(changedletter)
        print("r1",postr1)    
        rotor2(postr1)
        
def rotor2(mssg):
    global reverse
    postr2=[]
    
    if reverse==False:
        for char in mssg:
            
            if char in alphabetlist:
                changedletter = rotor2listTemp[(alphabetlist.index(char) - abs(countm1 - countf1)) % 26]
                postr2.append(changedletter)   
                 
        print("r2",postr2)
        rotor1(postr2)        
    else:
        for char in mssg:
        
            if char in alphabetlist:
                changedletter=alphabetlist[(rotor2listTemp.index(char) + abs(countm1 - countf1)) % 26]
                postr2.append(changedletter)
        print("r2",postr2)    
        rotor3(postr2)

def rotor3(mssg):
    global countshift
    global reverse
    postr3=[]
    
    if reverse==False:
        shift()
        for char in mssg:
            countshift += 1
            test=[]
            if char in alphabetlist:
                changedletter=rotor3listTemp[alphabetlist.index(char)]
                postr3.append(changedletter)
                #rotor2 needs to be called here but that will only send one character first, then both on 2nd run
                test.append(postr3[-1])
                print("r3inloop postr3andTest",postr3,test)
                print("r3list is now",rotor3listTemp)
                rotor2(test)
                if countshift != len(mssg):
                    shift()
                     
        #print("r3 (rev F) Finally (except running PB-the mssg is)",postr3)
        #rotor2(postr3)        
    
    else:
        for char in mssg:
        
            if char in alphabetlist:
                changedletter=alphabetlist[rotor3listTemp.index(char)]
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

def code():
    global finalmsg, countf, countm, exportCounter, exportRotors
    #rotorinput=list(input("Enter initial rotor settings for rotors-L,M and R:"))
    omssg= entryvar.get()
    omssg= omssg.upper()
    rotorsetting(int(rotor1_var.get()) + 1,int(rotor2_var.get()) + 1,int(rotor3_var.get()) + 1)
    exportRotors.append(alphabetlist[int(rotor1_var.get())] + alphabetlist[int(rotor2_var.get())] + alphabetlist[int(rotor3_var.get())])
    # print(rotor1listTemp)
    # print(rotor2listTemp)
    # print(rotor3listTemp)
    mssglst=list(omssg)
    plugboard(mssglst)
    flat_list = [item for sublist in finalmsg for item in sublist]
    fnlMsg=''.join(flat_list)
    print("final message", fnlMsg)
       
    flat_list = []
    finalmsg = []
    print(countf,countm)
    countf = 0
    countm = 0
    print("flat list is ",flat_list)
    print("final msg is ", finalmsg)
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
    global exportRotors
    output.delete(0, END)
    entry.delete(0, END)
    exportRotors = []
def export():
    global exportCounter, exportRotors
    exportCounter +=1
    fileNum = str(exportCounter)
    fileName = ("Export"+ fileNum+ ".txt")
    file = open(fileName, "w+") 
    textTuple = output.get(0, END)
    print (textTuple)
    for i in range(0, len(textTuple)):
        file.write(textTuple[i] + " Rotor Settings: [" + exportRotors[i] + "]" + "\r\n")
    file.close() 
def callBack():
    webbrowser.open_new(r"https://www.codesandciphers.org.uk/enigma/rotorspec.htm")
def _helpOff():
    global helpStatus, helpWindow
    helpWindow.destroy()
    helpStatus = False    
def _help():
    global helpText, helpStatus, helpWindow
    if helpStatus == True:
        _helpOff()
    helpWindow = Tk()
    helpWindow.wm_title("Help Window")
    helpWindow.configure(background='white')
    helpStatus = True
    frameHelpText= Frame(helpWindow, borderwidth=0, relief=FLAT, background='white')
    frameHelpText.pack(side=TOP, padx=0, pady=0)
    label = Label(frameHelpText, text=helpText, background = 'white', anchor='s') #font=("times new roman"), background='white')
    label.pack(side= LEFT, fill="both")
    frameButtons= Frame(helpWindow, borderwidth=0, relief=FLAT, background='white')
    frameButtons.pack(side=TOP, padx=0, pady=0)
    okButton = Button(frameButtons, text="OK", width=10, command = _helpOff, background='white')
    okButton.pack(side = LEFT, pady = 10, padx = 10)
    learnMoreButton = Button(frameButtons, text="Learn More", width=10, command = callBack, background='white')
    learnMoreButton.pack(side = LEFT, pady = 10, padx = 10)
    helpWindow.mainloop()
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
_credits = Label(window, text = "Made by Krishnaraj Pandya and Ahmed Hassan", background='white')
_credits.pack(side = BOTTOM, padx=10, pady=10)

window.mainloop()
