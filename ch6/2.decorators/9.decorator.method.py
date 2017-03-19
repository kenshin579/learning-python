def p_decorate(func):
    def func_wrapper(self):
        return "<p>{0}</p>".format(func(self))

    return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate #note: 클래스안에서의 method도 가능함
    def get_fullname(self):
        return self.name + " " + self.family

my_person = Person()
print(my_person.get_fullname())
