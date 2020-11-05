from random import randrange as rnd, choice
from random import randint
import tkinter as tk
import math
import time

lx = 800
ly = 650
number_of_goals = 3
v0 = 10
lifetime_ball = 50
r_min = 20
r_max = 50
addition = 1
addition_bonus = 2
FPS = 60
g = 9.81


class Ball:
    def __init__(self, x=40, y=450):
        """
        Конструктор класса Ball
        
        Args:
            x - начальное положение мяча по горизонтали
            y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.live = 1
        self.time = lifetime_ball
        self.loser = True
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )

    def set_coords(self):
        """
        Метод сохраняет обновленные координаты мяча на экране
        """
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, ускорения свободного падения,
        и стен по краям окна (размер окна lx х ly).
        """
        self.vy -= g/FPS
        if self.x >= lx - self.r:
            self.vx = -abs(self.vx)
        if self.y >= ly - 50 - self.r:
            self.vy = abs(self.vy)
        if self.x <= self.r:
            self.vx = abs(self.vx)
        if self.y <= self.r:
            self.vy = -abs(self.vy)
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()

    def hittest(self, obj):
        """
        Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        dx = obj.x - self.x
        dy = obj.y - self.y
        dr = obj.r + self.r
        if math.sqrt(dx**2 + dy**2) <= dr:
            self.loser = False
            return True
        else:
            return False

    def timer(self):
        """
        Метод отсчитывает время существования шарика и удаляет шарик спустя заданное в конструкторе время.
        """
        if self.time > 0:
            self.time -= 1
        else:
            canv.delete(self.id)
            self.x = 0
            self.y = 0
            self.r = 0
            self.set_coords()            


class Gun:
    def __init__(self):
        """
        Конструктор класса Gun.
        """
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20,450,50,420,width=7)

    def fire2_start(self, event):
        """
        Метод, запускающий процесс прицеливания.
        """
        self.f2_on = 1

    def fire2_end(self, event):
        """
        Метод, описывающий выстрел мячом.

        Выстрел происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши и времени зажатия ЛКМ.
        """
        global balls, bullet, bullet_sum
        bullet += 1
        bullet_sum += 1
        new_ball = Ball()
        new_ball.r += 5
        if event.x != new_ball.x:
            self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        else:
            self.an = 2*math.atan(1)       
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """
        Метод, описывающий прицеливание.
        направление полета мяча зависит от положения мыши.
        """
        if event and event.x != 20:
            self.an = math.atan((event.y-450) / (event.x-20))
        elif event:
            self.an = 2*math.atan(1)
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        """
        Метод, описывающий увеличение мощности выстрела при удержании ЛКМ.
        """
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target:
    def __init__(self):
        """
        Конструктор класса Target.
        """
        self.x = 0
        self.y = 0
        self.r = 0
        self.color = 'red'
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        self.new_target()
        self.vx = randint(-v0, v0)
        self.vy = randint(-v0, v0)
        
    def new_target(self):
        """
        Инициализация новой цели.
        Появляется в правой нижней части экрана.
        """
        x_1 = self.x = rnd(3*lx/4, lx - r_max)
        y_1 = self.y = rnd(ly/2, ly - r_max)
        r_1 = self.r = rnd(r_min, r_max)
        color = self.color = 'red'
        canv.coords(self.id, x_1-r_1, y_1-r_1, x_1+r_1, y_1+r_1)
        canv.itemconfig(self.id, fill=color)

    def hit(self):
        """
        Метод удаляет цель при попадание шарика в цель.
        """
        canv.coords(self.id, -10, -10, -10, -10)

    def set_coords(self):
        """
        Метод сохраняет обновленные координаты цели на экране.
        """
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )
    
    def move(self):
        """
        Метод описывает перемещение цели за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy и стен по краям окна (размер окна lx х ly).
        """
        if self.x >= lx - self.r:
            self.vx = -abs(self.vx)
        if self.y >= ly - 50 - self.r:
            self.vy = -abs(self.vy)
        if self.x <= self.r:
            self.vx = abs(self.vx)
        if self.y <= self.r:
            self.vy = abs(self.vy)
        self.x += self.vx
        self.y += self.vy
        self.set_coords()


def new_game():
    """
    Это функция, соответствующая одному "раунду" игры, то есть пока не уничтожатся все цели на экране.
    Выход в главное меню при нажатии на кнопку "Back to menu".
    """
    global g1, targets, screen1, balls, bullet, points, finished, miss
    for t in targets:
        t.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)    
    for t in targets:
        t.live = 1
    number_of_live = number_of_goals
    while (number_of_live > 0) and not finished:
        canv.itemconfig(id_points, text=points)
        for b in balls:
            b.move()
            b.timer()
            for t in targets:
                if b.hittest(t) and t.live:
                    t.live = 0
                    t.hit()
                    number_of_live -= 1
            if number_of_live == 0:
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                if bullet <= 2:
                    points += addition_bonus
                else:
                    points += addition
        for t in targets:
            if t.live:
                t.move()
        g1.targetting()
        canv.update()
        time.sleep(1/FPS)
        g1.power_up()
    canv.itemconfig(screen1, text='')
    canv.delete(g1)
    for ball in balls:
        if ball.loser:
            miss += 1
        canv.delete(ball.id)


def end():
    """
    Это функция, завершающая игру для данного игрока, открывает меню.
    Выполняется при нажатии на кнопку button с надписью "Back to menu".
    """
    global finished
    finished = True


def start():
    """
    Функция, закрывающая меню и открывающая окно с игрой.
    Выполняется при нажатии на кнопку b1 с надписью "Start!".
    """
    global started
    started = True
    root_hello.destroy()


def leaving():
    """
    Функция, выполняющая завершение всей программы, то есть это выход из игры.
    Выполняется при нажатии на кнопку b3 с надписью "Exit".
    """
    global worked
    root_hello.destroy()
    worked = False


def best_scores():
    """
    Функция закрывает окно меню и открывает таблицу с 10 лучшими результатами.
    В качестве параметра сортировки берется shooting percentage, то есть доля шариков, попавших в цель.
    Выход в меню при нажатии кнопки "Back to menu"
    """
    root_hello.destroy()
    root_scores = tk.Tk()
    root_scores.geometry('600x600')
    back = tk.Button(text='Back to menu', command=lambda: root_scores.destroy(), width=10, font='28')
    back.grid(row=0, column=0, columnspan=4, pady=5)
    results = []
    with open('Scores.txt') as file:
        for j, line in enumerate(file):
            if j < 10:
                B = line.split()
                name_1 = ' '.join(B[1:-10])
                score_1 = B[-9]
                shots_1 = B[-4]
                perc_1 = B[-1]
                results.append([name_1, score_1, shots_1, perc_1])
    head_name = tk.Label(root_scores, text=' name ', font='28')
    head_name.grid(row=1, column=0)
    head_score = tk.Label(root_scores, text=' score ', font='28')
    head_score.grid(row=1, column=1)
    head_shots = tk.Label(root_scores, text=' number of shots fired ', font='28')
    head_shots.grid(row=1, column=2)
    head_perc = tk.Label(root_scores, text=' shooting percentage ', font='28')
    head_perc.grid(row=1, column=3)
    for i, s in enumerate(results):
        bar_0 = tk.Label(root_scores, text=s[0], font='28')
        bar_0.grid(row=2+i, column=0)
        bar_1 = tk.Label(root_scores, text=s[1], font='28')
        bar_1.grid(row=2+i, column=1)
        bar_2 = tk.Label(root_scores, text=s[2], font='28')
        bar_2.grid(row=2+i, column=2)
        bar_3 = tk.Label(root_scores, text=s[3], font='28')
        bar_3.grid(row=2+i, column=3)
    root_scores.mainloop()


worked = True
while worked:
    started = False
    root_hello = tk.Tk()
    root_hello.title('menu')
    root_hello.geometry('200x200')
    hi = tk.Label(root_hello, text='What is your name?', font='28')
    message = tk.StringVar()
    txt = tk.Entry(root_hello, width=20, font='28', textvariable=message)
    b1 = tk.Button(text='Start!', command=start, width=10, font='28')
    b2 = tk.Button(text='Best scores', command=best_scores, width=10, font='28')
    b3 = tk.Button(text='Exit', command=leaving, width=10, font='28')
    hi.pack()
    txt.pack()
    b1.pack(pady=10)
    b2.pack()
    b3.pack(pady=10)
    root_hello.mainloop()
    if started:
        name = message.get()
        root = tk.Tk()
        root.title('game')
        fr = tk.Frame(root)
        root.geometry(str(lx) + 'x' + str(ly))
        canv = tk.Canvas(root, bg='white')
        canv.pack(fill=tk.BOTH, expand=1)
        button = tk.Button(text='Back to menu', height=2, width=15, command=end)
        button.pack()
        targets = []
        bullet_sum = 0
        for i in range(number_of_goals):
            targets.append(Target())
        screen1 = canv.create_text(400, 300, text='', font='28')
        g1 = Gun()
        bullet = 0
        balls = []
        points = 0
        miss = 0
        id_points = canv.create_text(30, 30, text=points, font='28')
        finished = False
        while not finished:
            root.after(750, new_game())
        root.destroy()
        with open("Scores.txt", "a") as file:
            result = 'name: ' + name
            result += '  score: ' + str(points)
            result += '   number of shots fired: ' + str(bullet_sum)
            if bullet_sum != 0:
                percentage = "%.1f" % (100 - 100*miss/bullet_sum)
            else:
                percentage = "%.1f" % (0)
            result += '   shooting percentage: ' + str(percentage) + '\n'
            file.write(result)
        root.mainloop()
        percents = []
        inp = open('Scores.txt', 'r')
        if inp.read() != '':
            with open('Scores.txt') as file:
                for j, line in enumerate(file):
                    *A, x = line.split()
                    ost = line[:-len(x)-1]
                    percents.append((j, ost, float(x)))
            percents = sorted(percents, key=lambda i: -i[2])
            with open("Scores.txt", "w") as file:
                for i in percents:
                    file.write(i[1] + str(i[2]) + '\n')
