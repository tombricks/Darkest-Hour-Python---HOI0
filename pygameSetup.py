import pygame
import random

title = 'Hearts of Iron 0'
pygame.display.set_caption(title)
font = 'arial.ttf'
pygame.init()
X = 1280
Y = 720
window = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()
framesSurpassed = 0
keys = pygame.key.get_pressed()
surfWidth = 0

def randomNumber(min, max):
    return random.randint(min, max)

def createText(text, x, y, textFont, size, colour, direction='right'):
    global surfWidth
    smallText = pygame.font.Font(textFont, size)
    textSurf, textRect = text_objects(text, smallText, colour)
    if direction == 'right':
        textRect.left = x
    elif direction == 'left':
        textRect.right = x
    textRect.centery = y
    window.blit(textSurf, textRect)


def button(x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos
    click = pygame.mouse.get_pressed()
    if x + w > mouse()[0] > x and y + h > mouse()[1] > y:
        drawRect(w, h, x, y, ac)
        if click[0] == 1 and action is not None:
            print()
    else:
        drawRect(w, h, x, y, ic)


def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()


def placeImage(image, x, y, w, h):
    image = pygame.image.load(image)
    image = pygame.transform.scale(image, (w, h))
    window.blit(image, (x, y))


def drawRect(width, height, xcord, ycord, colour):
    s = pygame.Surface((width, height), pygame.SRCALPHA)
    s.fill(colour)
    window.blit(s, (xcord, ycord))


def drawBlur(x, y, colour, direction, height, width):
    global tempVar
    tempVar = 0
    if direction == 'west' or direction == 'east':
        for _ in range(width):
            if direction == 'west':
                drawRect(tempVar, height, x - tempVar, y, colour)
                tempVar += 1
            elif direction == 'east':
                drawRect(tempVar, height, x, y, colour)
                tempVar += 1
    if direction == 'north' or direction == 'south':
        for _ in range(height):
            if direction == 'north':
                drawRect(width, tempVar, x, y - tempVar, colour)
                tempVar += 1
            elif direction == 'south':
                drawRect(width, tempVar, x, y, colour)
                tempVar += 1


def drawBorder(x, y, height, width, border, colour):
    drawRect(width, border, x, y, colour)
    drawRect(border, height, x, y, colour)
    drawRect(width, border, x, y + height - border, colour)
    drawRect(border, height, x + width - border, y, colour)
