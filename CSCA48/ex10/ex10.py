from container import *


def banana_game(s1, s2, c):
    if c.is_empty():
        if len(s1) > len(s2):
            return False
        elif s1 == '' and s2 == '':
            return True
        elif s1 == '' or s2 == '':
            return False
        elif s1[0] == s2[0]:
            c1 = c.copy()
            move = banana_game(s1[1:], s2[1:], c)
            c1.put(s1[0])
            put = banana_game(s1[1:], s2, c1)
            return move or put
        else:
            c.put(s1[0])
            return banana_game(s1[1:], s2, c)
    else:
        if len(s1) == 0:
            if len(s2) == 0:
                while not c.is_empty():
                    c.get()
                return True
            elif c.peek() == s2[0]:
                c.get()
                return banana_game(s1, s2[1:], c)
            else:
                while not c.is_empty():
                    c.get()
                return False
        elif len(s2) == 0:
            while not c.is_empty():
                c.get()
            return False
        else:
            if s1[0] == s2[0]:
                c1 = c.copy()
                c2 = c.copy()
                get = False
                move = banana_game(s1[1:], s2[1:], c)
                try:
                    c1.put(s1[0])
                    put = banana_game(s1[1:], s2, c1)
                except:
                    while not c.is_empty():
                        c.get()
                    put = False
                if c2.peek() == s2[0]:
                    c2.get()
                    get = banana_game(s1, s2[1:], c2)
                return move or put or get
            else:
                if c.peek() != s2[0]:
                    try:
                        c.put(s1[0])
                        return banana_game(s1[1:], s2, c)
                    except:
                        while not c.is_empty():
                            c.get()
                        return False
                else:
                    c1 = c.copy()
                    c.get()
                    get = banana_game(s1, s2[1:], c)
                    try:
                        c1.put(s1[0])
                        put = banana_game(s1[1:], s2, c1)
                    except:
                        while not c.is_empty():
                            c.get()
                        put = False
                    return get or put
