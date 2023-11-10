
import pygame
import random

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAVITY = 2
PLAYER_WIDTH = 200
PLAYER_HEIGHT = 200
PLAYER_SURF_JUMP = -20
PLAYER2_WIDTH = 200
PLAYER2_HEIGHT = 200
PLAYER2_SURF_JUMP = -20
OBS_WIDTH = 100
OBS_HEIGHT = 100
OBS_SPEED = 1
NUM_INITIAL_OBSS = 10
BG_WIDTH = 800
BG_HEIGHT = 595
CLOUD_SPEED = 2
NUM_INITIAL_CLOUDS = 10  # Adjust this to increase the number of initial clouds
BULLET_WIDTH = 10
BULLET_HEIGHT = 10
BULLET_SPEED = 100

GREEN = (0, 255, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (13, 255, 255)
BLUE = (20, 30, 120)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("I don't know")
clock = pygame.time.Clock()

PLAYER_FIRE_COOLDOWN = 2
player_cooldown = 0

bg_image = pygame.image.load("C:/Users/zspea/bg11.png").convert_alpha()
bg_image = pygame.transform.scale(bg_image, (BG_WIDTH, BG_HEIGHT))
bg_rect = bg_image.get_rect()
scroll = 0
scroll_speed = 10


player_surf = pygame.image.load("C:/Users/zspea/gr4.png").convert_alpha()
player_surf2 = pygame.image.load("C:/Users/zspea/gr3.png").convert_alpha()
player_surf1 = pygame.image.load("C:/Users/zspea/gr11.png").convert_alpha()
player_surf3 = pygame.image.load("C:/Users/zspea/gr8.png").convert_alpha()
player_surf0 = pygame.image.load("C:/Users/zspea/gr5.png").convert_alpha()
player_surf = pygame.transform.scale(player_surf, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_surf3 = pygame.transform.scale(player_surf3, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_surf0 = pygame.transform.scale(player_surf0, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_surf2 = pygame.transform.scale(player_surf2, (PLAYER2_WIDTH, PLAYER2_HEIGHT))
player_surf1 = pygame.transform.scale(player_surf1, (PLAYER_WIDTH, PLAYER_HEIGHT))
player_rect = player_surf.get_rect()
player_rect3 = player_surf3.get_rect()
player_rect0 = player_surf.get_rect()
player_rect2 = player_surf2.get_rect()
player_rect1 = player_surf1.get_rect()
player_rect.bottomleft = (100, 600)
player_rect3.bottomleft = (100, 600)
player_rect0.bottomleft = (100, 600)
player_rect2.bottomleft = (0, SCREEN_HEIGHT - PLAYER2_HEIGHT - SCREEN_HEIGHT/2)
player_y_momentum = 0
player_on_ground = False
player2_y_momentum = 0
player2_on_ground = False
player_on_ground1 = False



obs_image = pygame.image.load("C:/Users/zspea/1UFO.png").convert_alpha()
obs_image = pygame.transform.scale(obs_image, (OBS_WIDTH, OBS_HEIGHT))
obs_rect = obs_image.get_rect()
obs_rect.bottomright = (600, 600)
obs_y_momentum = 0

bullets = []


clouds = []

def generate_cloud(x):
    cloud = pygame.Rect(x, random.randint(50, 300), 100, 50)
    return cloud

# Generate initial clouds
for x in range(0, SCREEN_WIDTH * 2, 150):
    clouds.append(generate_cloud(x))
    

# Animation variables
current_image_index = 0
images = [player_surf1, player_surf, player_surf0, player_surf2, player_surf, player_surf0, player_surf2]

clock = pygame.time.Clock()
FPS = 10
run = True
e_timer = 0  # Timer variable
e_timer_limit = 1500  # Time limit in milliseconds (1 second)

while run:
    clock.tick(FPS)

    # Scroll background
    keys = pygame.key.get_pressed()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                current_image_index = 0
            if event.key == pygame.K_RIGHT:
                current_image_index = 0

    if player_cooldown > 0:
       player_cooldown -= 1
            

    
    # Scroll background
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        scroll -= scroll_speed
    if keys[pygame.K_LEFT]:
        scroll += scroll_speed


    # Apply gravity to the player
    player_y_momentum += GRAVITY
    player_rect.y += player_y_momentum
    player2_y_momentum += GRAVITY
    player_rect2.y += player2_y_momentum


    obs_y_momentum += OBS_SPEED
    obs_rect.x -= obs_y_momentum

    # Check if player is on the ground
    if player_rect.y >= SCREEN_HEIGHT - PLAYER_HEIGHT:
        player_y_momentum = 0

    if player_rect2.y >= SCREEN_HEIGHT - PLAYER2_HEIGHT:
        player2_y_momentum = 0



    if player_rect.bottom > SCREEN_HEIGHT:
        player_rect.bottom = SCREEN_HEIGHT
    if player_rect.top > SCREEN_HEIGHT:
        player_rect.top = SCREEN_HEIGHT = False
    if player_rect.top > SCREEN_HEIGHT:
        player_rect.top = SCREEN_HEIGHT = False


    # Move clouds and triangles when arrow keys are pressed
    if keys[pygame.K_RIGHT]:
        for cloud in clouds:
            cloud.x -= CLOUD_SPEED
            current_image_index = (current_image_index + 1) % len(images)

    if keys[pygame.K_LEFT]:
        for cloud in clouds:
            cloud.x += CLOUD_SPEED
            current_image_index = (current_image_index + 1) % len(images)
 
 
    # Shooting1
    if keys[pygame.K_SPACE] and player_cooldown == 0:
        bullet_img = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT))
        bullet_img.fill(GREEN)
        bullet_rect = bullet_img.get_rect(midtop=(player_rect.centerx, player_rect.centery))
        bullets.append(bullet_rect)
        player_cooldown = PLAYER_FIRE_COOLDOWN
        

    # Bullet movement and collisions
    for bullet in bullets:
        bullet.move_ip(BULLET_SPEED, 0)
        if bullet.top <= 0:
            bullets.remove(bullet)
                          
  # Apply gravity to the player
    player_y_momentum += GRAVITY
    player_rect.y += player_y_momentum

# Check if player is on the ground
    if player_rect.y >= SCREEN_HEIGHT - PLAYER_HEIGHT:
        player_y_momentum = 0
        player_on_ground = True
        player_rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT


# Handle player jump
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_on_ground:
        player_y_momentum = PLAYER_SURF_JUMP
        player_on_ground = False
    curremt_image_index = 5
    screen.fill(BLUE)

    # Blit the background surface onto the screen with the scroll offset
    screen.blit(bg_image, (scroll, 0))
    # Loop the background image
    for x in range(-BG_WIDTH, SCREEN_WIDTH, BG_WIDTH):
        screen.blit(bg_image, (scroll % BG_WIDTH + x, 0))

    # Draw clouds
    for cloud in clouds:
        pygame.draw.ellipse(screen, GREEN, cloud)
    

    screen.blit(obs_image, obs_rect)

    for bullet in bullets:
        pygame.draw.rect(screen, GREEN, bullet)

    screen.blit(images[current_image_index], player_rect)
    
    pygame.display.update()

pygame.quit()
exit()
