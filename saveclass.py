import pickle

class User:
    def __init__(self, name, password):
        self.username = name
        self.userpass = password

    def getname(self):
        return self.username

    def edit(self, name, password):
        self.username = name
        self.userpass = password

    def __str__(self):
        return f'User: {self.username}, Password: {self.userpass}'

Users = []
menustr = 'Сделайте выбор (a - добавить; d - удалить; e - изменить;l - просмотр; s - сохранить: q - выход) ===>'
menu = set('adelqs')

def adduser():
    uname = input('Имя: ')
    upass = input('Пароль: ')
    user = User(uname, upass)
    Users.append(user)
    Users.sort(key=lambda x: x.getname())

def deluser():
    uname = input('Имя: ')
    for user in Users:
        if user.getname() == uname:
            Users.remove(user)

def edituser():
    uname = input('Имя: ')
    for user in Users:
        if user.getname() == uname:
            uname = input('Имя: ')
            upass = input('Пароль: ')
            user.edit(uname, upass)
            break

def listuser():
    for user in Users: print(user)

def saveuser(var1):
    with open('saveclass.ini', 'wb') as cf:
        pickle.dump(var1, cf)
    print('Save users ...')

def loaduser():
    with open('saveclass.ini', 'rb') as cf:
        var1 = pickle.load(cf)
        return var1

Users = loaduser()

while True:
    m = input(menustr)
    if not m in menu:
        print("Недопустимый выбор ...")
        continue
    if m == 'a':
        adduser()
    elif m == 'd':
        deluser()
    elif m == 'e':
        edituser()
    elif m == 'l':
        listuser()
    elif m == 'q':
        break
    elif m == 's':
        saveuser(Users)




