import json

with open("data_file.json", "r") as write_file:
    DataBase = json.load(write_file)

def get_All(data):
    data_return = []

    for item in data['goods']:
        temp = ''
        for key, value in item.items():
            if key == 'name':
                temp += str(value) + ' '
            elif key == 'unit_name':
                temp += str(value) + ' '
            elif key == 'unit_price':
                temp += 'по цене: ' + str(value) + ' р. за штуку '
            elif key == 'quantity':
                temp += 'в количестве: ' + str(value) + '. '
            elif key == 'date_last_delivery':
                temp += 'Последняя дата поставки: ' + str(value)
        data_return.append(temp)
        #print(data_return)

        # for item in data['goods']:
        #     print(item)

    return data_return

def add_New_Good_To_DB(good):
    DataBase['goods'].append(good)
    print(DataBase)

def change_DataBase(index, unit_price, quantity):
    DataBase['goods'][index]['unit_price'] = unit_price
    DataBase['goods'][index]['quantity'] = quantity

def data_Rewrite():
    DB_Json = json.dumps(DataBase)

    with open("data_file.json", "w") as my_file:
        my_file.write(DB_Json)