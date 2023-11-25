import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
x_addition = 300
y_addition = 300
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
pygame.display.set_caption("Just a blob")
print(player_pos)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)


    if player_pos.x <= 0:
        x_addition *= -1
    if player_pos.y <= 0:
        y_addition *= -1
    if player_pos.x >= 1280:
        x_addition *= -1
    if player_pos.y >= 720:
        y_addition *= -1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y_addition -= 100
    if keys[pygame.K_s]:
        y_addition += 100
    if keys[pygame.K_a]:
        x_addition -= 100
    if keys[pygame.K_d]:
        x_addition += 100

    player_pos.x += x_addition * dt
    player_pos.y += y_addition * dt
    #
    # print(x_addition,player_pos.x)
    # print(y_addition,player_pos.y)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
