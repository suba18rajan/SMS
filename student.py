from tkinter import *
from tkinter import ttk
import pymysql
from tkcalendar import *
from tkinter import messagebox
class student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1520x800+0+0")
        
        title = Label(
            self.root,
            text="Student Management System",
            bd=10,
            relief=GROOVE,
            font=("goudy old style", 40, "bold"),
            bg="crimson",
            fg="white",
        )
        title.pack(side=TOP,fill=X)
        
        self.var_roll_no=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_dob=StringVar()
        self.txt_address=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=600)


        m_title=Label(Manage_Frame,text="Mange Students",bg="crimson",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll_no = Label(Manage_Frame, text="Roll No",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll_no.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll_no=Entry(Manage_Frame,textvariable=self.var_roll_no,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll_no.grid(row=1,column=1,pady=10,padx=20,sticky="w")


        lbl_name = Label(Manage_Frame, text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.var_name,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email = Label(Manage_Frame, text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email=Entry(Manage_Frame,textvariable=self.var_email,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state='readonly')
        combo_gender['values']=("Select","Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)

        lbl_contact = Label(Manage_Frame, text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact=Entry(Manage_Frame,textvariable=self.var_contact,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        #lbl_dob= Label(Manage_Frame, text="D.O.B",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        #lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        #txt_dob=Entry(Manage_Frame,textvariable=self.var_dob,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        #txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        
        def pick_date(event):
            global cal,date_window
            date_window=Toplevel()
            date_window.grab_set()
            date_window.title('Choose Date Of Birth')
            date_window.geometry('250x220+590+370')
            cal=Calendar(date_window,selectmode="day",date_pattern="dd/mm/yyyy")
            cal.place(x=0,y=0)

            submit_btn=Button(date_window,text="Submit",command=grab_date)
            submit_btn.place(x=80,y=190)


        def grab_date():
           dob_entry.delete(0,END)
           dob_entry.insert(0,cal.get_date())
           date_window.destroy()

        dob=Label(self.root,text="D.O.B",bg="crimson",fg="white",font=("times new roman",17,"bold"))
        dob.place(x=60,y=490)
        dob_entry=Entry(self.root,textvariable=self.var_dob,highlightthickness=0,relief=GROOVE,font=("times new roman",15,"bold"))
        dob_entry.place(x=190,y=490)
        dob_entry.insert(0,"dd/mm/yyyy")
        dob_entry.bind("<1>",pick_date)



        lbl_address= Label(Manage_Frame, text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_address.place(x=20,y=450)
        

        self.txt_address=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_address.place(x=160,y=440)


        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=15,y=530,width=420)


        addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)



        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=600,y=100,width=850,height=600)
        
        lbl_search= Label(Detail_Frame, text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,padx=30,pady=10,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("Roll_no","Name","Contact")
        combo_search.grid(row=0,column=1,padx=30,pady=10)

        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,padx=30,pady=10,sticky="w")

        Searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=30,pady=10)
        Showallbtn=Button(Detail_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=30,pady=10)


        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=820,height=500)


        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll_no","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll_no",text="Roll No")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("roll_no",width=120)
        self.Student_table.column("name",width=120)
        self.Student_table.column("email",width=120)
        self.Student_table.column("gender",width=120)
        self.Student_table.column("contact",width=120)
        self.Student_table.column("dob",width=120)
        self.Student_table.column("address",width=170)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        #footer
        lbl_footer=Label(self.root,text="SMS-Student Management System | Developed By SUBASHINI Student of CSE\n Adhiyamaan College Of Engineering(Autonomous),Hosur",font=("times new roman",12),bg="crimson",fg="white",relief=GROOVE).pack(side=BOTTOM,fill=X)


    def add_students(self):
        if self.var_roll_no.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error","All fields are required!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",
                (self.var_roll_no.get(),
                 self.var_name.get(),
                self.var_email.get(),
                self.var_gender.get(),
                self.var_contact.get(),
                self.var_dob.get(),
                self.txt_address.get('1.0',END)
                ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success","Record has been inserted")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()    

    def clear(self):
        self.var_roll_no.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.txt_address.delete("1.0", END)
        
        
    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.var_roll_no.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END,row[6])

    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
         self.var_name.get(),
         self.var_email.get(),
         self.var_gender.get(),
         self.var_contact.get(),
         self.var_dob.get(),
         self.txt_address.get('1.0',END),
         self.var_roll_no.get()
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.var_roll_no.get())
        con.commit()
        con.close
        self.fetch_data()
        self.clear()
        
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()   
        




        
        


root=Tk()
obj=student(root)
root.mainloop()