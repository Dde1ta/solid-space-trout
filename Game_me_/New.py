import pygame

# pygame setup
file_hi = open("New_high_score.txt","r")
high_score = file_hi.read()
file_hi = open("New_high_score.txt","w")
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
GRAVITY = 5
player_speed_x = 0
player_speed_y = 0
score = 0
try:
    hi_score = int(high_score)
except:
    hi_score = 0
scoring = False
font = pygame.font.Font(None,40)
pygame.display.set_caption("Keep at middle")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            try:
                if hi_score>int(high_score):
                    file_hi.write(str(hi_score))
            except:
                file_hi.write(str(0))
            running = False

    screen.fill("purple")
    pygame.draw.circle(screen, "red", player_pos, 40)
    keys = pygame.key.get_pressed()
    if player_pos.y >= 720:
        player_speed_y -= 75
    if player_pos.x <= 0:
        player_speed_x = 0
        score = 0
    if player_pos.x >= 1280:
        player_speed_x = 0
        score = 0
    if keys[pygame.K_a]:
        if player_pos.x <= 0:
            player_speed_x = 0
            player_pos.x = 0
            scoring = True
        else:
            player_speed_x -= 10
            scoring = True
    if keys[pygame.K_d]:
        if player_pos.x >= 1280:
            player_speed_x = 0
            player_pos.x = 1280
        else:
            player_speed_x += 10
    player_pos.y += player_speed_y
    player_speed_y += GRAVITY
    player_pos.x += player_speed_x
    if player_speed_x > 0:
        player_speed_x -= 1
    elif player_speed_x < 0:
        player_speed_x += 1
    else:
        scoring = False
    if scoring:
        score+=1
        if hi_score <= score:
            hi_score = score
    score_font = font.render(f"Score: {score}",True, (255, 255, 255))
    hi_score_font = font.render(f"High Score: {hi_score}", True, (255, 255, 255))
    screen.blit(score_font,(100,10))
    screen.blit(hi_score_font,(1000,10))
    pygame.display.flip()
    clock.tick(30)
file_hi.close()
pygame.quit()
