from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from tkinter import messagebox
import datetime

class Stock_Management_Systems:

    def __init__(self,root):
        self.root = root
        self.root.title("Xavier MN Stock Management Systems")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background='gainsboro')
        #=================================================Frame===========================================
        MainFrame = Frame(self.root, bd =20, width =1350, height =700, bg="black",padx=200,relief=RIDGE)
        MainFrame.grid()

        WidgetFrame= Frame(MainFrame ,bd=10, width =750, height=600,pady= 2,padx=10,bg="gainsboro" ,relief=RIDGE)
        WidgetFrame.pack(side=LEFT)
        #===============================================Sub Frame==============================================
        WidgetFrame0= Frame(WidgetFrame ,bd=5, width =712, height=143,padx=5,bg="gainsboro" ,relief=RIDGE)
        WidgetFrame0.grid(row=0, column=0)

        WidgetFrame1= Frame(WidgetFrame ,bd=5, width =712, height=170,padx=5,bg="gainsboro" ,relief=RIDGE)
        WidgetFrame1.grid(row=1, column=0)

        WidgetFrame2= Frame(WidgetFrame ,bd=5, width =712, height=168,padx=5,bg="gainsboro" ,relief=RIDGE)
        WidgetFrame2.grid(row=2, column=0)

        WidgetFrame3= Frame(WidgetFrame ,bd=5, width =712, height=95,padx=5,bg="gainsboro" ,relief=RIDGE)
        WidgetFrame3.grid(row=3, column=0)
        #===============================================Variables===========================================
        ProdCode = StringVar()
        ProdType = StringVar()
        NoDays = StringVar()
        CostPDay = StringVar()
        CreLimit = StringVar()
        CreCheck = StringVar()
        SettDueDay = StringVar()
        PaymentD = StringVar()
        Discount = StringVar()
        Deposit = StringVar()
        PayDayDue = StringVar()
        PaymentM = StringVar()

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        Tax = StringVar()
        SubTotal = StringVar()
        Total = StringVar()
        Receipt_Ref = StringVar()

        def iExit():
            iExit = tkinter.messagebox.askyesno("Stock Management System", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():

            ProdCode.set("")
            ProdType.set("")
            NoDays.set("")
            CostPDay.set("")
            CreLimit.set("")
            CreCheck.set("")
            SettDueDay.set("")
            PaymentD.set("")
            Discount.set("")
            Deposit.set("")
            PayDayDue.set("")
            PaymentM.set("")
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            Tax.set("")
            SubTotal.set("")
            Total.set("")

            self.txtInfo0.delete("1.0", END)
            self.txtInfo1.delete("1.0", END)
            self.txtInfo2.delete("1.0", END)
            self.txtInfo3.delete("1.0", END)
            return

        def checkCredit():
            if (var1.get() == 1):
                self.txtInfo0.insert(END,"Customer's Check Credit Approved")
            elif var1.get()== 0:
                self.txtInfo0.delete("1.0",END)

        def TermAgreed():
            if (var2.get() == 1):
                self.txtInfo1.insert(END,"Terms Agreed")
            elif var2.get()== 0:
                self.txtInfo1.delete("1.0",END)

        def AcctOnHold():
            if (var3.get() == 1):
                self.txtInfo2.insert(END,"Customer's Account On Hold")
            elif var3.get() == 0:
                self.txtInfo2.delete("1.0",END)

        def RestrictedMails():
            if (var4.get() == 1):
                self.txtInfo3.insert(END,"Restricted Mail for Customer")
            elif var4.get() == 0:
                self.txtInfo3.delete("1.0",END)

        def Product(evt):
            values =str(self.cboProdType.get())
            pType = values
            if pType == "2019 Car":
                ProdCode.set("CAR9735")
                CostPDay.set("$65")
                CreCheck.set("No")
                SettDueDay.set("65")
                PaymentD.set("No")
                Deposit.set("No")
                PaymentM.set("Visa")

            elif pType == "2019 SUV":
                ProdCode.set("SUV0678")
                CostPDay.set("$90")
                CreCheck.set("No")
                SettDueDay.set("90")
                PaymentD.set("No")
                Deposit.set("No")
                PaymentM.set("Cash")

            elif pType == "2019 Van":
                ProdCode.set("Van1345")
                CostPDay.set("$80")
                CreCheck.set("No")
                SettDueDay.set("80")
                PaymentD.set("No")
                Deposit.set("No")
                PaymentM.set("Cash")

            elif pType == "2019 Truck":
                ProdCode.set("Truck3984")
                CostPDay.set("$105")
                CreCheck.set("No")
                SettDueDay.set("105")
                PaymentD.set("No")
                Deposit.set("No")
                PaymentM.set("Cash")

        def NoofDays(evt):
            values =str(self.cboNoDays.get())
            NDays = values
            if NDays == "1-30":
                PayDayDue.set(30)
                CreLimit.set("$100")
                Discount.set("7%")

            elif (NDays == "31-90"):
                PayDayDue.set(90)
                CreLimit.set("$175")
                Discount.set("14%")

            elif (NDays == "91-270"):
                PayDayDue.set(270)
                CreLimit.set("$225")
                Discount.set("21%")

            elif (NDays == "271-365"):
                PayDayDue.set(365)
                CreLimit.set("$275")
                Discount.set("28%")

            elif (NDays == "0" or NDays ==""):
                messagebox.showinfo("Zero selected", "You choose zero?")
                Reset()

        def TotalCost():
            n = float(PayDayDue.get())
            s = float(SettDueDay.get())
            price = (n * s)
            ST ="$",str('%.2f'%(price))
            iTax ="$", str('%.2f'%((price)*0.15))
            Tax.set(iTax)
            SubTotal.set(ST)
            TC = "$",str('%.2f'%(((price)*0.15)+ price))
            Total.set(TC)
            

        

#================================================Widget Frame0==========================================

        self.Ib1ProdType =Label(WidgetFrame0, font=('arial', 18,'bold'), text="Product Type:",padx=2,pady=16, bg="gainsboro")
        self.Ib1ProdType.grid(row=0, column=0,sticky=W)

        self.cboProdType=ttk.Combobox(WidgetFrame0,textvariable=ProdType, state='readonly',
                                        font=('arial', 18,'bold'), width=19)
        self.cboProdType.bind("<<ComboboxSelected>>",Product)
        self.cboProdType['value']=('','2019 Car','2019 SUV','2019 Van','2019 Truck')
        self.cboProdType.current(0)
        self.cboProdType.grid(row=0, column=1)

        self.Ib1NoDays =Label(WidgetFrame0, font=('arial', 18,'bold'), text="No of Days:",padx=2,pady=2,bg="gainsboro")
        self.Ib1NoDays.grid(row=0, column=2,sticky=W)

        self.cboNoDays=ttk.Combobox(WidgetFrame0,textvariable=NoDays, state='readonly',
                                        font=('arial', 18,'bold'), width=19)
        self.cboNoDays.bind("<<ComboboxSelected>>", NoofDays)
        self.cboNoDays['value']=('0','1-30','31-90','91-270','271-365')
        self.cboNoDays.current(0)
        self.cboNoDays.grid(row=0, column=3)

        self.Ib1ProdCode =Label(WidgetFrame0, font=('arial', 16,'bold'), text="Product Code:",padx=1,pady=16, bg="gainsboro")
        self.Ib1ProdCode.grid(row=1, column=0,sticky=W)

        self.txtProdCode=Entry(WidgetFrame0, textvariable=ProdCode, font=('arial',16,'bold'), bd=8,
        fg="black", width=22, justify=LEFT).grid(row=1,column=1)

        self.Ib1ProdCode =Label(WidgetFrame0, font=('arial', 16,'bold'), text="Product Code:",padx=1,pady=2, bg="gainsboro")
        self.Ib1ProdCode.grid(row=1, column=2,sticky=W)

        self.txtCostPDay=Entry(WidgetFrame0, textvariable=CostPDay, font=('arial',16,'bold'), bd=8,
        fg="black", width=21, justify=LEFT).grid(row=1,column=3)

        #===========================================Widget Frame1===============================================================
        self.Ib1CreLimit =Label(WidgetFrame1, font=('arial', 18,'bold'), text="Credit Limit:",padx=2,pady=2, bg="gainsboro")
        self.Ib1CreLimit.grid(row=0, column=0,sticky=W)

        self.cboCreLimit=ttk.Combobox(WidgetFrame1,textvariable=CreLimit, state='readonly',
                                        font=('arial', 18,'bold'), width=18)
        self.cboCreLimit['value']=('','Select a option','$150','$200','$250','$300')
        self.cboCreLimit.current(0)
        self.cboCreLimit.grid(row=0, column=1,pady=2)

        self.Ib1CreCheck =Label(WidgetFrame1, font=('arial', 18,'bold'), text="Credit Check:",padx=2,pady=2, bg="gainsboro")
        self.Ib1CreCheck.grid(row=0, column=2,sticky=W)

        self.cboCreCheck=ttk.Combobox(WidgetFrame1,textvariable=CreCheck, state='readonly',
                                        font=('arial', 18,'bold'), width=18)
        self.cboCreCheck['value']=('','Select a option','Yes','No')
        self.cboCreCheck.current(0)
        self.cboCreCheck.grid(row=0, column=3, pady=2)

        
        self.Ib1SettDueDay =Label(WidgetFrame1, font=('arial', 18,'bold'), text="Sett.Due.Day:",padx=2,pady=2, bg="gainsboro")
        self.Ib1SettDueDay.grid(row=1, column=0,sticky=W)

        self.txtSettDueDay=Entry(WidgetFrame1, textvariable=SettDueDay, font=('arial',16,'bold'), bd=2,
        fg="black", width=20, justify=LEFT).grid(row=1,column=1)

        self.Ib1PaymentD =Label(WidgetFrame1, font=('arial', 18,'bold'), text="Payment Due:",padx=1,pady=2, bg="gainsboro")
        self.Ib1PaymentD.grid(row=1, column=2,sticky=W)

        self.cboPaymentD=ttk.Combobox(WidgetFrame1,textvariable=PaymentD, state='readonly',
                                        font=('arial', 18,'bold'), width=18)
        self.cboPaymentD['value']=('','Select a option','Yes','No')
        self.cboPaymentD.current(0)
        self.cboPaymentD.grid(row=1, column=3, pady=2)

        self.Ib1Discount =Label(WidgetFrame1, font=('arial', 18,'bold'), text="Discount:",padx=1,pady=2, bg="gainsboro")
        self.Ib1Discount.grid(row=2, column=0,sticky=W)

        self.cboDiscount=ttk.Combobox(WidgetFrame1,textvariable=Discount, state='readonly',
                                        font=('arial', 18,'bold'), width=18)
        self.cboDiscount['value']=('0','5','10','15','20')
        self.cboDiscount.current(0)
        self.cboDiscount.grid(row=2, column=1,pady=2)

        self.Ib1Deposit =Label(WidgetFrame1, font=('arial', 18,'bold'), text="Deposit:",padx=1,pady=2, bg="gainsboro")
        self.Ib1Deposit.grid(row=2, column=2,sticky=W)

        self.cboDeposit=ttk.Combobox(WidgetFrame1,textvariable=Deposit, state='readonly',
                                       font=('arial', 18,'bold'), width=18)
        self.cboDeposit['value']=('','Select a option','Yes','No')
        self.cboDeposit.current(0)
        self.cboDeposit.grid(row=2, column=3,pady=2)

        self.Ib1PayDayDue =Label(WidgetFrame1, font=('arial', 18,'bold'), text="Pay Day Due:",padx=1,pady=2, bg="gainsboro")
        self.Ib1PayDayDue.grid(row=3, column=0,sticky=W)

        self.txtPayDayDue=Entry(WidgetFrame1, font=('arial',16,'bold'), bd=2,
        fg="black", width=20, justify=LEFT).grid(row=3,column=1)

        self.Ib1PaymentM =Label(WidgetFrame1, font=('arial', 18,'bold'), text="Payment Methond:",padx=0,pady=4, bg="gainsboro")
        self.Ib1PaymentM.grid(row=3, column=2,sticky=W)

        self.cboPaymentM=ttk.Combobox(WidgetFrame1,textvariable=PaymentM, state='readonly',
                                        font=('arial', 18,'bold'), width=18)
        self.cboPaymentM['value']=('','Select a option','Cash','Visa','Master Card','Bitcoin')
        self.cboPaymentM.current(0)
        self.cboPaymentM.grid(row=3, column=3,pady=2)

        #========================================Widget Frame2======================================================================

        WidgetFrame2L = Frame(WidgetFrame2 ,bd=5, width =300, height=160, padx=5,bg="gainsboro" ,relief=RIDGE)
        WidgetFrame2L.grid(row=0, column=0)
        WidgetFrame2R = Frame(WidgetFrame2 ,bd=5, width =300, height=160, padx=5,pady=10,bg="gainsboro" ,relief=RIDGE)
        WidgetFrame2R.grid(row=0, column=1)

        #===============================================================Widget Frame 2l=========================================================

        self.chkCheckCredit = Checkbutton(WidgetFrame2L, text="Check Credit", variable=var1, onvalue = 1, offvalue = 0,
                     font=('arial',16, 'bold'),bg="gainsboro", command=checkCredit).grid(row=0,column=0,sticky=W)

        self.chkTermAgreed = Checkbutton(WidgetFrame2L, text="Term Agreed", variable=var2, onvalue = 1, offvalue = 0,
                         font=('arial',16, 'bold'),bg="gainsboro", command=TermAgreed).grid(row=1,column=0, sticky=W)

        self.chkAccountOnHold = Checkbutton(WidgetFrame2L, text="Account On Hold", variable=var3, onvalue = 1, offvalue = 0,
                       font=('arial',16, 'bold'),bg="gainsboro", command=AcctOnHold).grid(row=2,column=0, sticky=W)

        self.chkRestrictMailing = Checkbutton(WidgetFrame2L, text="Restrict Mailing", variable=var4, onvalue = 1, offvalue = 0,
                         font=('arial',16, 'bold'),bg="gainsboro", command=RestrictedMails).grid(row=3,column=0, sticky=W)

        self.txtInfo0 = Text(WidgetFrame2L, height=2, width=26, font=('arial', 9, 'bold'))
        self.txtInfo0.grid(row=0, column=1,pady=2)

        self.txtInfo1 = Text(WidgetFrame2L, height=2, width=26, font=('arial', 9, 'bold'))
        self.txtInfo1.grid(row=1, column=1,pady=2)

        self.txtInfo2 = Text(WidgetFrame2L, height=2, width=26, font=('arial', 9, 'bold'))
        self.txtInfo2.grid(row=2, column=1,pady=2)

        self.txtInfo3 = Text(WidgetFrame2L, height=2, width=26, font=('arial', 9, 'bold'))
        self.txtInfo3.grid(row=3, column=1,pady=2)

        #======================Widget Frame2r======================================================================================================

        self.Ib1Tax =Label(WidgetFrame2R, font=('arial', 18,'bold'), text="Tax",padx=4,pady=1, fg="black", bg="gainsboro")
        self.Ib1Tax.grid(row=0, column=0,sticky=W)
        self.txtTax=Entry(WidgetFrame2R, textvariable=Tax, font=('arial',16,'bold'), bd=8,
        fg="black", width=24, justify=LEFT).grid(row=0,column=1,pady=1,padx=4)

        self.Ib1SubTotal =Label(WidgetFrame2R, font=('arial', 18,'bold'), text="Sub Total",padx=4,pady=1,fg="black", bg="gainsboro")
        self.Ib1SubTotal.grid(row=1, column=0,sticky=W)
        self.txtSubTotal=Entry(WidgetFrame2R, textvariable=SubTotal, font=('arial',16,'bold'), bd=8,
        fg="black", width=24, justify=LEFT).grid(row=1,column=1,pady=1,padx=4)

        self.Ib1Total =Label(WidgetFrame2R, font=('arial', 18,'bold'), text="Total",padx=4,pady=1,fg="black", bg="gainsboro")
        self.Ib1Total.grid(row=2, column=0,sticky=W)
        self.txtSubTotal=Entry(WidgetFrame2R, textvariable=Total, font=('arial',16,'bold'), bd=8,
        fg="black", width=24, justify=LEFT).grid(row=2,column=1,pady=1,padx=4)

        #===============================================Widget Frame3 Buttons=================================================================================

        self.btnTotal = Button(WidgetFrame3, padx=36, pady=2, bd=4, fg="black",font=('arial',20,'bold'), width=12,height=2,
                          bg="gainsboro",text="Total", command = TotalCost).grid(row=0,column=0)

        self.btnReset = Button(WidgetFrame3, padx=33, pady=2, bd=4, fg="black",font=('arial',20,'bold'), width=13,height=2,
                          bg="gainsboro",text="Reset", command = Reset).grid(row=0,column=1)

        self.btnExit = Button(WidgetFrame3, padx=36, pady=2, bd=4, fg="black",font=('arial',20,'bold'), width=12, height=2,
                         bg="gainsboro",text="Exit", command = iExit).grid(row=0,column=2)

        #===============================================End of Buttons=====================================================================

        

        
        
                           
                                    
        
                                 
        


                                    



if __name__=='__main__':
    root = Tk()
    application = Stock_Management_Systems(root)
    root.mainloop()
