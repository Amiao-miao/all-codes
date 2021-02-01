class IterableHelper:

    @staticmethod
    def get_count(iterable,func):
        count = 0
        for item in iterable:
            if func(item):
                count += 1
        return count

    @staticmethod
    def get_min(iterable,func):
        min_value = iterable[0]
        for item in range(1,len(iterable)):
            if func(min_value)>iterable[item].money:
                min_value=iterable[item]
        return min_value

    @staticmethod
    def order_by(iterable,func):
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if func(iterable[r]) > func(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]