import pygame, random
pygame.init()
pygame.font.init()

"""This is a about our dog Ficsi who hates Lemons and therefore needs to dodge them. All drawings
    of Ficsi were made by my sister so this is our joint project :D"""

x = 700
y = 400
win = pygame.display.set_mode((x, y))
run = True
clock = pygame.time.Clock()
bgrect = pygame.Rect(20, 20, x - 40, y - 40)
runFicsiImg = [pygame.image.load("FicsiRun/Ficsirun1"), pygame.image.load("FicsiRun/Ficsirun2"),
               pygame.image.load("FicsiRun/Ficsirun3"), pygame.image.load("FicsiRun/Ficsirun4"),
               pygame.image.load("FicsiRun/Ficsirun5"), pygame.image.load("FicsiRun/Ficsirun6"),
               pygame.image.load("FicsiRun/Ficsirun7"), pygame.image.load("FicsiRun/Ficsirun8"),
               pygame.image.load("FicsiRun/Ficsirun9"), pygame.image.load("FicsiRun/Ficsirun10"),
               pygame.image.load("FicsiRun/Ficsirun11"), pygame.image.load("FicsiRun/Ficsirun12")]
jumpFicsiImg = [pygame.image.load("FicsiJump/FicsiJump1"),
                pygame.image.load("FicsiJump/FicsiJump3"), pygame.image.load("FicsiJump/FicsiJump4"),
                pygame.image.load("FicsiJump/FicsiJump5"), pygame.image.load("FicsiJump/FicsiJump6"),
                pygame.image.load("FicsiJump/FicsiJump7"), pygame.image.load("FicsiJump/FicsiJump9")]
duckFicsiImg = []
bgs = [pygame.image.load("Bgs/bg1"), pygame.image.load("Bgs/bg2"), pygame.image.load("Bgs/bg3"),
       pygame.image.load("Bgs/bg14"), pygame.image.load("Bgs/bg5"), pygame.image.load("Bgs/bg6"),
       pygame.image.load("Bgs/bg17"), pygame.image.load("Bgs/bg8"), pygame.image.load("Bgs/bg9"),
       pygame.image.load("Bgs/bg10"), pygame.image.load("Bgs/bg11"), pygame.image.load("Bgs/bg12"),
       pygame.image.load("Bgs/bg13"), pygame.image.load("Bgs/bg14"), pygame.image.load("Bgs/bg15"),
       pygame.image.load("Bgs/bg16"), pygame.image.load("Bgs/bg17"), pygame.image.load("Bgs/bg18"),
       pygame.image.load("Bgs/bg19"), pygame.image.load("Bgs/bg20")]
sky = [pygame.image.load("Bgs/sky1"), pygame.image.load("Bgs/sky2"), pygame.image.load("Bgs/sky3"),
       pygame.image.load("Bgs/sky4"), pygame.image.load("Bgs/sky5"), pygame.image.load("Bgs/sky6"),
       pygame.image.load("Bgs/sky7"), pygame.image.load("Bgs/sky8"), pygame.image.load("Bgs/sky9"),
       pygame.image.load("Bgs/sky10"), pygame.image.load("Bgs/sky11"), pygame.image.load("Bgs/sky12"),
       pygame.image.load("Bgs/sky13"), pygame.image.load("Bgs/sky14"), pygame.image.load("Bgs/sky15"),
       pygame.image.load("Bgs/sky16"), pygame.image.load("Bgs/sky17"), pygame.image.load("Bgs/sky18"),
       pygame.image.load("Bgs/sky19"), pygame.image.load("Bgs/sky20")]
lemonimg = pygame.image.load("lemon")
isJump = False
isDuck = False
lost = False
jumpCount = 10
Frame = 0
jumpFrame = 0
difficulty = 10
difficulty2 = 60
bg = pygame.Rect(0, 0, x, y)
skyrect = pygame.Rect(0, 0, x, y)
bgnum = 0
skynum = 0


def foo(Frame, frequency, lst, num):
    if yn(Frame, frequency):
        num += 1
    if num > len(lst)-1:
        num = 0
    return num


def yn(a, c):
    # decide if something, whether float or int is the same number
    b = a // c
    bb = a / c
    if b - bb == 0:
        return True
    else:
        return False


class Ficsi:
    def __init__(self, a):
        self.W = a
        self.H, self.H2 = a, a
        self.halfH = self.H // 2
        self.x = x // 4
        self.y, self.y2 = y // 2, y // 2
        self.duckH = self.y2 + self.halfH
        self.rectangle = pygame.Rect(self.x, self.y, self.W, self.H)
        self.num = 0
        self.jnum = 0

    def draw(self):
        global jumpFrame
        if isJump:
            self.jnum = foo(jumpFrame, 4, jumpFicsiImg, self.jnum)
            print("JUMPED!   dog Nr. ", self.jnum)
            win.blit(jumpFicsiImg[self.jnum], self.rectangle)
            jumpFrame += 1
        elif isDuck:
            pygame.draw.rect(win, (0, 255, 0), self.rectangle)
            jumpFrame = 0
            self.jnum = 0
        else:
            self.num = foo(Frame, 1, runFicsiImg, self.num)
            win.blit(runFicsiImg[self.num], self.rectangle)
            jumpFrame = 0
            self.jnum = 0

    def update(self):
        self.rectangle = pygame.Rect(self.x, self.y, self.W, self.H)

    def move(self):
        global isJump, jumpCount, isDuck
        keys = pygame.key.get_pressed()
        # JUMPING
        if keys[pygame.K_SPACE]:
            isJump = True
        if isJump:
            if yn(Frame, 1):
                if jumpCount >= -10:
                    neg = 1
                    if jumpCount < 0:
                        neg = -1
                    self.y -= (jumpCount ** 2) * 0.35 * neg
                    jumpCount -= 1
                else:
                    isJump = False
                    jumpCount = 10
        # DUCKING
        elif keys[pygame.K_s]:
            isDuck = True
        elif not keys[pygame.K_s]:
            isDuck = False
            self.H = self.H2
            self.y = self.y2
        if isDuck:
            self.H = self.halfH
            self.y = self.duckH


class Lemon:
    def __init__(self, grounded):
        self.W = 50
        self.H = 50
        self.x = x
        if grounded == 1:
            self.y = (y // 2) + 50
        elif grounded == 2:
            self.y = y // 2
        elif grounded == 3:
            self.y = (y // 2) - random.randint(50, 100)
        self.rectangle = pygame.Rect(self.x, self.y, self.W, self.H)

    def update(self):
        self.rectangle = pygame.Rect(self.x, self.y, self.W, self.H)

    def move(self):
        self.x -= difficulty

    def draw(self):
        global lemonimg
        win.blit(lemonimg, self.rectangle)


Lemons = [Lemon(random.randint(1, 3))]
ficsi = Ficsi(100)


def redrawWin():
    global Frame, run, lost, difficulty, difficulty2, bgnum, skynum
    win.fill((255, 255, 255))
    if not lost:
        skynum = foo(Frame, 6, sky, skynum)
        bgnum = foo(Frame, 2, bgs, bgnum)
        win.blit(sky[skynum], skyrect)
        win.blit(bgs[bgnum], bg)
        for lemon in Lemons:
            lemon.move()
            lemon.update()
            lemon.draw()
            if ficsi.rectangle.colliderect(lemon.rectangle):
                lost = True
        ficsi.move()
        ficsi.update()
        ficsi.draw()
        print("displaying running dog Nr. ", ficsi.num)
        print("displaying jumping dog Nr. ", ficsi.jnum)
        pygame.display.update()
        Frame += 1
        if yn(Frame, difficulty2):
            Lemons.append(Lemon(random.randint(1, 3)))
        if yn(Frame, 40):
            difficulty += 1
        if yn(Frame, 60) and difficulty2 >= 25:
            difficulty2 -= 5
            print(difficulty2)
    if lost:
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Score: "+str(Frame//10), True, (255, 255, 0))
        textRect = text.get_rect()
        textRect.center = (x // 2, y // 2)
        win.blit(sky[skynum], skyrect)
        win.blit(bgs[bgnum], bg)
        win.blit(text, textRect)
        pygame.display.update()


def main():
    global run
    while run:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        if run:
            redrawWin()


main()
