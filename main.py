import click


class todo():
    def __init__(self):
        self.file = open("todo.txt", "r")
        self.todo_list = self.file.read().splitlines()
        self.file.close()

    def add(self, s):
        self.todo_list.append(s)
        self.write_file()

    def rm(self, s):
        try:
            self.todo_list.remove(s)
            self.write_file()
        except ValueError:
            print("selected todo not in list, Try again")

    def list(self):
        for i in self.todo_list:
            print(i)

    def write_file(self):
        self.file = open("todo.txt", "w")
        self.file.write("\n".join(self.todo_list))
        self.file.close()


@click.group()
def grp():
    pass


@grp.command()
@click.argument("s", default="")
def add(s):
    a = todo()
    if s != "":
        a.add(s)
    else:
        s = input("please type the task you want to add :")
        a.add(s)


@grp.command()
@click.argument("s", default="")
def rm(s):
    a = todo()
    if s != "":
        a.rm(s)
    else:
        a.list()
        s = input("please type the task you want to remove(select from above list :")
        a.rm(s)


@grp.command()
def list():
    a = todo()
    a.list()


