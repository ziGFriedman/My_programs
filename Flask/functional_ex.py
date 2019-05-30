from contextlib import contextmanager

'''Декоратор превращает генератор в контекст менеджер'''
@contextmanager
def do_work(filname):
    f = open(__file__)
    yield f
    f.close()

with do_work(14) as w:
    print(w)
