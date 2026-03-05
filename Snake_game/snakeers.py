import pygame
import random
import json

pygame.init()

WIDTH = 600
HEIGHT = 400
BLOCK = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

green = (0,255,0)
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)


def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, green, [block[0], block[1], BLOCK, BLOCK])


def message(text):
    msg = font.render(text, True, red)
    screen.blit(msg, [WIDTH/6, HEIGHT/3])


def game_loop():

    x = WIDTH/2
    y = HEIGHT/2

    dx = 0
    dy = 0

    snake = []
    snake_length = 1

    foodx = random.randrange(0, WIDTH-BLOCK, BLOCK)
    foody = random.randrange(0, HEIGHT-BLOCK, BLOCK)

    score = 0
    game_over = False

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -BLOCK
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = BLOCK
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -BLOCK
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = BLOCK
                    dx = 0

        x += dx
        y += dy

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_over = True

        screen.fill(black)

        pygame.draw.rect(screen, red, [foodx, foody, BLOCK, BLOCK])

        head = []
        head.append(x)
        head.append(y)
        snake.append(head)

        if len(snake) > snake_length:
            del snake[0]

        for block in snake[:-1]:
            if block == head:
                game_over = True

        draw_snake(snake)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = random.randrange(0, WIDTH-BLOCK, BLOCK)
            foody = random.randrange(0, HEIGHT-BLOCK, BLOCK)
            snake_length += 1
            score += 10

        clock.tick(10)

    return score


def save_data(data):
    try:
        with open("snake_players.json","r") as f:
            existing = json.load(f)
    except:
        existing = []

    existing.append(data)

    with open("snake_players.json","w") as f:
        json.dump(existing,f,indent=4)


def main():

    email = input("Enter your email: ")

    print("Game 1 starting...")
    score1 = game_loop()

    print("Game 2 starting...")
    score2 = game_loop()

    feedback = input("Please give your feedback about the game: ")

    player_data = {
        "email": email,
        "score_game1": score1,
        "score_game2": score2,
        "feedback": feedback
    }

    save_data(player_data)

    print("Data saved successfully!")


main()