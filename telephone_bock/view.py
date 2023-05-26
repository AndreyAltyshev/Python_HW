def user_input():
    ask = int(input(" Выбери ниже: \n  1 - записать пользователя \n  2 - поиск по имени \n" 
                    "3 - отсортировать справочник по имени \n  4 - сортировка по дате рождения \n"
                     "5 - вывод только имён абонентов \n "
                      " 6 - вывод справочника \n 7 - изменить контакт \n"
                        " 8 - удалить контакт\n 9 - выход \n"))
    return ask

def man():
    family = input("Введите фамилию: ")
    name = input("Введите имя: ")
    father = input("Введите отчество: ")
    date = input("Введите дату рождения: ")
    telephone = input("Введите номер телефона: ")
    data = family + "; " + name + "; "+ father + "; " + date + "; "  + telephone + "; " + "\n" 
    return data

def search():
    str_search = input("Введите Строку для поиска:")
    return str_search

def edditor():
    edit_data = input("Введите имя абонента которого надо изменить или удалить. ")
    return edit_data
    

