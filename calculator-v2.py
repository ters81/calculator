import tkinter as tk
from tkinter import messagebox


# Функция ввода цифр в поле ввода

def add_digit(digit):
    value_1 = entry_field.get('1.0', '1.18')
    value_2 = entry_field.get('2.0', '2.2')
    value_3 = entry_field.get('3.0', '3.18')

    if value_2:
        if len(value_3) == 18:
            pass

        elif ')' in value_3:
            pass

        elif digit == '.' and len(value_3) == 0:
            # Если ввести точку, то подставиться "0.".
            entry_field.insert('3.0', '0.')

        elif digit == '0' and len(value_3) > 0 and value_3[0] == '0' and '.' not in value_3:
            # Чтобы вначале ввода вводился только 1 ноль при вводе числа
            pass

        elif digit == '.' and value_3.count('.') == 1:
            # Чтобы вводилась только одна точка при вводе числа
            pass

        else:
            # Ввод цифр
            entry_field.insert(tk.E, digit)
    else:
        if len(value_1) == 18:
            pass

        elif digit == '.' and len(value_1) == 0:
            # Если ввести точку, то подставиться "0.".
            entry_field.insert('1.0', '0.')

        elif digit == '.' and value_1 == '-':
            # Если ввести точку при уже введенном "-", то подставиться "-0."
            entry_field.delete('1.0', '1.2')
            entry_field.insert('1.0', '-0.')

        elif digit == '0' and len(value_1) > 0 and value_1[0] == '0' and '.' not in value_1:
            # Чтобы вначале ввода вводился только 1 ноль при вводе числа
            pass

        elif digit == '.' and value_1.count('.') == 1:
            # Чтобы вводилась только одна точка при вводе числа
            pass

        else:
            # Ввод цифр
            entry_field.insert(tk.E, digit)


def add_operation(operation):
    value_1 = entry_field.get('1.0', '1.18')
    value_3 = entry_field.get('3.0', '3.18')

    if (operation == '-' and len(value_1) == 0) or (operation == '-' and value_1 == '-'):
        entry_field.delete('1.0', tk.END)
        entry_field.insert('1.0', '-')

    elif (operation in '/*+' and value_1 == '-') or (operation in '/*+' and len(value_1) == 0) or value_3.count('-') == 1:
        pass

    # Возможность ввести отрицательное число после скобки во 2-м вводимом значении
    elif value_3 and value_3[0] == '(' and operation == '-':
        entry_field.insert('3.1', '-')

    else:
        entry_field.delete('1.0', tk.END)
        entry_field.insert('1.0', value_1 + '\n')
        entry_field.delete('2.0', '2.18')
        entry_field.insert('2.0', ' ' + operation + '\n')


def add_brackets(bracket):
    value_2 = entry_field.get('2.0', '2.2')
    value_3 = entry_field.get('3.0', '3.18')

    if value_2 and len(value_3) == 0 and bracket == '(':
        entry_field.insert('3.0', bracket)
    elif value_2 and bracket == ')' and '(' in value_3 and len(value_3) > 1 and value_3.count(')') < 1:
        entry_field.insert(tk.END, bracket)

def calculate():
    value_1 = entry_field.get('1.0', '1.18')
    value_2 = entry_field.get('2.0', '2.2')
    value_3 = entry_field.get('3.0', '3.18')

    if '(' in value_3 and ')' not in value_3:
        messagebox.showinfo('Внимание', 'Закройте скобки!')

    try:
        result = str(round(eval(value_1 + value_2 + value_3), 15))
        if result[-2::] == '.0':
            result = result.rstrip('0').rstrip('.')
        entry_field_result.delete(0, tk.END)
        entry_field_result.insert(0, result)

    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'Нельзя делить на 0!')
        entry_field.insert(0, 0)

def clear_entry_field():
    entry_field.delete('1.0', tk.END)
    entry_field_result.delete(0, tk.END)
    entry_field_result.insert(0, '0')


def calculate_button():
    calculate()


def make_digit_button(digit):
    return tk.Button(text=digit, bg='#f1f3f4', font='arial', bd=2, command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(text=operation, bg='#dadce0', font='arial', fg='blue', bd=2,
                     command=lambda: add_operation(operation))

def make_brackets(bracket):
    return tk.Button(text=bracket, bg='#dadce0', font='arial', fg='blue', bd=2,
                     command=lambda: add_brackets(bracket))

def make_calc_button(operation):
    return tk.Button(text=operation, bg='#4285f4', font='arial', fg='white', bd=2, command=lambda: calculate_button())


win = tk.Tk()

# Размеры окна
# win.geometry("240x260")
win.minsize(240, 300)
win.maxsize(240, 300)

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
entry_field = tk.Text(master=win, font='arial', width=15, height=5, borderwidth=5)
# entry_field.insert('1.0', '0')
# entry_field['state'] = tk.DISABLED
entry_field.grid(row=0, column=0, columnspan=3, stick='we', pady=5, padx=5)

# Поле вывода результата
entry_field_result = tk.Entry(master=win, font='arial', width=15, borderwidth=5, justify=tk.RIGHT)
entry_field_result.insert(0, '0')
# entry_field_result['state'] = tk.DISABLED
entry_field_result.grid(row=1, column=0, columnspan=3, stick='we', pady=5, padx=5)

# Кнопки с цифрами
tk.Button(text='AC', bg='#dadce0', font='arial', bd=2, command=lambda: clear_entry_field()).grid(row=0, column=4,
                                                                                                 columnspan=2,
                                                                                                 stick='wens', padx=5,
                                                                                                 pady=5)

# Скобки - используются только для ввода 2-го значения (например: отнять отрицательное число, поделить на отрицательное)
make_brackets('(').grid(row=1, column=4, stick='wens', padx=2, pady=5)
make_brackets(')').grid(row=1, column=5, stick='wens', padx=5, pady=5)

# Символы операций
make_operation_button('/').grid(row=2, column=4, columnspan=2, stick='wens', padx=5, pady=5)
make_operation_button('*').grid(row=3, column=4, columnspan=2, stick='wens', padx=5, pady=5)
make_operation_button('+').grid(row=4, column=4, columnspan=2, stick='wens', padx=5, pady=5)
make_operation_button('-').grid(row=5, column=4, columnspan=2, stick='wens', padx=5, pady=5)

make_digit_button('.').grid(row=5, column=1, stick='wens', padx=5, pady=5)
make_calc_button('=').grid(row=5, column=2, stick='wens', padx=5, pady=5)

make_digit_button('0').grid(row=5, column=0, stick='wens', padx=5, pady=5)
make_digit_button('1').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_button('2').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_button('3').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_button('4').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_button('5').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_button('6').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_button('7').grid(row=4, column=0, stick='wens', padx=5, pady=5)
make_digit_button('8').grid(row=4, column=1, stick='wens', padx=5, pady=5)
make_digit_button('9').grid(row=4, column=2, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, weight=1)
win.grid_columnconfigure(1, weight=1)
win.grid_columnconfigure(2, weight=1)
win.grid_columnconfigure(3, weight=1)

win.grid_rowconfigure(1, weight=1)
win.grid_rowconfigure(2, weight=1)
win.grid_rowconfigure(3, weight=1)
win.grid_rowconfigure(4, weight=1)

win.mainloop()
