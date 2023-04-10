#Pong Game project using pygame
#Group members: Liam Rivers, Ethan Mahar, Johnathon Hetrick, Gavin Gloeckner
#For CSC 1200
#pip install pygame <----- if needed


#pygame is what allows us to run Pong
import pygame
pygame.init()

#main colors used in the game
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 255, 0)

#making a playing screen

#determines screen size and sets it
size = (700, 500)
screen = pygame.display.set_mode(size)
#names screen
pygame.display.set_caption("Pong")

#main loop to determine if screen remains up or not
carryOn = True

#clock will control refresh rate, to prevent the screen updating itself too fast and crashing
clock = pygame.time.Clock()

#this loop detects if the user wants to close the game
while carryOn:
    #the event is for anything user did
    for event in pygame.event.get():
        #the if statement detects if the user wants to close the program
        if event.type ==pygame.QUIT:
            #by setting loop to false this closes the screen
            carryOn = False




    #GAME LOGIC CODE



    #DRAWING CODE


    #makes the screen black
    screen.fill(BLACK)

    #makes the net
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    #updates screen with net
    pygame.display.flip()

    #sets the game to 60 frames per second
    clock.tick(60)

#upon exiting the program, we close the game
pygame.quit()