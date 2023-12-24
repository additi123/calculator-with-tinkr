import tkinter as tk

calculation = ""
def add(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate():
    global calculation
    try:
       
        result = str(eval(calculation))
        calculation = ""
        update_display(result)

    except ZeroDivisionError:
        clear()
        udpate_display("Cannot divide by 0")


    except:
        clear()
        update_display("error")




def clear():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

def update_display(value=""):
    text_result.delete(1.0, "end")
    text_result.insert(1.0, value)



screen = tk.Tk()
screen.geometry("300x275")
screen.title("Calculator")

text_result = tk.Text(screen, height=2, width=16, font=('Arial', 25))
text_result.grid(columnspan=5)


btn_1 = tk.Button(screen, text="1", command=lambda: add(1), width=5, font=('Arial', 15))
btn_1.grid(row=3, column=0)

btn_2 = tk.Button(screen, text="2", command=lambda: add(2), width=5, font=('Arial', 15))
btn_2.grid(row=3, column=1)

btn_3 = tk.Button(screen, text="3", command=lambda: add(3), width=5, font=('Arial', 15))
btn_3.grid(row=3, column=2)

btn_4 = tk.Button(screen, text="4", command=lambda: add(4), width=5, font=('Arial', 15))
btn_4.grid(row=2, column=0)

btn_5 = tk.Button(screen, text="5", command=lambda: add(5), width=5, font=('Arial', 15))
btn_5.grid(row=2, column=1)

btn_6 = tk.Button(screen, text="6", command=lambda: add(6), width=5, font=('Arial', 15))
btn_6.grid(row=2, column=2)

btn_7 = tk.Button(screen, text="7", command=lambda: add(7), width=5, font=('Arial', 15))
btn_7.grid(row=1, column=0)


btn_8 = tk.Button(screen, text="8", command=lambda: add(8), width=5, font=('Arial', 15))
btn_8.grid(row=1, column=1)

btn_9 = tk.Button(screen, text="9", command=lambda: add(9), width=5, font=('Arial', 15))
btn_9.grid(row=1, column=2)

btn_0 = tk.Button(screen, text="0", command=lambda: add(0), width=5, font=('Arial', 15))
btn_0.grid(row=4, column=1)


btn_add = tk.Button(screen, text="+", command=lambda: add("+"), width=5, font=('Arial', 15))
btn_add.grid(row=4, column=3)

btn_minus = tk.Button(screen, text="-", command=lambda: add("-"), width=5, font=('Arial', 15))
btn_minus.grid(row=3, column=3)

btn_mult = tk.Button(screen, text="*", command=lambda: add("*"), width=5, font=('Arial', 15))
btn_mult.grid(row=2, column=3)

btn_div = tk.Button(screen, text="/", command=lambda: add("/"), width=5, font=('Arial', 15))
btn_div.grid(row=1, column=3)

btn_openbrac= tk.Button(screen, text="(", command=lambda: add("("), width=5, font=('Arial', 15))
btn_openbrac.grid(row=4, column=0)

btn_closebrac= tk.Button(screen, text=")", command=lambda: add(")"), width=5, font=('Arial', 15))
btn_closebrac.grid(row=4, column=2)

btn_equal= tk.Button(screen, text="=", command=evaluate, width=12, font=('Arial', 15))
btn_equal.grid(row=5, column=2, columnspan=2)

btn_clear= tk.Button(screen, text="CE", command=clear , width=12, font=('Arial', 15))
btn_clear.grid(row=5, column=0, columnspan=2)


screen.mainloop()
