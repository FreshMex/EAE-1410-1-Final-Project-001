
##These will go into the nova_blaster_main.py



suicideLIST = pygame.sprite.Group()

def makeSuiciders():
    numSuicide = 5

    while numSuicide > 0:
        randx = randrange(-1000, 1200 + 1000)
        randy = randrange(-1000, 900 + 1000)

        if not (randx > 0 and randx < 1200 and randy > 0 and randy < 900):
            v1 = vector(randx, randy)
            v2 = vector.fromPoints((randx, randy), (SPSpos.vX, SPSpos.vY))

            suicideLIST.add(suiciders(v1, screen, v2, 5.0, 100))
            numSuicide -= 1



def main():

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                return
            
        if len(suicideLIST) < 1:
            makeSuiciders()


        suiciderCollisions = pygame.sprite.spritecollide(SS1, suicideLIST, True, True)
        suiciderBulletCollisions = pygame.sprite.spritecollide(suicideLSIT, bulletlist, True, True)


        for SX in suiciderLIST:
            SX.displayMeteor
