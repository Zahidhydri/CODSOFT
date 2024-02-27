from tkinter import *
import math

#==================================================================================================
def calculator():
    # Basic Structure===========================                                                   
    zahid = Tk()     # Main Window
    #zahid=Toplevel(My_Project_Window)
    zahid.configure(background='#1ff',relief="ridge",bd=10)
    '''
    for i in range(7):
            zahid.columnconfigure(i,weight=1,minsize=0)
    for i in range(11):
            zahid.rowconfigure(i,weight=1,minsize=0)
    '''
    #zahid.geometry("625x479")
    #zahid.attributes("-fullscreen",True)
    zahid.resizable(0,0)
    zahid.title("1222A - Zahid Hydri - Python Calculator")

    # Golbal Variable =========================
    global calculate
    calculate = ""
    equation = StringVar()
    # Functions ==================================
    def click(button):
        global calculate
        calculate = calculate + str(button)
        equation.set(calculate)

    def Clear():
        global calculate
        calculate = ""
        equation.set("0")

    def back():
        global calculate
        calculate = calculate[:-1]
        equation.set(calculate)

    def Equal ():
        global calculate
        try:
                if "^" in calculate:
                        calculate=calculate.replace("^","**")
                        result = str(eval(calculate))
                if "pi" in calculate:
                        calculate=calculate.replace("pi","*22/7")
                        result = str(eval(calculate))

                else:      
                        result = str(eval(calculate))
                
                if result =="0":
                        equation.set("= "+ result)
                        calculate = ""
                else:
                        equation.set("= "+ result)
                        calculate = result
        except:
                equation.set("error")
                calculate =""

    def percentage():
        global calculate
        try:
                if calculate.isnumeric() :
                        result=str(eval(calculate+"/100"))
                elif "/" in calculate:
                        result=str(eval(calculate+"*100"))

                else:
                        result=str(eval(calculate+"/100"))  
                equation.set("= "+ result+"%")
                calculate = result
        except:
                equation.set("error")
                calculate =""

    def unroot():
        global calculate
        try:
                result = str(eval(calculate + "**0.5"))
                equation.set("= "+ result)
                calculate = result
        except:
                equation.set("error")
                calculate =""

    def facto():
        global calculate
        try:
                result = str(math.factorial(int(str(eval(calculate )))))
                equation.set("= "+ result)
                calculate = result
        except:
                equation.set("error")
                calculate =""

    def logg():
        global calculate
        try:
                result = str(math.log(float(calculate)))
                equation.set("= "+ result)
                calculate = result
        except:
                equation.set("error")
                calculate =""


    def logg10():
        global calculate
        try:
                result = str(math.log10(float(calculate)))
                equation.set("= "+ result)
                calculate = result
        except:
                equation.set("error")
                calculate =""

    def sine():
        global calculate
        try:
                result = round(math.sin((math.radians(float(calculate)))),9)
                result = str(result)
                equation.set("= "+ result)
                calculate = result
        except:
                equation.set("error")
                calculate =""

    def cose():
        global calculate
        try:
                result = round(math.cos((math.radians(float(calculate)))),9)
                result = str(result)
                equation.set("= "+ result)
                calculate = result
        except:
                equation.set("error")
                calculate =""

    def tan():
        global calculate
        try:
                result = round(math.tan((math.radians(float(calculate)))),9)
                result = str(result)
                equation.set("= "+ result)
                calculate = result
        except:
                equation.set("error")
                calculate =""

    def cot():
        global calculate
        try:
                result = round(1/math.tan((math.radians(float(calculate)))),9)
                result = str(result)
                equation.set("= "+ result)
                calculate = result
        except:
                equation.set("error")
                calculate =""

    def csec():
        global calculate
        try:
                result = round(1/math.sin((math.radians(float(calculate)))),9)
                result = str(result)
                equation.set("= "+ result)
                calculate = result
        except:
                equation.set("error")
                calculate =""

    def sec():
        global calculate
        try:
                result = round(1/math.cos((math.radians(float(calculate)))),9)
                result = str(result)
                equation.set("= "+ result)
                calculate = result
        except:
                equation.set("error")
                calculate =""
                   
    # Graphics =====================================================================================

    label_0 = Label(zahid,font = ('bausaus',15,'bold'),bg="#f9f",bd=2,text=" ")
    #label_0.grid(row=1,column=1,columnspan=6,sticky="ew")

    #label_1d = Label(zahid,font = ('bausaus',15,'bold'),bg="#f9f",bd=2,text=strftime("%A, %B %d, %Y "),justify = LEFT)
    #label_1d.grid(row=1,column=1,columnspan=3,sticky="w")

    label_1t = Label(zahid,font = ('bausaus',15,'bold'),bg="#f9f",bd=2,justify = RIGHT)
    #label_1t.grid(row=1,column=4,columnspan=3,sticky="e")

    label = Label(zahid,font = ('cooper black',32,'bold'),bg="#1ff",text="Python Calculator",relief="groove",bd=10)
    label.grid(row=2,column=1,columnspan=6,sticky="ew")

    entry = Entry(zahid,font = ('arial',24,'bold'),textvariable = equation,width = 34,bd = 0,highlightbackground = "black",highlightcolor = "black",highlightthickness = 3,bg = "#eef",justify = RIGHT)
    entry.grid(row = 3,column = 1,columnspan=6,ipady=10)

    # Buttons ===========================================================================
    one = Button(zahid,font = ('bausaus',20,'bold'),text="1",fg = "black",width = 5,height = 1,bg = "#fff",
                    cursor = "hand2",command = lambda: click(1))
    one.grid(row = 5, column = 1,padx = 1, pady = 1,ipadx = 10)
    two = Button(zahid,font = ('bausaus',20,'bold'),text="2",fg = "black",width = 5,height = 1,bg = "#fff",
                    cursor = "hand2",command = lambda: click(2))
    two.grid(row = 5, column = 2,padx = 1, pady = 1,ipadx = 10)
    three = Button(zahid,font = ('bausaus',20,'bold'),text="3",fg = "black",width = 5,height = 1,bg = "#fff",
                    cursor = "hand2",command = lambda: click(3))
    three.grid(row = 5, column = 3,padx = 1, pady = 1,ipadx = 10)
    four = Button(zahid,font = ('bausaus',20,'bold'),text="4",fg = "black",width = 5,height = 1,bg = "#fff",
                    cursor = "hand2",command = lambda: click(4))
    four.grid(row = 6, column = 1,padx = 1, pady = 1,ipadx = 10)
    five = Button(zahid,font = ('bausaus',20,'bold'),text="5",fg = "black",width = 5,height = 1,bg = "#fff",
                    cursor = "hand2",command = lambda: click(5))
    five.grid(row = 6, column = 2,padx = 1, pady = 1,ipadx = 10)
    six = Button(zahid,font = ('bausaus',20,'bold'),text="6",fg = "black",width = 5,height = 1,bg = "#fff",
                    cursor = "hand2",command = lambda: click(6))
    six.grid(row = 6, column = 3,padx = 1, pady = 1,ipadx = 10)
    seven = Button(zahid,font = ('bausaus',20,'bold'),text="7",fg = "black",width = 5,height = 1,bg = "#fff",
                    cursor = "hand2",command = lambda: click(7))
    seven.grid(row = 7, column = 1,padx = 1, pady = 1,ipadx = 10)
    eight = Button(zahid,font = ('bausaus',20,'bold'),text="8",fg = "black",width = 5,height = 1,bg = "#fff",
                    cursor = "hand2",command = lambda: click(8))
    eight.grid(row = 7, column = 2,padx = 1, pady = 1,ipadx = 10)
    nine = Button(zahid,font = ('bausaus',20,'bold'),text="9",fg = "black",width = 5,height = 1,bg = "#fff",
                    cursor = "hand2",command = lambda: click(9))
    nine.grid(row = 7, column = 3,padx = 1, pady = 1,ipadx = 10)
    zero = Button(zahid,font = ('bausaus',20,'bold'),text="0",fg = "black",width = 10,height = 1,bg = "#fff",
                    cursor = "hand2",command = lambda: click(0))
    zero.grid(row = 8, column = 1,columnspan = 2,padx = 1, pady = 1,ipadx = 25)

    point = Button(zahid,font = ('bausaus',20,'bold'),text=".",fg = "black",width = 5,height = 1,bg = "#fff",
                    cursor = "hand2",command = lambda: click("."))
    point.grid(row = 8, column = 3,padx = 1, pady = 1,ipadx = 10)

    plus = Button(zahid,font = ('bausaus',20,'bold'),text="+",fg = "black",width = 5,height = 1,bg = "#11f",
                    cursor = "hand2",command = lambda: click("+"))
    plus.grid(row = 5, column = 4,padx = 2, pady = 1,ipadx = 20)
    minus = Button(zahid,font = ('bausaus',20,'bold'),text="-",fg = "black",width = 5,height = 1,bg = "#11f",
                    cursor = "hand2",command = lambda: click("-"))
    minus.grid(row = 6, column = 4,padx = 2, pady = 1,ipadx = 20)
    multiply = Button(zahid,font = ('bausaus',20,'bold'),text="*",fg = "black",width = 5,height = 1,bg = "#11f",
                    cursor = "hand2",command = lambda: click("*"))
    multiply.grid(row = 7, column = 4,padx = 2, pady = 1,ipadx = 20)
    divide = Button(zahid,font = ('bausaus',20,'bold'),text="/",fg = "black",width = 5,height = 1,bg = "#11f",
                    cursor = "hand2",command = lambda: click("/"))
    divide.grid(row = 8, column = 4,padx = 2, pady = 1,ipadx = 20)

    power = Button(zahid,font = ('bausaus',20,'bold'),text = "^",fg = "black",width = 5,height = 1,bg = "#19f",
                    cursor = "hand2",command = lambda: click("^"))
    power.grid(row = 4,column = 2,rowspan = 1,padx = 1,pady = 1,ipadx=10)
    root = Button(zahid,font = ('bausaus',20,'bold'),text = "√",fg = "black",width = 5,height = 1,bg = "#19f",
                    cursor = "hand2",command = lambda: unroot())
    root.grid(row = 4,column = 3,rowspan = 1,padx = 1,pady = 1,ipadx=10)
    percent = Button(zahid,font = ('bausaus',20,'bold'),text = "%",fg = "black",width = 5,height = 1,bg = "#19f",
                    cursor = "hand2",command = lambda: percentage())
    percent.grid(row = 4,column = 4,rowspan = 1,padx = 1,pady = 1,ipadx = 20)

    cancel = Button(zahid,font = ('bausaus',20,'bold'),text = "X",fg = "black",width = 5,height = 1,bg = "#f91",
                    cursor = "hand2",command = lambda: back())
    cancel.grid(row = 4,column = 1,columnspan = 1,rowspan = 1,padx = 1,pady = 1,ipadx=10)

    fact = Button(zahid,font = ('bausaus',20,'bold'),text = "x!",fg = "black",width = 3,height = 1,bg = "#f09",
                    cursor = "hand2",command = lambda: facto())
    fact.grid(row = 4,column = 6,rowspan = 1,padx = 1,pady = 1)
    pii = Button(zahid,font = ('bausaus',20,'bold'),text = "pi",fg = "black",width = 3,height = 1,bg = "#f09",
                    cursor = "hand2",command = lambda: click("pi"))
    pii.grid(row = 4,column = 5,rowspan = 1,padx = 1,pady = 1)
    log = Button(zahid,font = ('bausaus',20,'bold'),text = "log",fg = "black",width = 3,height = 1,bg = "#ff1",
                    cursor = "hand2",command = lambda: logg())
    log.grid(row = 5,column = 5,rowspan = 1,padx = 1,pady = 1)
    log10 = Button(zahid,font = ('bausaus',15,'bold'),text = "log10",fg = "black",width = 4,height = 1,bg = "#ff1",
                    cursor = "hand2",command = lambda: logg10())
    log10.grid(row = 5,column = 6,rowspan = 1,padx = 1,pady = 1,ipadx=2,ipady=7)
    sin = Button(zahid,font = ('bausaus',20,'bold'),text = "sin",fg = "black",width = 3,height = 1,bg = "#90f",
                    cursor = "hand2",command = lambda: sine())
    sin.grid(row = 6,column = 5,rowspan = 1,padx = 1,pady = 1)
    cos = Button(zahid,font = ('bausaus',20,'bold'),text = "cos",fg = "black",width = 3,height = 1,bg = "#90f",
                    cursor = "hand2",command = lambda: cose())
    cos.grid(row = 7,column = 5,rowspan = 1,padx = 1,pady = 1)
    tangent = Button(zahid,font = ('bausaus',20,'bold'),text = "tan",fg = "black",width = 3,height = 1,bg = "#90f",
                    cursor = "hand2",command = lambda: tan())
    tangent.grid(row = 8,column = 5,rowspan = 1,padx = 1,pady = 1)
    cotan = Button(zahid,font = ('bausaus',20,'bold'),text = "cot",fg = "black",width = 3,height = 1,bg = "#98f",
                    cursor = "hand2",command = lambda: cot())
    cotan.grid(row = 8,column = 6,rowspan = 1,padx = 1,pady = 1)
    cosecent = Button(zahid,font = ('bausaus',15,'bold'),text = "cosec",fg = "black",width = 3,height = 1,bg = "#98f",
                    cursor = "hand2",command = lambda: csec())
    cosecent.grid(row = 6,column = 6,rowspan = 1,padx = 1,pady = 1,ipadx=8,ipady=6)
    secent = Button(zahid,font = ('bausaus',20,'bold'),text = "sec",fg = "black",width = 3,height = 1,bg = "#98f",
                    cursor = "hand2",command = lambda: sec())
    secent.grid(row = 7,column = 6,rowspan = 1,padx = 1,pady = 1)

    clear = Button(zahid,font = ('bausaus',20,'bold'),text = "AC",fg = "black",width = 10,height = 1,bg = "#f22",
                    cursor = "hand2",command = lambda: Clear())
    clear.grid(row = 9, column = 1,columnspan = 2,padx = 1, pady = 1,ipadx = 25)     

    equal = Button(zahid,font = ('bausaus',20,'bold'),text = "=",fg = "black",width = 19,height = 1,bg = "#2e2",
                    cursor = "hand2",command = lambda: Equal())
    equal.grid(row = 9, column = 3,columnspan = 4,padx = 1, pady = 1,ipadx = 25)

    label_2 = Label(zahid,font = ('bausaus',20,'bold'),relief="ridge",bd=6,bg = "#f9f",text=" \
                                - 1222A - Zahid .S. Hydri.  ",justify = RIGHT)
    label_2.grid(row = 10,column = 1,columnspan = 6)

    exit_c = Button(zahid,font = ('arial',14,'bold'),width = 8,bd = 0,fg = "#fff",bg = "#f1f",text = "Exit",cursor = "hand2",command = lambda:zahid.destroy())
    exit_c.grid(row = 10,column = 1,columnspan = 1)

    zahid.mainloop()


calculator()


    
