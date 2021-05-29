# Python program to illustrate a stop watch  
# using Tkinter  
#importing the required libraries  
import tkinter as Tkinter  
from datetime import datetime 
from datetime import timedelta
import winsound
counter = 66600
running = False
action = "work"
wrktotal=0
brktotal=0
eff=0
goal=-1

def wrk():
    global action
    global actionlabel
    action="work"
    actionlabel["text"]="Option chosen: "+action

def brk():
    global action
    global actionlabel
    action='break'
    actionlabel["text"]="Option chosen: "+action

def counter_label(label):  
    def count():  
        if running:  
            global counter  
            global goal
    
            check=counter-66600
            if check == int(goal):
                winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)

            # To manage the intial delay.  
            if counter==66600:              
                display="Starting..."
            else: 
                tt = datetime.fromtimestamp(counter) 
                string = tt.strftime("%H:%M:%S") 
                display=string  
    
            label['text']=display   # Or label.config(text=display)  
            # label.after(arg1, arg2) delays by   
            # first argument given in milliseconds  
            # and then calls the function given as second argument.  
            # Generally like here we need to call the   
            # function in which it is present repeatedly.  
            # Delays by 1000ms=1 seconds and call count again.  
            label.after(1000, count)   
            counter += 1

    
    # Triggering the start of the counter.  
    count()       
    
# start function of the stopwatch  
def Start(label):  
    global running  
    global action
    running=True
    counter_label(label)  
    n2 = datetime.now()
    text.insert(Tkinter.END, "Started "+action+" at "+n2.strftime("%H:%M:%S")+", ")
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
    
# Stop function of the stopwatch  
def Stop():  
    global running
    global counter
    global action
    n = datetime.now()
    text.insert(Tkinter.END, "Stopped "+action+" at "+n.strftime("%H:%M:%S")+"\n")
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
    
# Reset function of the stopwatch  
def Reset(label):  
    global counter
    global running
    global wrktotal
    global brktotal 
    global root
    if action=="work":
        wrktotal+=counter-66600
        wrklabel["text"]="Total work done: "+str(timedelta(seconds=wrktotal))
    if action=="break":
        brktotal+=counter-66600
        brklabel["text"]="Total break taken: "+str(timedelta(seconds=brktotal))
    counter=66600
    
    # If rest is pressed after pressing stop.  
    if running==False:        
        reset['state']='disabled'
        label['text']='Welcome!'
    
    # If reset is pressed while the stopwatch is running.  
    else:                 
        label['text']='Starting...'

    eff=(wrktotal/(wrktotal+brktotal))*100
    efflabel["text"]="Total productivity percetage: "+str(round(eff,2))

def setGoal():
    def inpsubmit():
        global goal
        global root
        goal=inpp.get();
        print("goal is "+goal)
        strg=str(goal)
        newWindow.destroy()
        goallabel["text"]="Current goal: "+goal+" seconds"


    newWindow = Tkinter.Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("200x200")
    lebb= Tkinter.Label(newWindow, text ="Enter your goal")
    lebb.pack()
    inpp= Tkinter.Entry(newWindow)
    inpp.pack()
    inpButton= Tkinter.Button(newWindow, text="submit", command=inpsubmit)
    inpButton.pack()
    
root = Tkinter.Tk()  
root.title("Stopwatch")  
    
# Fixing the window size.  
root.minsize(width=1000, height=500)  
f = Tkinter.Frame(root) 
label = Tkinter.Label(root, text="Python Timer", fg="black", font="Arial 30")  
label.pack()  
actionlabel= Tkinter.Label(root, text="Option chosen: "+action, fg="black", font="Arial 15")
actionlabel.pack()
f2 = Tkinter.Frame(root)
text=Tkinter.Text(root, height=10, width=60)
text.insert(Tkinter.END, "Log - \n")
start = Tkinter.Button(f, text='Start', width=6, command=lambda:Start(label))  
stop = Tkinter.Button(f, text='Stop',width=6,state='disabled', command=Stop)  
reset = Tkinter.Button(f, text='Save',width=6, state='disabled', command=lambda:Reset(label))  
work = Tkinter.Button(f2, text="Work", width=6, command=wrk)
brkbutton = Tkinter.Button(f2, text="Break", width=6, command=brk)
chooselabel= Tkinter.Label(f2, text="Choose activity: ")
f.pack(anchor = 'center',pady=5) 
start.pack(side="left")  
stop.pack(side ="left")  
reset.pack(side="left")  
chooselabel.pack(side="left")
work.pack(side="right")
brkbutton.pack(side="right")
wrklabel= Tkinter.Label(root,text="Total work done: "+str(wrktotal))
wrklabel.pack()
brklabel= Tkinter.Label(root, text="Total break taken: "+str(brktotal))
brklabel.pack()
efflabel= Tkinter.Label(root, text="Total productivity percetage: "+str(eff))
efflabel.pack()
goallabel= Tkinter.Label(root, text="Current goal : Not set")
goalbutton= Tkinter.Button(root, text="Set goal", command=setGoal)
goallabel.pack()
goalbutton.pack()
f2.pack()
text.pack(pady=20)
root.mainloop()
