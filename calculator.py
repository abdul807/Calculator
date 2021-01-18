'''
   This was created by Abdul Matin
''' 



from tkinter import *

class Application(Frame):
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.task=''
        self.userin = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.user_input=Entry(self,bg='blue',bd=20,insertwidth=4,
        width=24,font=('vernada',20,'bold'),textvariable=self.userin,
        justify=RIGHT)
        self.user_input.grid(columnspan=4)

        self.user_input.insert(0,'0')


        self.button1=Button(self,bg='blue',
        bd=7,text='7',padx=26,pady=33,font=('Helvetica',20,'bold'),
        command=lambda :self.buttonClick(7))
        self.button1.grid(row=2,column=0,sticky=W)

        self.button2=Button(self,bg='blue',
        bd=7,text='8',padx=26,pady=33,font=('Helvetica',20,'bold'),
        command=lambda :self.buttonClick(8))
        self.button2.grid(row=2,column=1,sticky=W)

        self.button3=Button(self,bg='blue',
        bd=7,text='9',padx=26,pady=33,font=('Helvetica',20,'bold'),
        command=lambda :self.buttonClick(9))
        self.button3.grid(row=2,column=2,sticky=W)

        self.button4=Button(self,bg='blue',
        bd=7,text='4',padx=26,pady=33,font=('Helvetica',20,'bold'),
        command=lambda :self.buttonClick(4))
        self.button4.grid(row=3,column=0,sticky=W)

        self.button5=Button(self,bg='blue',
        bd=12,text='5',padx=33,pady=25,font=('Helvetica',20,'bold'),
        command=lambda :self.buttonClick(5))
        self.button5.grid(row=3,column=1,sticky=W)

        self.button6=Button(self,bg='blue',
        bd=12,text='6',padx=33,pady=25,font=('Helvetica',20,'bold'),
        command=lambda :self.buttonClick(6))
        self.button6.grid(row=3,column=2,sticky=W)


        self.button7=Button(self,bg='blue',
        bd=7,text='1',padx=26,pady=33,font=('Helvetica',20,'bold'),
        command=lambda :self.buttonClick(1))
        self.button7.grid(row=4,column=0,sticky=W)

        self.button8=Button(self,bg='blue',
        bd=12,text='2',padx=33,pady=25,font=('Helvetica',20,'bold'),
        command=lambda :self.buttonClick(2))
        self.button8.grid(row=4,column=1,sticky=W)

        self.button9=Button(self,bg='blue',
        bd=12,text='3',padx=33,pady=25,font=('Helvetica',20,'bold'),
        command=lambda :self.buttonClick(3))
        self.button9.grid(row=4,column=2,sticky=W)


        self.button9=Button(self,bg='blue',
        bd=12,text='0',padx=33,pady=25,font=('Helvetica',20,'bold'),
        command=lambda :self.buttonClick(0))
        self.button9.grid(row=5,column=0,sticky=W)

        self.addbutton=Button(self,bg='blue',
        bd=12,text='+',padx=36,pady=25,font=('Helvetica',20,'bold'),
        command=lambda :self.buttonClick('+'))
        self.addbutton.grid(row=2,column=3,sticky=W)

        self.subbutton=Button(self,bg='blue',
        bd=12,text='-',padx=39,pady=25,font=('Helvetica',20,'bold'),
        command=lambda :self.buttonClick('-'))
        self.subbutton.grid(row=3,column=3,sticky=W)

        self.mulbutton=Button(self,bg='blue',
        bd=7,text='*',padx=38,pady=25,font=('Helvetica',20,'bold'),
        command=lambda :self.buttonClick('*'))
        self.mulbutton.grid(row=4,column=3,sticky=W)

        self.divbutton=Button(self,bg='blue',
        bd=7,text='/',padx=26,pady=33,font=('Helvetica',20,'bold'),
        command=lambda :self.buttonClick('/'))
        self.divbutton.grid(row=5,column=3,sticky=W)

        self.equalbutton=Button(self,bg='blue',
        bd=7,text='=',padx=100,pady=25,font=('Helvetica',20,'bold'),
        command=self.calculatetask)
        self.equalbutton.grid(row=5,column=1,sticky=W,columnspan=2)

        self.clearbutton=Button(self,bg='blue',
        bd=7,text='AC',padx=26,pady=33,font=('Helvetica',20,'bold'),
        )
        self.clearbutton.grid(row=1,columnspan=4)


    def calculatetask(self):
        self.data=self.user_input.get()
        try:
            self.answer=eval(self.data)
            self.displaytext(self.answer)
            self.task=self.answer
            
        except SyntaxError as e:
            self.displaytext('invalid synthax')
            self.task=''


    def displaytext(self,value):
        self.user_input.delete(0,END)
        self.user_input.insert(0,value)

    def cleardisplay(self):
        self.task=''
        self.user_input.delete(0,END)
        self.user_input.insert(0,'0')


    def buttonClick(self,number):
        self.task= str(self.task) + str(number)
        self.userin.set(self.task)




    










windows=Tk()
windows.title('calculator')
app = Application(windows)
#app.resizable(width=False,height=False)

app.mainloop()


        


