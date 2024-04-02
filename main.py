import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600

grid_size = 20
grid_width = screen_width/grid_size
grid_height = screen_height/grid_size

UP = (0,-1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

fruit_sound = pygame.mixer.Sound("fruit_sound.wav")
fruit_sound.set_volume(0.3)

class Snake:
    def __init__(self):
        self.length = 1
        self.position = [screen_width // 2, screen_height // 2]
        self.direction = RIGHT
        self.rect = pygame.Rect(self.position, (grid_size,grid_size))

    def turn(self, point):
        self.direction = point

    def move(self):
        current = self.position
        x, y = self.direction
        new = (current[0] + x * grid_size), (current[1] + y * grid_size)
        self.position = new
        self.rect = pygame.Rect(self.position, (grid_size,grid_size))

    def draw(self, surface):
        pygame.draw.rect(surface, (0,255,0), self.rect)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                if event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                if event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
                if event.key == pygame.K_LEFT:
                    self.turn(LEFT)

class Fruit:
    def __init__(self):
        self.position = (20,20)
        self.rect = pygame.Rect(self.position, (grid_size,grid_size))

    def random_position(self):
        self.position = ((random.randint(0, grid_width - 1) * grid_size),(random.randint(0, grid_height - 1) * grid_size))
        self.rect = pygame.Rect(self.position, (grid_size,grid_size))
   
    def draw(self, surface):
        pygame.draw.rect(surface, (0,0,255), self.rect)


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

def main():
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Snake")


    clock = pygame.time.Clock()

    snake = Snake()
    fruit = Fruit()

    while True:
        screen.fill((255,255,255))
        snake.handle_keys()
        snake.move()
        snake.draw(screen)
        fruit.draw(screen)

        if snake.rect.colliderect(fruit.rect):
            fruit_sound.play()
            fruit.random_position()

        pygame.display.update()

        clock.tick(10)

if __name__ == "__main__":
    main()