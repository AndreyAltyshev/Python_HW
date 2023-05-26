import view
def add_dat(data):
    with open("db.txt", "a" ) as file:
        file.write(data)
    print("Телефонная книга обновлена.\n")

def search_name(name):
    with open("db.txt", "r" ) as file:
        data = file.readlines()
        flag = False
        search_dict = dict()
        count = 0
        for i in data:
            if name in i:
                flag = True
                count += 1
                search_dict.update({count: i})
                print(count, ":", i)
        if flag == False:
            print("Абонента по заданным данным не найдено \n")
        return search_dict
                
def sort_db_name():
    with open("db.txt", "r") as file:
        data = file.readlines()
        data.sort()
    with open("db.txt", "w") as file:
        file.writelines(data)

def sort_db_data():
    with open("db.txt", "r") as file:
        data = file.readlines()
        data.sort(key= lambda x: x[4])
    with open("db.txt", "w") as file:
        file.writelines(data)

def print_name():
    with open("db.txt", "r") as file:
        data = file.readlines()
        for i in data:
            print(i.split(";")[0])

def print_db():
    with open("db.txt", "r") as file:
           print(file.read())  

def edit_db(edit_data):
    with open("db.txt", "r") as file:
        search_res = search_name(edit_data)
        if len(list(search_res)) > 1:
            num = int(input("Уточните номер строки требуемого абонента"))
        elif len(list(search_res)) == 1:
            num = 1
        else:
            return
        data = file.readlines()
        for i in range(len(data)):
            if data[i] == search_res[num]:
                data[i] = view.man()
    with open("db.txt", "w" ) as file:
        file.writelines(data)


def remove_abonent(remove_data):
    with open("db.txt", "r") as file:
        search_res = search_name(remove_data)
        if len(list(search_res)) > 1:
            num = int(input("Уточните номер строки требуемого абонента"))
        elif len(list(search_res)) == 1:
            num = 1
        else:
            return
        data = file.readlines()
        for i in range(len(data)):
            if data[i] == search_res[num]:
                data.pop(i)
    with open("db.txt", "w" ) as file:
        file.writelines(data)




                



