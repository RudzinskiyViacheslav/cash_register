import tkinter
from tkinter import *
from datetime import datetime
from tkinter import messagebox as mb
from models import *

def new_Window(root, id_number):
    def add_Good():
        add_Name = text_Add_Name.get('1.0', 'end-1c')
        add_Unit_Name = text_Add_Unit_Name.get('1.0', 'end-1c')
        add_Unit_Price = text_Add_Unit_Price.get('1.0', 'end-1c')
        add_Quantity = text_Add_Quantity.get('1.0', 'end-1c')
        add_Correction_Date = datetime.today().strftime("%Y-%m-%d")

        try:
            add_New_Good = {"id": id_number+1, "name": add_Name, "unit_name": add_Unit_Name,
                        "unit_price": int(add_Unit_Price), "quantity": int(add_Quantity),
                        "date_last_delivery": add_Correction_Date
                            }
        except ValueError as err:
            text_Add_Unit_Price.delete('1.0', 'end')
            text_Add_Quantity.delete('1.0', 'end')
            mb.showerror(title="Ошибка", message="Поля цены и количества товара заполните цифрами")

        for value in add_New_Good.values():
            if value == '':
                tkinter.messagebox.showerror(title=None, message='Заполните все поля',)
                break
        else:
            add_New_Good_To_DB(add_New_Good)
            window2.destroy()


    window2 = tkinter.Toplevel(root)
    window2.geometry('750x350')
    window2.configure(background='#FF5555')

    Label(window2, text="Добавить новый товар", font='Inter 19 bold', bg='#A66BFF', ).place(x=270, y=20)

    Label(window2, text="Наименование", font='Inter 15 bold', bg='#A66BFF', ).place(x=20, y=100)
    Label(window2, text="Единица измерения товара", font='Inter 15 bold', bg='#A66BFF', ).place(x=380, y=100)

    text_Add_Name = Text(window2, fg='white', font='Inter 15', bg='#594036', width=33, height=1, padx=10, pady=10, )
    text_Add_Name.place(x=20, y=130)

    text_Add_Unit_Name = Text(window2, fg='white', font='Inter 15', bg='#594036', width=33, height=1, padx=10, pady=10, )
    text_Add_Unit_Name.place(x=380, y=130)

    Label(window2, text="Цена единицы товара", font='Inter 15 bold', bg='#A66BFF', ).place(x=20, y=180)
    Label(window2, text="Количество", font='Inter 15 bold', bg='#A66BFF', ).place(x=380, y=180)

    text_Add_Unit_Price = Text(window2, fg='white', font='Inter 15', bg='#594036', width=33, height=1, padx=10, pady=10, )
    text_Add_Unit_Price.place(x=20, y=210)

    text_Add_Quantity = Text(window2, fg='white', font='Inter 15', bg='#594036', width=33, height=1, padx=10, pady=10, )
    text_Add_Quantity.place(x=380, y=210)

    btn_Сreate_New_Good = Button(window2, text="Добавить запись", fg='white', font='Inter 15', bg='#A66BFF', width=20,
                                 height=2, command=add_Good)
    btn_Сreate_New_Good.place(x=260, y=270)

    window2.mainloop()