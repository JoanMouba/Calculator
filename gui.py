import tkinter as tk
import operator


class CalcApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.operand1 = None
        self.operand2 = None
        self.operator = None
        self.display_str = []

    # CALLBACKS
    def click_numeric_btn(self,number):
        current = self.result_entry.get()
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, str(current)+str(number))
        return

    def click_reset_btn(self):
        self.result_entry.delete(0, tk.END)
        self.operand1 = None
        self.operand2 = None
        self.operator = None
        return

    def click_operator_btn(self, op):
        self.operator = op
        self.operand1 = int(self.result_entry.get())
        self.display_str.append(str(self.operator))
        self.result_entry.delete(0, tk.END)
        return

    def click_equal_btn(self):
        if  self.result_entry.get() is not None:
            self.display_str.append(str(int(self.result_entry.get())))
            self.operand2 = int(self.result_entry.get())
        else:
            self.operand2 = 0
        self.result_entry.delete(0, tk.END)
        if self.operator=="+":
            print("ADDITION")
            self.result_operation = operator.add(self.operand1, self.operand2)
        if self.operator == "-":
            print("SUBTRACTION")
            self.result_operation = operator.sub(self.operand1, self.operand2)
        if self.operator=="*":
            print("MULTIPLICATION")
            self.result_operation = operator.mul(self.operand1, self.operand2)
        if self.operator=="/":
            print("DIVISION")
            self.result_operation = operator.floordiv(self.operand1, self.operand2)
        if self.operator=="%":
            print("MODULO")
            self.result_operation = operator.mod(self.operand1, self.operand2)
        for i in self.display_str:print(i)
        self.result_entry.insert(0, self.result_operation )
        #
        return

    def create_widgets(self):
        # FRAMES
        self.user_frame = tk.LabelFrame(self, text="User name", padx=5, pady=5)
        self.user_frame.pack()

        self.numeric_keypad_frame = tk.LabelFrame(self, text="Numeric Keypad", padx=5, pady=5, width=50)
        self.numeric_keypad_frame.pack()
        self.numeric_keypad_frame.pack(padx=15, pady=15)

        # Define Result Entry
        self.result_entry = tk.Entry(self.numeric_keypad_frame, width=60, borderwidth=5,  fg="grey")
        self.result_entry.insert(0, "")
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define Buttons
        self.btn_zero_0 = tk.Button(self.numeric_keypad_frame, text="0", padx=50, pady=20, command=lambda: self.click_numeric_btn(0))
        self.btn_one_1 = tk.Button(self.numeric_keypad_frame, text="1", padx=50, pady=20, command=lambda: self.click_numeric_btn(1))
        self.btn_two_2 = tk.Button(self.numeric_keypad_frame, text="2", padx=50, pady=20, command=lambda: self.click_numeric_btn(2))
        self.btn_three_3 = tk.Button(self.numeric_keypad_frame, text="3", padx=50, pady=20, command=lambda: self.click_numeric_btn(3))
        self.btn_four_4 = tk.Button(self.numeric_keypad_frame, text="4", padx=50, pady=20, command=lambda: self.click_numeric_btn(4))
        self.btn_five_5 = tk.Button(self.numeric_keypad_frame, text="5", padx=50, pady=20, command=lambda: self.click_numeric_btn(5))
        self.btn_six_6 = tk.Button(self.numeric_keypad_frame, text="6", padx=50, pady=20, command=lambda: self.click_numeric_btn(6))
        self.btn_seven_7 = tk.Button(self.numeric_keypad_frame, text="7", padx=50, pady=20, command=lambda: self.click_numeric_btn(7))
        self.btn_height_8 = tk.Button(self.numeric_keypad_frame, text="8", padx=50, pady=20, command=lambda: self.click_numeric_btn(8))
        self.btn_nine_9 = tk.Button(self.numeric_keypad_frame, text="9", padx=50, pady=20, command=lambda: self.click_numeric_btn(9))

        # Define Maths Operators Buttons
        self.btn_plus_op = tk.Button(self.numeric_keypad_frame, text="+", bg="black", fg="yellow", padx=40, pady=20, command=lambda:self.click_operator_btn("+"))
        self.btn_minus_op = tk.Button(self.numeric_keypad_frame, text="-", bg="black", fg="yellow", padx=40, pady=20, command=lambda:self.click_operator_btn("-"))
        self.btn_division_op = tk.Button(self.numeric_keypad_frame, text="/", bg="black", fg="yellow", padx=40, pady=20, command=lambda:self.click_operator_btn("/"))
        self.btn_multiplication_op = tk.Button(self.numeric_keypad_frame, text="*", bg="black", fg="yellow", padx=40, pady=20, command=lambda:self.click_operator_btn("*"))
        self.btn_modulo_op = tk.Button(self.numeric_keypad_frame, text="%", fg="yellow", bg="black", padx=40, pady=20, command=lambda:self.click_operator_btn("%"))
        self.btn_equal_op = tk.Button(self.numeric_keypad_frame, text="=", padx=50, pady=50, command=self.click_equal_btn)
        self.btn_reset = tk.Button(self.numeric_keypad_frame, text="RESET", padx=40, pady=50, command= self.click_reset_btn)
        self.btn_quit = tk.Button(self.numeric_keypad_frame, text="QUIT", fg="red", bg="blue", padx=40, pady=20, command=self.master.destroy)

        # Put the Buttons on the Frame
        self.btn_one_1.grid(row=1, column=0)
        self.btn_two_2.grid(row=1, column=1)
        self.btn_three_3.grid(row=1, column=2)
        self.btn_plus_op.grid(row=1, column=3)

        self.btn_four_4.grid(row=2, column=0)
        self.btn_five_5.grid(row=2, column=1)
        self.btn_six_6.grid(row=2, column=2)
        self.btn_minus_op.grid(row=2, column=3)

        self.btn_seven_7.grid(row=3, column=0)
        self.btn_height_8.grid(row=3, column=1)
        self.btn_nine_9.grid(row=3, column=2)
        self.btn_division_op.grid(row=3, column=3)

        self.btn_reset.grid(row=4, rowspan=2, column=0)
        self.btn_zero_0.grid(row=4, column=1)
        self.btn_equal_op.grid(row=4, column=2, rowspan=2)
        self.btn_multiplication_op.grid(row=4, column=3)
        self.btn_quit.grid(row=5, column=1)
        self.btn_modulo_op.grid(row=5, column=3)

root = tk.Tk()
root.title("Epignosis Calculator")
app = CalcApplication(master=root)
app.mainloop()


if __name__ == '__main__':
    print("CALCULATOR GUI...")
