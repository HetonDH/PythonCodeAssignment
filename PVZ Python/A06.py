import pygame
import random
import pygame.freetype
import time


class Plant:
    def __init__(self, img, rows, cols, cell_size, max_health, attack):
        self.max_health = max_health
        self.attack_num = attack
        self.health = self.max_health
        self.pos = (rows, cols)
        self.image = img
        self.rect = img.get_rect()
        self.cell_size = cell_size
        y = rows * cell_size + 30
        x = cols * cell_size + 120
        self.rect.topleft = (y, x)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        blood = self.rect.left, self.rect.top - 10, self.cell_size * self.health / self.max_health, 8
        border = self.rect.left, self.rect.top - 10, self.cell_size, 8
        pygame.draw.rect(screen, (0, 255, 0), blood, 0)
        pygame.draw.rect(screen, (0, 0, 0), border, 1)

class Cake(Plant):
    max_health = 8
    price = 2
    attack = 2

    def __init__(self, image, rows, cols, cell_size):
        super().__init__(image, rows, cols, cell_size, self.max_health, self.attack)


class Candy(Plant):
    max_health = 5
    price = 3
    attack = 10

    def __init__(self, image, rows, cols, cell_size):
        super().__init__(image, rows, cols, cell_size, self.max_health, self.attack)


class Walnut(Plant):
    max_health = 15
    price = 4
    attack = 2

    def __init__(self, image, rows, cols, cell_size):
        super().__init__(image, rows, cols, cell_size, self.max_health, self.attack)


class Zombie:
    def __init__(self, img, x, rows, cell_size, max_health, attack_num, speed):
        self.health = max_health
        self.max_health = max_health
        self.attack_num = attack_num
        self.image = img
        self.cell_size = cell_size
        self.rect = img.get_rect()
        y = random.randrange(0, rows) * cell_size + 120
        self.rect.topleft = (x, y)
        # print(self.rect.topleft)
        self.attack = False
        self.speed = speed

    def attack_plant(self, food):
        self.attack = False
        for n in food:
            if n.rect.top == self.rect.top and n.rect.left + self.cell_size >= self.rect.left > n.rect.left and n.health > 0:
                self.attack = True
                n.health = n.health - self.attack_num
                self.health = self.health - n.attack_num

    def move(self):
        # print(self.attack)
        if not self.attack and self.rect.left >= 0:
            self.rect.move_ip(-self.speed, 0)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        blood = self.rect.left, self.rect.top - 10, self.cell_size * self.health / self.max_health, 8
        border = self.rect.left, self.rect.top - 10, self.cell_size, 8
        pygame.draw.rect(screen, (0, 255, 0), blood, 0)
        pygame.draw.rect(screen, (0, 0, 0), border, 1)


class Mice(Zombie):
    attack_num = 1
    max_health = 3
    speed = 1

    def __init__(self, image, x, row, cell_size):
        super().__init__(image, x, row, cell_size, self.attack_num, self.max_health, self.speed)


class Dog(Zombie):
    attack_num = 2
    max_health = 5
    speed = 1

    def __init__(self, image, x, row, cell_size):
        super().__init__(image, x, row, cell_size, self.attack_num, self.max_health, self.speed)


class Tiger(Zombie):
    attack_num = 8
    max_health = 8
    speed = 1

    def __init__(self, image, x, row, cell_size):
        super().__init__(image, x, row, cell_size, self.attack_num, self.max_health, self.speed)


def main():
    pygame.init()
    width = 1200
    height = 750
    cell_size = 60
    row_total = 18
    col_total = 10

    account = 10

    pygame.font.init()
    smallfont = pygame.font.SysFont('Comic Sans MS', 20)
    largefont = pygame.font.SysFont('Comic Sans MS', 30)
    hugefont = pygame.font.SysFont('Comic Sans MS', 50)
    screen = pygame.display.set_mode((width, height))

    walnut = pygame.image.load("walnut.png").convert_alpha()
    candy = pygame.image.load("candy.png").convert_alpha()
    cake = pygame.image.load("cake.png").convert_alpha()
    mice = pygame.image.load("mice.png").convert_alpha()
    dog = pygame.image.load("dog.png").convert_alpha()
    tiger = pygame.image.load("tiger.png").convert_alpha()

    walnut = pygame.transform.scale(walnut, (cell_size, cell_size))
    candy = pygame.transform.scale(candy, (cell_size, cell_size))
    cake = pygame.transform.scale(cake, (cell_size, cell_size))
    mice = pygame.transform.scale(mice, (cell_size, cell_size))
    dog = pygame.transform.scale(dog, (cell_size, cell_size))
    tiger = pygame.transform.scale(tiger, (cell_size, cell_size))

    food_name = ['walnut', 'candy', 'cake']
    food_imgs = [walnut, candy, cake]
    foods = {'walnut': {
        'img': walnut,
        'price': 4
    },
        'candy': {
            'img': candy,
            'price': 3
        },
        'cake': {
            'img': cake,
            'price': 2
        }}

    money = pygame.image.load("money.png").convert_alpha()
    smon = pygame.transform.scale(money, (cell_size // 2, cell_size // 2))

    white = (255, 255, 255)
    clock = pygame.time.Clock()

    play_food = []
    animals = []
    occu_pos = []

    is_chosen = False
    chose = -1
    over = False
    while not over:
        account += 0.002
        clock.tick(600)

        screen.fill(white)
        for i in range(len(foods)):
            screen.blit(food_imgs[i], (30 + i * 70, 10))
            text = smallfont.render(str(foods[food_name[i]]['price']), False, (0, 0, 0))
            screen.blit(smon, (38 + i * 70, 75))
            screen.blit(text, (72 + i * 70, 75))

        mon = pygame.transform.scale(money, (cell_size, cell_size))
        screen.blit(mon, (920, 20))
        acc_text = largefont.render(str(int(account)), False, (0, 0, 0))
        screen.blit(acc_text, (990, 25))

        pos = pygame.mouse.get_pos()

        color = 0, 0, 0
        width = 1
        for i in range(0, col_total + 1):
            pygame.draw.line(screen, color, (30, 120 + i * cell_size), (1050, 120 + i * cell_size), width)
        for i in range(0, row_total):
            pygame.draw.line(screen, color, (30 + i * cell_size, 120), (30 + i * cell_size, 900), width)

        for p in play_food:
            if p.health > 0:
                # p.attack_animal(animals)
                p.draw(screen)
            else:
                occu_pos.remove(p.pos)
                play_food.remove(p)

        rand = random.randint(0, 10000)

        if 4990 <= rand <= 4998:
            ani = Mice(mice, 1050, col_total, cell_size)
            animals.append(ani)
            ani.draw(screen)
        elif 4985 <= rand <= 4989:
            ani = Dog(dog, 1050, col_total, cell_size)
            animals.append(ani)
            ani.draw(screen)
        elif 4999 <= rand <= 5000:
            ani = Tiger(tiger, 1050, col_total, cell_size)
            animals.append(ani)
            ani.draw(screen)

        for ani in animals:
            # print(mouse.rect.topleft)
            if ani.rect.left >= 30 and ani.health > 0:
                ani.attack_plant(play_food)
                ani.move()
                ani.draw(screen)
            elif ani.health <= 0:
                animals.remove(ani)
            elif ani.rect.left < 30:
                # pygame.quit()
                over = True

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not is_chosen and pos[1] <= 70:
                    if 10 <= pos[0] <= 70:
                        chose = 0
                    elif 80 <= pos[0] <= 140:
                        chose = 1
                    elif 150 <= pos[0] <= 210:
                        chose = 2
                    if chose >= 0:
                        is_chosen = True
                elif is_chosen:
                    chose_pos = pos
                    screen.blit(food_imgs[chose], chose_pos)
                    is_chosen = False
                    row_num = (pos[0] - 30) // cell_size
                    col_num = (pos[1] - 120) // cell_size

                    if 990 >= pos[0] >= 30 and 840 >= pos[1] >= 120 and account >= foods[food_name[chose]]['price']\
                            and (row_num, col_num) not in occu_pos:
                        account -= foods[food_name[chose]]['price']
                        if chose == 0:
                            c = Walnut(walnut, row_num, col_num, cell_size)
                        if chose == 1:
                            c = Candy(candy, row_num, col_num, cell_size)
                        if chose == 2:
                            c = Cake(cake, row_num, col_num, cell_size)
                        play_food.append(c)
                        occu_pos.append((row_num, col_num))
        if is_chosen:
            screen.blit(food_imgs[chose], pos)

        pygame.display.update()

        pygame.time.delay(10)

    pygame.time.delay(10)
    screen.fill(white)

    over = hugefont.render('Game Over!', False, (0, 0, 0))
    screen.blit(over, (400, 300))
    pygame.display.update()


if __name__ == '__main__':
    main()
