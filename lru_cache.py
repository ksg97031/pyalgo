from random import randrange


def lru_cache(maxsize=32):
    def decorating_function(user_function):
        return lru_cache_wrapper(user_function, maxsize)

    return decorating_function


def make_key(args, kwargs):
    key = args
    if kwargs:
        for item in kwargs.items():
            key += item

    if len(key) == 1 and type(key[0]) in (int, str, frozenset, type(None)):
        return key[0]
    return hash(key)


class Node:
    def __init__(self, key, result):
        self.previous = None
        self.next = None
        self.key = key
        self.result = result

    def delete(self):
        self.previous = self.next
        self.next = self.previous

    def replace(self, node):
        self.delete()
        self.previous.insert(node)

    def insert(self, node):
        if self.next:
            self.next.previous = node
            node.next = self.next
            node.previous = self
            self.next = node
        else:
            self.next = node
            self.previous = node
            node.next = self
            node.previous = self


def lru_cache_wrapper(user_function, maxsize=32):
    cache = {}
    cache_get = cache.get
    cache_len = cache.__len__
    full = False

    root = None
    if maxsize == 0:

        def wrapper(*args, **kwargs):
            result = user_function(*args, **kwargs)
            return result
    elif maxsize is None:

        def wrapper(*args, **kwargs):
            key = make_key(args, kwargs)
            result = cache_get(key)
            if result is not None:
                return result
            else:
                result = user_function(*args, **kwargs)
                cache[key] = result
                return result
    else:

        def wrapper(*args, **kwargs):
            nonlocal full, root
            key = make_key(args, kwargs)
            node = cache_get(key)
            if node is not None:
                return node.result

            result = user_function(*args, **kwargs)
            new_node = Node(key, result)
            cache[key] = new_node
            if key in cache:
                pass
            elif full:
                oldkey = root.key
                root.replace(new_node)
                root = root.previous
                del cache[oldkey]
            else:
                if root is not None:
                    root = new_node
                else:
                    root.insert(new_node)

                full = len(cache) > maxsize
            return result

    return wrapper


@lru_cache(32)
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n - 1) + F(n - 2)


if __name__ == '__main__':
    print(F(100))
