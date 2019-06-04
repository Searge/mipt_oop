class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


# ИДЕНТИФИКАТОРЫ СОБЫТИЙ
INT, FLOAT, STR = int, float, str


class EventGet:
    def __init__(self, kind, value):
        self.kind = {int: INT, float: FLOAT, str: STR}[value]
        self.value = None


class EventSet:
    def __init__(self, kind, value):
        self.kind = {int: INT, float: FLOAT, str: STR}[type(value)]
        self.value = value


class NullHandler:
    def __init__(self, succesor=None):
        """
        Передаем следующее звено цепочки:
        """
        self.__succesor = succesor

    def handle(self, obj, event):
        if self.__succesor is not None:
            self.__succesor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == INT:
            if event.value is None:
                return obj.integer_field
            else:
                obj.integer_field = event.value
        else:
            return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == FLOAT:
            if event.value is None:
                return obj.integer_field
            else:
                obj.integer_field = event.value
        else:
            return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == STR:
            if event.value is None:
                return obj.integer_field
            else:
                obj.integer_field = event.value
        else:
            return super().handle(obj, event)


if __name__ == "__main__":
    chain = IntHandler(FloatHandler(StrHandler(NullHandler())))
