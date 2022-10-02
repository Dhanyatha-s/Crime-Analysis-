
from tkinter import *
from PIL import ImageTk,Image
from fileinput import close
from subprocess import call
from tkinter import messagebox
from wsgiref import validate
import mysql.connector

from cProfile import label
from decimal import Rounded
from tkinter import *
from turtle import bgcolor
from PIL import ImageTk,Image
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
####login-----------------------------------------------------------------------------------------------
root=Tk()
root.geometry('1100x700')
#root.resizable(False,False)
root.title("login page")
#root.config(bg="green")
root.state('zoomed')

def login():
    if username.get()== ""or password.get()=="":
        messagebox.showerror("Error","Enter Username and Password",parent=root)
    else:
        try:
            con=mysql.connector.connect(host="localhost",user="root",password="",database="crime-analysis")
            cur=con.cursor()
            cur.execute("select * from login_to_crime where username=%s and password=%s",(username.get(),password.get()))
            row=cur.fetchone()
            if row is None:
                messagebox.showerror("Error","Invalid User name and Password",parent=root)
            else:
                messagebox.showinfo("success","Successfully Login",parent=root)
                close()
                #passMain()
            con.close()
        except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=root)

def clear():
    u_ent.delete(0,END)
    p_ent.delete(0,END)

#def close():
    #root.destroy()




#--------------------------------------------------login tkinter----------------------------------------------------------------------
#bgImage=ImageTk.PhotoImage(file="logo8.jpg")
#bgLabel=Label(root,image=bgImage)
#bgLabel.grid()
#root.config(bg="#4C0033")
label0=Label(root,text='CRIME ANALYSIS AND PRIDICTION',font=('Malgun Gothic Bold',30,'italic'),bg="black",fg="red").place(x=350,y=10)
label=Label(root,text='LOGIN',font=('Malgun Gothic Bold',23,'italic'),bg="black",fg="firebrick1").place(x=610,y=100)

username=StringVar()
password=StringVar()

user_name=Label(root,text="Username",font=('Malgun Gothic Bold',10,'bold'),bg="black",fg="white").place(x=530,y=300)
u_ent=Entry(root,bd=0,fg='black',textvariable=username).place(x=650,y=300)
#u_ent.focus()
passwd=Label(root,text="Password",font=('Malgun Gothic Bold',10,'bold'),bg="black",fg="white").place(x=530,y=370)
p_ent=Entry(root,bd=0,fg='black',show="*",textvariable=password).place(x=650,y=370)


Log_butt=Button(root,text="Login",font=('Malgun Gothic Bold',15,'italic'),bg="yellow",fg="black",command=login).place(x=570,y=550)
Clear_butt1=Button(root,text='Clear',font=('Malgun Gothic Bold',15,'italic'),bg="yellow",fg="black",command=clear).place(x=670,y=550)
#butt2=Button(root,text='back',font=('Malgun Gothic Bold',15,'italic'),bg="#046582",fg="white").place(x=1200,y=600)


####-----------------------------graph-------------------------------------------------------------------------

def crimepg():
    crimepg=Toplevel(root)
    root.destroy()
    
    def graph():
        crimes1=pd.read_csv("42_District_wise_crimes_committed_against_women_2001_2012.csv")
        crimes2=pd.read_csv("42_District_wise_crimes_committed_against_women_2013.csv")


        crimes = pd.concat([crimes1,crimes2],  ignore_index=False, axis=0)
        # rename the STATE/UT column to STATE
        crimes.rename(columns={'STATE/UT':'STATE'}, inplace=True)

        del crimes1
        del crimes2
        print('Dataset is ready....')
        # know the shape of dataset
        crimes.shape
        states = crimes.STATE.unique()
        #print(states)


            


        crimes_total = crimes[crimes['DISTRICT'] == 'TOTAL']

        # drop DISTRCT Column as we do not intend to use at this point
        crimes_total.drop('DISTRICT', axis=1, inplace=True)
        # filter out the Total crimes for each State & UT for the year 2001
        crimes_total_2001 = crimes_total[crimes_total['Year'] == 2001]
        crimes_total_2001.drop('Year', axis=1, inplace=True)

        x = crimes_total_2001['STATE'].values
        y = crimes_total_2001['Rape'].values

        # plot the bar graph
        fig, ax = plt.subplots()
        crime_rape = crimes_total_2001['STATE'].values
        y_pos = np.arange(len(crime_rape))
        performance = crimes_total_2001['Rape'].values
        ax.barh(y_pos, performance, align='center',color='green', ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(crime_rape)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Rapes')
        ax.set_title('RAPE VS STATE')
        fig.set_size_inches(20, 18, forward=True)
        plt.show()

        # Any results you write to the current directory are saved as output.
        # creating a new data set

        crimes_total_women1 = pd.read_csv('42_District_wise_crimes_committed_against_women_2001_2012.csv')
        crimes_total_women2 = pd.read_csv('42_District_wise_crimes_committed_against_women_2013.csv')

        crimes_total_women = pd.concat([crimes_total_women1,crimes_total_women2],  ignore_index=False, axis=0)
        crimes_total_women.rename(columns={'STATE/UT':'STATE'}, inplace=True)

        del crimes_total_women1
        del crimes_total_women2

        # calculating total crimes of all kinds in each state from 2001 to 2013
        crimes_total_women = crimes_total_women[crimes_total_women['DISTRICT'] == 'TOTAL']
        crimes_total_women.drop('DISTRICT', axis=1, inplace=True)

        crimes_total_women['Total Crimes']= crimes_total_women.iloc[:, -9:-1].sum(axis=1)

        crimes_total_women = crimes_total_women.groupby(['STATE'])['Total Crimes'].sum()

        # plot graph of crimes committed on women since 2001-2013 in each state/ UT
        fig1, ax1 = plt.subplots()
        states = crimes_total_women.index.tolist()
        y_pos = np.arange(len(states))
        performance = crimes_total_women.tolist()
        ax1.barh(y_pos, performance, align='center',color='green', ecolor='black')
        ax1.set_yticks(y_pos)
        ax1.set_yticklabels(states)
        ax1.invert_yaxis()  # labels read top-to-bottom
        ax1.set_xlabel('All Crimes Aganist Women')
        ax1.set_title('Crime VS STATE')
        fig1.set_size_inches(20, 18, forward=True)
        plt.show()
    
    crimepage=Tk()
    crimepage.title("CRIME INFORMATION")
    crimepage.geometry('1200x600')
    crimepage.resizable(False,False)
    bgImg=ImageTk.PhotoImage(file="crimepage1.png")
    lab=Label(crimepage,image=bgImg).grid()


    #Adding transparent background property
    #crimepage.wm_attributes('-transparentcolor', 'red')

    #Create a Label
    Label(crimepage, text= "-----CRIME INFO-----", font=('Helvetica 40'),bg="gray").place(x=370,y=10)
    Label(crimepage,text="Let the crime be know before it happen",font=('Algerian 10'),bg="violet").place(x=490,y=70)

    #Set the Menu initially
    menu= StringVar()
    menu.set("Categories")

    menu1=StringVar()
    menu1.set("Crime Type")


    #Create a dropdown Menu
    drop= OptionMenu(crimepage,menu,"District level crime aganist women 2001 to 2012","District level crime aganist women 2013")
    drop.place(x=890,y=90)
    drop.config(bd=0,bg="cyan",width=40,height=3)

    #create a dropdown menu for crime type
    lab1=Label(crimepage,text="Crime Type",fg="black",bg="lightblue",width=20,height=2).place(x=100,y=170)
    drop1= OptionMenu(crimepage, menu1,"Rape","Kidnapping and Abduction","Assault on women-modesty","Insult to modesty of women","Cruelty by Husband of his Relatives","Importation of Girls")
    drop1.place(x=60,y=230)
    drop1.config(bd=0,bg="cyan",width=40,height=6)

    #create a dropdown menu for state
    menu2=StringVar()
    menu2.set("States")
    lab2=Label(crimepage,text="States",fg="black",bg="lightblue",width=20,height=2).place(x=440,y=170)
    drop2= OptionMenu(crimepage, menu2,'ANDHRA PRADESH' ,'ARUNACHAL PRADESH' ,'ASSAM' ,'BIHAR' ,'CHHATTISGARH', 'GOA',
    'GUJARAT','HARYANA' ,'HIMACHAL PRADESH' ,'JAMMU & KASHMIR', 'JHARKHAND',
    'KARNATAKA', 'KERALA' ,'MADHYA PRADESH' ,'MAHARASHTRA' ,'MANIPUR', 'MEGHALAYA',
    'MIZORAM', 'NAGALAND', 'ODISHA' ,'PUNJAB' ,'RAJASTHAN' ,'SIKKIM' ,'TAMIL NADU',
    'TRIPURA', 'UTTAR PRADESH' ,'UTTARAKHAND' ,'WEST BENGAL', 'A & N ISLANDS',
    'CHANDIGARH', 'D & N HAVELI', 'DAMAN & DIU', 'DELHI' ,'LAKSHADWEEP',
    'PUDUCHERRY')
    drop2.place(x=380,y=230)
    drop2.config(bd=0,bg="cyan",width=30,height=6)

    #createing dropdown for year
    lab3=Label(crimepage,text="Year",width=19,height=2,fg="black",bg="lightblue").place(x=710,y=170)
    menu3=StringVar()
    menu3.set(" Select year from 2001 to 2013")
    drop3=OptionMenu(crimepage,menu3,"2001","2002","2003","2004","2005","2005","2006","2007","2008","2009","2010","2011","2012","2013")
    drop3.place(x=690,y=230)
    drop3.config(bd=0,bg="cyan",width=30,height=6)


    #label=Label(crimepage,text="")
    btn=Button(crimepage,text="submit",bg="yellow",fg="black",width=20,height=1,font=('italic',10,'bold'),command=graph).place(x=1000,y=500)
    #butt1=Button(crimepage,text='Signin',font=('italic',15,'bold'),bg="yellow",fg="black").place(x=300,y=220)





    crimepage.mainloop()

bgImage=ImageTk.PhotoImage(file="tttt.webp")
bgLabel=Label(root,image=bgImage)
bgLabel.grid()
label0=Label(root,text='CRIME ANALYSIS AND PRIDICTION',font=('Malgun Gothic Bold',30,'italic'),bg="black",fg="red").place(x=350,y=10)
label=Label(root,text='LOGIN',font=('Malgun Gothic Bold',23,'italic'),bg="black",fg="firebrick1").place(x=610,y=100)

username=StringVar()
password=StringVar()

user_name=Label(root,text="Username",font=('Malgun Gothic Bold',10,'bold'),bg="black",fg="white").place(x=530,y=300)
u_ent=Entry(root,bd=0,fg='black',textvariable=username).place(x=650,y=300)
#u_ent.focus()
passwd=Label(root,text="Password",font=('Malgun Gothic Bold',10,'bold'),bg="black",fg="white").place(x=530,y=370)
p_ent=Entry(root,bd=0,fg='black',show="*",textvariable=password).place(x=650,y=370)


Log_butt=Button(root,text="Login",font=('Malgun Gothic Bold',15,'italic'),bg="yellow",fg="black",command=login).place(x=570,y=550)
Clear_butt1=Button(root,text='Clear',font=('Malgun Gothic Bold',15,'italic'),bg="yellow",fg="black",command=clear).place(x=670,y=550)
butt2=Button(root,text='Next',font=('Malgun Gothic Bold',15,'italic'),bg="#046582",fg="white",command=crimepg).place(x=1200,y=600)

root.mainloop()
