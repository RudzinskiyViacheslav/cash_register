import tkinter
from tkinter import *
from datetime import datetime
from tkinter import messagebox as mb
from models import *

def window_for_buy(index):

    def make_Order():
        client_Name = text_Client_Name.get('1.0', 'end-1c')
        client_Phone = text_Client_Phone.get('1.0', 'end-1c')
        client_Adress = text_Client_Adress.get('1.0', 'end-1c')
        client_Quantity = text_Client_Quantity.get('1.0', 'end-1c')

        try:
            client_Phone = int(client_Phone)
            client_Quantity = int(client_Quantity)
        except ValueError as err:
            text_Client_Phone.delete('1.0', 'end')
            text_Client_Quantity.delete('1.0', 'end')
            mb.showerror(title="Ошибка", message="Поля номера телефона и количества товара заполните цифрами")

        if client_Quantity > DataBase['goods'][index]['quantity']:
            mb.showerror(title="Ошибка", message="Количество товара в заказе не может превышать общее"
                                                 "количество товара в наличии")

        client_Data = {"name": client_Name, "phone": client_Phone, "adress": client_Adress,
                       "good_name": DataBase['goods'][index]['name'],
                       "total_price": DataBase['goods'][index]['unit_price'] * client_Quantity,
                       "quantity": client_Quantity}

        for value in client_Data.values():
            if value == '':
                tkinter.messagebox.showerror(title=None, message='Заполните все поля',)
                break
        else:
            DataBase['goods'][index]['quantity'] -= client_Quantity

            check_Text = 'Чек от заказа {0} на имя {1}(номер телефона: {2}) по адресу {3}' \
                         ' в количестве {4} на общую сумму {5}'.format(client_Data['good_name'],
                                                                       client_Data['name'],
                                                                       client_Data['phone'],
                                                                       client_Data['adress'],
                                                                       client_Data['quantity'],
                                                                       client_Data['total_price'])
            check = open("Check.txt", "w")
            check.write(check_Text)
            check.close()
            window_buy.destroy()



    window_buy = Tk()
    window_buy.title("Оформление заказа")
    window_buy.geometry('750x350')
    window_buy.configure(background='#FF5555')

    Label(window_buy, text='Заказ на "' + DataBase['goods'][index]['name'] + '"',
          font='Inter 19 bold', bg='#A66BFF', ).place(x=270, y=20)

    Label(window_buy, text="ФИО заказчика", font='Inter 15 bold', bg='#A66BFF', ).place(x=20, y=100)
    Label(window_buy, text="Номер телефона", font='Inter 15 bold', bg='#A66BFF', ).place(x=380, y=100)

    text_Client_Name = Text(window_buy, fg='white', font='Inter 15', bg='#594036', width=33, height=1, padx=10, pady=10, )
    text_Client_Name.place(x=20, y=130)

    text_Client_Phone = Text(window_buy, fg='white', font='Inter 15', bg='#594036', width=33, height=1, padx=10,
                              pady=10, )
    text_Client_Phone.place(x=380, y=130)

    Label(window_buy, text="Адрес", font='Inter 15 bold', bg='#A66BFF', ).place(x=20, y=180)
    Label(window_buy, text="Количество товара", font='Inter 15 bold', bg='#A66BFF', ).place(x=380, y=180)

    text_Client_Adress = Text(window_buy, fg='white', font='Inter 15', bg='#594036', width=33, height=1, padx=10,
                               pady=10, )
    text_Client_Adress.place(x=20, y=210)

    text_Client_Quantity = Text(window_buy, fg='white', font='Inter 15', bg='#594036', width=33, height=1, padx=10, pady=10, )
    text_Client_Quantity.place(x=380, y=210)

    btn_Place_Order = Button(window_buy, text="Оформить заказ", fg='white', font='Inter 15', bg='#A66BFF', width=20,
                                 height=2, command=make_Order)
    btn_Place_Order.place(x=260, y=270)

    window_buy.mainloop()