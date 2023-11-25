import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height())
GRAVITY = 5
player_speed_x = 0
player_speed_y = 0
score = 0
scoring = False
font = pygame.font.Font(None,40)
pygame.display.set_caption("jump to top")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if hi_score>int(high_score):
                file_hi.write(str(hi_score))
            running = False

    screen.fill("purple")
    pygame.draw.circle(screen, "red", player_pos, 40)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_pos.x += 5
    if keys[pygame.K_d]:
        player_pos.x += 5

pygame.quit()