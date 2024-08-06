import random
"""lambda func"""
first = 'Мама мыла раму'
second = 'Рамена мало было'
func = lambda x, y: x == y
numbers = [35, 2, 3]
numbers_2 = [3, 4, 6]
result = map(func, first, second)
print(list(result))

"""Замыкание"""
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for i in data_set:
                file.write(str(i) + '\n')
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

"""Метод __call__:"""
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())