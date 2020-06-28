class Comment:  # класс-заглушка чтобы в Post можно было использовать тип Comment
    pass


class Post:

    import uuid

    __author: str = None
    __title: str = None
    __data: str = None
    __UUID: uuid = None
    __comments: list = None

    def __init__(self, *args):
        import uuid
        try:  # безопасное извлечение аргументов конструктора
            self.__author, self.__title, self.__data = args[0], args[1], args[2]
        except IndexError:
            print("Post init error: 3 arguments expected: author, title, data")
            return
        self.__UUID = uuid.uuid4()

    def set_author(self, author: str):
        self.__author = author

    def set_title(self, title: str):
        self.__title = title

    def set_data(self, data: str):
        self.__data = data

    def get_author(self):
        return self.__author

    def get_title(self):
        return self.__title

    def get_data(self):
        return self.__data

    def get_uuid(self):
        return self.__UUID

    def get_comments(self):
        return self.__comments

    def has_comments(self):
        return True if self.__comments is not None else False

    def add_comment(self, comment: Comment):
        if self.__comments is None:
            self.__comments = []

        self.__comments.append(comment)
        comment.set_parent(self)

    def report(self):
        """
        создает файл-отчет с указанием текущей даты и времени
        :return:
        """
        import datetime
        with open("./text_" + "{0:%Y-%m-%d_%H-%M-%S}.txt".format(datetime.datetime.now()), "a") as file:
            file.write(self.to_string())

    def to_string(self, spaces=0):
        """
        рекурсивная функция преобразования объекта класса Post и его наследников к строке
        :param spaces: количество отступов
        :return: возвращает объект, преобразованный к строке
        """
        text = (spaces * "\t") + f"Author: {self.__author}\n"
        text += (spaces * "\t") + f"Title: {self.__title}\n"
        text += (spaces * "\t") + f"Data: {self.__data}\n"
        text += (spaces * "\t") + f"UUID: {self.__UUID}\n"
        text += (spaces * "\t") + f"Comments({len(self.get_comments()) if self.has_comments() else 0}):\n\n"
        if self.has_comments():
            for comment in self.__comments:
                text += comment.to_string(spaces=spaces + 1)
                text += "\n"

        return text


class Comment(Post):

    __parent: Post = None  # родительский Post или Comment

    def __init__(self, *args):
        super().__init__(*args)

    def set_parent(self, parent: Post):
        self.__parent = parent

    def get_parent(self):
        return self.__parent

    def add_comment(self, comment: Comment):
        if comment is self:
            return
        if self.has_comments() and comment in self.get_comments():
            return
        super().add_comment(comment)

    def to_string(self, spaces=0):
        """
        переопределение родительского метода с целью включения в текст пункта Parent
        :param spaces:
        :return:
        """
        text = (spaces * "\t") + f"Parent: {self.get_parent().get_uuid()}\n"
        text += super().to_string(spaces)  # вызов родительского метода
        return text
