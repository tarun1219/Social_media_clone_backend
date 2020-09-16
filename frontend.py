from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.user_delete(0,END)
    e1.user_insert(END,selected_tuple[1])

       

def user_view_command():
    list1.delete(0,END)
    for row in backend.user_view():
        list1.insert(END,row)
def user_insert_command():
    backend.user_insert(userid.get(),username.get())
    list1.delete(0,END)
    list1.insert(END,(userid.get(),username.get()))

def photo_view_command():
    list1.delete(0,END)
    for row in backend.photo_view():
        list1.insert(END,row)
def photo_insert_command():
    backend.photo_insert(photoid.get(),imageurl.get(),pics_userid.get())
    list1.delete(0,END)
    list1.insert(END,(photoid.get(),imageurl.get(),userid.get()))

def like_view_command():
    list1.delete(0,END)
    for row in backend.like_view():
        list1.insert(END,row)
def like_insert_command():
    backend.like_insert(userlike.get(),userliked.get())
    list1.delete(0,END)
    list1.insert(END,(userlike.get(),userliked.get()))
def follower_view_command():
    list1.delete(0,END)
    for row in backend.follower_view():
        list1.insert(END,row)
def follower_insert_command():
    backend.follower_insert(follower.get(),followee.get())
    list1.delete(0,END)
    list1.insert(END,(follower.get(),followee.get()))
def comm_view_command():
    list1.delete(0,END)
    for row in backend.comm_view():
        list1.insert(END,row)
def comm_insert_command():
    backend.comm_insert(commid.get(),comment.get(),cuserid.get(),cpicid.get())
    list1.delete(0,END)
    list1.insert(END,(commid.get(),comment.get(),cuserid.get(),cpicid.get()))
def tag_view_command():
    list1.delete(0,END)
    for row in backend.tag_view():
        list1.insert(END,row)
def tag_insert_command():
    backend.tag_insert(tagid.get(),tagname.get())
    list1.delete(0,END)
    list1.insert(END,(tagid.get(),tagname.get()))
window=Tk()
window.wm_title("Social Media")

l1=Label(window,text="User")
l1.grid(row=0,column=0)
userid=IntVar()
e1=Entry(window,textvariable=userid)
e1.grid(row=0,column=1)
username=StringVar()
e2=Entry(window,textvariable=username)
e2.grid(row=0,column=2)
user_insert=Button(window,text="Insert", width=12,command=user_insert_command)
user_insert.grid(row=0,column=5)
user_view=Button(window,text="View", width=12,command=user_view_command)
user_view.grid(row=0,column=6)


l2=Label(window,text="Photos")
l2.grid(row=1,column=0)
photoid=IntVar()
e1=Entry(window,textvariable=photoid)
e1.grid(row=1,column=1)
imageurl=StringVar()
e1=Entry(window,textvariable=imageurl)
e1.grid(row=1,column=2)
pics_userid=IntVar()
e1=Entry(window,textvariable=userid)
e1.grid(row=1,column=3)
photo_insert=Button(window,text="Insert", width=12,command=photo_insert_command)
photo_insert.grid(row=1,column=5)
photo_view=Button(window,text="View", width=12,command=photo_view_command)
photo_view.grid(row=1,column=6)

l3=Label(window,text="Likes")
l3.grid(row=2,column=0)
userlike=IntVar()
e1=Entry(window,textvariable=userlike)
e1.grid(row=2,column=1)
userliked=IntVar()
e2=Entry(window,textvariable=userliked)
e2.grid(row=2,column=2)
like_insert=Button(window,text="Insert", width=12,command=like_insert_command)
like_insert.grid(row=2,column=5)
like_view=Button(window,text="View", width=12,command=like_view_command)
like_view.grid(row=2,column=6)


l4=Label(window,text="Follower")
l4.grid(row=3,column=0)
follower=StringVar()
e1=Entry(window,textvariable=follower)
e1.grid(row=3,column=1)
followee=StringVar()
e2=Entry(window,textvariable=followee)
e2.grid(row=3,column=2)
follower_insert=Button(window,text="Insert", width=12,command=follower_insert_command)
follower_insert.grid(row=3,column=5)
follower_view=Button(window,text="View", width=12,command=follower_view_command)
follower_view.grid(row=3,column=6)

l5=Label(window,text="Comments")
l5.grid(row=4,column=0)
commid=IntVar()
e1=Entry(window,textvariable=commid)
e1.grid(row=4,column=1)
comment=StringVar()
e2=Entry(window,textvariable=comment)
e2.grid(row=4,column=2)
cuserid=IntVar()
e3=Entry(window,textvariable=cuserid)
e3.grid(row=4,column=3)
cpicid=IntVar()
e4=Entry(window,textvariable=cpicid)
e4.grid(row=4,column=4)
comm_insert=Button(window,text="Insert", width=12,command=comm_insert_command)
comm_insert.grid(row=4,column=5)
comm_view=Button(window,text="View", width=12,command=comm_view_command)
comm_view.grid(row=4,column=6)

l6=Label(window,text="Tags")
l6.grid(row=5,column=0)
tagid=IntVar()
e1=Entry(window,textvariable=tagid)
e1.grid(row=5,column=1)
tagname=StringVar()
e1=Entry(window,textvariable=tagname)
e1.grid(row=5,column=2)
tag_insert=Button(window,text="Insert", width=12,command=tag_insert_command)
tag_insert.grid(row=5,column=5)
tag_view=Button(window,text="View", width=12,command=tag_view_command)
tag_view.grid(row=5,column=6)

list1=Listbox(window,height=15,width=115)
list1.grid(row=8,column=0,rowspan=25,columnspan=16)

    #list1.configure(yscrollcommand=sb1.set)
    #sb1.configure(command=list1.yview)

    #list1.bind('<<ListboxSelect>>',get_selected_row)


window.mainloop()



