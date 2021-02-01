class IterableHelper:

    @staticmethod
    def find_single(iterable,func):
        for item in iterable:
            if func(item):
                return item

    @staticmethod
    def select(iterable,func):
        for item in iterable:
            yield func(item)