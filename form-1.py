from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
def Create():
    id = user_entry.get()
    name =name_entry.get()
    phone = phone_entry.get()

    if(id == ""or name == "" or phone == ""):
        MessageBox.showinfo("Alert","Insert values!!")

    else:
        con = mysql.connect(host="localhost",user="root",password="Sundar@12345",database="tkinter_db")  
        cursor = con.cursor()
        cursor.execute("insert into users values('" + id + "', '"+ name+"','"+ phone +  "')")  
        cursor.execute("commit")

        MessageBox.showinfo("Status","Successfully inserted!")
        con.close();

def Update():
    id = user_entry.get()
    name =name_entry.get()
    phone = phone_entry.get()

    if(id == ""or name == "" or phone == ""):
        MessageBox.showinfo("Alert","Insert values!!")

    else:
        con = mysql.connect(host="localhost",user="root",password="Sundar@12345",database="tkinter_db")  
        cursor = con.cursor()
        cursor.execute("Update users set name ='" + name + "', phone='"+ phone+"' where id = '"+id+"'")  
        cursor.execute("commit")

        MessageBox.showinfo("Status","Successfully updated!")
        con.close();

def Delete():

    if(user_entry.get()==""):
        MessageBox.showinfo("Alert","Enter ID to delete!!")

    else:
        con = mysql.connect(host="localhost",user="root",password="Sundar@12345",database="tkinter_db")  
        cursor = con.cursor()
        cursor.execute("delete from users where id ='"+user_entry.get()+"'")  
        cursor.execute("commit");
        
        user_entry.delete(0,'end')
        name_entry.delete(0,'end')
        phone_entry.delete(0,'end')

        MessageBox.showinfo("Status","Successfully deleted!")
        con.close();

def Select():

    if(user_entry.get()==""):
        MessageBox.showinfo("Alert","Enter ID to select!!")

    else:
        con = mysql.connect(host="localhost",user="root",password="Sundar@12345",database="tkinter_db")  
        cursor = con.cursor()
        cursor.execute("select * from users where id ='"+user_entry.get()+"'")  
        rows = cursor.fetchall()

        for row in rows:
            name_entry.insert(0,row[1])
            phone_entry.insert(0,row[2])
      
            con.close();

root = Tk()
root.geometry("350x200")
root.title("CRUD")
root.eval('tk::PlaceWindow . Center')
user_id = Label(root, text="Id:")

user_id.place(x=50,y=30)
user_entry = Entry (root, width=32)
user_entry.place(x=150,y=30)

name = Label(root, text="Full name:")
name.place(x=50,y=80)
name_entry = Entry(root, width=32)
name_entry.place(x=150,y=80)

phone = Label(root,text="Phone")
phone.place(x=50,y=130)
phone_entry = Entry(root, width=32)
phone_entry.place(x=150,y=130)

Create_Button = Button(root,text="Create",command=Create, bg='green').place(x=150,y=160) 
Update_Button = Button(root,text="Update",command=Update, bg='yellow').place(x=200,y=160) 
Delete_Button = Button(root,text="Delete",command=Delete, bg='red').place(x=253,y=160) 
Select_Button = Button(root,text="Select",command=Select, bg='grey').place(x=303,y=160) 

root.mainloop()