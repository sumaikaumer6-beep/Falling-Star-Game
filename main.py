import pygame
import random
import requests
pygame.init()
width = 800
height = 600
def send_score_to_api(name,score):
    try:
        url = "http://127.0.0.1:8000/api/save"
        data = {"player_name":name,"score":score}
        response=requests.post(url, json=data,timeout=2)
        print("Score saved to API")
    except:
        print("API server not running")

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Falling Star Game")
player_name="Player1"
clock = pygame.time.Clock()
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (width, height))
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)
black=(0,0,0)
white=(255,255,255)
yellow=(255,255,0)
basket_x=250
basket_y=height - 30
star_x=random.randint(0,580)
star_y=0
score=0
font=pygame.font.Font(None, 30)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:basket_x-=5
    if keys[pygame.K_RIGHT]:basket_x+=5
    star_y += 4
    if basket_x < star_x +  20 and basket_x +100 > star_x :
        if basket_y < star_y + 20 :
            score+=1
            star_x= random.randint(0,580)
            star_y= 0
    if star_y> height:
       print(f"Game Over!{player_name} Score: {score}")
       send_score_to_api(player_name,score)
       running = False
    window.blit(background,(0,0))

    pygame.draw.rect(window, white, (basket_x, basket_y, 100, 20))
    pygame.draw.circle(window, yellow, (star_x, star_y), 10)
    text = font.render(str(score), True, white)
    pygame.display.update()
    clock.tick(60)
pygame.quit()