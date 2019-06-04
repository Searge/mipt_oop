# Реализовать Chain of Responsibility

Вам дан объект класса SomeObject, содержащего три поля: `integer_field`, `float_field` и `string_field`:

```python
class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""
```

Необходимо реализовать:

- `EventGet(<type>)` создаёт событие получения данных соответствующего типа
- `EventSet(<value>)` создаёт событие изменения поля типа `type(<value>)`

Необходимо реализовать классы `NullHandler`, `IntHandler`, `FloatHandler`, `StrHandler` так, чтобы можно было создать цепочку:

```python
chain = IntHandler(FloatHandler(StrHandler(NullHandler())))
```

- `Chain.handle(obj, EventGet(int))` — вернуть значение `obj.integer_field`
- `Chain.handle(obj, EventGet(str))` — вернуть значение `obj.string_field`
- `Chain.handle(obj, EventGet(float))` — вернуть значение `obj.float_field`
- `Chain.handle(obj, EventSet(1))` — установить значение `obj.integer_field =1`
- `Chain.handle(obj, EventSet(1.1))` — установить значение `obj.float_field = 1.1`
- `Chain.handle(obj, EventSet("str"))` — установить значение `obj.string_field = "str"`

Пример работы:

```python
>>> obj = SomeObject()
>>> obj.integer_field = 42
>>> obj.float_field = 3.14
>>> obj.string_field = "some text"
>>> chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
>>> chain.handle(obj, EventGet(int))
42
>>> chain.handle(obj, EventGet(float))
3.14
>>> chain.handle(obj, EventGet(str))
'some text'
>>> chain.handle(obj, EventSet(100))
>>> chain.handle(obj, EventGet(int))
100
>>> chain.handle(obj, EventSet(0.5))
>>> chain.handle(obj, EventGet(float))
0.5
>>> chain.handle(obj, EventSet('new text'))
>>> chain.handle(obj, EventGet(str))
'new text'
```