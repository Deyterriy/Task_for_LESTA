""" реализация с использованим встроенного модуля collections.deque"""

from collections import deque


class FIFO_1:
    def __init__(self, max_size):
        self.buffer = deque(max_size=max_size)

    def push(self, item):
        self.buffer.append(item)

    def pop(self):
        return self.buffer.popleft()

    def __len__(self):
        return len(self.buffer)


# Плюсы данного варианта: эффективная реализация, благодаря встроенному модулю
# лаконично, просто и понятно
# Минусы: модуль collections.deque не позволяет явно указывать размер буфера
# снижение эффективности для тяжелых(больших) буфферов.


class FIFO_2:
    """Реализация буфера с использованием массива с началом и концом."""

    def __init__(self, max_size):
        self.buffer = [None] * max_size
        self.head = 0
        self.tail = 0

    def push(self, item):
        self.buffer[self.head] = item
        self.head = (self.head + 1) % len(self.buffer)
        if self.head == self.tail:
            self.tail = (self.tail + 1) % len(self.buffer)

    def pop(self):
        if self.head == self.tail:
            return None
        item = self.buffer[self.tail]
        self.tail = (self.tail + 1) % len(self.buffer)
        return item

    def __len__(self):
        return (self.head - self.tail) % len(self.buffer)


# Плюсы: Можно явно указать начальный размер буфера
# В следсвие этого данная реализация очень эффективна для тяжелых буферов
# Минусы: Более сложная реализация, особенно в сравнении с первой
# Нужно ослеживать начало и конец буфера.
