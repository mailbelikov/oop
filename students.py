class Ocenka:
    def __init__(self, date, ocenka):
        self.date = date
        self.ocenka = ocenka

    def get(self):
        return (self.date, self.ocenka)

    def __str__(self):
        return f'{self.date}, {self.ocenka}'

class Journal:
    def __init__(self):
        self.journal = {'Русский язык': [],
                       'Математика': [],
                       'Физика': [],
                       'Химия': [],
                       'Иностранный язык': [],
                       'Информатика': []}

    def getAll(self):
        return self.journal

    def getJournal(self, jourkey):
        return self.journal[jourkey]

    def addOcenka(self, jourkey, ocen):
        self.journal[jourkey].append(ocen)

class Student:
    def __init__(self, name, soname):
        self.journal = Journal()
        self.name = name
        self.soname = soname

    def getName(self):
        return self.name

    def __str__(self):
        return  f'Студент: {self.name} {self.soname}: {self.journal.getAll()}'

class Group:
    def __init__(self):
        self.group = []

    def addStudent(self, stud):
        self.group.append(stud)

    def delStudent(self, stud):
        self.group.remove(stud)

    def getStudent(self, name):
        for s in self.group:
            if s.getName().upper() == name.upper(): return s

    def addOcenka(self, name, predmet, ocen):
        for s in self.group:
            if s.getName().upper() == name.upper():
                s.journal.addOcenka(predmet, ocen)

    def __str__(self):
        return f'{self.group}'

g = Group()
oc0 = Ocenka('15-05-2023', 4)
oc1 = Ocenka('17-05-2023', 3)
oc2 = Ocenka('20-05-2023', 5)
j0 = 'Математика'
j1 = 'Химия'
s0 = Student('Беликов', 'Андрей')
s0.journal.addOcenka(j0, oc0)
s0.journal.addOcenka(j0, oc1)
s1 = Student('Петров', 'Николай')
s1.journal.addOcenka(j1, oc1)
s2 = Student('Николаев', 'Петр')
s2.journal.addOcenka(j0, oc2)
g.addStudent(s0)
g.addStudent(s1)
g.addStudent(s2)

print(g.getStudent('Беликов'))
print(g.getStudent('Беликов').journal.getJournal(j0))
print(g.getStudent('петров').journal.getJournal(j1))
print(g.getStudent('николаев').journal.getJournal(j0))




