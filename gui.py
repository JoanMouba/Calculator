import tkinter as tk

class CalcApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def print_result(self):
        self.result_lbl = tk.Label(self.display_frame, text="Hello " + self.username_entry.get())
        self.result_lbl.pack()
        print("Result")

    def create_widgets(self):
        # FRAMES
        self.display_frame = tk.LabelFrame(self, text="Display", padx=5, pady=5)
        self.display_frame.pack(padx=15, pady=15)
        self.display_lbl = tk.Label(self.display_frame, text="Result ...", bg="white",  fg="grey", width=30, padx=5, pady=5)
        self.display_lbl.pack()

        self.user_frame = tk.LabelFrame(self, text="User name", padx=5, pady=5)
        self.user_frame.pack()

        self.numeric_keypad_frame = tk.LabelFrame(self, text="Numeric Keypad", padx=5, pady=5, width=50)
        self.numeric_keypad_frame.pack()
        self.numeric_keypad_frame.pack(padx=15, pady=15)

        # BUTTONS
        self.result_entry = tk.Entry(self.numeric_keypad_frame, width=35, borderwidth=5,  fg="grey")
        self.result_entry.insert(0, "Result...")
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.btn_one_1 = tk.Button(self.numeric_keypad_frame, text="1", padx=40, pady=20, state=tk.DISABLED)
        self.btn_one_1.grid(row=1, column=0)
        self.btn_two_2 = tk.Button(self.numeric_keypad_frame, text="2", padx=40, pady=20)
        self.btn_two_2.grid(row=1, column=1)
        self.btn_three_3 = tk.Button(self.numeric_keypad_frame, text="3", padx=40, pady=20)
        self.btn_three_3.grid(row=1, column=2)
        self.btn_plus_op = tk.Button(self.numeric_keypad_frame, text="+", bg="black", fg="yellow", padx=40, pady=20)
        self.btn_plus_op.grid(row=1, column=3)

        self.btn_four_4 = tk.Button(self.numeric_keypad_frame, text="4", padx=40, pady=20)
        self.btn_four_4.grid(row=2, column=0)
        self.btn_five_5 = tk.Button(self.numeric_keypad_frame, text="5", padx=40, pady=20)
        self.btn_five_5.grid(row=2, column=1)
        self.btn_six_6 = tk.Button(self.numeric_keypad_frame, text="6", padx=40, pady=20)
        self.btn_six_6.grid(row=2, column=2)
        self.btn_minus_op = tk.Button(self.numeric_keypad_frame, text="-", bg="black", fg="yellow", padx=40, pady=20)
        self.btn_minus_op.grid(row=2, column=3)

        self.btn_seven_7 = tk.Button(self.numeric_keypad_frame, text="7", padx=40, pady=20)
        self.btn_seven_7.grid(row=3, column=0)
        self.btn_height_8 = tk.Button(self.numeric_keypad_frame, text="8", padx=40, pady=20)
        self.btn_height_8.grid(row=3, column=1)
        self.btn_nine_9 = tk.Button(self.numeric_keypad_frame, text="9", padx=40, pady=20)
        self.btn_nine_9.grid(row=3, column=2)
        self.btn_division_op = tk.Button(self.numeric_keypad_frame, text="/", bg="black", fg="yellow", padx=40, pady=20)
        self.btn_division_op.grid(row=3, column=3)

        self.btn_reset = tk.Button(self.numeric_keypad_frame, text="RESET", padx=40, pady=20)
        self.btn_reset.grid(row=3, column=0)
        self.btn_quit = tk.Button(self.numeric_keypad_frame, text="QUIT", fg="red", bg="blue", padx=40, pady=20, command=self.master.destroy)
        self.btn_quit.grid(row=3, column=1)
        self.btn_equal_op = tk.Button(self.numeric_keypad_frame, text="=", padx=40, pady=20, command=self.print_result)
        self.btn_equal_op.grid(row=3, column=2)
        self.btn_multiplication_op = tk.Button(self.numeric_keypad_frame, text="*", bg="black", fg="yellow", padx=40, pady=20)
        self.btn_multiplication_op.grid(row=3, column=3)

        # LABELS AND ENTRY
        # StringVar_entry_username = tk.StringVar()
        # self.app_title_lbl = tk.Label(self)
        # self.username_label = tk.Label(self, text="User Name")
        # self.username_label.pack(side="left")
        # self.entry_username = tk.Entry(self, bd=5, textvariable=StringVar_entry_username)
        # self.entry_username.pack(side="right")

        # CANVAS
        # self.calc_canvas = tk.Canvas(self, bg="blue", height=250, width=300)
        # coord = 10, 50, 240, 210
        # arc = self.calc_canvas.create_arc(coord, start=0, extent=150, fill='brown')

        # CHECKBOXES
        # CheckVar_normal = tk.IntVar()
        # CheckVar_scientific = tk.IntVar()
        #
        # self.calc_normal_mode_check = tk.Checkbutton(self, text="Normal", activeforeground="blue",
        #                                              activebackground="yellow", variable=CheckVar_normal,\
        #                                              onvalue=1, offvalue=0, height=5, width=20)
        # self.calc_scientific_mode_check = tk.Checkbutton(text="Scientific", activeforeground="blue",
        #                                                  activebackground="yellow",  variable=CheckVar_scientific, \
        #                                                  onvalue=1, offvalue=0, height=5, width=20)


root = tk.Tk()
root.title("Epignosis Calculator")
app = CalcApplication(master=root)
app.mainloop()


if __name__ == '__main__':
    print("CALCULATOR GUI...")
