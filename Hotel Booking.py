from openpyxl import *
from tkinter import *
from PIL import ImageTk, Image
import sqlite3




def focus1(event): 

    LastName_field.focus_set() 
  
  
def focus2(event): 
    
    FName_field.focus_set() 
  
  
def focus3(event): 
    # set focus on the share_field box 
    share_field.focus_set() 
  
  
def focus4(event): 
    
    business_no_field.focus_set() 
    
def focus5(event):
    mobile_no_field.focus_set()
  

def focus6(event): 
    # set focus on the email_id_field box 
    email_id_field.focus_set() 
  
  
def focus7(event): 
    
    DOAr_field.focus_set() 

def focus8(event):
        DODe_field.focus_set()
    
    
def focus9(event):
    
    CCName_field.focus_set()
    
    
def focus10(event):
    
    CC_no_field.focus_set()
    
    
def focus11(event):
    
    ExDate_field.focus_set()
    
    
def focus12(event):
        CVV_field.focus_set()
    
def focus13(event):
    Sig_field.focus_set()
    
def focus14(event):
    Pri_field.focus_set()
    
def focus15(event):
    Date_field.focus_set()



  
def clear(): 
      
    title_field.delete(0, END) 
    LastName_field.delete(0, END) 
    FName_field.delete(0, END) 
    share_field.delete(0, END) 
    business_no_field.delete(0, END) 
    mobile_no_field.delete(0, END)
    email_id_field.delete(0, END) 
    DOAr_field.delete(0, END) 
    DODe_field.delete(0, END)
    CCName_field.delete(0, END)
    CC_no_field.delete(0, END)
    ExDate_field.delete(0, END)
    CVV_field.delete(0, END)
    Sig_field.delete(0, END)
    Pri_field.delete(0, END)
    Date_field.delete(0, END)
  
  
def insert(): 
      
    if (title_field.get() == "" and
        LastName_field.get() == "" and
        FName_field.get() == "" and
        share_field.get() == "" and
        business_no_field.get() == "" and
        mobile_no_field.get() == "" and
        email_id_field.get() == "" and
        DOAr_field.get() == "" and
        DODe_field.get() == "" and
        CCName_field.get() == "" and
        CC_no_field.get() == "" and
        ExDate_field.get() == "" and
        CVV_field.get() == ""): 
              
        print("empty input") 
  
    else: 

        
        title_field.focus_set() 
        a=title_field.get()
        b=LastName_field.get()
        c=FName_field.get()
        d=share_field.get()
        e=business_no_field.get()
        f=mobile_no_field.get()
        g=email_id_field.get()
        h=DOAr_field.get()
        i=DODe_field.get()
        j=CCName_field.get()
        k=CC_no_field.get()
        l=ExDate_field.get()
        m=CVV_field.get()
        n=var1.get()
        o=var3.get()
        conn = sqlite3.connect('form2.db')
        with conn:
            cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Student (title TEXT,Last TEXT,First TEXT,Share TEXT,Buissness INT,Mobile INT,Email TEXT,Arrival INT,Departure INT,CCname TEXT,CCno INT,Expiry INT,CVV INT,Payment INT,Room INT)')
        cursor.execute('INSERT INTO Student (title,Last,First,Share,Buissness,Mobile,Email,Arrival,Departure,CCname,CCno,Expiry,CVV,Payment,Room) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,))
        conn.commit()

        clear() 
  
  
if __name__ == "__main__": 
      
    root = Tk() 
    root.configure(background='white') 
  
   
    root.title("Hotel Booking Management") 
  
    root.geometry("800x700") 
   
  
    
    heading = Label(root, text="Fill your details to complete your room Booking", bg="white") 
  
    
    title = Label(root, text="Title", bg="white") 
  
    LastName = Label(root, text="Last Name", bg="white") 
  
    FName = Label(root, text="First Name", bg="white") 
  
    
    share = Label(root, text="Share With", bg="white") 
  
    
    business_no = Label(root, text="Business No.", bg="white")
    
    
    mobile_no = Label(root, text="Mobile No.", bg="white")
  
    email_id = Label(root, text="Email id", bg="white") 
  
    DOAr = Label(root, text="Date of Arrival", bg="white") 
    
    
    DODe = Label(root, text="Date of Departure", bg="white")
    
    CCName = Label(root, text="Credit Card Name", bg="white")
    
    CC_no = Label(root, text="Credit Card No.", bg="white")
    
    
    ExDate = Label(root, text="Expiry Date", bg="white")
    
    
    CVV = Label(root, text="CVV No.", bg="white")
    
    
    paymentM = Label(root, text="Payment Methord", bg="white")
    
    var1=IntVar()
    CC = Radiobutton(root, text="Credit Card", variable=var1, value=1)
    
    
    var2=IntVar()
    DBT = Radiobutton(root, text="Direct Bank Transfer", variable=var1, value=2)
    
    NR = Label(root, text="Negotiated Rates", bg="white")
    
    DRS = Label(root, text="Delux Room Single", bg="white")
    Label(root, text="Delux Room Double", bg="white").grid(row=16, column=2)
    Label(root, text="R1700", bg="white").grid(row=16, column=1)
    Label(root, text="R1700", bg="white").grid(row=16, column=3)
    Label(root, text="Suites Room Single", bg="white").grid(row=17, column=0)
    Label(root, text="Suites Room Double", bg="white").grid(row=17, column=2)
    Label(root, text="R1700", bg="white").grid(row=17, column=3)
    Label(root, text="R1700", bg="white").grid(row=17, column=1)
    
    RP = Label(root, text="Room Preference:", bg="white")
    
    var3=IntVar()
    Radiobutton(root, text="King Bed", variable=var3, value=1).grid(row=18, column=1)
    
    var4=IntVar()
    Radiobutton(root, text="Twin Bed", variable=var3,value=2).grid(row=18, column=2)
    
    line1 = Label(root, text="The above rates are quoted per room, per night. The rates include breakfast, 14% vat, and Excludes 1% Tourism Levy\n and a voluntary R10 donation to the Arabella Community Trust that will be levies onto your account.", bg="white")
    
    line2 = Label(root, text="Total amount payable      ZAR___________ x______________ nights = ZAR________________ due to Arabella\n Hotel and Spa", bg="white")
    
    line3 = Label(root, text="Credit Card will be charged on receipt of this form and details will also be used to settle all incidentals not settle on\n departure. A copy of the final folio will be sent to you should there be any unsettled charges.", bg="white")
    
    line4 = Label(root, text="In order to qualify for the above rates, your booking needs to be made on or before 15th January 2016", bg="white")
    
    line5 = Label(root, text="Terms and conditions can be found on the next page.", bg="white")
    
    line6 = Label(root, text="The rate is valid for seven days before and after the conference dates. Check in time is 14:00 & check out time is 11:00", bg="white")
    
    line7 = Label(root, text="By your signature hereto, you are accepting all terms and conditions specified on this form and confirm that all information\n given is current and accurate.", bg="white")
    
    Sig = Label(root, text="Signature", bg="white")
    
    Pri = Label(root, text="Print Name", bg="white")
    
    Date = Label(root, text="Date", bg="white")
  
    heading.grid(row=0, column=1) 
    title.grid(row=1, column=0) 
    LastName.grid(row=2, column=0) 
    FName.grid(row=3, column=0) 
    share.grid(row=4, column=0) 
    business_no.grid(row=5, column=0)
    mobile_no.grid(row=6, column=0)
    email_id.grid(row=7, column=0) 
    DOAr.grid(row=8, column=0) 
    DODe.grid(row=9, column=0) 
    CCName.grid(row=10, column=0) 
    CC_no.grid(row=11, column=0) 
    ExDate.grid(row=12, column=0) 
    CVV.grid(row=13, column=0)
    paymentM.grid(row=14, column=0)
    CC.grid(row=14, column=1)
    DBT.grid(row=14, column=2)
    NR.grid(row=15, column=0)
    DRS.grid(row=16, column=0)
    RP.grid(row=18, column=0)
    Sig.grid(row=26, column=0)
    Pri.grid(row=26, column=2)
    Date.grid(row=27, column=0)
    line1.grid(row=19, column=0,columnspan=4)
    line2.grid(row=20, column=0,columnspan=4)
    line3.grid(row=21, column=0,columnspan=4)
    line4.grid(row=22, column=0,columnspan=4)
    line5.grid(row=23, column=0,columnspan=4)
    line6.grid(row=24, column=0,columnspan=4)
    line7.grid(row=25, column=0,columnspan=4)
    

 
  
    title_field = Entry(root) 
    LastName_field = Entry(root) 
    FName_field = Entry(root) 
    share_field = Entry(root) 
    business_no_field = Entry(root) 
    mobile_no_field = Entry(root)
    email_id_field = Entry(root) 
    DOAr_field = Entry(root) 
    DODe_field = Entry(root)
    CCName_field = Entry(root)
    CC_no_field = Entry(root)
    ExDate_field = Entry(root)
    CVV_field = Entry(root)
    Sig_field = Entry(root)
    Pri_field = Entry(root)
    Date_field = Entry(root)
  
  
    title_field.bind("<Return>", focus1) 
 
    LastName_field.bind("<Return>", focus2) 
  
    

    FName_field.bind("<Return>", focus3) 
  
    

    share_field.bind("<Return>", focus4) 
  
    business_no_field.bind("<Return>", focus5) 
    
    mobile_no_field.bind("<Return>", focus6)
    email_id_field.bind("<Return>", focus7) 
    

    DOAr_field.bind("<Return>", focus8) 
    
    

    DODe_field.bind("<Return>", focus9) 
    
    CCName_field.bind("<Return>", focus10) 
    
    CC_no_field.bind("<Return>", focus11) 
    
    ExDate_field.bind("<Return>", focus12) 
    
    CVV_field.bind("<Return>", focus13)
    
    Sig_field.bind("<Return>", focus14)
    
    Pri_field.bind("<Return>", focus15)
  
 
    title_field.grid(row=1, column=1, ipadx="50") 
    LastName_field.grid(row=2, column=1, ipadx="50") 
    FName_field.grid(row=3, column=1, ipadx="50") 
    share_field.grid(row=4, column=1, ipadx="50") 
    business_no_field.grid(row=5, column=1, ipadx="50") 
    mobile_no_field.grid(row=6, column=1, ipadx="50")
    email_id_field.grid(row=7, column=1, ipadx="50") 
    DOAr_field.grid(row=8, column=1, ipadx="50") 
    DODe_field.grid(row=9, column=1, ipadx="50")
    CCName_field.grid(row=10, column=1, ipadx="50")
    CC_no_field.grid(row=11, column=1, ipadx="50")
    ExDate_field.grid(row=12, column=1, ipadx="50")
    CVV_field.grid(row=13, column=1, ipadx="50")
    Sig_field.grid(row=26, column=1, ipadx="50")
    Pri_field.grid(row=26, column=3, ipadx="50")
    Date_field.grid(row=27, column=1, ipadx="50")
    
    
    
  
    submit = Button(root, text="Submit", fg="Black", 
                            bg="Red", command=insert) 
    submit.grid(row=29, column=2) 
  
  
    root.mainloop()
my_conn = sqlite3.connect('form2.db')
###### end of connection ####

##### tkinter window ######
import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.title("Booking Database")
my_w.geometry("950x250") 



r_set=my_conn.execute('''SELECT * from student LIMIT 0,10''');
n_set=["Title",'Last Name','First Name','Share With','Business Number','Mobile Number','Email ID','Date Of Arrival','Date Of Departure','Credit Card Name','Credit Card Number','Expiry Date','CVV Number','Payment Method','Room Preference']
for i in range(len(n_set)):
    e = Text(my_w, width=14, fg='black',font=("Helvetica 10"),height=2, wrap = WORD) 
    e.grid(row=0, column=i) 
    e.insert(END, n_set[i])
i=1
for student in r_set: 
    for j in range(len(student)):
        e = Text(my_w, width=12, fg='blue',height=1) 
        e.grid(row=i, column=j) 
        e.insert(END, student[j])
    i=i+1
my_w.mainloop()

 
 
