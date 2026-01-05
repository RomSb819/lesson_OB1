import random
import sys
import pygame


# ======================
# Настройки игры
# ======================
CELL_SIZE = 20                 # размер "клетки" сетки
GRID_W, GRID_H = 32, 24        # размер поля в клетках (32x24)
WIDTH, HEIGHT = GRID_W * CELL_SIZE, GRID_H * CELL_SIZE

FPS_START = 10                 # стартовая скорость
FPS_MAX = 25                   # максимальная скорость
SPEEDUP_EVERY = 3              # ускорение каждые N очков

# Цвета (RGB)
BG = (20, 20, 20)
GRID = (30, 30, 30)
SNAKE = (50, 200, 80)
SNAKE_HEAD = (80, 240, 110)
FOOD = (220, 60, 60)
TEXT = (230, 230, 230)


def draw_grid(surface: pygame.Surface):
    """Рисуем лёгкую сетку (не обязательно, но приятно)."""
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(surface, GRID, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, GRID, (0, y), (WIDTH, y))


def cell_to_px(cell):
    """(cx, cy) -> (x, y) в пикселях."""
    cx, cy = cell
    return cx * CELL_SIZE, cy * CELL_SIZE


def random_food(snake_cells: list[tuple[int, int]]) -> tuple[int, int]:
    """Создаём еду в свободной клетке, не занятой змейкой."""
    occupied = set(snake_cells)
    free = [(x, y) for x in range(GRID_W) for y in range(GRID_H) if (x, y) not in occupied]
    if not free:
        # теоретически: змейка заняла всё поле
        return (-1, -1)
    return random.choice(free)


def is_opposite(a, b) -> bool:
    """Проверка: направления противоположны?"""
    return a[0] == -b[0] and a[1] == -b[1]


def render_text_center(screen, font, text, y, color=TEXT):
    surf = font.render(text, True, color)
    rect = surf.get_rect(center=(WIDTH // 2, y))
    screen.blit(surf, rect)


def new_game():
    """Сброс состояния игры."""
    # Змейка начинается из 3 клеток по центру
    start_x, start_y = GRID_W // 2, GRID_H // 2
    snake = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
    direction = (1, 0)      # движемся вправо
    next_dir = direction
    food = random_food(snake)
    score = 0
    fps = FPS_START
    paused = False
    game_over = False
    return snake, direction, next_dir, food, score, fps, paused, game_over


def main():
    pygame.init()
    pygame.display.set_caption("Змейка (Pygame)")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("consolas", 24)
    font_big = pygame.font.SysFont("consolas", 36)

    snake, direction, next_dir, food, score, fps, paused, game_over = new_game()

    while True:
        # ======================
        # События
        # ======================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_SPACE and not game_over:
                    paused = not paused

                if event.key == pygame.K_r:
                    snake, direction, next_dir, food, score, fps, paused, game_over = new_game()

                # Управление: стрелки / WASD
                if not game_over and not paused:
                    if event.key in (pygame.K_UP, pygame.K_w):
                        cand = (0, -1)
                        if not is_opposite(cand, direction):
                            next_dir = cand
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        cand = (0, 1)
                        if not is_opposite(cand, direction):
                            next_dir = cand
                    elif event.key in (pygame.K_LEFT, pygame.K_a):
                        cand = (-1, 0)
                        if not is_opposite(cand, direction):
                            next_dir = cand
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        cand = (1, 0)
                        if not is_opposite(cand, direction):
                            next_dir = cand

        # ======================
        # Логика
        # ======================
        if not paused and not game_over:
            direction = next_dir

            head_x, head_y = snake[0]
            dx, dy = direction
            new_head = (head_x + dx, head_y + dy)

            # Столкновение со стеной
            if not (0 <= new_head[0] < GRID_W and 0 <= new_head[1] < GRID_H):
                game_over = True
            else:
                # Столкновение с собой
                if new_head in snake:
                    game_over = True
                else:
                    snake.insert(0, new_head)

                    # Съели еду?
                    if new_head == food:
                        score += 1
                        food = random_food(snake)

                        # Ускорение
                        if score % SPEEDUP_EVERY == 0 and fps < FPS_MAX:
                            fps += 1
                    else:
                        # если не съели — убираем хвост (движение)
                        snake.pop()

        # ======================
        # Рендер
        # ======================
        screen.fill(BG)
        draw_grid(screen)

        # Еда
        fx, fy = cell_to_px(food)
        pygame.draw.rect(screen, FOOD, (fx, fy, CELL_SIZE, CELL_SIZE), border_radius=6)

        # Змейка
        for i, (cx, cy) in enumerate(snake):
            x, y = cell_to_px((cx, cy))
            color = SNAKE_HEAD if i == 0 else SNAKE
            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE), border_radius=6)

        # HUD
        hud = font.render(f"Score: {score}   Speed: {fps}   (Space: pause, R: restart, Esc: quit)", True, TEXT)
        screen.blit(hud, (10, 10))

        if paused:
            render_text_center(screen, font_big, "PAUSE", HEIGHT // 2 - 20)
            render_text_center(screen, font, "Нажми SPACE чтобы продолжить", HEIGHT // 2 + 20)

        if game_over:
            render_text_center(screen, font_big, "GAME OVER", HEIGHT // 2 - 40)
            render_text_center(screen, font, f"Score: {score}", HEIGHT // 2)
            render_text_center(screen, font, "Нажми R чтобы начать заново", HEIGHT // 2 + 35)

        pygame.display.flip()
        clock.tick(fps)


if __name__ == "__main__":
    main()
