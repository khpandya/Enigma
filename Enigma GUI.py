#import_libraries
from tkinter import *
from tkinter.messagebox import *

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
scale = Scale(frame1, from_=0, to=25, variable = rotor1_var, showvalue=0, command=update1, length= 150, background='white')
scale.grid(row=1, column=0, padx=60, pady=10)
rotor2_var = DoubleVar()
scale = Scale(frame1, from_=0, to=25, variable = rotor2_var, showvalue=0, command=update2, length= 150, background='white')
scale.grid(row=1, column=1, padx=60, pady=10)
rotor3_var = DoubleVar()
scale = Scale(frame1, from_=0, to=25, variable = rotor3_var, showvalue=0, command=update3, length= 150, background='white')
scale.grid(row=1, column=2, padx=60, pady=10)

#labels for sliders
lab1 = Label(frame1, background='white')
lab1.grid(row=2, column=0)
lab2 = Label(frame1, background='white')
lab2.grid(row=2, column=1)
lab3 = Label(frame1, background='white')
lab3.grid(row=2, column=2)

def code():
    print("Replace this print statement with the code that runs after (de)code is pressed")
    print(entryvar.get())

    #output result
    value = StringVar()
    value.set("Final result")
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

#clear output
def clear():
    output.delete(0, END)

#button to run
runButton = Button(window, text="Run", width=10, command=code, background='white')
runButton.pack()

#output result
frame2 = Frame(window)
output = Listbox(frame2, height=5, width=50, borderwidth=0, background='white')
output.pack(side = LEFT, fill = Y, padx=5, pady=5)
frame2.pack()

#button to clear output
b2 = Button(window, text="Clear", width=10, command=clear, background='white')
b2.pack(padx=5, pady=5)

#credits
_credits = Label(window, text = "ENGI 1020 project by Krishnaraj Pandya", background='white')
_credits.pack(side = BOTTOM, padx=10, pady=10)

#quit_button
quitButton = Button(window, text="Quit", width=10, command=window.destroy, background='white')
quitButton.pack(side = BOTTOM)

window.mainloop()
