import tkinter as tk
from tkinter import messagebox


# Функция ввода цифр в поле ввода

x = True

# def decor(func):
#     # Блокировка окон ввода/вывода (избегание ввода букв в окна)
#     def dec(*args, **kwargs):
#         entry_field['state'] = tk.NORMAL
#         func(*args, **kwargs)
#         entry_field['state'] = tk.DISABLED
#     return dec


def add_digit(digit):
    entry_field['state'] = tk.NORMAL
    global x
    value_1 = entry_field.get('1.0', '1.18')
    value_2 = entry_field.get('2.0', '2.2')
    value_3 = entry_field.get('3.0', '3.18')

    if value_2 and x:
        if len(value_3) == 18:
            # Вводимое второе число не больше 18 символов
            pass

        elif ')' in value_3:
            # После закрытия скобки во втором числе, ввод прекращается
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

        elif value_3 == '0' and digit != '.':
            #  Чтобы небыло возможности ввести во втором числе например '085' ... замена на '85'
            entry_field.delete('3.0', '3.2')
            entry_field.insert('3.0', digit)

        elif value_3 == '(0' and digit != '.':
            #  Чтобы небыло возможности ввести во втором числе например '(085...' ... замена на '(85...'
            entry_field.delete('3.0', '3.3')
            entry_field.insert('3.0', '(' + digit)

        elif value_3 == '(-0' and digit != '.':
            #  Чтобы небыло возможности ввести во втором числе например '(-085...' ... замена на '(-85...'
            entry_field.delete('3.0', '3.4')
            entry_field.insert('3.0', '(-' + digit)

        elif digit == '.' and (value_3 == '(' or value_3 == '(-'):
            # Если ввести точку во втором числе при открытой скобке или скобке с минусом, то подставиться "0."
            result = entry_field.get('3.0', '3.2')
            entry_field.delete('3.0', '3.2')
            entry_field.insert('3.0', result + '0.')

        else:
            # Ввод цифр
            entry_field.insert(tk.E, digit)
    elif x:
        if len(value_1) == 18:
            # Вводимое второе число не больше 18 символов
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

        elif value_1 == '0' and digit != '.':
            #  Чтобы небыло возможности ввести в первом числе например '085' ... замена на '85'
            entry_field.delete('1.0', '1.2')
            entry_field.insert('1.0', digit)

        else:
            # Ввод цифр
            entry_field.insert(tk.E, digit)
    else:
        entry_field.delete('1.0', tk.END)
        if digit == '.':
            entry_field.insert('1.0', '0.')
        else:
            entry_field.insert('1.0', digit)
        entry_field_result['state'] = tk.NORMAL
        entry_field_result.delete(0, tk.END)
        entry_field_result.insert(0, '0')
        entry_field_result['state'] = tk.DISABLED
        x = True
    entry_field['state'] = tk.DISABLED


def add_operation(operation):
    entry_field['state'] = tk.NORMAL
    global x
    value_1 = entry_field.get('1.0', '1.18')
    value_3 = entry_field.get('3.0', '3.18')

    if value_3 and value_3 != '(':
        calculate()
        result = entry_field_result.get()
        entry_field.delete('1.0', tk.END)
        entry_field.insert('1.0', result + '\n')
        entry_field.insert('2.0', ' ' + operation + '\n')

    elif (operation == '-' and len(value_1) == 0) or (operation == '-' and value_1 == '-'):
        entry_field.delete('1.0', tk.END)
        entry_field.insert('1.0', '-')

    elif (operation in '/*+' and value_1 == '-') or (operation in '/*+' and len(value_1) == 0) or value_3.count('-') == 1:
        pass

    elif value_3 and value_3[0] == '(' and operation == '-':
        # Возможность ввести отрицательное число после скобки во 2-м вводимом числе
        entry_field.insert('3.1', '-')

    else:
        entry_field.delete('1.0', tk.END)
        entry_field.insert('1.0', value_1 + '\n')
        entry_field.delete('2.0', '2.18')
        entry_field.insert('2.0', ' ' + operation + '\n')
    x = True
    entry_field['state'] = tk.DISABLED


def add_brackets(bracket):
    entry_field['state'] = tk.NORMAL
    value_2 = entry_field.get('2.0', '2.2')
    value_3 = entry_field.get('3.0', '3.18')

    if value_2 and len(value_3) == 0 and bracket == '(':
        entry_field.insert('3.0', bracket)

    elif value_2 and bracket == ')' and '(' in value_3 and len(value_3) > 1 and value_3.count(')') < 1:
        entry_field.insert(tk.END, bracket)
    entry_field['state'] = tk.DISABLED


def calculate():
    entry_field_result['state'] = tk.NORMAL
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
    entry_field_result['state'] = tk.DISABLED


def clear_entry_field():
    entry_field['state'] = tk.NORMAL
    entry_field_result['state'] = tk.NORMAL
    entry_field.delete('1.0', tk.END)
    entry_field_result.delete(0, tk.END)
    entry_field_result.insert(0, '0')
    entry_field['state'] = tk.DISABLED
    entry_field_result['state'] = tk.DISABLED


def calculate_button():
    calculate()
    global x
    x = False


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


def press_key(event):
    if event.char.isdigit() or event.char == '.':
        add_digit(event.char)
    elif event.char in '/*+-':
        add_operation(event.char)
    elif event.char == '\r':
        calculate_button()
    elif event.char == '\x1b':
        clear_entry_field()
    # print(event)


win = tk.Tk()

# Размеры окна
win.geometry("240x300")
win.resizable(False, False)

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
win.title('Калькулятор v2')

win.bind('<Key>', press_key)

# Поле ввода
entry_field = tk.Text(master=win, font='arial', width=15, height=3, borderwidth=5)
entry_field.grid(row=0, column=0, columnspan=3, stick='we', pady=5, padx=5)
entry_field['state'] = tk.DISABLED


# Поле вывода результата
entry_field_result = tk.Entry(master=win, font='arial', width=15, borderwidth=5, justify=tk.RIGHT)
entry_field_result.insert(0, '0')
entry_field_result.grid(row=1, column=0, columnspan=3, stick='we', pady=5, padx=5)
entry_field_result['state'] = tk.DISABLED


# Кнопки с цифрами
tk.Button(text='AC', bg='#dadce0', font='arial', bd=2, command=lambda: clear_entry_field()).grid(row=0, column=4,
                                                                                                 columnspan=2,
                                                                                                 stick='wens', padx=5,
                                                                                                 pady=5)

# Скобки - используются только для ввода 2-го значения (например: отнять отрицательное число, поделить на отрицательное)
make_brackets('(').grid(row=1, column=4, stick='wens', padx=2, pady=5)
make_brackets(')').grid(row=1, column=5, stick='wens', padx=5, pady=5)

# Символы цифр и операций
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
