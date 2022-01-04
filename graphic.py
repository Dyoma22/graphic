from tkinter import *
click=0
def clicker(event):
	global click
	click+=1
	if click==100:
		click=0
	lbl.configure(text=click)
def clicker_minus(event):
	global click
	if click==-100:
		click=0
	click-=1
	lbl.configure(text=click)
def txt_to_lbl(event):
	#pass
	text=txt.get()#From Entry to text
	lbl.configure(text=text)
	txt.delete(0,END)
def valik():
	valik_=var.get()
	lbl.configure(text=valik_)
	txt.insert(0,valik_)
okno=Tk()
okno.title("Okno Name")
okno.geometry("600x800")
scrollbar=Scrollbar(okno)
scrollbar.pack(side=RIGHT,fill=Y)
knopka=Button(okno,text="Im button\nPress me!",font="Arial 20",fg="black",bg="lightblue",height=4,width=20,relief=GROOVE)#RAISED, SUNKEN
knopka.bind("<Button-1>",clicker)#Левая кнопка мыши
knopka.bind("<Button-3>",clicker_minus)#Правая кнопка мыши
lbl=Label(okno,text="...",height=4,width=20,font="Arial 20",fg="black",bg="blue")
txt=Entry(okno,width=20,font="Arial 20",fg="lightblue",bg="black",justify=CENTER)
txt.bind("<Return>",txt_to_lbl)#Enter
i1=PhotoImage(file="1.png")
i2=PhotoImage(file="2.png")
i3=PhotoImage(file="3.png")
var=StringVar()
var.set("One")
r1=Radiobutton(okno,image=i1,variable=var,value="One",command=valik)
r2=Radiobutton(okno,image=i2,variable=var,value="Two",command=valik)
r3=Radiobutton(okno,image=i3,variable=var,value="Three",command=valik)
lb3=Listbox(okno)
lb3.insert(1, "Hello")
lb3.insert(2, "World")
lb3.insert(3, ":)")
lb3.insert(4, "You can copy me!")




txt.pack()#pack Добавляет в программу функцию
lbl.pack()
knopka.pack()#side=LEFT,TOP,RIGHT НАХОЖДЕНИЯ КНОПКИ
r1.pack()
r2.pack()
r3.pack()
lb3.pack()
okno.mainloop()
