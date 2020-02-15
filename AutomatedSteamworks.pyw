from directkeys import DIPressKey,DIReleaseKey,SPACE,A,W,D,X
from tkinter import Tk, Label, StringVar, OptionMenu, messagebox
from win32gui import GetWindowText, GetForegroundWindow
from multiprocessing import Process, Value, freeze_support
from pynput import keyboard
import time
import random
import sys

#global variables
tk = Tk()
OptionList = [
"Random",
"SPACE",
"A,W,D",
"A,D,W",
"W,A,D",
"W,D,A",
"D,W,A",
"D,A,W"
]

hkValue = ["CURRENTLY RUNNING\n Press F4 to PAUSE","CURRENTLY PAUSED\n Press F4 to UNPAUSE"]
hkColor =['green','red']
running = True
themeColor = '#121212'
keys = [A,W,D,SPACE]
keys2 = keys.copy()
holder = 0
rand = A
currentPattern = OptionList[0]

def keySpammer(v,v2): # spams key inputs
    global currentPattern
    isMHWorldOpen = False
    windowsForm()
    counter = 0
    hkLabel = Label(text="", font=('Arial Black', 16), fg='white',bg=themeColor)
    hkLabel.pack()
    while(running):
        application = checkWindow()
        #print(application)
        #print(v.value)
        try:
            hkLabel.config(text=hkValue[v.value],fg=hkColor[v.value])
            tkUpdate()
        except:
            break
        while('MONSTER HUNTER' in application and running and v.value == 0):
            #print(application)
            counter += 1
            try:
                hkLabel.config(text=hkValue[v.value],fg=hkColor[v.value])
                tkUpdate()
            except:
                break
            application = checkWindow()
            if(currentPattern == "Random"):
                randomKeys()
            elif(currentPattern != "Random"):
                patternKeys()
            if(counter > 2):
                DIPressKey(X)
                time.sleep(0.01)
                DIReleaseKey(X)
                counter = 0
    print(running)
    v2.value = 1

def randomKeys():
    global keys,keys2,rand
    if(len(keys) > 0):
        rand = random.randrange(0,len(keys))
        DIPressKey(keys[rand])
        time.sleep(0.01)
        DIReleaseKey(keys[rand])
        keys.remove(keys[rand])
    else:
        keys = keys2.copy()

def patternKeys():
    global keys,keys2
    if(len(keys) > 0):
        DIPressKey(keys[0])
        time.sleep(0.01)
        DIReleaseKey(keys[0])
        keys.remove(keys[0])
    else:
        keys = keys2.copy()

def tkUpdate():
    global tk
    tk.update_idletasks()
    tk.update()

def windowsForm():
    global tk, OptionList

    tk.title('Automated Steamworks')
    tk.geometry("400x300")
    tk['bg'] = themeColor
    try:
        tk.iconbitmap('AutomatedSteamworks.exe')
    except:
        print("missing file")
    label = Label(text='Note: Works only if MHWorld is your main window!\n I "might" add controller inputs in the future', font=('Tahoma', 12), fg='Red',bg=themeColor)
    label.pack(side="bottom")

    #dropdown
    labelTest = Label(text="Select Input Pattern", font=('Arial Black', 12), fg='white',bg=themeColor)
    labelTest.pack(side="top")
    variable = StringVar(tk)
    variable.set(OptionList[0])
    opt = OptionMenu(tk, variable, *OptionList, command=getValue)
    opt.config(width=90, font=('Arial Black', 12),bg=themeColor,fg='white',activebackground=themeColor,activeforeground='white')
    opt["menu"].config(font=('Arial Black', 12),bg=themeColor,fg='white',activeforeground='white')
    opt.pack(side="top")


def getValue(selection):
    global currentPattern, keys, keys2
    if(selection != "Random"):
        holder = Convert(selection)
        newKeys =[]
        for x in holder:
            newKeys.append(stringToKeys(x))
        keys = newKeys.copy()
        keys.append(SPACE)
        keys2 = keys.copy()
    elif(selection == "Random"):
        keys = [A,W,D,SPACE]
        keys2 = keys.copy()
    print(keys)
    print(selection)
    currentPattern = selection

def stringToKeys(argument): 
    switcher = { 
        'A': A, 
        'W': W, 
        'D': D,
        'SPACE': SPACE
    } 
    return switcher.get(argument, "nothing")


def Convert(string): 
	li = list(string.split(",")) 
	return li

def on_closing():
    global tk,running
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application?',icon = 'warning')
    if MsgBox == 'yes':
       running = False
       tk.destroy()

def checkWindow():
    path = GetWindowText(GetForegroundWindow())
    return path.split('\\')[-1] 

def pro1(v,v2):
    tk.protocol("WM_DELETE_WINDOW", on_closing)
    keySpammer(v,v2)

def on_activate_s():
    print('F4 pressed')
    if(holder.value == 0):
        holder.value = 1
    elif(holder.value == 1):
        holder.value = 0
def hotkey(v):
    global holder
    holder = v
    with keyboard.GlobalHotKeys({
            '<f4>': on_activate_s}) as s:
        s.join()

def main():
    freeze_support()
    v = Value('i', 0)
    v2 = Value('i', 0)
    p1 = Process(target=hotkey, args=(v,))
    p2 = Process(target=pro1, args=(v,v2))
    p1.start()
    p2.start()
    while True:
        time.sleep(1)
        if (v2.value == 1):
            p1.terminate()
            p2.terminate()
            p1.join()
            p2.join()
            break
    sys.exit(0)

if __name__ == '__main__':
    main()
 
    

    
