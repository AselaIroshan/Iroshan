from tkinter import *

class Calculator(Tk):
    def __init__(self): 
        super().__init__()
        self.title("Calculator")
        self.config(bg="black")
        
        # Display
        self.label = Label(self, text="0", font=('TkFixedFont', 50), bg="gray14", fg="white", anchor="e", padx=10)
        self.label.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.Graphics()

        ##Track_data
        self.INPUT_NUMBER = []
        self.TEMP_LIST = []
        self.DISPLAY_LIST = []
        self.OPERATOR = None
        self.dot_used = False  


    ##grapic_inite
    def Graphics(self):
        for i in range(0, 6):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

        # Buttons
        Button(self, text="AC",command=self.clear, bg="gray50", font=('TkFixedFont', 24), bd=0 ).grid(row=1, column=0, sticky="nsew")
        Button(self, text="+/-",command=self.convert, bg="gray50", font=('TkFixedFont', 24), bd=0).grid(row=1, column=1, sticky="nsew")
        Button(self, text="%", command= self.prentage,  bg="gray50", font=('TkFixedFont', 24), bd=0).grid(row=1, column=2, sticky="nsew")
        Button(self, text="/", command=self.div, bg="orange", font=('TkFixedFont', 24), bd=0).grid(row=1, column=3, sticky="nsew")

        Button(self, text="7", command=self.num_7, bg="gray35", font=('TkFixedFont', 24), bd=0).grid(row=2, column=0, sticky="nsew")
        Button(self, text="8", command=self.num_8, bg="gray35", font=('TkFixedFont', 24), bd=0).grid(row=2, column=1, sticky="nsew")
        Button(self, text="9", command=self.num_9, bg="gray35", font=('TkFixedFont', 24), bd=0).grid(row=2, column=2, sticky="nsew")
        Button(self, text="*", command=self.mul, bg="orange", font=('TkFixedFont', 24), bd=0).grid(row=2, column=3, sticky="nsew")

        Button(self, text="4", command=self.num_4, bg="gray35", font=('TkFixedFont', 24), bd=0).grid(row=3, column=0, sticky="nsew")
        Button(self, text="5", command=self.num_5, bg="gray35", font=('TkFixedFont', 24), bd=0).grid(row=3, column=1, sticky="nsew")
        Button(self, text="6", command=self.num_6, bg="gray35", font=('TkFixedFont', 24), bd=0).grid(row=3, column=2, sticky="nsew")
        Button(self, text="-", command=self.sub, bg="orange", font=('TkFixedFont', 24), bd=0).grid(row=3, column=3, sticky="nsew")

        Button(self, text="1", command=self.num_1, bg="gray35", font=('TkFixedFont', 24), bd=0).grid(row=4, column=0, sticky="nsew")
        Button(self, text="2", command=self.num_2, bg="gray35", font=('TkFixedFont', 24), bd=0).grid(row=4, column=1, sticky="nsew")
        Button(self, text="3", command=self.num_3, bg="gray35", font=('TkFixedFont', 24), bd=0).grid(row=4, column=2, sticky="nsew")
        Button(self, text="+", command=self.sum,   bg="orange", font=('TkFixedFont', 24), bd=0).grid(row=4, column=3, sticky="nsew")

        Button(self, text="0", command=self.num_0, bg="gray35", font=('TkFixedFont', 24), bd=0).grid(row=5, column=0, columnspan=2, sticky="nsew")
        Button(self, text=".", command=self.dot, bg="gray35", font=('TkFixedFont', 24), bd=0).grid(row=5, column=2, sticky="nsew")
        Button(self, text="=", command=self.final, bg="orange", font=('TkFixedFont', 24), bd=0).grid(row=5, column=3, sticky="nsew")

    ##button fun
    def num_1(self):
        self.TEMP_LIST.append("1")
        self.Display("1")

    def num_2(self):
        self.TEMP_LIST.append("2")
        self.Display("2")

    def num_3(self):
        self.TEMP_LIST.append("3")
        self.Display("3")

    def num_4(self):
        self.TEMP_LIST.append("4")
        self.Display("4")

    def num_5(self):
        self.TEMP_LIST.append("5")
        self.Display("5")

    def num_6(self):
        self.TEMP_LIST.append("6")
        self.Display("6")

    def num_7(self):
        self.TEMP_LIST.append("7")
        self.Display("7")

    def num_8(self):
        self.TEMP_LIST.append("8")
        self.Display("8")

    def num_9(self):
        self.TEMP_LIST.append("9")
        self.Display("9")

    def num_0(self):
        self.TEMP_LIST.append("0")
        self.Display("0")
    
    ##Desimal {.}
    def dot(self):
        if not self.dot_used:
            self.TEMP_LIST.append(".")
            self.Display(".")
            self.dot_used = True  

    ##disply data
    def Display(self, symbol):
        self.DISPLAY_LIST.append(symbol)
        data = "".join(self.DISPLAY_LIST)
        self.label.config(text=data)

    ##calculation method
    def sum(self):
        self.handle_operator("+")
        
    def sub(self):
        self.handle_operator("-")

    def mul(self):
        self.handle_operator("*")

    def div(self):
        self.handle_operator("/")
    
    def prentage(self):
        self.handle_operator("%")

    def handle_operator(self, operator):
        if self.OPERATOR is not None:
            self.calculate()
        if len(self.TEMP_LIST) != 0:
            self.INPUT_NUMBER.append(float("".join(self.TEMP_LIST)))
            self.TEMP_LIST = []
            self.dot_used = False  # Reset dot usage for next number
        self.OPERATOR = operator
        self.Display(operator)
    

    ##conver numbers to positive or nagative
    def convert(self):
        if len(self.INPUT_NUMBER)!= 0 :
            temp = self.INPUT_NUMBER[0]
            temp = temp * -1
            self.INPUT_NUMBER[0] = temp
            self.DISPLAY_LIST = []
            self.DISPLAY_LIST.append(str(temp))
            self.label.config(text=str(self.INPUT_NUMBER[0]))

    
    ##when press {=} button
    def final(self):
        self.calculate()
        self.label.config(text=str(self.INPUT_NUMBER[0]))
        self.OPERATOR = None

    def calculate(self):
        if len(self.TEMP_LIST) != 0:
            self.INPUT_NUMBER.append(float("".join(self.TEMP_LIST)))
            self.TEMP_LIST = []
            self.dot_used = False  
        if len(self.INPUT_NUMBER) == 2:
            if self.OPERATOR == "+":
                result = self.INPUT_NUMBER[0] + self.INPUT_NUMBER[1]
            elif self.OPERATOR == "-":
                result = self.INPUT_NUMBER[0] - self.INPUT_NUMBER[1]
            elif self.OPERATOR == "*":
                result = self.INPUT_NUMBER[0] * self.INPUT_NUMBER[1]
            elif self.OPERATOR == "/":
                result = self.INPUT_NUMBER[0] / self.INPUT_NUMBER[1]
            elif self.OPERATOR == "%":
                result = (self.INPUT_NUMBER[0]) * (self.INPUT_NUMBER[1] / 100)
            self.INPUT_NUMBER = [result]
    ## whan press {AC}betton
    def clear(self):
        self.TEMP_LIST = []
        self.INPUT_NUMBER = []
        self.DISPLAY_LIST = []
        self.OPERATOR = None
        self.dot_used = False  # Reset dot usage for new calculation
        self.label.config(text="0")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
