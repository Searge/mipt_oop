class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


# ИДЕНТИФИКАТОРЫ СОБЫТИЙ
INT, FLOAT, STR = int, float, str


class EventGet:
    def __init__(self, value):
        self.kind = {int: INT, float: FLOAT, str: STR}[value]
        self.value = None


class EventSet:
    def __init__(self, value):
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
            # RETURN for moving on...
            return self.__succesor.handle(obj, event)


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
                return obj.float_field
            else:
                obj.float_field = event.value
        else:
            return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == STR:
            if event.value is None:
                return obj.string_field
            else:
                obj.string_field = event.value
        else:
            return super().handle(obj, event)


if __name__ == "__main__":
    obj = SomeObject()

    obj.integer_field = 42
    obj.float_field = 3.14
    obj.string_field = "some text"

    chain = IntHandler(FloatHandler(StrHandler(NullHandler())))

    print(chain.handle(obj, EventGet(int)))
    print(chain.handle(obj, EventGet(float)))
    print(chain.handle(obj, EventGet(str)))

    chain.handle(obj, EventSet(100))
    print(chain.handle(obj, EventGet(int)))

    chain.handle(obj, EventSet(0.5))
    print(chain.handle(obj, EventGet(float)))

    chain.handle(obj, EventSet('new text'))
    print(chain.handle(obj, EventGet(str)))
