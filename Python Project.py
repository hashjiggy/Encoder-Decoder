from tkinter import*
from tkinter import messagebox
import base64

win=Tk()
win.geometry('800x400')
win.resizable(0,0)
win.title("Message Encoder and Decoder")

#define variables

t = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()



#function to encode

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#function to decode

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
        
    return "".join(dec)

##menubar functions

def enc():
    Label(win, text ='ENCODE', font = 'arial 30 bold').place(x=300,y=10)
    mode.set('e')

def dec():
    Label(win, text ='DECODE', font = 'arial 30 bold').place(x=300,y=10)
    mode.set('d')





#function to set mode

def Mode():
    if(t.get()=='' and private_key.get()==''):
        messagebox.showerror('ERROR','Enter valid information')
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), t.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), t.get()))
    else:
        messagebox.showerror('ERROR','Select any mode')



#Function to exit window
        
def Exit():
    win.destroy()


#Function to reset
def Reset():
    t.set("")
    private_key.set("")
    mode.set("")
    Result.set("")

##menubar

menubar=Menu(win)
file= Menu(menubar,tearoff=0)
file.add_command(label="ENCODE",command=enc)
file.add_command(label="DECODE",command=dec)
menubar.add_cascade(label="OPTION",menu=file)
win.config(menu=menubar)

#################### Label and Button #############

#Message
Label(win, font= 'arial 12 bold', text='MESSAGE').place(x= 250,y=80)
Entry(win, font = 'arial 10', textvariable = t, bg = 'ghost white').place(x=480, y = 80)

#key
Label(win, font = 'arial 12 bold', text ='KEY').place(x=250, y = 130)
Entry(win, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=480, y = 130)


#result
Entry(win, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=480, y = 180)

######result button
Button(win, font = 'arial 10 bold', text = 'RESULT'  ,padx =2,bg ='ghost white' ,command = Mode,activebackground='red',activeforeground='yellow',relief='ridge').place(x=250, y = 180)


#reset button
Button(win, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'ghost white', padx=2,activebackground='red',activeforeground='yellow',relief='ridge').place(x=300, y = 300)

#exit button
Button(win, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'ghost white', padx=2, pady=2,activebackground='red',activeforeground='yellow',relief='ridge').place(x=400, y = 300)
win.mainloop()