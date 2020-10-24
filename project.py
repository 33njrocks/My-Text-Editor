from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
from tkinter.font import Font,families
#CREATING INSTANCE OF CLASS TK.THIS CREATES A BASE WINDOW FOR OUR GUI APPLICATION.
root = Tk()

#SETTING SIZE FOR OUR WINDOW.
root.geometry("500x500")

#SETTING MINIMUM SIZE FOR OUR WINDOW.
root.minsize(200,200)

#CHANGING TITLE OF EDITOR.
root.title("MY TEXT EDITOR")

#CHANGING EDITOR'S ICON
root.iconbitmap('image.ico')

def new():
    #DELETING THE PREVIOUS CONTENT AND CHANGING TITLE
    global file
    file=None
    textarea.delete("1.0",END)
    root.title("NEW WINDOW!!")
def open_file():
    #OPEN DIALOGBOX
    global file
    file = filedialog.askopenfilename(defaultextension="*.txt",filetypes=(("Text Files","*.txt"),("Python Files","*.py"),("All Files","*.*")))
    #IF NO FILENAME IS GIVEN THEN ASSIGN IT AS NONE.
    if file == "":
        file=None
    else:
        #ELSE OPEN THE FILE.
        root.title(os.path.basename(file))
        textarea.delete(1.0,END)
        f = open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()
def save():
    #IF FILE IS NOT EMPTY THEN SIMPLY OPEN THE FILE IN WRITE MODE AND GET THE CONTENT.
    global file
    if file != None:
        f = open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()
def save_as():
    global file
    #SAVING THE FILE WITH A NAME.
    file = filedialog.asksaveasfilename(initialfile="Untitled.txt",defaultextension="*.txt",filetypes=(("Text Files","*.txt"),("Python Files","*.py"),("All Files","*.*")))
    if file == "":
        file = None
    else:
        f = open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()
        root.title(os.path.basename(file))

def status_bar():
    global sbar
    if var.get() == 1:
        statusvar = StringVar()
        statusvar.set("Ready")
        sbar = Label(root,textvariable=statusvar,anchor="w")
        sbar.pack(side=BOTTOM,fill=X)
    else:
        sbar.destroy()
    
def my_font():
    #CREATING FUNCTIONALITY FOT FONT GUI.
    def _ok():
        go()
        font.destroy()
    def cancel():
        font.destroy()
    def go():
        #EXTRACTING THE LISTBOX AND CHECKBUTTONS VALUES TO APLLY FONT FUNCTIONALITY IN TEXTAREA.
        cs_1 = list1.curselection()[0]
        x = list1.get(cs_1)
        cs_2 = list2.curselection()[0]
        y = list2.get(cs_2)
        a,b = var1.get(),var2.get()
        if a==1:
            a='bold'
        if b==1:
            b='italic'
        my_font = Font(family=x,size=y,weight=a,slant=b,underline=var3.get())
        textarea.config(font=my_font)
    #CREATING A FONT GUI.
    font = Toplevel(root)
    font.title("CHANGE FONT")
    font.geometry('480x400')
    font.maxsize(500,400)
    font.iconbitmap('image.ico')

    #CREATING FRAMES.
    frame1 = Frame(font,borderwidth=5,relief=SUNKEN)
    Label(frame1,text="Font Family",font=('Helvetica',14,'bold')).pack()
    list1 = Listbox(frame1,width=30,exportselection=0)
    list1.pack(side=LEFT)
    #INSERTING FONT FAMILIES LIST IN LISTBOX 1.
    for items in list(families()):
        list1.insert(END,items)
    s1 = Scrollbar(frame1)
    s1.config(command=list1.yview)
    s1.pack(side=RIGHT,fill=Y)
    list1.config(yscrollcommand=s1.set)
    frame1.pack(side=LEFT,anchor=NW,padx=20,pady=20)
    
    frame2 = Frame(font,borderwidth=5,relief=SUNKEN)
    Label(frame2,text="Font Size",font=('Helvetica',14,'bold')).pack()
    list2 = Listbox(frame2)
    list2.pack(side=LEFT)
    for items in range(0,200,2):
        list2.insert(END,items)
    s2 = Scrollbar(frame2)
    s2.config(command=list2.yview)
    s2.pack(side=RIGHT,fill=Y)
    list2.config(yscrollcommand=s2.set)
    frame2.pack(padx=20,pady=20,side=TOP)

    frame3 = Frame(font,borderwidth=5,relief=SUNKEN)
    Label(frame3,text="Font Style",font=('Helvetica',10,'bold')).pack()
    var1 = IntVar()
    check1 = Checkbutton(frame3,text="BOLD",variable=var1)
    check1.pack(side=LEFT)
    var2 = IntVar()
    check2 = Checkbutton(frame3,text="ITALIC",variable=var2)
    check2.pack(side=LEFT)
    var3 = IntVar()
    check3 = Checkbutton(frame3,text="UNDERLINE",variable=var3)
    check3.pack()
    frame3.pack(anchor=W)

    frame4 = Frame(font)
    Button(frame4,text="OK",padx=20,fg='blue',command=_ok).pack(side=LEFT)
    Button(frame4,text="CANCEL",padx=5,fg='blue',command=cancel).pack(padx=10)
    frame4.pack(side=BOTTOM,anchor=E,padx=10,pady=10)
    font.mainloop()
def quit():
    root.destroy()
#CREATING CUT , COPY AND PASTE EVENTS.
def cut():
    textarea.event_generate("<<Cut>>")
def copy():
    textarea.event_generate("<<Copy>>")
def paste():
    textarea.event_generate("<<Paste>>")
def delete():
    #SELECTING THE HIGHLIGHTED TEXT FIRST , FINDING INDEX OF FIRST CHARACTER AND THEN DELETING THE SELECTED TEXT.
    text = textarea.selection_get()
    count = textarea.search(text,1.0,stopindex=END)
    for i in range(len(text)):
        textarea.delete(count)
def myfunc():
    messagebox.showinfo("About Editor","This editor is created by Naman Jaiswal")

#CREATING TEXTAREA
textarea = Text(root,bg='whitesmoke',fg='blue',wrap=WORD,undo=True)
textarea.pack(fill=BOTH,expand=True,padx=3)

#CREATING MENUS AND SUBMENUS
mymenu = Menu(root)
#SUBMENU FOR FILE
m1=Menu(mymenu,tearoff=0)
m1.add_command(label="NEW",command=new)
m1.add_command(label="OPEN",command=open_file)
m1.add_separator()
m1.add_command(label="SAVE",command=save)
m1.add_command(label="SAVE AS",command=save_as)
m1.add_separator()
m1.add_command(label="QUIT",command=quit)

#SUBMENU FOR EDIT
m2=Menu(mymenu,tearoff=0)
m2.add_command(label="UNDO",command=textarea.edit_undo)
m2.add_command(label="REDO",command=textarea.edit_redo)
m2.add_separator()
m2.add_command(label="CUT",command=cut)
m2.add_command(label="COPY",command=copy)
m2.add_command(label="PASTE",command=paste)
m2.add_separator()
m2.add_command(label="DELETE",command=delete)

#SUBMENU FOR VIEW
m3 = Menu(mymenu,tearoff=0)
var = IntVar()
m3.add_checkbutton(label="STATUS BAR",variable=var,command=status_bar)

mymenu.add_cascade(label="FILE",menu=m1)
mymenu.add_cascade(label="EDIT",menu=m2)
mymenu.add_cascade(label="VIEW",menu=m3)
mymenu.add_command(label="FONT",command=my_font)
mymenu.add_command(label="ABOUT",command=myfunc)

root.config(menu=mymenu)

#CREATING A SCROLLBAR IN TEXTAREA.
scroll = Scrollbar(textarea,cursor="arrow")
scroll.config(command=textarea.yview)
scroll.pack(side=RIGHT,fill=Y)
textarea.config(yscrollcommand=scroll.set)

#THIS HELPS TO ADD FEATURES IN WINDOW.
root.mainloop()