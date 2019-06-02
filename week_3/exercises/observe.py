from abc import ABC, abstractmethod


class Engine:
    def __init__(self):
        self.subscribers = set()


class ObservableEngine(Engine):

    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        # Объявим множество всех полученных достижений
        self.achievements = set()

    def update(self, message):
        # Добавим название достижения во множество достижений
        self.achievements.add(message["title"])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = []

    def update(self, message):
        if message not in self.achievements:
            self.achievements.append(message)


if __name__ == "__main__":
    observable = ObservableEngine()
    short_printer = ShortNotificationPrinter()
    full_printer = FullNotificationPrinter()

    observable.subscribe(short_printer)
    observable.subscribe(short_printer)
    observable.subscribe(full_printer)

    observable.notify({"title": "Покоритель",
                       "text": "Дается при выполнении всех заданий в игре"})
    observable.notify({"title": "Победитель",
                       "text": "Дается при выполнении заданий в игре"})
    observable.notify({"title": "Покоритель",
                       "text": "Дается при выполнении всех заданий в игре"})
    observable.notify({"title": "Вин",
                       "text": "Дается в игре"})

    print(short_printer.achievements)
    print(full_printer.achievements)
