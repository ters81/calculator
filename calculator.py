import tkinter as tk


# Функция ввода цифр в поле ввода

def add_digit(digit):
    value = entry_field.get()
    if digit == '.' and value.count('.') == 1:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, value)
    else:
        if value[0] == '0' and digit == '.':
            value = value
        elif value[0] == '0' and len(value) == 1:
            value = value[:-1]
        entry_field.delete(0, tk.END)
        entry_field.insert(0, value + str(digit))

def add_operation(operation):
    value = entry_field.get()
    if value[-1] in '÷x+-':
        value = value[:-1]
    entry_field.delete(0, tk.END)
    entry_field.insert(0, value + operation)


def make_digit_button(digit):
    return tk.Button(text=digit, bg='#f1f3f4', font='arial', bd=2, command=lambda: add_digit(digit))

def make_operation_button(operation):
    return tk.Button(text=operation, bg='#dadce0', font='arial', fg='blue', bd=2, command=lambda: add_operation(operation))

def make_calc_button(operation):
    return tk.Button(text=operation, bg='#4285f4', font='arial', fg='white', bd=2, command=lambda: add_digit(operation))

win = tk.Tk()

# Размеры окна
# win.geometry("240x260")
win.minsize(240, 260)
win.maxsize(240, 260)

# Размещение окна по центру экрана
win.update_idletasks()
s = win.geometry()
s = s.split('+')
s = s[0].split('x')
s_win = s[0]
width_win = int(s[0])
height_win = int(s[1])
w = win.winfo_screenwidth()
h = win.winfo_screenheight()
w = w // 2
h = h // 2
w = w - width_win // 2
h = h - height_win // 2
win.geometry(f'+{w}+{h}')

# Внешний вид окна
win.config(bg='#ffffff', relief='raised')
# Название окна
win.title('Калькулятор')

# Поле ввода
entry_field = tk.Entry(master=win, font='arial', width=15, justify=tk.RIGHT, borderwidth=5)
entry_field.insert(0, '0')
entry_field.grid(row=0, column=0, columnspan=3, stick='we', pady=5, padx=5)

# Кнопки с цифрами
tk.Button(text='AC', bg='#dadce0', font='arial', bd=2).grid(row=0, column=4, stick='wens', padx=5, pady=5)
make_operation_button('÷').grid(row=1, column=4, stick='wens', padx=5, pady=5)
make_operation_button('×').grid(row=2, column=4, stick='wens', padx=5, pady=5)
make_operation_button('+').grid(row=3, column=4, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=4, column=4, stick='wens', padx=5, pady=5)

tk.Button(text='.', bg='#f1f3f4', font='arial', bd=2, command=lambda: add_digit('.')).grid(row=4, column=1,
                                                                                           stick='wens', padx=5, pady=5)
make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
tk.Button(text='0', bg='#f1f3f4', font='arial', bd=2, command=lambda: add_digit(0)).grid(row=4, column=0, stick='wens',
                                                                                         padx=5, pady=5)

make_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)

# x = 1
# for i in range(1, 4):
#     for j in range(3):
#         tk.Button(text=f'{x}', bg='#f1f3f4', font='arial', bd=2, command=lambda: add_digit()).grid(row=i, column=j, stick='wens', padx=5, pady=5)
#         x += 1


win.grid_columnconfigure(0, weight=1)
win.grid_columnconfigure(1, weight=1)
win.grid_columnconfigure(2, weight=1)
win.grid_columnconfigure(3, weight=1)

win.grid_rowconfigure(1, weight=1)
win.grid_rowconfigure(2, weight=1)
win.grid_rowconfigure(3, weight=1)
win.grid_rowconfigure(4, weight=1)

win.mainloop()
