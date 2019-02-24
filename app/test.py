class QiYue:
    name = 'qiyue'
    age = 18

    def __init__(self):
        self.gender = 'male'

    def keys(self):
        return ('name', 'age', 'gender')

    def __getitem__(self, item):
        return getattr(self, item)


o = QiYue()
print(dict(o), o.__dict__)
# print(o['name'])
# print(o['age'])

# print(QiYue().__dict__)
# dict
