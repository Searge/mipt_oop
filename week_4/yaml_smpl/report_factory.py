import yaml

with open('md.yml', 'r') as md:
    yml_MD = md.read()

with open('html.yml', 'r') as html:
    yml_HTML = html.read()

# теперь ReportFactory - потомок yaml.YAMLObject.
# Сделано для того, чтобы yaml оработчик знал новый тип данных,
# указанный в yaml_tag он будет определён в фабриках - потомках


class ReportFactory(yaml.YAMLObject):
    """
    данные yaml фала - структура отчёта одинакова для всех потомков.
    В связи с этим - получение отчёта из yaml файла - классовый метод
    со специальным именем from_yaml
    """

    @classmethod
    def from_yaml(cls, loader, node):
        # сначала опишем функции для обработки каждого нового типа
        # метод loader.construct_mapping() формирует из содержания node словарь

        def get_report(loader, node):
            # обработчик создания отчёта !report
            data = loader.construct_mapping(node)
            rep = cls.make_report(data["title"])
            rep.filename = data["filename"]
            # на данный момент data["parts"] пуст.
            # Он будет заполнен позже, соответствующим обработчиком,
            # сохраняем на него ссылку, дополнив сразу частями из rep.parts
            data["parts"].extend(rep.parts)
            rep.parts = data["parts"]
            return rep

        def get_chapter(loader, node):
            # обработчик создания части !chapter
            data = loader.construct_mapping(node)
            ch = cls.make_chapter(data["caption"])
            # аналогично предыдущему обработчику
            data["parts"].extend(ch.objects)
            ch.objects = data["parts"]
            return ch

        def get_link(loader, node):
            # обработчик создания ссылки !link
            data = loader.construct_mapping(node)
            lnk = cls.make_link(data["obj"], data["href"])
            return lnk

        def get_img(loader, node):
            # обработчик создания изображения !img
            data = loader.construct_mapping(node)
            img = cls.make_img(data["alt_text"], data["src"])
            return img

        # добавляем обработчики
        loader.add_constructor(u"!report", get_report)
        loader.add_constructor(u"!chapter", get_chapter)
        loader.add_constructor(u"!link", get_link)
        loader.add_constructor(u"!img", get_img)

        # возвращаем результат yaml обработчика - отчёт
        return loader.construct_mapping(node)['report']

    # ниже - без изменений

    @classmethod
    def make_report(cls, title):
        return cls.Report(title)

    @classmethod
    def make_chapter(cls, caption):
        return cls.Chapter(caption)

    @classmethod
    def make_link(cls, obj, href):
        return cls.Link(obj, href)

    @classmethod
    def make_img(cls, alt_text, src):
        return cls.Img(alt_text, src)

# Далее берём непосредственно фабрики по производству элементов отчёта.
# Добавляем соответствие фабрик yaml типу


class MDreportFactory(ReportFactory):
    # указываем соответствие
    yaml_tag = u'!MDreport'

    class Report:
        def __init__(self, title):
            self.parts = []
            self.parts.append("# "+title+"\n\n")

            self.filename = ""

        def add(self, part):
            self.parts.append(part)

        def save(self):
            # вносим изменения - имя файла отчёта указываеться в yaml файле
            try:
                file = open(self.filename, "w", encoding="utf-8")
                print('\n'.join(map(str, self.parts)), file=file)
            finally:
                if isinstance(self.filename, str) and file is not None:
                    file.close()

    class Chapter:
        def __init__(self, caption):
            self.caption = caption
            self.objects = []

        def add(self, obj):
            print(obj)
            self.objects.append(obj)

        def __str__(self):
            return f'## {self.caption}\n\n' + ''.join(map(str, self.objects))

    class Link:
        def __init__(self, obj, href):
            self.obj = obj
            self.href = href

        def __str__(self):
            return f'[{self.obj}]({self.href})'

    class Img:
        def __init__(self, alt_text, src):
            self.alt_text = alt_text
            self.src = src

        def __str__(self):
            return f'![{self.alt_text}]({self.src})'


class HTMLreportFactory(ReportFactory):
    yaml_tag = u'!HTMLreport'

    class Report:
        def __init__(self, title):
            self.title = title
            self.parts = []
            self.parts.append("<html>")
            self.parts.append("<head>")
            self.parts.append("<title>" + title + "</title>")
            self.parts.append("<meta charset=\"utf-8\">")
            self.parts.append("</head>")
            self.parts.append("<body>")

            self.filename = ""

        def add(self, part):
            self.parts.append(part)

        def save(self):
            try:
                file = open(self.filename, "w", encoding="utf-8")
                print('\n'.join(map(str, self.parts)), file=file)
            finally:
                if isinstance(self.filename, str) and file is not None:
                    file.close()

    class Chapter:
        def __init__(self, caption):
            self.caption = caption
            self.objects = []

        def add(self, obj):
            self.objects.append(obj)

        def __str__(self):
            ch = f'<h1>{self.caption}</h1>'
            return ch + ''.join(map(str, self.objects))

    class Link:
        def __init__(self, obj, href):
            self.obj = obj
            self.href = href

        def __str__(self):
            return f'<a href="{self.href}">{self.obj}</a>'

    class Img:
        def __init__(self, alt_text, src):
            self.alt_text = alt_text
            self.src = src

        def __str__(self):
            return f'<img alt = "{self.alt_text}", sr c ="{self.src}"/>'


# Осталось провести загрузку yaml файла и вывести результат
