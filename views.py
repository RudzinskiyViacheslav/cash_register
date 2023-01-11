from tkinter import *
from tkinter import messagebox as mb
from new_window import *
from window_buy import window_for_buy

def window():

    def show_All():
        global data
        data = get_All(DataBase)

        box_select_Show_All['state'] = 'normal'
        box_select_Show_All.delete(0, END)

        for item in data:
            box_select_Show_All.insert('end', item + '\n')

        btn_Select_Good['state'] = 'normal'
        btn_Buy['state'] = 'normal'

    def select_Good():


        try:
            select_Data_Index = box_select_Show_All.curselection()[0]

            text_Change_Unit_Price['state'] = 'normal'
            text_Change_Quantity['state'] = 'normal'

            text_Change_Unit_Price.delete('1.0', 'end')
            text_Change_Quantity.delete('1.0', 'end')

            text_Change_Unit_Price.insert('1.0', DataBase['goods'][select_Data_Index]['unit_price'])
            text_Change_Quantity.insert('1.0', DataBase['goods'][select_Data_Index]['quantity'])

            btn_Change_Good['state'] = 'normal'

        except IndexError as err:
            mb.showerror(title="Ошибка", message="Сначала выберите товар для его редактирования")

    def buy():
        select_Data_Index = box_select_Show_All.curselection()[0]
        window_for_buy(select_Data_Index)
        try:

            text_Change_Unit_Price['state'] = 'normal'
            text_Change_Quantity['state'] = 'normal'

            text_Change_Unit_Price.delete('1.0', 'end')
            text_Change_Quantity.delete('1.0', 'end')

            text_Change_Unit_Price.insert('1.0', DataBase['goods'][select_Data_Index]['unit_price'])
            text_Change_Quantity.insert('1.0', DataBase['goods'][select_Data_Index]['quantity'])

            btn_Change_Good['state'] = 'normal'

        except IndexError as err:
            mb.showerror(title="Ошибка", message="Сначала выберите товар для его редактирования")

    def new_Good():
        new_Window(root, len(DataBase['goods']))

    def change_Good():
        change_selected_unit_price = text_Change_Unit_Price.get('1.0', 'end')
        change_selected_quantity = text_Change_Quantity.get('1.0', 'end')

        flag_To_Go_Unit_Price = False
        flag_To_Go_Quantity = False

        if change_selected_unit_price != '':
            try:
                change_selected_unit_price = int(change_selected_unit_price)
                flag_To_Go_Unit_Price = True
            except ValueError as err:
                text_Change_Unit_Price.delete('1.0', 'end')
                mb.showerror(title="Ошибка", message="Поле цены товара заполните цифрами")

        if change_selected_quantity != '':
            try:
                change_selected_quantity = int(change_selected_quantity)
                flag_To_Go_Quantity = True
            except ValueError as err:
                text_Change_Quantity.delete('1.0', 'end')
                mb.showerror(title="Ошибка", message="Поле количества товара заполните цифрами")
        print(flag_To_Go_Unit_Price, flag_To_Go_Quantity)
        if flag_To_Go_Quantity and flag_To_Go_Unit_Price == True:
            select_Data_Index = box_select_Show_All.curselection()[0]

            change_DataBase(select_Data_Index, change_selected_unit_price, change_selected_quantity)

            text_Change_Unit_Price.delete('1.0', 'end')
            text_Change_Quantity.delete('1.0', 'end')

            text_Change_Unit_Price['state'] = 'disabled'
            text_Change_Quantity['state'] = 'disabled'

            btn_Select_Good['state'] = 'disabled'
            btn_Change_Good['state'] = 'disabled'

            show_All()

    def on_Closing():
        data_Rewrite()
        root.destroy()

    root = Tk()

    root.title("Курсовая работа. Выполнил: Игорек")
    root.geometry('1400x800')
    root.configure(background='#FF5555')

    #Показать все товары (кнопка + поле)
    box_select_Show_All = Listbox(root, width=110, height=15, bg='#594036', borderwidth=0, font='Inter 15',
                                  fg='white', state = 'disabled')
    box_select_Show_All.place(x=20, y=20)

    btn_Show_All = Button(root, text="Показать все товары", fg='white', font='Inter 15', bg='#A66BFF', width=20,
                          height=2, command = show_All)
    btn_Show_All.place(x=1150, y=20)

    #Кнопка нового товара
    btn_New_Good = Button(root, text="Новое поступление", fg='white', font='Inter 15', bg='#A66BFF', width=20,
                          height=2, command=new_Good)
    btn_New_Good.place(x=1150, y=100)

    #Кнопка оформленика покупки
    btn_Buy = Button(root, text="Оформить покупку", fg='white', font='Inter 15', bg='#A66BFF', width=20,
                          height=2, command=buy, state = 'disabled')
    btn_Buy.place(x=1150, y=180)

    #Кнопка обновления старого товара
    btn_Select_Good = Button(root, text="Обновить товар", fg='white', font='Inter 15', bg='#A66BFF', width=20,
                          height=2, command=select_Good, state = 'disabled')
    btn_Select_Good.place(x=1150, y=260)

    #Поля для обновления товара
    Label(root, text="Цена единицы товара", font='Inter 15 bold', bg='#A66BFF', ).place(x=20, y=320)
    Label(root, text="Количество", font='Inter 15 bold', bg='#A66BFF', ).place(x=450, y=320)

    text_Change_Unit_Price = Text(root, fg='white', font='Inter 15', bg='#594036', width=38, height=1,
                                  padx=10, pady=10, state = 'disabled')
    text_Change_Unit_Price.place(x=20, y=350)

    text_Change_Quantity = Text(root, fg='white', font='Inter 15', bg='#594036', width=38, height=1,
                                padx=10, pady=10, state = 'disabled')
    text_Change_Quantity.place(x=450, y=350)

    btn_Change_Good = Button(root, text="Отправить", fg='white', font='Inter 15', bg='#A66BFF', width=20,
                             height=2, command=change_Good, state='disabled')
    btn_Change_Good.place(x=880, y=344)

    root.protocol("WM_DELETE_WINDOW", on_Closing)
    root.mainloop()