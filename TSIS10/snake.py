import psycopg2
import pygame as pg
import random
import time

# Подключение к базе данных
def connect_to_db():
    conn = psycopg2.connect(
        dbname="postgres", user="postgres", password="12e09456", host="localhost"
    )
    return conn

# Функция для создания таблиц в базе данных
def create_tables():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS "user" (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user_score (
            score_id SERIAL PRIMARY KEY,
            user_id INT REFERENCES "user"(user_id),
            score INT,
            level INT
        )
        """
    )

    conn.commit()
    cursor.close()
    conn.close()

# Функция для вставки данных о пользователе и его счете в базу данных
def insert_user_score(username, score, level):
    conn = connect_to_db()
    cursor = conn.cursor()

    # Получаем user_id по имени пользователя
    cursor.execute("SELECT user_id FROM \"user\" WHERE username = %s", (username,))
    user_id = cursor.fetchone()

    # Если пользователь существует, получаем его user_id, иначе создаем нового пользователя
    if not user_id:
        cursor.execute(
            "INSERT INTO \"user\" (username) VALUES (%s) RETURNING user_id",
            (username,),
        )
        user_id = cursor.fetchone()[0]
    else:
        user_id = user_id[0]

    # Вставляем данные о пользователе и его счете в таблицу user_score
    cursor.execute(
        "INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
        (user_id, score, level),
    )

    conn.commit()
    cursor.close()
    conn.close()

# Функция для получения последнего счета и уровня пользователя из базы данных
def get_player_with_max_score():
    conn = connect_to_db()
    cursor = conn.cursor()

    # Получаем имя пользователя с максимальным счетом
    cursor.execute(
        """
        SELECT "user".username
        FROM user_score
        JOIN "user" ON user_score.user_id = "user".user_id
        ORDER BY score DESC
        LIMIT 1
        """
    )
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result
def get_last_score_and_level(username):
    conn = connect_to_db()
    cursor = conn.cursor()

    # Получаем последний счет и уровень пользователя по его имени
    cursor.execute(
        """
        SELECT score, level 
        FROM user_score 
        JOIN "user" ON user_score.user_id = "user".user_id 
        WHERE "user".username = %s 
        ORDER BY score_id DESC 
        LIMIT 1
        """,
        (username,),
    )
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result


# Запрос имени пользователя
username = input("Введите ваше имя: ")

# Создание таблиц перед началом игры
create_tables()

# Получение последнего счета и уровня пользователя из базы данных
last_score, last_level = get_last_score_and_level(username) or (0, 1)

print(f"Ваш предыдущий счет {last_score}")
# Инициализация Pygame
# Функция для получения имени игрока с максимальным счетом из базы данных


# Получение имени игрока с максимальным счетом из базы данных
max_score_player = get_player_with_max_score()

if max_score_player:
    print("Игрок с максимальным счетом:", max_score_player[0])
else:
    print("Ни один игрок еще не набрал счета.")
pg.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Создание экрана
screen = pg.display.set_mode((800, 600))
pg.display.set_caption("Змейка")
mus=pg.mixer.Sound("kk.mp3")



back_graund=pg.image.load("fsnake.png")
back_graund=pg.transform.scale(back_graund,(800,600))

clock = pg.time.Clock()
level = 1
font = pg.font.SysFont("comicsansms", 20)
font_big = pg.font.SysFont("comicsansms", 56)
status = "Нуб"
game_over = font_big.render("Game Over", 1, "BLUE")
score = 0
apple_time = pg.USEREVENT + 1
apple_in_pole = True
apl_Count = 0
thre_point=1
time_aple=[8,11]
pg.time.set_timer(apple_time, 1000)

# Функция отрисовки змейки и яблока
def draw_objects(snake, apple):
    screen.blit(back_graund,(0,0))
    for segment in snake:
        pg.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    if score%7==0 and thre_point==1:    
       pg.draw.rect(screen, RED, (apple[0] * CELL_SIZE, apple[1] * CELL_SIZE, CELL_SIZE*2, CELL_SIZE*2))
    else:
        pg.draw.rect(screen, RED, (apple[0] * CELL_SIZE, apple[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Главная функция игры
snake = [(GRID_WIDTH // 2 , GRID_HEIGHT // 2 )]
direction = pg.Vector2(1, 0)
apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
big_apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
fps = 6
apple_area = [(apple[0], apple[1]), (apple[0] + 1, apple[1]),
              (apple[0], apple[1] + 1), (apple[0] + 1, apple[1] + 1)]
mus.play()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == apple_time:
            apl_Count = (apl_Count + 1) % (time_aple[1]+1)
    
    
    keys = pg.key.get_pressed()
    if apl_Count == time_aple[0] and apple_in_pole == True:
        apple = (-10, -10)
        apple_in_pole = False
        thre_point=0
    if apl_Count == time_aple[1] and apple_in_pole == False:
        apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        apple_in_pole = True

    if keys[pg.K_UP] and direction.y != 1:
        direction = pg.Vector2(0, -1)
    elif keys[pg.K_DOWN] and direction.y != -1:
        direction = pg.Vector2(0, 1)
    elif keys[pg.K_LEFT] and direction.x != 1:
        direction = pg.Vector2(-1, 0)
    elif keys[pg.K_RIGHT] and direction.x != -1:
        direction = pg.Vector2(1, 0)

    snake_head = snake[0] + direction
    if snake_head[0] < 0 or snake_head[0] >= GRID_WIDTH or snake_head[1] < 0 or snake_head[1] >= GRID_HEIGHT or snake_head in snake:
        mus.stop()
        pg.mixer.Sound("g_o.mp3").play()
        screen.fill("Red")
        screen.blit(game_over, (250, 240))
        screen.blit(font.render(f"Ваш счет :{score}", True, GREEN), (250,400 ))
        screen.blit(font.render(f"Вы дошли до {level} уровня", True, GREEN), (250, 380))

        if level == 2:
            status = "Любитель"
        elif level == 3:
            status = "Профи"
        elif level == 4:
            status = "Сумасшедший"
        elif level >= 5 and level<=7:
            status = "Читер"
        elif level >= 8:
            status="Ты кто такой?Давай досвидвния!"
        insert_user_score(username,score,level)
        screen.blit(font_big.render(f"Ваш статус: {status}", True, GREEN), (150, 140))
        pg.display.flip()
        time.sleep(2)
        running = False

    snake.insert(0, snake_head)
    if score%7==0 and thre_point==1:
        if snake_head in apple_area:
            apple_in_pole = False
            apple = (-10, -10)
            apl_Count = time_aple[0]
            score += 3
            if score % 5 == 0:
                level += 1
                time_aple=[time_aple[0]-4,time_aple[1]-2]
                fps += 2
            pg.mixer.Sound('ymmu.mp3').play()
        else:
            snake.pop()
    else:
        if snake_head==apple:
            
                apple_in_pole = False
                apple = (-10, -10)
                apl_Count = time_aple[0]
                score += 1
                thre_point=1
                if score % 5 == 0:
                    level += 1
                    fps += 2
                pg.mixer.Sound("ymmu.mp3").play()
        else:
                snake.pop()
            
    if score%7==0 and thre_point==1:
            apple_area = [(apple[0], apple[1]), (apple[0] + 1, apple[1]),
                        (apple[0], apple[1] + 1), (apple[0] + 1, apple[1] + 1)]

    score_dr = font.render(f"Счет:{str(score)}", 1, GREEN)
    level_dr = font.render(f"Уровень:{str(level)}", 1, GREEN)
    draw_objects(snake, apple)
    screen.blit(score_dr, (10, 10))
    screen.blit(level_dr, (690, 10))

    pg.display.flip()
    clock.tick(fps)

pg.quit()