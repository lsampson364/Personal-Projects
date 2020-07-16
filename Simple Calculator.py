import tkinter as tk
import math

class Calculator:
    def __init__(self,master = None):

        self.master = master

        # These variables are the operands the calculator uses to preform operations.
        self.operand_1 = None
        self.operand_2 = None

        self.result = None # This variable is where the result of the operation is placed.
        self.operation = None # This variable lets the calculator know which operation is being done.

        self.index = 1  # This variable is an index that tells the cursor where to place a number in the display box.

        self.decimal = False    # When this variable is true, the calculator turns
                                # the strings in the operand variables to floting point numbers.

        self.FLOAT = False  # This variable lets the calculater know when the decimal point has been used.
                            # When this variable is True, the calculator will prevent the user from entering
                            # more than one decimal point.

        self.start = True   # The display box needs to start with a '0'
                            # in it to look like most calculators when they
                            # are on. This variable lets the calculator know
                            # when to delete the lead '0' so the numbers display correctly.

        # Create display box
        self.display = tk.Entry(root, width=35, borderwidth = 5, justify = 'right')

        # Create the buttons
        self.zero =tk.Button(root,text = "0", padx = 40, pady=20, command=lambda: self.button_click(0))

        self.one = tk.Button(root,text = "1", padx = 40, pady=20, command=lambda: self.button_click(1))
        self.two = tk.Button(root,text = "2", padx = 40, pady=20, command=lambda: self.button_click(2))
        self.three = tk.Button(root,text = "3", padx = 40, pady=20, command=lambda: self.button_click(3))

        self.four = tk.Button(root,text = "4", padx = 40, pady=20, command=lambda: self.button_click(4))
        self.five = tk.Button(root,text = "5",  padx = 40, pady=20, command=lambda: self.button_click(5))
        self.six = tk.Button(root,text = "6",  padx = 40, pady=20, command=lambda: self.button_click(6))

        self.seven = tk.Button(root,text = "7", padx = 40, pady=20, command=lambda: self.button_click(7))
        self.eight = tk.Button(root,text = "8", padx = 40, pady=20, command=lambda: self.button_click(8))
        self.nine = tk.Button(root,text = "9", padx = 40, pady=20, command=lambda: self.button_click(9))

        self.addition = tk.Button(root, text="+", padx = 40, pady=20, command=lambda: self.add() )
        self.subtraction = tk.Button(root, text="-", padx = 40, pady=20, command=lambda: self.subtract() )
        self.division = tk.Button(root, text= chr(247), padx = 40, pady=20, command=lambda: self.divide() )
        self.multiplication = tk.Button(root, text= chr(215), padx = 40, pady=20, command=lambda: self.multiply() )
        self.equals = tk.Button(root, text="=", padx = 40, pady=20, command=lambda: self.compute() )

        # The below code creates the decimal point button and AC/clear buttons respectively
        self.dec = tk.Button(root,text = ".", padx = 40, pady=20, command=lambda: self.if_decimal())
        self.AC = tk.Button(root, text="Clear", padx = 30, pady=20, command=lambda: self.clear() )

    def is_number(self, string):
        '''This functions checks to see if the passed in string is a number.
        If the string can be converted to a float without raising value error,then its
        a number and the function will return true. If converting th string raises an error,
        it is not a number and the function will return false.'''
        try:
            float(string)
            return True
        except ValueError:
            return False

    def if_start(self):
        ''' This function deletes the leading zero so numbers display correctly.
        When self.start is true, this function will delete everything in the display box. Then,
        it will check if the decimal point has been used. If it has, the function will add
        the zero and the decimal point back to the display box. self.start is then changed to false,
        letting the calculator know that it is that the user is no longer at the beginning of a number.
        Further calls of this function will result in the empty string being inserted in to the display box,
        until self.start is true again.'''
        if self.start:
            self.display.delete(0,"end")
            if self.FLOAT:
                self.display.insert(self.index-2,"0.")
            self.start = False

        else:
            self.display.insert(self.index,"")

    def button_click(self, number):
        '''This function implements a numerical button press. When this function is called,
        the if_start() function is called first to check if there is a leading zero that needs to be deleted.
        The function will then insert the number into the display box at the specified index(self.index) and
        increment the index by 1.'''
        self.if_start()
        self.display.insert(self.index, number)
        self.index+=1

    def if_decimal(self):
        '''This functions implements a decimal point button press. When this function is called, it checks
         to see if the decimal point button has been pressed yet, denoted by self.FLOAT == False. If the
         decimal point button has not been pressed, self.decimal is set to true, letting the calculator know to
         convert the operands to floats in the computation step. self.FLOAT is set to true, letting the calculator
         know that the decimal button has been pressed.  The decimal point is  then inserted at the specified index
         and the index is incremented by 1. If the decimal button is pressed when self.FLOAT is true, the
         function will insert the empty string into the display box.'''

        if not self.FLOAT:
            self.decimal = True
            self.FLOAT = True
            self.display.insert(self.index,'.')
            self.index+=1
        else:
            self.display.insert(self.index,"")

    def add(self):
        '''This function implements the plus sign button press. When called, this function
        checks to see if string is a number. If it is, store the first operand. The display is then cleared and
        the plus sign is displayed. self.FLOAT is re-initialized to False to re-enable the use of the
        decimal button. self.start is re-initialized to True to delete the lead characters once more
        when the user starts to type the second operand. self.operation is set to 1 to let the compute
        function know which operation to perform. '''
        if self.is_number(self.display.get()):
            self.operand_1 = self.display.get()
            print("operand 1 = ", self.operand_1)
            self.display.delete(0,"end")
            self.display.insert(0, "+ ")
            self.FLOAT = False
            self.start = True
            self.operation = 1

    def subtract(self):
        '''This function implements the minus sign button press. When called, this function
        checks to see if string is a number. If it is, store the first operand. The display is then cleared and
        the minus sign is displayed. self.FLOAT is re-initialized to False to re-enable the use of the
        decimal button. self.start is re-initialized to True to delete the lead characters once more
        when the user starts to type the second operand. self.operation is set to 2 to let the compute
        function know which operation to perform. '''
        if self.is_number(self.display.get()):
            self.operand_1 = self.display.get()
            print("operand 1 = ", self.operand_1)
            self.display.delete(0,"end")
            self.display.insert(0, "-")
            self.FLOAT = False
            self.start = True
            self.operation = 2

    def multiply(self):
        '''This function implements the multiplication sign button press. When called, this function
        checks to see if string is a number. If it is, store the first operand. The display is then cleared and
        the multiplication sign is displayed. self.FLOAT is re-initialized to False to re-enable the use of the
        decimal poin button. self.start is re-initialized to True to delete the lead characters once more
        when the user starts to type the second operand. self.operation is set to 3 to let the compute
        function know which operation to perform. '''
        if self.is_number(self.display.get()):
            self.operand_1 = self.display.get()
            print("operand 1 = ", self.operand_1)
            self.display.delete(0,"end")
            self.display.insert(0, chr(215))
            self.FLOAT = False
            self.start = True
            self.operation = 3

    def divide(self):
        '''This function implements the divide sign button press. When called, this function
        checks to see if string is a number. If it is, store the first operand. The display is then cleared and
        the divide sign is displayed. self.FLOAT is re-initialized to False to re-enable the use of the
        decimal button. self.start is re-initialized to True to delete the lead characters once more
        when the user starts to type the second operand. self.operation is set to 4 to let the compute
        function know which operation to perform. '''
        if self.is_number(self.display.get()):
            self.operand_1 = self.display.get()
            print("operand 1 = ", self.operand_1)
            self.display.delete(0,"end")
            self.display.insert(0, chr(247))
            self.FLOAT = False
            self.start = True
            self.operation = 4

    def clear(self):
        '''This button clears the display and resets all of
        the flags and operands to their original states'''
        self.display.delete(0,"end")
        self.display.insert(0,0)
        self.operand_1 = None
        self.operand_2 = None
        self.FLOAT = False
        self.start = True
        self.index = 1

    def compute(self):
        '''This function implements the press of the equals button. When called, this function
        stores whats is in the display window into the second operand variable. If no operation
        been selected, the first operand will be set to 0 (it would be none type if I didnt) and
        the operation would be set to 1(addition).This is to keep the calculator from "breaking" if
        the user presses equals without choosing an operation. The display is then cleared.

        If the operation selected is addition, the is_number() function will check if the second operand
        contains a number. If it does not the second operand will be set equal to the first operand. This is
        to prevent the calculator from "breaking" if the user presses equals without entering 2 operands.
        This function then checks the self.decimal variable to see if the decimal point has been used. If it
        has then the operand will be converted into floating point. If it hasn't the operands will be converted
        into integers. This logic was place in to a try/except block because it is possible for the user to
        type non-numeric strings into the display box. To prevent the calculator from "breaking" andto inform
        the user that typing into the display box is not how the caculator is intended to be used, if the
        caculator detects that the operands are not numbers, it will display:

        "Invalid input method. Please use buttons for input"

        The same logic applies for subtraction, muliplication and division.

        The compute function will then store and display the the result. Lastly the self.start variable is
        set to true, allowing the user to begin a new calculation.
        '''


        self.operand_2 = self.display.get()
        print("operand 2 = ", self.operand_2)
        if self.operation is None:
            self.operand_1 = 0
            self.operation = 1

        self.display.delete(0,"end")
        if self.operation == 1:
            if not self.is_number(self.operand_2):
                self.operand_2 = self.operand_1

            if self.decimal:
                try:
                    self.result = float(self.operand_1) + float(self.operand_2)
                except ValueError:
                    self.clear()
                    self.display.delete(0,"end")
                    self.display.insert(0,"Invalid input method. Please use buttons for input")

            else:
                try:
                    self.result = int(self.operand_1) + int(self.operand_2)
                except ValueError:
                    self.clear()
                    self.display.delete(0,"end")
                    self.display.insert(0,"Invalid input method. Please use buttons for input")

        elif self.operation == 2:
            if not self.is_number(self.operand_2):
                self.operand_2 = self.operand_1

            if self.decimal:
                try:
                    self.result = float(self.operand_1) - float(self.operand_2)
                except ValueError:
                    self.clear()
                    self.display.delete(0,"end")
                    self.display.insert(0,"Invalid input method. Please use buttons for input")

            else:
                try:
                    self.result = int(self.operand_1) - int(self.operand_2)
                except ValueError:
                    self.clear()
                    self.display.delete(0,"end")
                    self.display.insert(0,"Invalid input method. Please use buttons for input")

        elif self.operation == 3:
            if not self.is_number(self.operand_2):
                self.operand_2 = self.operand_1

            if self.decimal:
                try:
                    self.result = float(self.operand_1) * float(self.operand_2)
                except ValueError:
                    self.clear()
                    self.display.delete(0,"end")
                    self.display.insert(0,"Invalid input method. Please use buttons for input")

            else:
                try:
                    self.result = int(self.operand_1) * int(self.operand_2)
                except ValueError:
                    self.clear()
                    self.display.delete(0,"end")
                    self.display.insert(0,"Invalid input method. Please use buttons for input")

        elif self.operation == 4:
            if not self.is_number(self.operand_2):
                self.operand_2 = self.operand_1

            if self.decimal:
                try:
                    self.result = float(self.operand_1) / float(self.operand_2)
                except ValueError:
                    self.clear()
                    self.display.delete(0,"end")
                    self.display.insert(0,"Invalid input method. Please use buttons for input")
            else:
                try:
                    self.result = int(self.operand_1) / int(self.operand_2)
                except ValueError:
                    self.clear()
                    self.display.delete(0,"end")
                    self.display.insert(0,"Invalid input method. Please use buttons for input")

        self.display.insert(0,self.result)
        print("result = ", self.result)
        self.start = True

#Declare the caculator object "calc" then create, title and size the parent window of calc
root = tk.Tk()
calc = Calculator(master=root)
calc.master.title("LS-89")
calc.master.geometry("450x330")

#Place Display on the screen
calc.display.grid(row=0, column=0, columnspan =3, padx=10, pady=10)
calc.display.insert(0,0)

#Place the buttons on the screen
calc.one.grid(row = 3, column =0)
calc.two.grid(row = 3, column =1)
calc.three.grid(row = 3, column =2)

calc.four.grid(row = 2, column =0)
calc.five.grid(row = 2, column =1)
calc.six.grid(row = 2, column =2)

calc.seven.grid(row = 1, column =0)
calc.eight.grid(row = 1, column =1)
calc.nine.grid(row = 1, column =2)

calc.zero.grid(row = 4, column =0)
calc.dec.grid(row = 4, column =1)
calc.AC.grid(row = 4, column =2)

calc.addition.grid(row = 0, column =3)
calc.subtraction.grid(row = 1, column =3)
calc.division.grid(row = 2, column =3)
calc.multiplication.grid(row = 3, column =3)
calc.equals.grid(row = 4, column =3)

calc.master.mainloop()
