class File:
    def __init__(self, text):
        self.text = text

    def __enter__(self):
        # Код, который должен быть выполнен до блока
        return f'{self.text} и __enter__'

    def __exit__(self, exc_type, exc_value, traceback):
        # Код, который должен быть выполнен после блока
        pass

sample = File('ваш текст')
with sample as method_enter:
    print(method_enter)  # ваш текст и __enter__

with File('ваш текст') as method_enter:
    print(method_enter)  # ваш текст и __enter__ Без экземпляра, на самом классе

class File:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r+', encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with File('example.txt') as f:
    for line in f:
        print(line)