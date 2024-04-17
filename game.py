import pygame 

pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill((0,0,128))

WINNER_FONT = pygame.font.SysFont("Times new roman", 100)
OBJECT_WIDTH, OBJECT_HEIGHT =  50,50

salt = pygame.image.load("salt.png")
peanutbutter = pygame.image.load("peanut_butter.png")
cat = pygame.image.load("cat.png")
jam = pygame.image.load("jam.png")
pepper = pygame.image.load("pepper.png")
dog = pygame.image.load("dog.png")


jamy = (pygame.transform.scale(jam, (OBJECT_WIDTH, OBJECT_HEIGHT)))
peppery = (pygame.transform.scale(pepper, (OBJECT_WIDTH, OBJECT_HEIGHT)))
dogy = (pygame.transform.scale(dog, (OBJECT_WIDTH, OBJECT_HEIGHT)))
salty = (pygame.transform.scale(salt, (OBJECT_WIDTH, OBJECT_HEIGHT)))
peanutbuttery = (pygame.transform.scale(peanutbutter, (OBJECT_WIDTH, OBJECT_HEIGHT)))
caty = (pygame.transform.scale(cat, (OBJECT_WIDTH, OBJECT_HEIGHT)))

screen.blit(jamy, (350,100))
screen.blit(peppery, (350,200))
screen.blit(dogy, (350,400))
screen.blit(salty, (150,100))
screen.blit(peanutbuttery, (150,200))
screen.blit(caty, (150,400))

#how to move the images 

#when they colide 

#winner screen 


pygame.display.update()










