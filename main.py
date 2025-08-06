#main program
import module as mo
import tkinter as tk
from tkinter import ttk

#Option GUI using tkinter

def obc1(): #action when button is pressed
    global option #sets var to global so we can use outside the func.
    option=1
    window.destroy() #closes window
def obc2(): #action when button is pressed
    global option #sets var to global so we can use outside the func.
    option=2
    window.destroy() #closes window

window=tk.Tk() #initialises window
window.title("Options: ")
window.geometry('300x200')

but1=tk.Button(window,text="Add record",command=obc1,width=20) #obc=on button command
but2=tk.Button(window,text="Display record",command=obc2,width=20)

but1.pack(pady=40) #spacing between buttons
but2.pack()
window.mainloop()

#options
if(option==1):
    #using tkinter to make an entry form and add the record
    def enter(): #acts when add button is pressed
        mo.store('../micro project/textfile.txt',namebox.get(),m1box.get(),
                 m2box.get(),m3box.get(),m4box.get(),m5box.get())
        win1.destroy()

    win1=tk.Tk()
    win1.geometry("300x300")
    win1.title("Add student record")
    namelabel=tk.Label(win1,text="Enter Student Name")
    namelabel.pack()
    namebox=tk.Entry(win1)
    namebox.pack()

    m1label=tk.Label(win1,text="Enter 1st sub marks: ")
    m1label.pack()
    m1box=tk.Entry(win1)
    m1box.pack()

    m2label=tk.Label(win1,text="Enter 2nd sub marks: ")
    m2label.pack()
    m2box=tk.Entry(win1)
    m2box.pack()

    m3label=tk.Label(win1,text="Enter 3rd sub marks: ")
    m3label.pack()
    m3box=tk.Entry(win1)
    m3box.pack()

    m4label=tk.Label(win1,text="Enter 4th sub marks: ")
    m4label.pack()
    m4box=tk.Entry(win1)
    m4box.pack()

    m5label=tk.Label(win1,text="Enter 5th sub marks: ")
    m5label.pack()
    m5box=tk.Entry(win1)
    m5box.pack()

    add_button=tk.Button(text="Add Record",command=enter)
    add_button.pack(pady=10)
    
    win1.mainloop()

elif(option==2):
    #Tkinter GUI for a simple textbox and button to enter name to find record
    def find():
        global data
        data=mo.retrieve('../micro project/textfile.txt',namebox.get())
        win2.destroy()
    win2=tk.Tk()
    win2.geometry("200x150")
    win2.title("Find Student Record")

    namelabel=tk.Label(win2,text="Enter Name")
    namelabel.pack(pady=10)
    namebox=tk.Entry(win2)
    namebox.pack()
    findbtn=tk.Button(win2,text="Find Record",command=find) #command executes find function when pressed
    findbtn.pack(pady=10)
    win2.mainloop()
    
    #Now we use Tkinter GUI to display record using the globalised data
    #create window
    win3=tk.Tk()
    win3.geometry("800x80")
    win3.title("Student Report Card")

    #treeview
    table=ttk.Treeview(win3,columns=('name','m1','m2','m3','m4','m5','grade'),show='headings') 
    #the elements in the columns are just placeholders, 'headings is used to get it consecutively
    table.heading('name',text="Student Name",)
    table.column("name",width=40,anchor="center") #allows us to adjust the width of each column
    table.heading('m1',text="Math")
    table.column("m1",width=20,anchor="center")
    table.heading('m2',text="Science")
    table.column("m2",width=20,anchor="center")
    table.heading('m3',text="Theology")
    table.column("m3",width=20,anchor="center")
    table.heading('m4',text="CompSci")
    table.column("m4",width=20,anchor="center")
    table.heading('m5',text="Morals")
    table.column("m5",width=20,anchor="center")
    table.heading('grade',text="grade")
    table.column("grade",width=30,anchor="center")
    table.pack(fill='both',expand=True) #fills the window with the columns of the table
    #inserting the data into the table
    try:
        table.insert(parent='',index=0,values=tuple(data))
        #if the data does not exist, the retrieve function will return an improper value
        #so we use exception handling to terminate the display table and show a warning GUI table
    except TypeError:
        win3.destroy()
        win4=tk.Tk()
        win4.geometry("200x30")
        win4.title("Warning!!")
        notfound=tk.Label(win4,text="Record Does Not Exist!!")
        notfound.pack()
        win4.mainloop()
        
    

    win3.mainloop()

    
