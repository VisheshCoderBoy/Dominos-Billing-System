import tkinter 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root=Tk()

a=StringVar()


b=("Cheese Pizza","California Pizza",'Pepperoni Pizza')
c=('Small','Medium','Large')

lbl=ttk.Label(root,text='Dominos Pizza Billing System ',font='Helvetica 22')
lbl.grid(padx=50)

lbl1=Label(root,text='Select Pizza :',font='Arial 18').grid(row=1,column=0,padx=10,pady=20,sticky=W)

select=ttk.Combobox(root,textvariable=a,width=30)
select['values']=b
select['state']='readonly'
select.place(x=170,y=62)

lbl2=Label(root,text='Select Size :',font='Arial 18').grid(row=2,column=0,padx=10,pady=10,sticky=W)
select1=ttk.Combobox(root,textvariable=b,width=30)
select1['values']=c
select1['state']='readonly'
select1.place(x=170,y=128)

iv=IntVar()
iv1=IntVar()
iv2=IntVar()


lbl2=Label(root,text="Select Toppings:",font='Arial 18').grid(row=3,column=0,sticky=W,padx=10,pady=10)

chk=Checkbutton(root,text='Capsicum',font='Arial 16',variable=iv)
chk.place(x=195,y=173)

chk1=Checkbutton(root,text='Onions',font='Arial 16',variable=iv1)
chk1.place(x=195,y=203)

chk2=Checkbutton(root,text='Tomatoes',font='Arial 16',variable=iv2)
chk2.place(x=195,y=233)


def abc():


    if select.get()=='Cheese Pizza'and select1.get()=='Large' and iv.get()==1 and iv1.get()==1 and iv2.get()==1:
        oop=Label(root,text='Your total price is 500 ',font='Arial 16').place(x=165,y=353)
    elif select.get()=='California Pizza'and select1.get()=='Large' and iv.get()==1 and iv1.get()==1 and iv2.get()==1:
        oop=Label(root,text='Your total price is 500 ',font='Arial 16').place(x=165,y=353)
    elif select.get()=='California Pizza'and select1.get()=='Large' and iv.get()==1 and iv1.get()==1 and iv2.get()==1:
        oop=Label(root,text='Your total price is 500 ',font='Arial 16').place(x=165,y=353)

    elif select.get()=='Cheese Pizza'and select1.get()=='Medium' and iv.get()==1 and iv1.get()==1 and iv2.get()==1:
        oop=Label(root,text='Your total price is 400 ',font='Arial 16').place(x=165,y=353)
    elif select.get()=='California Pizza'and select1.get()=='Medium' and iv.get()==1 and iv1.get()==1 and iv2.get()==1:
        oop=Label(root,text='Your total price is 400 ',font='Arial 16').place(x=165,y=353)
    elif select.get()=='California Pizza'and select1.get()=='Medium' and iv.get()==1 and iv1.get()==1 and iv2.get()==1:
        oop=Label(root,text='Your total price is 400 ',font='Arial 16').place(x=165,y=353)

    elif select.get()=='Cheese Pizza'and select1.get()=='Small' and iv.get()==1 and iv1.get()==1 and iv2.get()==1:
        oo=Label(root,text='Your total price is 300 ',font='Arial 16').place(x=165,y=353)
    elif select.get()=='California Pizza'and select1.get()=='Small' and iv.get()==1 and iv1.get()==1 and iv2.get()==1:
        oo=Label(root,text='Your total price is 300 ',font='Arial 16').place(x=165,y=353)
    elif select.get()=='California Pizza'and select1.get()=='Small' and iv.get()==1 and iv1.get()==1 and iv2.get()==1:
        oo=Label(root,text='Your total price is 300 ',font='Arial 16').place(x=165,y=353)

    


    elif select.get()=='Cheese Pizza'and select1.get()=='Small' and iv.get()==1 and iv1.get()==1:
        asdfz=Label(root,text='Your total price is 250 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza'and select1.get()=='Small' and iv.get()==1 and iv1.get()==1:
        asdfz=Label(root,text='Your total price is 250 ',font='Arial 16').place(x=165,y=353)
    elif select.get()=='Pepperoni Pizza' and select1.get()=='Small' and iv.get()==1 and iv1.get()==1 :
        asdfz=Label(root,text='Your total price is 250',font='Arial 16').place(x=165,y=353)
    

    elif select.get()=='Cheese Pizza'and select1.get()=='Medium' and iv.get()==1 and iv1.get()==1:
        zycv=Label(root,text='Your total price is 350 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza' and select1.get()=='Medium' and iv.get()==1 and iv1.get()==1 :
        zycv=Label(root,text='Your total price is 350',font='Arial 16').place(x=165,y=353)
    
    elif select.get()=='Pepperoni Pizza' and select1.get()=='Medium' and iv.get()==1  and iv1.get()==1:
        zycv=Label(root,text='Your total price is 350',font='Arial 16').place(x=165,y=353)


    elif select.get()=='Cheese Pizza'and select1.get()=='Large' and iv.get()==1 and iv1.get()==1:
        zyc=Label(root,text='Your total price is 450 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza' and select1.get()=='Large' and iv.get()==1 and iv1.get()==1 :
        zyc=Label(root,text='Your total price is 450',font='Arial 16').place(x=165,y=353)
    
    elif select.get()=='Pepperoni Pizza' and select1.get()=='Large' and iv.get()==1  and iv1.get()==1:
        zyc=Label(root,text='Your total price is 450',font='Arial 16').place(x=165,y=353)


    elif select.get()=='Cheese Pizza'and select1.get()=='Small' and iv.get()==1 and iv2.get()==1:
        asdz=Label(root,text='Your total price is 250 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza'and select1.get()=='Small' and iv.get()==1 and iv2.get()==1:
        asdz=Label(root,text='Your total price is 250 ',font='Arial 16').place(x=165,y=353)
    elif select.get()=='Pepperoni Pizza' and select1.get()=='Small' and iv.get()==1 and iv2.get()==1 :
        asdz=Label(root,text='Your total price is 250',font='Arial 16').place(x=165,y=353)
    

    elif select.get()=='Cheese Pizza'and select1.get()=='Medium' and iv.get()==1 and iv2.get()==1:
        zoy=Label(root,text='Your total price is 350 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza' and select1.get()=='Medium' and iv.get()==1 and iv2.get()==1 :
        zoy=Label(root,text='Your total price is 350',font='Arial 16').place(x=165,y=353)
    
    elif select.get()=='Pepperoni Pizza' and select1.get()=='Medium' and iv.get()==1  and iv2.get()==1:
        zoy=Label(root,text='Your total price is 350',font='Arial 16').place(x=165,y=353)


    elif select.get()=='Cheese Pizza'and select1.get()=='Large' and iv.get()==1 and iv2.get()==1:
        ziy=Label(root,text='Your total price is 450 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza' and select1.get()=='Large' and iv.get()==1 and iv2.get()==1 :
        ziy=Label(root,text='Your total price is 450',font='Arial 16').place(x=165,y=353)
    
    elif select.get()=='Pepperoni Pizza' and select1.get()=='Large' and iv.get()==1  and iv2.get()==1:
        ziy=Label(root,text='Your total price is 450',font='Arial 16').place(x=165,y=353)



    elif select.get()=='Cheese Pizza'and select1.get()=='Small' and iv1.get()==1 and iv2.get()==1:
        asdfz=Label(root,text='Your total price is 250 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza'and select1.get()=='Small' and iv.get()==1 and iv1.get()==1:
        asdfz=Label(root,text='Your total price is 250 ',font='Arial 16').place(x=165,y=353)
    elif select.get()=='Pepperoni Pizza' and select1.get()=='Small' and iv.get()==1 and iv1.get()==1 :
        z=Label(root,text='Your total price is 250',font='Arial 16').place(x=165,y=353)
    

    elif select.get()=='Cheese Pizza'and select1.get()=='Medium' and iv1.get()==1 and iv2.get()==1:
        zy=Label(root,text='Your total price is 350 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza' and select1.get()=='Medium' and iv1.get()==1 and iv2.get()==1 :
        zy=Label(root,text='Your total price is 350',font='Arial 16').place(x=165,y=353)
    
    elif select.get()=='Pepperoni Pizza' and select1.get()=='Medium' and iv1.get()==1  and iv2.get()==1:
        zy=Label(root,text='Your total price is 350',font='Arial 16').place(x=165,y=353)


    elif select.get()=='Cheese Pizza'and select1.get()=='Large' and iv1.get()==1 and iv2.get()==1:
        zy=Label(root,text='Your total price is 450 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza' and select1.get()=='Large' and iv1.get()==1 and iv2.get()==1 :
        zy=Label(root,text='Your total price is 450',font='Arial 16').place(x=165,y=353)
    
    elif select.get()=='Pepperoni Pizza' and select1.get()=='Large' and iv1.get()==1  and iv2.get()==1:
        zy=Label(root,text='Your total price is 450',font='Arial 16').place(x=165,y=353)
#___________________________________________________________________________________________________________________



    elif select.get()=='Cheese Pizza'and select1.get()=='Small' and iv.get()==1:
        z=Label(root,text='Your total price is 200 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza' and select1.get()=='Small' and iv.get()==1 :
        z=Label(root,text='Your total price is 200',font='Arial 16').place(x=165,y=353)
    
    elif select.get()=='Pepperoni Pizza' and select1.get()=='Small' and iv.get()==1 :
        z=Label(root,text='Your total price is 200',font='Arial 16').place(x=165,y=353)


    elif select.get()=='Cheese Pizza'and select1.get()=='Small' and iv1.get()==1:
        z=Label(root,text='Your total price is 200 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza' and select1.get()=='Small' and iv1.get()==1 :
        z=Label(root,text='Your total price is 200',font='Arial 16').place(x=165,y=353)
    
    elif select.get()=='Pepperoni Pizza' and select1.get()=='Small' and iv1.get()==1 :
        z=Label(root,text='Your total price is 200',font='Arial 16').place(x=165,y=353)


    elif select.get()=='Cheese Pizza'and select1.get()=='Small' and iv2.get()==1:
        z=Label(root,text='Your total price is 200 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza' and select1.get()=='Small' and iv2.get()==1 :
        z=Label(root,text='Your total price is 200',font='Arial 16').place(x=165,y=353)
    
    elif select.get()=='Pepperoni Pizza' and select1.get()=='Small' and iv2.get()==1 :
        z=Label(root,text='Your total price is 200',font='Arial 16').place(x=165,y=353)



    elif select.get()=='Cheese Pizza'and select1.get()=='Medium' and iv.get()==1:
        zy=Label(root,text='Your total price is 300 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza' and select1.get()=='Medium' and iv.get()==1 :
        zy=Label(root,text='Your total price is 300',font='Arial 16').place(x=165,y=353)
    
    elif select.get()=='Pepperoni Pizza' and select1.get()=='Medium' and iv.get()==1 :
        zy=Label(root,text='Your total price is 300',font='Arial 16').place(x=165,y=353)


    elif select.get()=='Cheese Pizza'and select1.get()=='Medium' and iv1.get()==1:
        zy=Label(root,text='Your total price is 300 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza' and select1.get()=='Medium' and iv1.get()==1 :
        zy=Label(root,text='Your total price is 300',font='Arial 16').place(x=165,y=353)
    
    elif select.get()=='Pepperoni Pizza' and select1.get()=='Medium' and iv1.get()==1 :
        zy=Label(root,text='Your total price is 300',font='Arial 16').place(x=165,y=353)


    elif select.get()=='Cheese Pizza'and select1.get()=='Medium' and iv2.get()==1:
        zy=Label(root,text='Your total price is 300 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza' and select1.get()=='Medium' and iv2.get()==1 :
        zy=Label(root,text='Your total price is 300',font='Arial 16').place(x=165,y=353)
    
    elif select.get()=='Pepperoni Pizza' and select1.get()=='Medium' and iv2.get()==1 :
        zy=Label(root,text='Your total price is 300',font='Arial 16').place(x=165,y=353)
    
    
    elif select.get()=='Cheese Pizza'and select1.get()=='Large' and iv.get()==1:
        azy=Label(root,text='Your total price is 400 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza' and select1.get()=='Large' and iv.get()==1 :
        azy=Label(root,text='Your total price is 400',font='Arial 16').place(x=165,y=353)
    
    elif select.get()=='Pepperoni Pizza' and select1.get()=='Large' and iv.get()==1 :
        azy=Label(root,text='Your total price is 400',font='Arial 16').place(x=165,y=353)


    elif select.get()=='Cheese Pizza'and select1.get()=='Large' and iv1.get()==1:
        azy=Label(root,text='Your total price is 400 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza' and select1.get()=='Large' and iv1.get()==1 :
        azy=Label(root,text='Your total price is 400',font='Arial 16').place(x=165,y=353)
    
    elif select.get()=='Pepperoni Pizza' and select1.get()=='Large' and iv1.get()==1 :
        azy=Label(root,text='Your total price is 400',font='Arial 16').place(x=165,y=353)


    elif select.get()=='Cheese Pizza'and select1.get()=='Large' and iv2.get()==1:
        azy=Label(root,text='Your total price is 400 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza' and select1.get()=='Large' and iv2.get()==1 :
        azy=Label(root,text='Your total price is 400',font='Arial 16').place(x=165,y=353)
    
    elif select.get()=='Pepperoni Pizza' and select1.get()=='Large' and iv2.get()==1 :
        azy=Label(root,text='Your total price is 400',font='Arial 16').place(x=165,y=353)




    elif select.get()=='Cheese Pizza'and select1.get()=='Small':
        q=Label(root,text='Your total price is 150 ',font='Arial 16').place(x=165,y=353)
    elif select.get()=='California Pizza'and select1.get()=='Small':
        q=Label(root,text='Your total price is 150 ',font='Arial 16').place(x=165,y=353)   
    elif select.get()=='Pepperoni Pizza'and select1.get()=='Small':
        q=Label(root,text='Your total price is 150 ',font='Arial 16').place(x=165,y=353)  

    elif select.get()=='Cheese Pizza'and select1.get()=='Medium':
        f=Label(root,text='Your total price is 250 ',font='Arial 16').place(x=165,y=353) 

    elif select.get()=='California Pizza'and select1.get()=='Medium':
        f=Label(root,text='Your total price is 250 ',font='Arial 16').place(x=165,y=353)
    elif select.get()=='Pepperoni Pizza'and select1.get()=='Medium':
        f=Label(root,text='Your total price is 250 ',font='Arial 16').place(x=165,y=353)

    elif select.get()=='Cheese Pizza'and select1.get()=='Large':
        s=Label(root,text='Your total price is 350 ',font='Arial 16').place(x=165,y=353) 
    elif select.get()=='California Pizza'and select1.get()=='Large':
        s=Label(root,text='Your total price is 350 ',font='Arial 16').place(x=165,y=353)      
    elif select.get()=='Pepperoni Pizza'and select1.get()=='Large':
        s=Label(root,text='Your total price is 350 ',font='Arial 16').place(x=165,y=353)

    elif select.get()=='Cheese Pizza':
        bd=Label(root,text='Please select the size ',font='Arial 16').place(x=165,y=353)
    elif select.get()=='California Pizza':
        bd=Label(root,text='Please select the size ',font='Arial 16').place(x=165,y=353)
    elif select.get()=='Pepperoni Pizza':
        bd=Label(root,text='Please select the size ',font='Arial 16').place(x=165,y=353)
    elif select1.get()=='Small':
        bd=Label(root,text='Please select the Pizza name ',font='Arial 16').place(x=165,y=353)
    elif select1.get()=='Medium':
        bd=Label(root,text='Please select the Pizza name ',font='Arial 16').place(x=165,y=353)
    elif select1.get()=='Large':
        bd=Label(root,text='Please select the Pizza name ',font='Arial 16').place(x=165,y=353)

    elif select1.get()=='Small' and iv.get()==1:
        bd=Label(root,text='Please select the Pizza name ',font='Arial 16').place(x=165,y=353)
    elif select1.get()=='Small' and iv1.get()==1:
        bd=Label(root,text='Please select the Pizza name ',font='Arial 16').place(x=165,y=353)
    elif select1.get()=='Small' and iv2.get()==1:
        bd=Label(root,text='Please select the Pizza name ',font='Arial 16').place(x=165,y=353)

    elif select1.get()=='Medium' and iv.get()==1:
        bd=Label(root,text='Please select the Pizza name ',font='Arial 16').place(x=165,y=353)
    elif select1.get()=='Medium' and iv1.get()==1:
        bd=Label(root,text='Please select the Pizza name ',font='Arial 16').place(x=165,y=353)
    elif select1.get()=='Medium' and iv2.get()==1:
        bd=Label(root,text='Please select the Pizza name ',font='Arial 16').place(x=165,y=353)

    elif select1.get()=='Large' and iv.get()==1:
        bd=Label(root,text='Please select the Pizza name ',font='Arial 16').place(x=165,y=353)
    elif select1.get()=='Large' and iv1.get()==1:
        bd=Label(root,text='Please select the Pizza name ',font='Arial 16').place(x=165,y=353)
    elif select1.get()=='Large' and iv2.get()==1:
        bd=Label(root,text='Please select the Pizza name ',font='Arial 16').place(x=165,y=353)    
        

    elif iv.get()==1:
        bdoo=Label(root,text='Please select the Pizza name and size',font='Arial 16').place(x=115,y=353)
    elif iv1.get()==1:
        bdoo=Label(root,text='Please select the Pizza name and size',font='Arial 16').place(x=115,y=353)
    elif iv2.get()==1:
        bdoo=Label(root,text='Please select the Pizza name and size',font='Arial 16').place(x=115,y=353)


    

btn=Button(root,text='Total',font='Arial 18',command=abc).place(x=195,y=313)


root.title('Pizza Billing System')
root.geometry('500x500')
root.mainloop()