
from tkinter import*
from tkinter import ttk

class Resistor:

    def __init__(self, root):
        self.root = root
        self.root.title("โปรแกรมคำนวนแถบสีความต้านทาน")
        self.root.geometry("1352x640+0+0")
        self.root.configure(background="floral white")

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=StringVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()
        var9=IntVar()

        var1.set("")
        var2.set("")
        var3.set("")
        var4.set("")
        var5.set("")
        var6.set("")
        var7.set("")
        var8.set("")
        var9.set("")
        

        def Band1_Black():
            var1.set(0)
        def Band1_Brown():
            var1.set(1)
        def Band1_Red():
            var1.set(2)
        def Band1_Orange():
            var1.set(3)
        def Band1_Yellow():
            var1.set(4)
        def Band1_Green():
            var1.set(5)
        def Band1_Blue():
            var1.set(6)
        def Band1_Violet():
            var1.set(7)
        def Band1_Gray():
            var1.set(8)
        def Band1_White():
            var1.set(9)
        #===================================================================.
        

        def Band2_Black():
            var2.set(0)
        def Band2_Brown():
            var2.set(1)
        def Band2_Red():
            var2.set(2)
        def Band2_Orange():
            var2.set(3)
        def Band2_Yellow():
            var2.set(4)
        def Band2_Green():
            var2.set(5)
        def Band2_Blue():
            var2.set(6)
        def Band2_Violet():
            var2.set(7)
        def Band2_Gray():
            var2.set(8)
        def Band2_White():
            var2.set(9)
        #====================================================================

        def Multiplier_Black():
            var3.set(1)
        def Multiplier_Brown():
            var3.set(10)
        def Multiplier_Red():
            var3.set(100)
        def Multiplier_Orange():
            var3.set(1000)
        def Multiplier_Yellow():
            var3.set(10000)
        def Multiplier_Green():
            var3.set(100000)
        def Multiplier_Blue():
            var3.set(1000000)
        def Multiplier_Violet():
            var3.set(10000000)
        def Multiplier_Gray():
            var3.set(100000000)
        def Multiplier_White():
            var3.set(1000000000)

        def sized():
            self.root.geometry("952x640+0+0")
        #====================================================================

        def Tolerance_Gold():
            var4.set(0.05)
        def Tolerance_Silver():
            var4.set(0.1)
        def Tolerance_None():
            var4.set(0.2)

        def iExit():
            iExit= tkinter.messagebox.askyesno("Resistor Colour Code Calculator","Confirm if you want to exit?")
            if iExit > 0:
                root.destroy()
                return

        

        def CalculateResistor():
            var9 =  "%d%d" %((var1.get(),var2.get()))
            t = float(var9)
            m = float(var3.get())
            s = float(var4.get())
            if (s == 0.05):                        
                q = ((t * m) /1000)*0.05
                a = (q)
                var5.set(str('%.1f'%(a)))
                var6.set(str('%.1f'%(t) + 'k ohm'))
                var7.set(str('%.1f'%(t - q) + 'k ohm'))
                var8.set(str('%.1f'%(t + q) + 'k ohm'))

            elif (s == 0.1):                        
                q = ((t * m) /1000)*0.1
                a = (q)
                var5.set(str('%.1f'%(a)))
                var6.set(str('%.1f'%(t) + 'k ohm'))
                var7.set(str('%.1f'%(t - q) + 'k ohm'))
                var8.set(str('%.1f'%(t + q) + 'k ohm'))

            elif (s == 0.2):                     
                q = ((t * m) /1000)*0.2
                a = (q)
                var5.set(str('%.1f'%(a)))
                var6.set(str('%.1f'%(t) + 'k ohm'))
                var7.set(str('%.1f'%(t - q) + 'k ohm'))
                var8.set(str('%.1f'%(t + q) + 'k ohm'))
            
            
            

        mainFrame=Frame(self.root, bg='floral white')
        mainFrame.grid()

        TitleFrame = Frame(mainFrame, bd=10, width = 1650, padx=10, bg='PaleTurquoise3', relief = RIDGE)
        TitleFrame.grid(row=0,column=0, columnspan=2)
        self.lblTitle = Label(TitleFrame, font=('arial' ,40, 'bold'),text="โปรแกรมคำนวนค่าความต้านทานจากแถบสี",
                              bg='floral white',padx=200)
        self.lblTitle.grid(row=0,column=0)

        ResistorFrame = Frame(mainFrame, bd=10, width = 1650, padx=20, bg='floral white', relief = RIDGE)
        ResistorFrame.grid(row=1,column=0,sticky=W)

        IndicatorFrame = Frame(mainFrame, bd=10, width = 1650, bg='floral white',  relief = RIDGE)
        IndicatorFrame.grid(row=1,column=1,sticky=W)


        self.lblTitle = Label(ResistorFrame, font=('arial' ,13, 'bold'),bg='plum2',text="แถบสีที่ 1")
        self.lblTitle.grid(row=0,column=0)
        self.lblTitle = Label(ResistorFrame, font=('arial' ,13, 'bold'),bg='plum2',text="แถบสีที่ 2")
        self.lblTitle.grid(row=0,column=1)
        self.lblTitle = Label(ResistorFrame, font=('arial' ,13, 'bold'),bg='plum2',text="ตัวคูณ")
        self.lblTitle.grid(row=0,column=2)
        self.lblTitle = Label(ResistorFrame, font=('arial' ,13, 'bold'),bg='plum2',text="ค่าความคลาดเคลื่อน")
        self.lblTitle.grid(row=0,column=3)

        self.black1=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='black',fg='white',
                           command=Band1_Black, bg='black')
        self.black1.grid(row=1,column=0)
        self.black2=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='0', fg='white',
                           command=Band2_Black,bg='black')
        self.black2.grid(row=1,column=1)
        self.black3=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='1', fg='white',
                           command=Multiplier_Black, bg='black')
        self.black3.grid(row=1,column=2)
        self.black4=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'),  fg='white', bg='black')
        self.black4.grid(row=1,column=3)
        #===================================================================================================================
        
        self.brown1=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='Brown', fg='black',
                           command=Band1_Brown,bg='brown')
        self.brown1.grid(row=2,column=0)
        self.brown2=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='1', fg='white',
                           command=Band2_Brown,bg='brown')
        self.brown2.grid(row=2,column=1)
        self.brown3=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='10', fg='white',
                           command=Multiplier_Brown,bg='brown')
        self.brown3.grid(row=2,column=2)
        self.brown4=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'),  fg='white', bg='brown')
        self.brown4.grid(row=2,column=3)
        #===================================================================================================================
        self.red1=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='Red', fg='black',
                         command=Band1_Red,bg='red')
        self.red1.grid(row=3,column=0)
        self.red2=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='2', fg='white',
                         command=Band2_Red,bg='red')
        self.red2.grid(row=3,column=1)
        self.red3=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='100', fg='white',
                         command=Multiplier_Red,bg='red')
        self.red3.grid(row=3,column=2)
        self.red4=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'),  fg='white', bg='red')
        self.red4.grid(row=3,column=3)
        #===================================================================================================================
     
        self.orange1=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='Orange', fg='black',
                            command=Band1_Orange,bg='orange')
        self.orange1.grid(row=4,column=0)
        self.orange2=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='3', fg='white',
                            command=Band2_Orange,bg='orange')
        self.orange2.grid(row=4,column=1)
        self.orange3=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='1000', fg='white',
                            command=Multiplier_Orange,bg='orange')
        self.orange3.grid(row=4,column=2)
        self.orange4=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'),  fg='white', bg='orange')
        self.orange4.grid(row=4,column=3)
        #==================================================================================================================
        self.Yellow1=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='Yellow', fg='black',
                            command=Band1_Yellow,bg='Yellow')
        self.Yellow1.grid(row=5,column=0)
        self.Yellow2=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='4', fg='black',
                            command=Band2_Yellow,bg='Yellow')
        self.Yellow2.grid(row=5,column=1)
        self.Yellow3=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='10000', fg='black',
                            command=Multiplier_Yellow,bg='Yellow')
        self.Yellow3.grid(row=5,column=2)
        self.Yellow4=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'),  fg='white', bg='Yellow')
        self.Yellow4.grid(row=5,column=3)
        #==================================================================================================================          
        self.Green1=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='Green', fg='black',
                           command=Band1_Green,bg='Green')
        self.Green1.grid(row=6,column=0)
        self.Green2=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='5', fg='white',
                           command=Band2_Green,bg='Green')
        self.Green2.grid(row=6,column=1)
        self.Green3=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='100000', fg='white',
                           command=Multiplier_Green,bg='Green')
        self.Green3.grid(row=6,column=2)
        self.Green4=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'),  fg='white', bg='Green')
        self.Green4.grid(row=6,column=3)
        #==================================================================================================================
          
        self.Blue1=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='Blue', fg='black',
                          command=Band1_Blue,bg='Blue')
        self.Blue1.grid(row=7,column=0)
        self.Blue2=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='6', fg='white',
                          command=Band2_Blue,bg='Blue')
        self.Blue2.grid(row=7,column=1)
        self.Blue3=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='1000000', fg='white',
                          command=Multiplier_Blue,bg='Blue')
        self.Blue3.grid(row=7,column=2)
        self.Blue4=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'),  fg='white', bg='Blue')
        self.Blue4.grid(row=7,column=3)
        #==================================================================================================================
          
        self.Violet1=Button(ResistorFrame,width = 16, font=('arial' ,14, 'bold'), text='Violet', fg='black',
                            command=Band1_Violet,bg='Violet')
        self.Violet1.grid(row=8,column=0)
        self.Violet2=Button(ResistorFrame,width = 16, font=('arial' ,14, 'bold'), text='7', fg='white',
                            command=Band2_Violet,bg='Violet')
        self.Violet2.grid(row=8,column=1)
        self.Violet3=Button(ResistorFrame,width = 16,font=('arial' ,14, 'bold'), text='10000000', fg='white',
                            command=Multiplier_Violet,bg='Violet')
        self.Violet3.grid(row=8,column=2)
        self.Violet4=Button(ResistorFrame,width = 16, font=('arial' ,14, 'bold'),  fg='white', bg='Violet')
        self.Violet4.grid(row=8,column=3)
        #===================================================================================================================
          
        self.Gray1=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='Gray', fg='black',
                          command=Band1_Gray,bg='Gray')
        self.Gray1.grid(row=9,column=0)
        self.Gray2=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='8', fg='white',
                          command=Band2_Gray,bg='Gray')
        self.Gray2.grid(row=9,column=1)
        self.Gray3=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='100000000', fg='white',
                          command=Multiplier_Gray,bg='Gray')
        self.Gray3.grid(row=9,column=2)
        self.Gray4=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'),  fg='white', bg='Gray')
        self.Gray4.grid(row=9,column=3)
        #===================================================================================================================
          
        self.White1=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='White', fg='black',
                           command=Band1_White,bg='White')
        self.White1.grid(row=10,column=0)
        self.White2=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='9', fg='black',
                           command=Band2_White,bg='White')
        self.White2.grid(row=10,column=1)
        self.White3=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='1000000000', fg='black',
                           command=Multiplier_White,bg='White')
        self.White3.grid(row=10,column=2)
        self.White4=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'),  fg='black', bg='White')
        self.White4.grid(row=10,column=3)
        #===================================================================================================================
          
        self.Gold1=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='Gold', fg='black',
                          command=Tolerance_Gold,bg='Gold')
        self.Gold1.grid(row=11,column=0)
        self.Gold2=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='', fg='black', bg='Gold')
        self.Gold2.grid(row=11,column=1)
        self.Gold3=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='0.1', fg='black', bg='Gold')
        self.Gold3.grid(row=11,column=2)
        self.Gold4=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'),  text='5%',fg='black',
                          command=Tolerance_Gold, bg='Gold')
        self.Gold4.grid(row=11,column=3)
        #==================================================================================================================
          
        self.Silver1=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='Silver', fg='black',
                            command=Tolerance_Silver,bg='Silver')
        self.Silver1.grid(row=12,column=0)
        self.Silver2=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='', fg='black', bg='Silver')
        self.Silver2.grid(row=12,column=1)
        self.Silver3=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'),  fg='black', bg='Silver')
        self.Silver3.grid(row=12,column=2)
        self.Silver4=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='10%', fg='black',
                            command=Tolerance_Silver,bg='Silver')
        self.Silver4.grid(row=12,column=3)
        #==================================================================================================================
              
        self.None1=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='None',fg='black',
                          command=Tolerance_None,bg='white')
        self.None1.grid(row=13,column=0)
        self.None2=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='', fg='black', bg='white')
        self.None2.grid(row=13,column=1)
        self.None3=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'),  fg='black', bg='white')
        self.None3.grid(row=13,column=2)
        self.None4=Button(ResistorFrame, width = 16, font=('arial' ,14, 'bold'), text='20%', fg='black',
                          command=Tolerance_None,bg='white')
        self.None4.grid(row=13,column=3)
        #====================================================IndicatorFrame===================================

        self.lblFirst = Label(IndicatorFrame, font=('arial' ,16, 'bold'),bg='plum2',text="แถบที่1")
        self.lblFirst.grid(row=0,column=0,sticky=W, pady=10)
        self.txtFirst = Entry(IndicatorFrame, font=('arial' ,16, 'bold'), width = 24, textvariable=var1)
        self.txtFirst.grid(row=0,column=1, pady=10, padx=4 ,columnspan=3)
        self.lblSecond = Label(IndicatorFrame, font=('arial' ,16, 'bold'),bg='plum2',text="แถบที่2")
        self.lblSecond.grid(row=1,column=0,sticky=W, pady=10)
        self.txtSecond = Entry(IndicatorFrame, font=('arial' ,16, 'bold'),width = 24, textvariable=var2)
        self.txtSecond.grid(row=1,column=1, pady=10, padx=4 ,columnspan=3)

        self.lblMultiplier = Label(IndicatorFrame, font=('arial' ,16, 'bold'),bg='plum2',text="ตัวคูณ")
        self.lblMultiplier.grid(row=2,column=0,sticky=W, pady=10)
        self.txtMultiplier = Entry(IndicatorFrame, font=('arial' ,16, 'bold'),width = 24, textvariable=var3)
        self.txtMultiplier.grid(row=2,column=1, pady=10,padx=4 , columnspan=3)
        self.lblTolerance = Label(IndicatorFrame, font=('arial' ,16, 'bold'),bg='plum2',text="ค่าความคลาดเคลื่อน")
        self.lblTolerance.grid(row=3,column=0,sticky=W, pady=10)
        self.txtTolerance = Entry(IndicatorFrame, font=('arial' ,16, 'bold'),width = 24, textvariable=var4)
        self.txtTolerance.grid(row=3,column=1, pady=10, padx=4 ,columnspan=3)

        self.lblResistorValue = Label(IndicatorFrame, font=('arial' ,16, 'bold'),bg='plum2',text="Resistor Value ")
        self.lblResistorValue.grid(row=5,column=0,sticky=W, pady=10)
        self.txtResistorValue  = Entry(IndicatorFrame, font=('arial' ,16, 'bold'),width = 24, textvariable=var6)
        self.txtResistorValue.grid(row=5,column=1, pady=10,padx=4 , columnspan=3)

        self.lblMinRange = Label(IndicatorFrame, font=('arial' ,16, 'bold'),bg='plum2',text="Min Range")
        self.lblMinRange.grid(row=6,column=0,sticky=W)
        self.txtMinRange = Entry(IndicatorFrame, font=('arial' ,16, 'bold'),width = 24, textvariable=var7)
        self.txtMinRange.grid(row=6,column=1, pady=10,padx=4 , columnspan=3)
        self.lblMaxRange = Label(IndicatorFrame, font=('arial' ,16, 'bold'),bg='plum2',text="Max Range")
        self.lblMaxRange.grid(row=7,column=0,sticky=W, pady=10)
        self.txtMaxRange  = Entry(IndicatorFrame, font=('arial' ,16, 'bold'),width = 24, textvariable=var8)
        self.txtMaxRange.grid(row=7,column=1, pady=10,padx=4 ,columnspan=3)

        btnCalculate=Button(IndicatorFrame, font=('arial' ,20, 'bold'),text="Calculate",width = 8,
                            command = CalculateResistor, height=4)
        btnCalculate.grid(row=8,column=1, pady=10)
        
 
      


if __name__=='__main__':
    root = Tk()
    application = Resistor(root)
    root.mainloop()
