from tkinter import *
def open_window():
    import frontend
window=Tk()

window.wm_title("Social Media")

#bg_image=PhotoImage(file='download.jpg')
#bg_label=Label(window,image=bg_image)
#bg_label.place(x=0,y=0,relwidth=1,relheight=1)
window.geometry("500x500+150+150")
label_0=Label(window,text="Social Media",width=20,font=("bold",20))
label_0.place(x=90,y=53)

label_1=Label(window,text="Username",width=20,font=("bold",10))
label_1.place(x=85,y=130)
name=StringVar()
entry_1=Entry(window,textvariable=name)
entry_1.place(x=215,y=130)

label_2=Label(window,text="Email ID",width=20,font=("bold",10))
label_2.place(x=85,y=180)
email=StringVar()
entry_2=Entry(window,textvariable=email)
entry_2.place(x=215,y=180)

label_3=Label(window,text="Gender",width=20,font=("bold",10))
label_3.place(x=85,y=230)
var=IntVar()
Radiobutton(window,text="Male",padx=5,variable=var,value=1).place(x=200,y=230)
Radiobutton(window,text="Female",padx=20,variable=var,value=2).place(x=255,y=230)

label_4=Label(window,text="Country",width=20,font=("bold",10))
label_4.place(x=85,y=285)
list_country=['Canada','India','UK','Nepal','Germany','US','France','Isreal']
c=StringVar()
droplist=OptionMenu(window,c,*list_country)
droplist.config(width=15)
c.set('Choose Country')
droplist.place(x=220,y=280)

Button(window,text='Register',width=20,bg='grey',fg='white',command=open_window).place(x=180,y=360)
#label_1=Label(window,text="User Name")
#label_1.grid(row=0,column=0)

#text_1=Text(window,height=1,width=20)
#text_1.grid(row=0,column=1)
window.mainloop()
