from turtle import Turtle, onkey, clear, write, title, ht, pu, Terminator, goto, listen, exitonclick

t1, t2, t3 = [], [], []
n0 = 6  # Количество колец
font0 = ("FreeMono", 18, "bold")


class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n * 1.5, 2)  # square-->rectangle
        self.fillcolor(n / 6., 0, 1 - n / 6.)
        self.st()


class Tower(list):

    def __init__(self, x):
        """create an empty tower. x is x-position of peg"""
        super().__init__()
        self.x = x

    def push(self, d):
        d.setx(self.x)
        d.sety(-150 + 34 * len(self))
        self.append(d)

    def pop(self, **kwargs):
        d = list.pop(self)
        d.sety(150)
        return d


def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n - 1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n - 1, with_, from_, to_)


def play():
    onkey(print, "space")
    clear()
    try:
        hanoi(n0, t1, t2, t3)
        write("Кликните на экран, чтобы выйти!",
              align="center", font=font0)
        title('Мы закончили - Башня собрана!')
    except Terminator:
        pass


def main():
    global t1, t2, t3
    title(f'Ханойская Башня из {n0} колец')
    ht()
    pu()
    goto(0, -225)  # writer turtle
    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)
    # make tower of n0 discs
    for i in range(n0, 0, -1):
        t1.push(Disc(i))
    # prepare user interface
    write("Нажмите Пробел, чтобы начать",
          align="center", font=font0)
    onkey(play, "space")
    listen()


if __name__ == "__main__":
    main()
    exitonclick()
