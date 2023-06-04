import pygame as game

import random as rand

game.init()

screenWidth = 720
screenHeight = 480

screen = game.display.set_mode((screenWidth, screenHeight))

# Initialize all image variables
apple = game.image.load("Images/apple.png")
compost = game.image.load("Images/compostbin.png")
bottle = game.image.load("Images/plasticbottle.png")
recycle = game.image.load("Images/recyclebin.png")
trash = game.image.load("Images/trashbin.png")
background = game.image.load("Images/background.png")

trashList = []  # add something to this por fabor
recycleList = [bottle]
compostList = [apple]

# helo
gameRunning = True

fps = 60
clockFps = game.time.Clock()

# this is for keeping the game at 60fps it should hopefully work


class Player(game.sprite.Sprite):
    def __init__(self, imageChosen):
        super().__init__()
        self.image = imageChosen
        self.image.blit(apple, (-100, -100))
        self.rect = self.image.get_rect()
        self.rect.center = [-50, -50]
        self.x = -10
        self.y = -10

    def movement(self):
        key = game.key.get_pressed()
        dist = 5
        if key[game.K_DOWN]:
            self.y += dist
        elif key[game.K_UP]:
            self.y -= dist
        if key[game.K_RIGHT]:
            self.x += dist
        elif key[game.K_LEFT]:
            self.x -= dist

    def drawItem(self):
        screen.blit(self.image, (self.x, self.y))


while gameRunning:
    chosenList = rand.randint(1, 2)
    if chosenList == 1:
        if len(recycleList) > 0:
            currItem = rand.choice(recycleList)
            # recycleList.remove(currItem)
            print('recycle')
    elif chosenList == 2:
        if len(trashList) > 0:
            currItem = rand.choice(trashList)
            # trashList.remove(currItem)
            print('trash')
    else:
        if len(compostList) > 0:
            currItem = rand.choice(compostList)
            compostList.remove(currItem)
            print('compost')
        else:
            print('Lists are over (change this in later code to sm like "You Win")')
            # we have no more items to give to the user so we needa end it here
            # whys it keep running this running what this seciton of if else things in th check disocrd

    playerGroup = game.sprite.Group()
    # make if condition to connect to each item's property and change the parameters
    item = Player(currItem)
    playerGroup.add(item)

    # key = game.key.get_pressed()
    # if key[game.K_a] == True:
    #     item.move_ip(-5, 0)
    # elif key[game.K_d] == True:
    #     item.move_ip(5, 0)

    for event in game.event.get():
        if event.type == game.QUIT:
            gameRunning = False

    item.movement()

    screen.blit(background, (0, -75))
    item.drawItem()
    clockFps.tick(fps)

    game.display.update()


game.quit()
