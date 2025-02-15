import pygame

#################################################
# OPPSETT
#################################################
pygame.init()
spill_vindu = pygame.display.set_mode((1000,750))
pygame.display.set_caption("Ninja Spillet")
ninja = pygame.image.load('ninja.tif')
ninja_angrep = pygame.image.load('ninja-angrep.tif')
bakgrunn = pygame.image.load('ninja-bakgrunn.tif')
dummy = pygame.image.load('ninja-dummy.tif')
dummy_nede = pygame.image.load('ninja-dummy-nede.tif')

#################################################
# KONSTANTER
#################################################
HVIT = (255,255,255)
SVART = (0,0,0)
RED = (255,0,0)

################################################
# VARIABLER
################################################
posisjon_x = 50
posisjon_y = 425
dummy_pos = [(425,400),(550,500)]
dummy_dead = [False,False]
hastighet_x = 5
hastighet_y = 0
sverd_angrep = False
spill = True

################################################
# FUNKSJONER
################################################
def tegn_ninja(v,x,y,s):
    if s:
        v.blit(ninja_angrep, (x,y))
    else:    
        v.blit(ninja, (x,y))

def tegn_dummy(v,x,y,s):
    for i in range(0,1):
        diff = (10,10)
        pos = (x,y)
        if s:
            dummy_dead[i] = True
        if dummy_dead[i]:
            v.blit(dummy_nede, (dummy_pos[i]))
        else:
            v.blit(dummy, (dummy_pos[i]))

################################################
# HOVED LØKKE
################################################
while spill:
    # VENT
    pygame.time.delay(50)
    
    # SJEKK FOR TASTETRYKK
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spill = False
        if event.type == pygame.KEYDOWN:
            # TAST NED , START BEVEGELSE
            if event.key == pygame.K_LEFT:
                hastighet_x = -5
            if event.key == pygame.K_RIGHT:
                hastighet_x = 5
            if event.key == pygame.K_UP:
                hastighet_y = -5
            if event.key == pygame.K_DOWN:
                hastighet_y = 5
            if event.key == pygame.K_q:
                spill = False
            if event.key == pygame.K_RCTRL:
                sverd_angrep = True
            # TAST OPP, STOPP BEVEGELSE
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                hastighet_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                hastighet_y = 0
            if event.key == pygame.K_RCTRL:
                sverd_angrep = False

    # OPPDATER POSISJON FOR BEVEGELSE
    posisjon_x += hastighet_x
    posisjon_y += hastighet_y
    

    #pygame.draw.rect(spill_vindu, (255,0,0), (x,y,width,heigth))
    
    spill_vindu.fill(HVIT)
    spill_vindu.blit(bakgrunn,(0,0))
    tegn_dummy(spill_vindu, posisjon_x, posisjon_y, sverd_angrep)
    tegn_ninja(spill_vindu, posisjon_x, posisjon_y, sverd_angrep)
    pygame.display.update()

pygame.quit()



