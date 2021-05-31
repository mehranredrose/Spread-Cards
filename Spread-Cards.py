#AD Project 2 by Mehran RedRose
#Mehran Abbasi 9708893

import pygame
from pygame.locals import *
from sys import exit
import math

#gets only digits not strings
def truedigit(): 
    number = input("\nEnter ur numbers one by one\t(for Finish Enter '0' ) : ")
    while not number.isdigit():
        print ('\n Ur input is not a Number ! Please Try again !\n')
        number = input("Enter a number\t\t\t(for Finish Enter '0' ) : ")
    number=int(number)
    return number

#saving the cards value
cards=[]
while (True):
    x = truedigit()
    if x==0:
        break
    cards.append(x)
#making the patrick and bob accounts
patrick=[]
bob=[]
sorted=cards.copy()
sorted.sort()
x=sorted.pop()
patrick.append(x)

#the main algorithm
while sorted!=[]:
    x=sorted.pop()
    if sum(patrick)<sum(bob):
        patrick.append(x)
    else:
        bob.append(x)

#starting graphic Part
pygame.init()
screen = pygame.display.set_mode((1500,800))
font = pygame.font.Font("BKoodkBd.ttf", 35)
font2 = pygame.font.Font("Felisha Roseland.otf", 40)

#turns degree to radians for creating circles
def degreesToRadians(deg):
    return deg/180.0 * math.pi

#values of colors in rgb
white = (255,255,255);
red = (255,0,0);
green = (163, 221, 203);
blue = (0,0,255);
darkBlue = (0, 88, 122);
black = (0,0,0);
pink = (247, 124, 135);
navy=(15, 48, 87);
cream=(244, 244, 244);
purple=(101, 64, 98);
yellow=(255, 214, 107);
lightpink=(255, 128, 139);

# loading the Picture of Patrick and Bob 
patrick_image = pygame.image.load('project-Patrick.png')
bob_image = pygame.image.load('Project-BOB.png') 

#the main() function :))))
while True:

    #turn the screen to navy
    screen.fill(navy);

    #signing Mehran Redrose on the top of screen
    textRR = font2.render(' MEHRAN  REDROSE', True, red, navy)
    textRect = textRR.get_rect()
    textRect.center = (748, 25)
    screen.blit(textRR, textRect)

    #creating the devided Parts for bob and patrick
    pygame.draw.line(screen,yellow, (380, 50), (380, 800),725)
    pygame.draw.line(screen,lightpink, (1115, 50), (1115, 800),725)

    #locating the profile of bob and patrick
    screen.blit(pygame.transform.scale(bob_image, (150, 150)), (300, 75))
    pygame.draw.circle(screen, pink, (375, 150), 85,10 ) 
    screen.blit(pygame.transform.scale(patrick_image, (150, 150)), (1040, 75))
    pygame.draw.circle(screen, yellow, (1115, 150), 85, 10) 

    #creating the <<sum>> Part
    pygame.draw.rect(screen, red, pygame.Rect(650, 120, 200, 100) ,2)
    pygame.draw.line(screen,navy, (748, 0), (748, 800),10)
    text = font.render(str(sum(bob)), True, black, yellow)
    textRect = text.get_rect()
    textRect.center = (700, 175)
    screen.blit(text, textRect)
    text2 = font.render(str(sum(patrick)), True, black, lightpink)
    textRect = text2.get_rect()
    textRect.center = (800, 175)
    screen.blit(text2, textRect)

    #coordinates of the card's place
    bob_column=[98.88,187.76,276.64,365.52,454.4,543.28,632.16]
    pat_column=[861.84,950.64,1039.52,1128.4,1217.28,1306.16,1395.04]
    row=[300,425,550,675]


    i=0
    j=0
    #giving cards to bob in graphic
    for x in bob:
        pygame.draw.line(screen,cream, (bob_column[i], row[j]), (bob_column[i],row[j]+100),75)
        text = font.render(str(x), True, black, cream)
        textRect = text.get_rect()
        textRect.center = (bob_column[i], row[j]+55)
        screen.blit(text, textRect)
        i+=1
        if i==7:
            j+=1
            i=0
    i=0
    j=0
    #giving cards to patrick in graphic
    for x in patrick:
        pygame.draw.line(screen,cream, (pat_column[i], row[j]), (pat_column[i],row[j]+100),75)
        text = font.render(str(x), True, black, cream)
        textRect = text.get_rect()
        textRect.center = (pat_column[i], row[j]+55)
        screen.blit(text, textRect)
        i+=1
        if i==7:
            j+=1
            i=0

    pygame.display.flip()
    
    #exit function
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit(); 
            quit()

    pygame.display.update()	
    