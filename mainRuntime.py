import sys
debug = True
from historySetup import *
from pygameSetup import *

nation = nations["ENG"]


def inside(x, y, w, h, x2, y2):
    if x + w > x2 > x and y + h > y2 > y:
        return True
    else:
        return False


class button():
    x = 0

    def __init__(self, x, y, w, h, ic, ac, action=None, active=True):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.ic = ic
        self.ac = ac
        self.action = action
        self.active = active

    def draw(self, mouse):
        if inside(self.x, self.y, self.w, self.h, mouse()[0], mouse()[1]) and self.active:
            drawRect(self.w, self.h, self.x, self.y, self.ac)
        else:
            drawRect(self.w, self.h, self.x, self.y, self.ic)


def widthOfText(fontSize, text):
    return (pygame.font.Font(font, fontSize)).size(text)[0]

buttons = {
    "leader": button(0 + 10, 9, 50, 70, colours["blank"], colours["black64"]),
    "flag": button(18, 18, 82, 52, colours["blank"], colours["black64"])
}

while True:
    nation.updateNames()
    window.fill(colours["blue255"])

    #   Top Bar
    placeImage("gfx/ui/top bar.png", 0, 0, 1280, 88)
    if nation == nations["ENG"]:
        placeImage("gfx/ui/ENG top bar.png", 0, 0, 191, 88)

    placeImage(nation.flag, 18, 18, 82, 52)
    placeImage("gfx/flags/flag overlay.tga", 18, 18, 82, 52)

    createText(nation.name, 114, 36, font, 16, colours["black128"])
    endOfCountryName = 114 + widthOfText(16, nation.name)
    createText(ideologies.name(nation.ideology), 114, 52, font, 12, colours["black128"])

    # Leader
    placeImage(nation.leader.portrait, endOfCountryName + 10, 9, 50, 70)
    createText(nation.leader.name, endOfCountryName + 65, 22, font, 16, colours["black128"])
    createText(nation.leader.title, endOfCountryName + 65, 38, font, 12, colours["black128"])
    createText(nation.leader.party, endOfCountryName + 65, 50, font, 12, colours["black128"])
    createText(subideologies.name(nation.leader.ideology), endOfCountryName + 65, 62, font, 12, colours["black128"])
    buttons["leader"].x = endOfCountryName + 10
    tempVar = [widthOfText(16, subideologies.name(nation.leader.ideology)), widthOfText(12, nation.leader.ideology), widthOfText(12, nation.leader.party)]
    endOfIdeologyName = endOfCountryName + 65 + max(tempVar)

    tempVar = 0
    for x in decisions.values():
        if x.visible:
            if x.available:
                buttons["decision_button_"+x.id] = button(960, 88, 320, 32, colours["blank"], colours["black64"])
            placeImage("gfx/ui/decision.png", 960, 88+tempVar, 320, 32)
            createText(x.name, 976, 104+tempVar, font, 16, colours["white255"])
            tempVar += 32

        if not x.visible or not x.available:
            try:
                buttons.pop("decision_button_"+x.id)
            except:
                pass


    for x in buttons.values():
        x.draw(pygame.mouse.get_pos)

    print(framesSurpassed)

    #   Event Grabber
    #   KEYDOWN only checks for a single press, not repeating presses. If you want that, use the if keys[KEYCODE]: command.
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            nation.ideology = ideologies.communism
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            nation.ideology = ideologies.fascism
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            nation.ideology = ideologies.neutrality
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            nation.ideology = ideologies.democratic

    framesSurpassed += 1
    drawBlur(0, 88, colours["black16"], 'south', 15, 1280)
    pygame.event.get()
    pygame.event.clear()
    pygame.display.update()
    clock.tick(1000)
