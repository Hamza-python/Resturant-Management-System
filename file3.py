import random
import datetime
import time
import tkinter.messagebox
from tkinter import *

root = Tk()
root.geometry("1350x750")
root.title("Restaurant Management System")
root.configure(background = 'SLate Gray4')

Tops = Frame(root, bg='black', bd=5, pady=5, relief=RIDGE)
Tops.pack(side=TOP)

lblTittle = Label(Tops, font=('arial' , 60 , 'bold'), text="Restaurant Management System", bd=21,
                  bg='ghost white', fg='Slate Gray4', justify=CENTER)
lblTittle.grid(row=0, column=0)



ReceiptCal_F = Frame(root, bg='Slate Gray4', bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F = Frame(ReceiptCal_F, bg='light grey', bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F = Frame(ReceiptCal_F, bg='light grey', bd=6,relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F = Frame(ReceiptCal_F, bg='light grey', bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root, bd=10, bg="light grey" , relief=RIDGE)
MenuFrame.pack(side=LEFT)

Cost_F = Frame(MenuFrame, bg='SlateGray4', bd=4)
Cost_F.pack(side=BOTTOM)

Drinks_F = Frame(MenuFrame, bg='light grey', bd=10)
Drinks_F.pack(side=TOP)

Drinks_F = Frame(MenuFrame, bg='light grey', bd=10,relief=RIDGE)
Drinks_F.pack(side=LEFT)

Cake_F = Frame(MenuFrame, bg='light grey', bd=10,relief=RIDGE)
Cake_F.pack(side=RIGHT)
# ---------------------------------varaibles------------------------------------------------------------------
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

dateoforder = StringVar()
Receipt_Ref = StringVar()
paidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofCakes = StringVar()
CostofDrinks = StringVar()
ServiceCharges = StringVar()

text_input = StringVar()
operator = ""

E_Coke = StringVar()
E_Pepsi = StringVar()
E_Sprite = StringVar()
E_Fanta = StringVar()
E_Marinda = StringVar()
E_Dew = StringVar()
E_Sting = StringVar()
E_LemonMalt = StringVar()

E_ChocolateCake = StringVar()
E_VanilaCake = StringVar()
E_StrawberryCake = StringVar()
E_MangoCake = StringVar()
E_IceCreamCake = StringVar()
E_MixFlavour = StringVar()
E_FruitCake = StringVar()
E_DryCake = StringVar()

E_Coke.set("0")
E_Pepsi.set("0")
E_Sprite.set("0")
E_Fanta.set("0")
E_Marinda.set("0")
E_Dew.set("0")
E_Sting.set("0")
E_LemonMalt.set("0")

E_ChocolateCake.set("0")
E_VanilaCake.set("0")
E_StrawberryCake.set("0")
E_MangoCake.set("0")
E_IceCreamCake.set("0")
E_MixFlavour.set("0")
E_FruitCake.set("0")
E_DryCake.set("0")

dateoforder.set(time.strftime("%d / %m / %y"))
# -----------------------------------------Function declared-------------------------------------------------==
def iExist():
    iExit = tkinter.messagebox.askyesno("Exit Restuarant System", "Confirm if you want to Exit")
    if iExit > 0:
        root.destroy()
        return

def reset():
    paidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofCakes.set("")
    CostofDrinks.set("")
    ServiceCharges.set("")
    txt_Receipt.delete("1.0", END)


    E_Coke.set("0")
    E_Pepsi.set("0")
    E_Sprite.set("0")
    E_Fanta.set("0")
    E_Marinda.set("0")
    E_Dew.set("0")
    E_Sting.set("0")
    E_LemonMalt.set("0")

    E_ChocolateCake.set("0")
    E_VanilaCake.set("0")
    E_StrawberryCake.set("0")
    E_MangoCake.set("0")
    E_IceCreamCake.set("0")
    E_MixFlavour.set("0")
    E_FruitCake.set("0")
    E_DryCake.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)

    txt_Lemon_malt.configure(state = DISABLED)
    txt_Fanta.configure(state = DISABLED)
    txt_Sprite.configure(state = DISABLED)
    txt_Coke.configure(state = DISABLED)
    txt_Dew.configure(state = DISABLED)
    txt_Chocolate_cake.configure(state = DISABLED)
    txt_Dry_cake.configure(state = DISABLED)
    txt_Fruit_cake.configure(state = DISABLED)
    txt_Ice_cream_Cake.configure(state = DISABLED)
    txt_Mango_cake.configure(state = DISABLED)
    txt_Marinda.configure(state = DISABLED)
    txt_Mix_flavour.configure(state = DISABLED)
    txt_Sting.configure(state = DISABLED)
    txt_Pepsi.configure(state = DISABLED)
    txt_Strawberry_cake.configure(state = DISABLED)
    txt_Valina_cake.configure(state = DISABLED)

def costitem():
    item1 = float(E_Coke.get())
    item2 = float(E_Pepsi.get())
    item3 = float(E_Sprite.get())
    item4 = float(E_Fanta.get())
    item5 = float(E_Marinda.get())
    item6 = float(E_Dew.get())
    item7 = float(E_Sting.get())
    item8 = float(E_LemonMalt.get())

    item9 = float(E_ChocolateCake.get())
    item10 = float(E_VanilaCake.get())
    item11 = float(E_StrawberryCake.get())
    item12 = float(E_MangoCake.get())
    item13 = float(E_IceCreamCake.get())
    item14 = float(E_MixFlavour.get())
    item15 = float(E_FruitCake.get())
    item16= float(E_DryCake.get())

    priceofdrinks = (item1 * 50) + (item2 * 50) + (item3 * 50) + (item4 * 50) + (item5 * 50) + (item6 * 50) + (item7 * 50) + (item8 * 60)
    priceofcakes = (item9 * 300) + (item10 * 200) + (item11 * 250) + (item12 * 400) + (item13 * 500) + (item14 * 400) + (item15 * 200) + (item16 * 150)


    DrinkPrice = "RS", str('%.2f'%(priceofdrinks))
    CakePrice = "RS", str('%.2f'%(priceofcakes))
    CostofDrinks.set(DrinkPrice)
    CostofCakes.set(CakePrice)
    SC = "RS", str('%.2f'%(10))
    ServiceCharges.set(SC)
    SubTotalItems = "RS", str('%.2f'%(priceofcakes + priceofdrinks + 10))
    SubTotal.set(SubTotalItems)
    Tax = "RS", str("%.2f"%(((priceofdrinks + priceofcakes) * 16) / 100))
    paidTax.set(Tax)
    TT = (((priceofdrinks + priceofcakes) * 16) / 100)
    TC = "RS", str('%.2f'%(priceofcakes + priceofdrinks + 10 + TT))
    TotalCost.set(TC)



def chkCoke():
    if var1.get() == 1:
        txt_Coke.configure(state = NORMAL)
        txt_Coke.delete(0, END)
        txt_Coke.focus()

    elif var1.get() == 0:
        txt_Coke.configure(state = DISABLED)
        E_Coke.set("0")


def chkPepsi():
    if var2.get() == 1:
        txt_Pepsi.configure(state = NORMAL)
        txt_Pepsi.delete(0, END)
        txt_Pepsi.focus()
    elif var2.get() == 0:
        txt_Pepsi.configure(state = DISABLED)
        E_Pepsi.set("0")

def chkSprite():
    if var3.get() == 1:
        txt_Sprite.configure(state = NORMAL)
        txt_Sprite.delete(0, END)
        txt_Sprite.focus()
    elif var3.get() == 0:
        txt_Sprite.configure(state = DISABLED)
        E_Sprite.set("0")

def chkFanta():
    if var4.get() == 1:
        txt_Fanta.configure(state = NORMAL)
        txt_Fanta.delete(0, END)
        txt_Fanta.focus()
    elif var4.get() == 0:
        txt_Fanta.configure(state = DISABLED)
        E_Fanta.set("0")

def chkMarinda():
    if var5.get() == 1:
        txt_Marinda.configure(state = NORMAL)
        txt_Marinda.delete(0, END)
        txt_Marinda.focus()
    elif var5.get() == 0:
        txt_Fanta.configure(state = DISABLED)
        E_Marinda.set("0")

def chkDew():
    if var6.get() == 1:
        txt_Dew.configure(state = NORMAL)
        txt_Dew.delete(0, END)
        txt_Dew.focus()
    elif var6.get() == 0:
        txt_Dew.configure(state = DISABLED)
        E_Dew.set("0")

def chkSting():
    if var7.get() == 1:
        txt_Sting.configure(state = NORMAL)
        txt_Sting.delete(0, END)
        txt_Sting.focus()
    elif var7.get() == 0:
        txt_Sting.configure(state = DISABLED)
        E_Sting.set("0")

def chkLemonMalt():
    if var8.get() == 1:
        txt_Lemon_malt.configure(state = NORMAL)
        txt_Lemon_malt.delete(0, END)
        txt_Lemon_malt.focus()
    elif var8.get() == 0:
        txt_Lemon_malt.configure(state = DISABLED)
        E_LemonMalt.set("0")

def chkChocolateCake():
    if var9.get() == 1:
        txt_Chocolate_cake.configure(state = NORMAL)
        txt_Chocolate_cake.delete(0, END)
        txt_Chocolate_cake.focus()

    elif var9.get() == 0:
        txt_Chocolate_cake.configure(state = DISABLED)
        E_ChocolateCake.set("0")


def chkValinacake():
    if var10.get() == 1:
        txt_Valina_cake.configure(state = NORMAL)
        txt_Valina_cake.delete(0, END)
        txt_Valina_cake.focus()
    elif var10.get() == 0:
        txt_Valina_cake.configure(state = DISABLED)
        E_VanilaCake.set("0")

def chkStrawberryCake():
    if var11.get() == 1:
        txt_Strawberry_cake.configure(state = NORMAL)
        txt_Strawberry_cake.delete(0, END)
        txt_Strawberry_cake.focus()
    elif var11.get() == 0:
        txt_Strawberry_cake.configure(state = DISABLED)
        E_StrawberryCake.set("0")

def chkMangoCake():
    if var12.get() == 1:
        txt_Mango_cake.configure(state = NORMAL)
        txt_Mango_cake.delete(0, END)
        txt_Mango_cake.focus()
    elif var12.get() == 0:
        txt_Mango_cake.configure(state = DISABLED)
        E_MangoCake.set("0")

def chkIcecreamCake():
    if var13.get() == 1:
        txt_Ice_cream_Cake.configure(state = NORMAL)
        txt_Ice_cream_Cake.delete(0, END)
        txt_Ice_cream_Cake.focus()
    elif var13.get() == 0:
        txt_Ice_cream_Cake.configure(state = DISABLED)
        E_IceCreamCake.set("0")

def chkMixFalvourCake():
    if var14.get() == 1:
        txt_Mix_flavour.configure(state = NORMAL)
        txt_Mix_flavour.delete(0, END)
        txt_Mix_flavour.focus()
    elif var14.get() == 0:
        txt_Mix_flavour.configure(state = DISABLED)
        E_MixFlavour.set("0")

def chkfruitCake():
    if var15.get() == 1:
        txt_Fruit_cake.configure(state = NORMAL)
        txt_Fruit_cake.delete(0, END)
        txt_Fruit_cake.focus()
    elif var15.get() == 0:
        txt_Fruit_cake.configure(state = DISABLED)
        E_FruitCake.set("0")

def chkDryCake():
    if var16.get() == 1:
        txt_Dry_cake.configure(state = NORMAL)
        txt_Dry_cake.delete(0, END)
        txt_Dry_cake.focus()
    elif var16.get() == 0:
        txt_Dry_cake.configure(state = DISABLED)
        E_DryCake.set("0")

def Receipt():
    txt_Receipt.delete("1.0", END)
    x = random.randint(12100, 90013)
    randomref = str(x)
    Receipt_Ref.set("BILL No: " + randomref)

    txt_Receipt.insert(END, "Receipt Ref:\t\t" + Receipt_Ref.get() + "\t\t" + "Date: " + dateoforder.get() + "\n")
    txt_Receipt.insert(END, "Items\t\t" + "Quantity " + "\t\tCost of per item\n")
    if var1.get() == 1:
        txt_Receipt.insert(END, "Coke:\t\t" + E_Coke.get() + "\t\t50" + "\n")
    if var2.get() == 1:
        txt_Receipt.insert(END, "Pepsi:\t\t" + E_Pepsi.get() + "\t\t50" + "\n")
    if var3.get() == 1:
        txt_Receipt.insert(END, "Sprite:\t\t" + E_Sprite.get() + "\t\t50" + "\n")
    if var4.get() == 1:
        txt_Receipt.insert(END, "Fanta:\t\t" + E_Fanta.get() + "\t\t50" + "\n")
    if var5.get() == 1:
        txt_Receipt.insert(END, "Marinda:\t\t" + E_Marinda.get() + "\t\t50" + "\n")
    if var6.get() == 1:
        txt_Receipt.insert(END, "Dew:\t\t" + E_Dew.get() + "\t\t50" + "\n")
    if var7.get() == 1:
        txt_Receipt.insert(END, "Sting:\t\t" + E_Sting.get() + "\t\t55" + "\n")
    if var8.get() == 1:
        txt_Receipt.insert(END, "Lemon Malt:\t\t" + E_LemonMalt.get() + "\t\t60" + "\n")
    if var9.get() == 1:
        txt_Receipt.insert(END, "Chocolate Cake:\t\t" + E_ChocolateCake.get() + "\t\t300" + "\n")
    if var10.get() == 1:
        txt_Receipt.insert(END, "Valina Cake:\t\t" + E_VanilaCake.get() + "\t\t200" + "\n")
    if var11.get() == 1:
        txt_Receipt.insert(END, "Strawberry Cake:\t\t" + E_StrawberryCake.get() + "\t\t250" + "\n")
    if var12.get() == 1:
        txt_Receipt.insert(END, "Mango Cake:\t\t" + E_MangoCake.get() + "\t\t400" + "\n")
    if var13.get() == 1:
        txt_Receipt.insert(END, "Ice Cream Cake:\t\t" + E_IceCreamCake.get() + "\t\t500" + "\n")
    if var14.get() == 1:
        txt_Receipt.insert(END, "Mix Flavour Cake:\t\t" + E_MixFlavour.get() + "\t\t400" + "\n")
    if var15.get() == 1:
        txt_Receipt.insert(END, "Fruit Cake:\t\t" + E_FruitCake.get() + "\t\t200" + "\n")
    if var16.get() == 1:
        txt_Receipt.insert(END, "Dry Cake:\t\t" + E_DryCake.get() + "\t\t150" + "\n")
    txt_Receipt.insert(END, "Cost of drinks \t\t=\t\t" + CostofDrinks.get() + "\n")
    txt_Receipt.insert(END, "Cost of Cakes \t\t=\t\t" + CostofCakes.get() + "\n")
    txt_Receipt.insert(END, "Service Charges \t\t=\t\t" + ServiceCharges.get() + "\n")
    txt_Receipt.insert(END, "Paid tax \t\t=\t\t" + paidTax.get() + "\n")
    txt_Receipt.insert(END, "Sub Total \t\t=\t\t" + SubTotal.get() + "\n")
    txt_Receipt.insert(END, "Total Cost \t\t=\t\t" + TotalCost.get() + "\n")
# ----------------------------------------Drinks----------------------------------------------------------------
Coke = Checkbutton(Drinks_F, text="Coke", variable=var1, onvalue=1, offvalue=0, font=('arial' , 18 , 'bold')
                    , bg='light grey', command = chkCoke).grid(row=0, sticky=W)
Pepsi = Checkbutton(Drinks_F, text="Pepsi", variable=var2, onvalue=1, offvalue=0, font=('arial' , 18 , 'bold')
                    , bg='light grey', command = chkPepsi).grid(row=1, sticky=W)
Sprite = Checkbutton(Drinks_F, text="Sprite", variable=var3, onvalue=1, offvalue=0, font=('arial' , 18 , 'bold')
                    , bg='light grey', command = chkSprite).grid(row=2, sticky=W)
Fanta = Checkbutton(Drinks_F, text="Fanta", variable=var4, onvalue=1, offvalue=0, font=('arial' , 18 , 'bold')
                    , bg='light grey', command = chkFanta).grid(row=3, sticky=W)
Marinda = Checkbutton(Drinks_F, text="Marinda", variable=var5, onvalue=1, offvalue=0, font=('arial' , 18 , 'bold')
                    , bg='light grey', command = chkMarinda).grid(row=4, sticky=W)
Dew = Checkbutton(Drinks_F, text="Dew", variable=var6, onvalue=1, offvalue=0, font=('arial' , 18 , 'bold')
                    , bg='light grey', command = chkDew).grid(row=5, sticky=W)
Sting = Checkbutton(Drinks_F, text="Sting", variable=var7, onvalue=1, offvalue=0, font=('arial' , 18 , 'bold')
                    , bg='light grey', command = chkSting).grid(row=6, sticky=W)
lemon_malt = Checkbutton(Drinks_F, text="Lemon malt", variable=var8, onvalue=1, offvalue=0, font=('arial' , 18 , 'bold')
                    , bg='light grey', command = chkLemonMalt).grid(row=7, sticky=W)

# ---------------------------------cakes----------------------------------------------------------------------------
Chocolate_cake = Checkbutton(Cake_F, text="Chocolate cake", variable=var9, onvalue=1, offvalue=0, font=('arial' , 18 , 'bold')
                    , bg='light grey', command = chkChocolateCake).grid(row=0, sticky=W)
Valina_cake = Checkbutton(Cake_F, text="Valina cake", variable=var10, onvalue=1, offvalue=0, font=('arial' , 18 , 'bold')
                    , bg='light grey', command = chkValinacake).grid(row=1, sticky=W)
Strawberry_cake = Checkbutton(Cake_F, text="Strawberry cake", variable=var11, onvalue=1, offvalue=0, font=('arial' , 18 , 'bold')
                    , bg='light grey', command = chkStrawberryCake).grid(row=2, sticky=W)
Mango_cake = Checkbutton(Cake_F, text="Mango cake", variable=var12, onvalue=1, offvalue=0, font=('arial' , 18 , 'bold')
                    , bg='light grey', command = chkMangoCake).grid(row=3, sticky=W)
Ice_cream_cake = Checkbutton(Cake_F, text="Ice cream cake", variable=var13, onvalue=1, offvalue=0, font=('arial' , 18 , 'bold')
                    , bg='light grey', command = chkIcecreamCake).grid(row=4, sticky=W)
Mix_flavour = Checkbutton(Cake_F, text="Mix Flavour", variable=var14, onvalue=1, offvalue=0, font=('arial' , 18 , 'bold')
                    , bg='light grey', command = chkMixFalvourCake).grid(row=5, sticky=W)
Fruit_cake = Checkbutton(Cake_F, text="Fruit cake", variable=var15, onvalue=1, offvalue=0, font=('arial' , 18 , 'bold')
                    , bg='light grey', command = chkfruitCake).grid(row=6, sticky=W)
Dry_cake = Checkbutton(Cake_F, text="Dry cake", variable=var16, onvalue=1, offvalue=0, font=('arial' , 18 , 'bold')
                    , bg='light grey', command = chkDryCake).grid(row=7, sticky=W)
# ---------------------------------entry box for Drinks----------------------------------------------------------------------------

txt_Coke = Entry(Drinks_F, font=('arial' , 16 , 'bold' ), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable = E_Coke)
txt_Coke.grid(row=0, column=1)
txt_Pepsi = Entry(Drinks_F, font=('arial' , 16 , 'bold' ), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable = E_Pepsi)
txt_Pepsi.grid(row=1, column=1)
txt_Sprite = Entry(Drinks_F, font=('arial' , 16 , 'bold' ), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable = E_Sprite)
txt_Sprite.grid(row=2, column=1)
txt_Fanta = Entry(Drinks_F, font=('arial' , 16 , 'bold' ), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable = E_Fanta)
txt_Fanta.grid(row=3, column=1)
txt_Marinda = Entry(Drinks_F, font=('arial' , 16 , 'bold' ), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable = E_Marinda)
txt_Marinda.grid(row=4, column=1)
txt_Dew = Entry(Drinks_F, font=('arial' , 16 , 'bold' ), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable = E_Dew)
txt_Dew.grid(row=5, column=1)
txt_Sting = Entry(Drinks_F, font=('arial' , 16 , 'bold' ), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable = E_Sting)
txt_Sting.grid(row=6, column=1)
txt_Lemon_malt = Entry(Drinks_F, font=('arial' , 16 , 'bold' ), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable = E_LemonMalt)
txt_Lemon_malt.grid(row=7, column=1)
# ---------------------------------entry box for cakes----------------------------------------------------------------
txt_Chocolate_cake = Entry(Cake_F, font=('arial' , 16 , 'bold' ), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable = E_ChocolateCake)
txt_Chocolate_cake.grid(row=0, column=1)
txt_Valina_cake = Entry(Cake_F, font=('arial' , 16 , 'bold' ), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable = E_VanilaCake)
txt_Valina_cake.grid(row=1, column=1)
txt_Strawberry_cake = Entry(Cake_F, font=('arial' , 16 , 'bold' ), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable = E_StrawberryCake)
txt_Strawberry_cake.grid(row=2, column=1)
txt_Mango_cake = Entry(Cake_F, font=('arial' , 16 , 'bold' ), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable = E_MangoCake)
txt_Mango_cake.grid(row=3, column=1)
txt_Ice_cream_Cake = Entry(Cake_F, font=('arial' , 16 , 'bold' ), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable = E_IceCreamCake)
txt_Ice_cream_Cake.grid(row=4, column=1)
txt_Mix_flavour = Entry(Cake_F, font=('arial' , 16 , 'bold' ), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable = E_MixFlavour)
txt_Mix_flavour.grid(row=5, column=1)
txt_Fruit_cake = Entry(Cake_F, font=('arial' , 16 , 'bold' ), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable = E_FruitCake)
txt_Fruit_cake.grid(row=6, column=1)
txt_Dry_cake  = Entry(Cake_F, font=('arial' , 16 , 'bold' ), bd=8, width=6, justify=LEFT, state=DISABLED, textvariable = E_DryCake)
txt_Dry_cake .grid(row=7, column=1)

# ----------------------------------Total cost------------------------------------------------------------
lblcostofdrinks = Label(Cost_F, font=('arial' , 14 , 'bold'), text="Cost of drinks", bd=7, bg='SlateGray4', fg='Black')
lblcostofdrinks.grid(row=0, column=0, sticky=W)
txtcostofdrinks = Entry(Cost_F, bg="white", bd=7, font=('arial' , 14 , 'bold'), textvariable = CostofDrinks ,insertwidth=2 ,justify=RIGHT)
txtcostofdrinks.grid(row=0, column=1)

lblcostofcakes = Label(Cost_F, font=('arial' , 14 , 'bold'), text="Cost of cakes", bd=7,bg='SlateGray4', fg='Black')
lblcostofcakes.grid(row=1, column=0, sticky=W)
txtcostofcakes = Entry(Cost_F, bg="white", bd=7, font=('arial' , 14 , 'bold'), textvariable = CostofCakes, insertwidth=2 ,justify=RIGHT)
txtcostofcakes.grid(row=1, column=1)

lblserviceCharges = Label(Cost_F, font=('arial' , 14 , 'bold'), text="Service Charges", bd=7, bg='SlateGray4', fg='Black')
lblserviceCharges.grid(row=2, column=0, sticky=W)
txtserviceCharges = Entry(Cost_F, bg="white", bd=7, font=('arial' , 14 , 'bold'), textvariable = ServiceCharges, insertwidth=2 ,justify=RIGHT)
txtserviceCharges.grid(row=2, column=1)

# ----------------------------------Payment information------------------------------------------------------------
lblpaidtax = Label(Cost_F, font=('arial' , 14 , 'bold'), text="\tpaid Tax", bd=7, bg='SlateGray4', fg='Black')
lblpaidtax.grid(row=0, column=2, sticky=W)
txtpaidtax = Entry(Cost_F, bg="white", bd=7, font=('arial' , 14 , 'bold'), textvariable = paidTax, insertwidth=2 ,justify=RIGHT)
txtpaidtax.grid(row=0, column=3)

lblsubtotal = Label(Cost_F, font=('arial' , 14 , 'bold'), text="\tSub Total", bd=7,bg='SlateGray4', fg='Black')
lblsubtotal.grid(row=1, column=2, sticky=W)
txtsubtotal = Entry(Cost_F, bg="white", bd=7, font=('arial' , 14 , 'bold'), textvariable = SubTotal, insertwidth=2 ,justify=RIGHT)
txtsubtotal.grid(row=1, column=3)

lbltotalcost = Label(Cost_F, font=('arial' , 14 , 'bold'), text="\tTotal Cost", bd=7, bg='SlateGray4', fg='Black')
lbltotalcost.grid(row=2, column=2, sticky=W)
txttotalcost = Entry(Cost_F, bg="white", bd=7, font=('arial' , 14 , 'bold'), textvariable = TotalCost, insertwidth=2 ,justify=RIGHT)
txttotalcost.grid(row=2, column=3)


# -----------------------------------Receipt----------------------------------------------------------
txt_Receipt = Text(Receipt_F, width=46, height=12, bg="white", bd=4, font=('arial', 12 , 'bold'))
txt_Receipt.grid(row=0, column=0)

# ----------------------------------Buttons------------------------------------------------------------
button_total = Button(Buttons_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="Total", bg="light grey", command = costitem).grid(row=0, column=0)
button_Receipt = Button(Buttons_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="Receipt", bg="light grey", command = Receipt).grid(row=0, column=1)
button_Reset = Button(Buttons_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="Reset", bg="light grey", command = reset).grid(row=0, column=2)
button_Exit = Button(Buttons_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="Exit", bg="light grey", command = iExist).grid(row=0, column=3)

# ---------------------------------Calculator Display--------------------------------------------------------------


def btn_Click(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btn_Clear():
    global operator
    operator = ""
    text_input.set("")

def btn_Equals():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""




txtdisplay = Entry(Cal_F, width=45, bg="white", bd=4, font=('arial' , 12 , 'bold'), justify=RIGHT, textvariable=text_input)
txtdisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtdisplay.insert(0, "0")
#---------------------------------Buttons Calculator-------------------------------------------------------
button_7 = Button(Cal_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="7", bg="light grey", command=lambda : btn_Click(7)).grid(row=2, column=0)
button_8 = Button(Cal_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="8", bg="light grey", command=lambda : btn_Click(8)).grid(row=2, column=1)
button_9 = Button(Cal_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="9", bg="light grey", command=lambda : btn_Click(9)).grid(row=2, column=2)
button_add = Button(Cal_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="+", bg="light grey", command=lambda : btn_Click("+")).grid(row=2, column=3)

#---------------------------------Buttons Calculator-------------------------------------------------------
button_4 = Button(Cal_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="4", command=lambda : btn_Click(4)).grid(row=3, column=0)
button_5 = Button(Cal_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="5", command=lambda : btn_Click(5)).grid(row=3, column=1)
button_6 = Button(Cal_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="6", command=lambda : btn_Click(6)).grid(row=3, column=2)
button_sub = Button(Cal_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="-", bg="light grey", command=lambda : btn_Click("-")).grid(row=3, column=3)
#---------------------------------Buttons Calculator-------------------------------------------------------
button_1 = Button(Cal_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="1", command=lambda : btn_Click(1)).grid(row=4, column=0)
button_2 = Button(Cal_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="2", command=lambda : btn_Click(2)).grid(row=4, column=1)
button_3 = Button(Cal_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="3", command=lambda : btn_Click(3)).grid(row=4, column=2)
button_multiply = Button(Cal_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="x", bg="light grey", command=lambda : btn_Click("*")).grid(row=4, column=3)
#---------------------------------Buttons Calculator-------------------------------------------------------
button_Clear = Button(Cal_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="C", bg="light grey", command=lambda : btn_Clear()).grid(row=5, column=0)
button_zero = Button(Cal_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="0", bg="light grey", command=lambda : btn_Click(0)).grid(row=5, column=1)
button_Equal = Button(Cal_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="=", bg="light grey", command=lambda : btn_Equals()).grid(row=5, column=2)
button_Divide = Button(Cal_F, padx=16, pady=1,bd=7,fg="Black", font=('arial' , 16 , 'bold'), width=4
                     , text="/", bg="light grey", command=lambda : btn_Click("/")).grid(row=5, column=3)

root.mainloop()

