# |Задание на выбор или дополнительное про классы (тема 10ого семинара)|
# Напишите класс Dragon (Дракон), экземпляр которого при инициализации принимaет аргументы:
# рост, огнеопасность, цвет.
# Класс обеспечивает выполнение методов (dr — экземпляр класса)
# экземпляры можно сравнивать: сначала по росту. затем по огнеопасности, затем по цвету по алфавиту
# экземпляры класса можно складывать: dr2 =dr + dr1. при этом возвращается новый экземпляр со значениями атрибутов:
# цвет меньший по алфавиту;
# рост - среднее арифметическое из двух округлённое до целого вниз,
# огнеопасность - большее из двух;
# из экземпляра класса можно вычесть число: dr -= number, из роста вычитается целая честь от деления роста на число, к
# огнеопасности прибавляется остаток от деления огнеопасности на число;
# Экземпляр можно вызвать с аргументом-строкой - возвращается строка-аргумент, повторенная количество раз, равное
# значению атрибута огнеопасность;
# change_color() - вызывается c аргументом - цветом, на который нужно поменять имеющийся цвет
# str- возвращает строку:
# Dragon with height «рост», danger <огнеопасность> and color «цвет».
# repr- возвращaет строку:
# Dragon(‹рост>, <огнеопасность>, <цвет>)

class Dragon:
    def __init__(self, height, danger, color):
        self.height = height
        self.danger = danger
        self.color = color

    def str(self):
        return f"Dragon with height {self.height}, danger {self.danger} and color {self.color}."

    @classmethod
    def Type_checking(self, other):
        if not isinstance(other, (int, Dragon)):
            raise ArithmeticError("правый операнд должен быть int или Dragon")
        return other

    def __eq__(self, other):
        temp = self.Type_checking(other)
        if self.height == temp.height:
            if self.danger == temp.danger:
                if self.color == temp.color:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        temp = self.Type_checking(other)
        if self.height < temp.height:
            if self.danger < temp.danger:
                if self.color < temp.color:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __le__(self, other):
        temp = self.Type_checking(other)
        if self.height <= temp.height:
            if self.danger <= temp.danger:
                if self.color <= temp.color:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __add__(self, other):
        temp = self.Type_checking(other)
        if type(temp) == Dragon:
            heig = (self.height + other.height)//2
            dang = max([self.danger, other.danger])
            col = min([self.color, other.color])
            return Dragon(heig, dang, col)
        else:
            return Dragon(self.height + other, self.danger, self.color)

    def __sub__(self, other):

        if type(other) == int:
            heig = self.height - self.height // other
            dang = self.danger + self.danger % other
            return Dragon(heig, dang, self.color)
        else:
            return print("правый операнд должен быть int ")

    def change_color(self, color):
        self.color = color
    
    def __repr__(self, text):
        for i in range(self.danger):
            print(text, end=" ")


dr = Dragon(69, 5, "brown")
dr1 = Dragon(69, 5, "gray")
print(dr > dr1, dr != dr1, dr <= dr1)
print(dr.str(), dr1.str(), sep="\n")
print()

dr.change_color("white")
dr -= 23
dr1 -= 2
dr2 = dr+dr1
print(dr.str(), dr1.str(), dr2.str(), sep="\n")
dr.__repr__("Welcome")
