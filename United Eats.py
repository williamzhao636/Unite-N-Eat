import pygame
import sys
import PIL
import string
import os

pygame.init()

def distance(x1, x2, y1, y2):
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return distance

def setupFoodOptions(data):
    data.menuOptions = ["Drink", "Entree", "Snacks"]
    data.menuOptionColors = [True, False, False]
    data.currentFoodOption = 0

    data.drinkOptions = ["Water", "Apple Juice", "Coke", "Coffee", "Hot Chocolate"]
    data.drinkPrices = ["1", "2", "1.5", "1.5", "2.5"]
    data.entreeOptions = ["Chicken Tendies", "Clam Chowder", "Spaghetti and Meatballs", "Sandwich"]
    data.entreePrices = ["8.5", "11", "12", "7.5"]
    data.snackOptions = ["Fruit Snacks", "Granola Bar", "Pretzels"]
    data.snackPrices = ["2", "2.5", "1.5"]

    data.drinkCurrentSelection = []
    for i in range(len(data.drinkOptions)):
        data.drinkCurrentSelection.append(False)
    data.entreeCurrentSelection = []
    for i in range(len(data.entreeOptions)):
        data.entreeCurrentSelection.append(False)
    data.snackCurrentSelection = []
    for i in range(len(data.snackOptions)):
        data.snackCurrentSelection.append(False)

def setupImages(data):
    data.unitedLogo = pygame.transform.scale(pygame.image.load(os.path.join('unitedLogo.png')).convert_alpha(), (500, 500))
    data.secondUnitedLogo = pygame.transform.scale(pygame.image.load(os.path.join('secondUnitedLogo.jpg')).convert_alpha(), (200, 200))
    data.background = pygame.transform.scale(pygame.image.load(os.path.join('gradient.png')).convert_alpha(), (540, 810))

def setupFonts(data):
    data.numFont30 = pygame.font.SysFont("Avenir.ttc", 30)

def displayOptions(screen, data):
    buttonBlue = (68, 139, 252)
    black = (0, 0, 0)
    grey = (180, 180, 180)
    tan = (237, 223, 209)

    #Display employee balance
    font = pygame.font.Font(None, 30)
    textString = "Balance: $%d"%data.employeeBalances[data.currentEmployee]
    textDimensions = font.size(textString)
    width, height = textDimensions[0], textDimensions[1]
    text = font.render(textString, True, black)
    screen.blit(text, [data.width/20, 5*data.height/64 - height/2])

    #Display different menus
    for i in range(len(data.menuOptionColors)):
        if data.menuOptionColors[i]:
            color = tan
        else:
            color = grey

        background = pygame.Rect(i*data.width/5 + data.width/40, data.height/6, data.width/5, data.height/20)
        pygame.draw.rect(screen, color, background)

        font = pygame.font.Font(None, 30)
        textString = data.menuOptions[i]
        textDimensions = font.size(textString)
        width, height = textDimensions[0], textDimensions[1]
        textX = (i*data.width/5 + 5*data.width/40) - width/2
        text = font.render(textString, True, black)
        screen.blit(text, [textX, data.height/6 + height/2])

    #Confirm button
    background = pygame.Rect(3*data.width/10, 48*data.height/64, 2*data.width/5, 2*data.height/16)
    pygame.draw.rect(screen, buttonBlue, background)

    font = pygame.font.Font(None, 40)
    textString = "Confirm"
    textDimensions = font.size(textString)
    width, height = textDimensions[0], textDimensions[1]
    text = font.render(textString, True, black)
    screen.blit(text, [data.width/2 - width/2, 52*data.height/64 - height/2])

    #Choice Background
    background = pygame.Rect(data.width/40, data.height/6 + data.height/20, 38*data.width/40, 5*data.height/16)
    pygame.draw.rect(screen, tan, background)

def checkChoiceClicked(data):
    pos = pygame.mouse.get_pos()
    mouseX, mouseY = pos[0], pos[1]

    #Check which header clicked
    for i in range(len(data.menuOptionColors)):
        if i*data.width/5 + data.width/40 < mouseX < (i+1)*data.width/5 + data.width/40 and data.height/6 < mouseY < data.height/6 + data.height/20:
            nextIndex = i
            nextChoice = data.menuOptions[nextIndex]
            for i in range(len(data.menuOptions)):
                data.menuOptionColors[i] = False
            data.menuOptionColors[nextIndex] = True
            data.mode = data.modes[data.modes.index(nextChoice)]

    #Check if Confirm button clicked
    if 3*data.width/10 < mouseX < 8*data.width/10 and 48*data.height/64 < mouseY < 56*data.height/64:
        data.currentSecond = pygame.time.get_ticks() // 1000
        data.mode = data.modes[8]


def init(data):
    data.employeeID = ["1234", "21058974", "8888"]
    data.enterField = ""
    data.fieldClicked = False
    data.employeeBalances = [757, 757, 757]
    data.currentEmployee = -1
    setupFoodOptions(data)
    setupImages(data)
    setupFonts(data)
    data.modes = ["Menu", "Start", "Help", "Choice", "Payment", "Drink", "Entree", "Snacks", "Breakroom"]
    data.mode = data.modes[0]
    #Delivery variables
    data.deliveryMinutes = 0
    data.deliverySeconds = 45
    data.currentSecond = 2
    data.breakroomSelection = [False, False, False, False, False, False, False]
    data.breakroomNum = -1
    data.breakroomChoices = [   "BAE Break Room",
                                "Arrivals Break Room",
                                "G84 Break Room",
                                "G92 Break Room",
                                "SOC Break Room",
                                "Ramp Break Room"]


def mouseMoved(data):
    pass

def mouseReleased(data):
    pass

def keyReleased(event, data):
    pass



def menuMousePressed(data):
    pos = pygame.mouse.get_pos()
    mouseX, mouseY = pos[0], pos[1]
    #Check if start button clicked
    if 2*data.width/8 < mouseX < 6*data.width/8 and 10*data.height/16 < mouseY < 48*data.height/64:
        data.mode = data.modes[1]
    #Check if help button clicked
    if 2*data.width/8 < mouseX < 6*data.width/8 and 50*data.height/64 < mouseY < 58*data.height/64:
        data.mode = data.modes[2]

def startMousePressed(data):
    pos = pygame.mouse.get_pos()
    mouseX, mouseY = pos[0], pos[1]
    #Check enter field clicked
    if 17*data.width/64 < mouseX < 47*data.width/64 and 26*data.height/64 < mouseY < 30*data.height/64:
        data.fieldClicked = True
    #Enter button
    if 2*data.width/8 < mouseX < 6*data.width/8 and 11*data.height/16 < mouseY < 13*data.height/16:
        if data.enterField in data.employeeID:
            data.currentEmployee = data.employeeID.index(data.enterField)
            data.mode = data.modes[5]

def drinkMousePressed(data):
    pos = pygame.mouse.get_pos()
    mouseX, mouseY = pos[0], pos[1]

    for i in range(len(data.drinkPrices)):
        centerX = int(5*data.width/64)
        centerY = int(30*i+data.height/4)
        if distance(mouseX, centerX, mouseY, centerY) < 10:
            if data.drinkCurrentSelection[i]:
                data.drinkCurrentSelection[i] = False
            else:
                data.drinkCurrentSelection[i] = True

    checkChoiceClicked(data)

def entreeMousePressed(data):
    pos = pygame.mouse.get_pos()
    mouseX, mouseY = pos[0], pos[1]

    for i in range(len(data.entreePrices)):
        centerX = int(5*data.width/64)
        centerY = int(30*i+data.height/4)
        if distance(mouseX, centerX, mouseY, centerY) < 10:
            if data.entreeCurrentSelection[i]:
                data.entreeCurrentSelection[i] = False
            else:
                data.entreeCurrentSelection[i] = True

    checkChoiceClicked(data)

def snacksMousePressed(data):
    pos = pygame.mouse.get_pos()
    mouseX, mouseY = pos[0], pos[1]

    for i in range(len(data.snackPrices)):
        centerX = int(5*data.width/64)
        centerY = int(30*i+data.height/4)
        if distance(mouseX, centerX, mouseY, centerY) < 10:
            if data.snackCurrentSelection[i]:
                data.snackCurrentSelection[i] = False
            else:
                data.snackCurrentSelection[i] = True

    checkChoiceClicked(data)

def breakroomMousePressed(data):
    pos = pygame.mouse.get_pos()
    mouseX, mouseY = pos[0], pos[1]


    clicked = False
    target = -1


    for i in range(len(data.breakroomSelection)):
        centerX = int(data.width/20)
        centerY = int(30*i+data.height/4)
        if distance(mouseX, centerX, mouseY, centerY) < 10:
            clicked = True
            target = i
            break

    if clicked:
        for i in range(len(data.breakroomSelection)):
            data.breakroomSelection[i] = False
        data.breakroomSelection[target] = True
        data.breakroomNum = target


    #Enter button
    if 2*data.width/8 < mouseX < 6*data.width/8 and 11*data.height/16 < mouseY < 13*data.height/16:
        data.mode = data.modes[4]

def mousePressed(data):
    if data.mode == "Menu":
        menuMousePressed(data)
    elif data.mode == "Start":
        startMousePressed(data)
    elif data.mode == "Drink":
        drinkMousePressed(data)
    elif data.mode == "Entree":
        entreeMousePressed(data)
    elif data.mode == "Snacks":
        snacksMousePressed(data)
    elif data.mode == "Breakroom":
        breakroomMousePressed(data)



def startKeyPressed(event, data):
    if data.fieldClicked:
        if pygame.key.name(event.key) in string.printable:
            data.enterField = data.enterField + pygame.key.name(event.key)
        elif event.key == pygame.K_BACKSPACE:
            data.enterField = data.enterField[:-1]

def keyPressed(event, data):
    if data.mode == "Start":
        startKeyPressed(event, data)


def timerFired(data):
    if data.mode == data.modes[4] and (not data.deliveryMinutes == 0 or not data.deliverySeconds == 0):
        if pygame.time.get_ticks() // 1000 > data.currentSecond:
            data.deliverySeconds -= 1
            data.currentSecond = pygame.time.get_ticks() // 1000
    if data.deliverySeconds < 0:
        data.deliveryMinutes -= 1
        data.deliverySeconds = 59



def draw(screen, data):
    # unitedBlue = (160, 191, 242)
    w, h = data.background.get_size()
    itemX = data.width/2 - w/2
    itemY = data.height/2 - h/2
    newRect = pygame.Rect(itemX, itemY, w, h)
    screen.blit(data.background, newRect)

    if data.mode == "Menu":
        menuDraw(screen, data)
    elif data.mode == "Start":
        startDraw(screen, data)
    elif data.mode == 'Help':
        helpDraw(screen, data)
    elif data.mode == "Choice":
        choiceDraw(screen, data)
    elif data.mode == "Payment":
        paymentDraw(screen, data)
    elif data.mode == "Drink":
        drinkDraw(screen, data)
    elif data.mode == "Entree":
        entreeDraw(screen, data)
    elif data.mode == "Snacks":
        snackDraw(screen, data)
    elif data.mode == "Breakroom":
        breakroomDraw(screen, data)

def breakroomDraw(screen, data):
    black = (0, 0, 0)
    white = (255, 255, 255)
    buttonBlue = (68, 139, 252)


    font = pygame.font.Font(None, 35)
    textString = "Please choose the break room for you meal:"
    textDimensions = font.size(textString)
    width, height = textDimensions[0], textDimensions[1]
    text = font.render(textString, True, black)
    screen.blit(text, [data.width/2 - width/2, 3*data.height/16 - height/2])


    for i in range(len(data.breakroomChoices)):
        #Drawing checkboxes
        color = white
        if data.breakroomSelection[i]:
            color = black

        optionX = int(data.width/20)
        optionY = int(30*i+data.height/4)
        pygame.draw.circle(screen, color, (optionX, optionY), 10)

        #List of food options
        font = pygame.font.Font(None, 30)
        textString = data.breakroomChoices[i]
        textDimensions = font.size(textString)
        width, height = textDimensions[0], textDimensions[1]
        text = font.render(textString, True, black)
        screen.blit(text, [data.width/8 , optionY - height/2])

    #Enter Button
    background = pygame.Rect(2*data.width/8, 11*data.height/16, 4*data.width/8, 2*data.height/16)
    pygame.draw.rect(screen, buttonBlue, background)

    enterFont = pygame.font.Font(None, 60)
    textString = "Enter"
    textDimensions = enterFont.size(textString)
    width, height = textDimensions[0], textDimensions[1]
    text = enterFont.render(textString, True, black)
    screen.blit(text, [data.width/2 - width/2, 12*data.height/16 - height/2])

def helpDraw(screen, data):
    pass

def paymentDraw(screen, data):
    black = (0, 0, 0)
    titleBlue = (18, 50, 154)
    black = (0, 0, 0)

    balance = data.employeeBalances[data.currentEmployee]
    price = 0
    for i in range(len(data.drinkCurrentSelection)):
        if data.drinkCurrentSelection[i] == True:
            price += float(data.drinkPrices[i])
    for i in range(len(data.entreeCurrentSelection)):
        if data.entreeCurrentSelection[i] == True:
            price += float(data.entreePrices[i])
    for i in range(len(data.snackCurrentSelection)):
        if data.snackCurrentSelection[i] == True:
            price += float(data.snackPrices[i])
    finalBalance = balance - price

    payment = ["Current Balance:", "Price:", "Final Balance:"]
    amounts = ["$%.2f" % balance, "$%.2f" % price, "$%.2f" % finalBalance]

    for i in range(len(payment)):
        font = pygame.font.Font(None, 30)
        textString = payment[i]
        textDimensions = font.size(textString)
        width, height = textDimensions[0], textDimensions[1]
        text = font.render(textString, True, black)
        screen.blit(text, [5*data.width/8 - width, 25*i+data.height/4 - height/2])

        font = pygame.font.Font(None, 30)
        textString = amounts[i]
        textDimensions = font.size(textString)
        width, height = textDimensions[0], textDimensions[1]
        text = font.render(textString, True, black)
        screen.blit(text, [7*data.width/8 - width, 25*i+data.height/4 - height/2])


    font = pygame.font.Font(None, 30)
    breakroom = data.breakroomChoices[data.breakroomNum]
    textString = "Your order will arrive at %s in:" % breakroom
    textDimensions = font.size(textString)
    width, height = textDimensions[0], textDimensions[1]
    text = font.render(textString, True, black)
    screen.blit(text, [data.width/2 - width/2, data.height/2 - height/2])

    minutes = data.deliveryMinutes
    if data.deliverySeconds < 10:
        seconds = "0" + str(data.deliverySeconds)
    else:
        seconds = str(data.deliverySeconds)

    textString = "%d:%s" % (minutes, seconds)
    textDimensions = font.size(textString)
    width, height = textDimensions[0], textDimensions[1]
    text = font.render(textString, True, black)
    screen.blit(text, [data.width/2 - width/2, data.height/2 + 40 - height/2])

    #Logo
    w, h = data.secondUnitedLogo.get_size()
    itemX = data.width/2 - w/2
    itemY = 4*data.height/5 - h/2
    newRect = pygame.Rect(itemX, itemY, w, h)
    screen.blit(data.secondUnitedLogo, newRect)

    #App Name
    font = pygame.font.Font(None, 60)
    textString = "Unite N Eat"
    textDimensions = font.size(textString)
    width, height = textDimensions[0], textDimensions[1]
    text = font.render(textString, True, titleBlue)
    screen.blit(text, [data.width/2 - width/2, data.height/10 - height/2])

def drinkDraw(screen, data):
    black = (0, 0, 0)
    white = (255, 255, 255)

    displayOptions(screen, data)
    #Drink Choices
    for i in range(len(data.drinkPrices)):
        color = white
        if data.drinkCurrentSelection[i]:
            color = black

        optionX = int(5*data.width/64)
        optionY = int(30*i+data.height/4)
        pygame.draw.circle(screen, color, (optionX, optionY), 10)

        #List of food options
        font = pygame.font.Font(None, 30)
        textString = data.drinkOptions[i]
        textDimensions = font.size(textString)
        width, height = textDimensions[0], textDimensions[1]
        text = font.render(textString, True, black)
        screen.blit(text, [data.width/8 , optionY - height/2])

        #List of food prices
        font = pygame.font.Font(None, 30)
        textString = data.drinkPrices[i]
        textDimensions = font.size(textString)
        width, height = textDimensions[0], textDimensions[1]
        text = font.render(textString, True, black)
        screen.blit(text, [60*data.width/64 - width, optionY - height/2])

def entreeDraw(screen, data):
    black = (0, 0, 0)
    white = (255, 255, 255)
    displayOptions(screen, data)

    #Drink Choices
    for i in range(len(data.entreePrices)):
        #Drawing checkboxes
        color = white
        if data.entreeCurrentSelection[i]:
            color = black

        optionX = int(5*data.width/64)
        optionY = int(30*i+data.height/4)
        pygame.draw.circle(screen, color, (optionX, optionY), 10)

        #List of food options
        font = pygame.font.Font(None, 30)
        textString = data.entreeOptions[i]
        textDimensions = font.size(textString)
        width, height = textDimensions[0], textDimensions[1]
        text = font.render(textString, True, black)
        screen.blit(text, [data.width/8 , optionY - height/2])

        #List of food prices
        font = pygame.font.Font(None, 30)
        textString = data.entreePrices[i]
        textDimensions = font.size(textString)
        width, height = textDimensions[0], textDimensions[1]
        text = font.render(textString, True, black)
        screen.blit(text, [60*data.width/64 - width, optionY - height/2])

def snackDraw(screen, data):
    buttonBlue = (68, 139, 252)
    black = (0, 0, 0)
    white = (255, 255, 255)

    displayOptions(screen, data)

    #Drink Choices
    for i in range(len(data.snackPrices)):
        #Drawing checkboxes
        color = white
        if data.snackCurrentSelection[i]:
            color = black

        optionX = int(5*data.width/64)
        optionY = int(30*i+data.height/4)
        pygame.draw.circle(screen, color, (optionX, optionY), 10)

        #List of food options
        font = pygame.font.Font(None, 30)
        textString = data.snackOptions[i]
        textDimensions = font.size(textString)
        width, height = textDimensions[0], textDimensions[1]
        text = font.render(textString, True, black)
        screen.blit(text, [data.width/8 , optionY - height/2])

        #List of food prices
        font = pygame.font.Font(None, 30)
        textString = data.snackPrices[i]
        textDimensions = font.size(textString)
        width, height = textDimensions[0], textDimensions[1]
        text = font.render(textString, True, black)
        screen.blit(text, [60*data.width/64 - width, optionY - height/2])

def menuDraw(screen, data):
    black = (0, 0, 0)
    buttonBlue = (68, 139, 252)
    titleBlue = (5, 33, 125)
    grey = (119, 124, 140)

    #Title
    titleFont = pygame.font.Font(None, 100)
    textString = "Unite N Eat"
    textDimensions = titleFont.size(textString)
    width, height = textDimensions[0], textDimensions[1]
    text = titleFont.render(textString, True, titleBlue)
    screen.blit(text, [data.width/2 - width/2, data.height/6 - height/2])

    #Button Background
    background = pygame.Rect(15*data.width/64, 39*data.height/64, 34*data.width/64, 20*data.height/64)
    pygame.draw.rect(screen, grey, background)

    #Start Button
    background = pygame.Rect(2*data.width/8, 10*data.height/16, 4*data.width/8, 8*data.height/64)
    pygame.draw.rect(screen, buttonBlue, background)

    font = pygame.font.Font(None, 60)
    textString = "Start"
    textDimensions = font.size(textString)
    width, height = textDimensions[0], textDimensions[1]
    text = font.render(textString, True, black)
    screen.blit(text, [data.width/2 - width/2, 11*data.height/16 - height/2])

    #Help Button
    background = pygame.Rect(2*data.width/8, 50*data.height/64, 4*data.width/8, 8*data.height/64)
    pygame.draw.rect(screen, buttonBlue, background)

    textString = "Help"
    textDimensions = font.size(textString)
    width, height = textDimensions[0], textDimensions[1]
    text = font.render(textString, True, black)
    screen.blit(text, [data.width/2 - width/2, 54*data.height/64 - height/2])

    #United logo
    w, h = data.unitedLogo.get_size()
    imageX = data.width/2 - w/2
    imageY = 26*data.height/64 - h/2
    newRect = pygame.Rect(imageX, imageY, w, h)
    screen.blit(data.unitedLogo, newRect)

def startDraw(screen, data):
    buttonBlue = (68, 139, 252)
    black = (0, 0, 0)
    white = (255, 255, 255)
    grey = (150, 150, 150)

    startFont = pygame.font.Font(None, 40)
    textString = "Please enter your employee ID"
    textDimensions = startFont.size(textString)
    width, height = textDimensions[0], textDimensions[1]
    text = startFont.render(textString, True, black)
    screen.blit(text, [data.width/2 - width/2, 3*data.height/16 - height/2])

    #Enter field
    background = pygame.Rect(14*data.width/64, 6*data.height/16, 36*data.width/64, 8*data.height/64)
    pygame.draw.rect(screen, grey, background)

    background = pygame.Rect(17*data.width/64, 26*data.height/64, 30*data.width/64, 4*data.height/64)
    pygame.draw.rect(screen, white, background)


    textString = data.enterField
    textDimensions = data.numFont30.size(textString)
    width, height = textDimensions[0], textDimensions[1]
    text = data.numFont30.render(textString, True, black)
    screen.blit(text, [data.width/2 - width/2, 7*data.height/16 - height/2])

    #Enter Button
    background = pygame.Rect(2*data.width/8, 11*data.height/16, 4*data.width/8, 2*data.height/16)
    pygame.draw.rect(screen, buttonBlue, background)

    enterFont = pygame.font.Font(None, 55)
    textString = "Enter"
    textDimensions = enterFont.size(textString)
    width, height = textDimensions[0], textDimensions[1]
    text = enterFont.render(textString, True, black)
    screen.blit(text, [data.width/2 - width/2, 12*data.height/16 - height/2])



def play(width, height):
    # size = (800, 800)
    size = (width, height)
    screen = pygame.display.set_mode(size)
    # screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    pygame.display.set_caption('Unite and Eat')
    clock = pygame.time.Clock()

    frameRate = 60

    #Struct class partially taken from 112 course notes
    class Struct(object):
        pass
    data = Struct()
    data.width = size[0]
    data.height = size[1]
    init(data)
    done = False

    while not done:
        black = (0, 0, 0)
        screen.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                keyPressed(event, data)
            if event.type == pygame.KEYUP:
                keyReleased(event, data)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePressed(data)
            if event.type == pygame.MOUSEBUTTONUP:
                mouseReleased(data)
            if event.type == pygame.MOUSEMOTION:
                mouseMoved(data)
            pass

        timerFired(data)
        draw(screen, data)

        clock.tick(frameRate)
        pygame.display.flip()

    pygame.quit()

play(540, 810)

sys.exit()
