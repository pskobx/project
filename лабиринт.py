import random
import os
import sys
import pygame
import pprint


def terminate():
    pygame.quit()
    sys.exit()


def end_screen(n):
    intro_text = ["Поздравляем, ты прошел", str(n) + '-ый уровень!']
    clock = pygame.time.Clock()
    fon = pygame.transform.scale(load_image('zast.png'), (width, height))
    screen.blit(fon, (0, 0))
    if sl == 550:
        font = pygame.font.Font(None, 40)
        text_coord = 50
    elif sl == 450:
        font = pygame.font.Font(None, 35)
        text_coord = 50
    elif sl == 350:
        font = pygame.font.Font(None, 30)
        text_coord = 40
    elif sl == 250:
        font = pygame.font.Font(None, 20)
        text_coord = 40
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def start_screen():
    intro_text = ["Лабиринт", "",
                  "Правила игры:",
                  "Управление стрелками",
                  "Для открытия дверей нужны ", "ключи, 1 ключ открывает только", "1 дверь, в правом верхнем углу",
                  " показано количество ключей", '', 'Удачи!']

    clock = pygame.time.Clock()
    fon = pygame.transform.scale(load_image('zast.png'), (width, height))
    screen.blit(fon, (0, 0))
    if sl == 550:
        font = pygame.font.Font(None, 40)
        text_coord = 20
    elif sl == 450:
        font = pygame.font.Font(None, 35)
        text_coord = 20
    elif sl == 350:
        font = pygame.font.Font(None, 30)
        text_coord = 20
    elif sl == 250:
        font = pygame.font.Font(None, 20)
        text_coord = 10
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    new_player, x, y = None, None, None
    keys = []
    doors = []
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                y2, x2 = y, x
                Tile('empty', x, y)
                new_player = Player(x, y)
            elif level[y][x] == 'k':
                Key(x, y)
                keys.append([x, y])
                Tile('empty', x, y)
            elif level[y][x] == 'd':
                Door(x, y)
                doors.append([x, y])
                Tile('empty', x, y)
            elif level[y][x] == 'e':
                Tile('exit', x, y)
    return new_player, x2, y2, keys, doors


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 2, tile_height * pos_y + 5)


class Key(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(key_group, all_sprites)
        self.image = key_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Door(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(door_group, all_sprites)
        self.image = door_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Выбор сложности')
    size = width, height = 350, 350
    screen = pygame.display.set_mode(size)
    FPS = 50
    intro_text = ["Выберите сложность игры:", "",
                  "1 - Очень легко",
                  "2 - Средне",
                  "3 - Сложно", "4 - Очень сложно"]
    clock = pygame.time.Clock()
    fon = pygame.transform.scale(load_image('zast.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 20
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    sl = 550
                    running = False
                if event.key == pygame.K_2:
                    sl = 450
                    running = False
                if event.key == pygame.K_3:
                    sl = 350
                    running = False
                if event.key == pygame.K_4:
                    sl = 250
                    running = False

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Лабиринт')
    size = width, height = sl, sl
    screen = pygame.display.set_mode(size)
    FPS = 50
    tile_images = {
        'wall': load_image('box.png'),
        'empty': load_image('grass.png'),
        'exit': load_image('exit.png')
    }
    player_image = load_image('mario.png', colorkey=-1)
    key_image = load_image('key.png', colorkey=-1)
    door_image = load_image('door.png')
    tile_width = tile_height = 50

    start_screen()
    run = True
    for leveln in range(1, 4):
        if not run:
            break
        else:
            all_sprites = pygame.sprite.Group()
            tiles_group = pygame.sprite.Group()
            player_group = pygame.sprite.Group()
            key_group = pygame.sprite.Group()
            door_group = pygame.sprite.Group()
            de = []
            num = 'map' + str(leveln) + '.txt'
            player, level_x, level_y, keys, doors = generate_level(load_level(num))
            k = (width // tile_width) // 2
            deone = [k - level_x, k - level_y]
            m = load_level(num)
            for i in range(len(m)):
                m[i] = list(m[i])
            mx = len(m[1])
            my = len(m)
            key = 0

            level = leveln
            while level == leveln:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        level = 0
                    if event.type == pygame.KEYDOWN:
                        if event.key in [pygame.K_UP, pygame.K_w]:
                            if level_y != 0:
                                if m[level_y - 1][level_x] == 'd' and key != 0:
                                    key -= 1
                                    for sprite in door_group:
                                        for sprite2 in player_group:
                                            if sprite.rect.x == sprite2.rect.x - 2 and sprite.rect.y == (
                                                    (sprite2.rect.y - 5) // tile_height - 1) * tile_height:
                                                sprite.kill()
                                    m[level_y - 1][level_x] = '.'
                                elif m[level_y - 1][level_x] == 'e':
                                    level += 1
                                elif m[level_y - 1][level_x] != '#' and m[level_y - 1][level_x] != 'd':
                                    level_y -= 1
                                    de = [0, -1]

                        if event.key in [pygame.K_RIGHT, pygame.K_d]:
                            if level_x != mx - 1:
                                if m[level_y][level_x + 1] == 'd' and key != 0:
                                    key -= 1
                                    for sprite in door_group:
                                        for sprite2 in player_group:
                                            if sprite.rect.x == ((
                                                                         sprite2.rect.x - 2) // tile_width + 1) * tile_width and sprite.rect.y == sprite2.rect.y - 5:
                                                sprite.kill()
                                    m[level_y][level_x + 1] = '.'
                                elif m[level_y][level_x + 1] == 'e':
                                    level += 1
                                elif m[level_y][level_x + 1] != '#' and m[level_y][level_x + 1] != 'd':
                                    level_x += 1
                                    de = [1, 0]

                        if event.key in [pygame.K_LEFT, pygame.K_a]:
                            if level_x != 0:
                                if m[level_y][level_x - 1] == 'd' and key != 0:
                                    key -= 1
                                    for sprite in door_group:
                                        for sprite2 in player_group:
                                            if sprite.rect.x == ((
                                                                         sprite2.rect.x - 2) // tile_width - 1) * tile_width and sprite.rect.y == sprite2.rect.y - 5:
                                                sprite.kill()
                                    m[level_y][level_x - 1] = '.'
                                elif m[level_y][level_x - 1] == 'e':
                                    level += 1
                                elif m[level_y][level_x - 1] != '#' and m[level_y][level_x - 1] != 'd':
                                    level_x -= 1
                                    de = [-1, 0]

                        if event.key in [pygame.K_DOWN, pygame.K_s]:
                            if level_y != my - 1:
                                if m[level_y + 1][level_x] == 'd' and key != 0:
                                    key -= 1
                                    for sprite in door_group:
                                        for sprite2 in player_group:
                                            if sprite.rect.x == sprite2.rect.x - 2 and sprite.rect.y == (
                                                    (sprite2.rect.y - 5) // tile_height + 1) * tile_height:
                                                sprite.kill()
                                    m[level_y + 1][level_x] = '.'
                                elif m[level_y + 1][level_x] == 'e':
                                    level += 1
                                elif m[level_y + 1][level_x] != '#' and m[level_y + 1][level_x] != 'd':
                                    level_y += 1
                                    de = [0, 1]
                for sprite in key_group:
                    for sprite2 in player_group:
                        if sprite.rect.x == sprite2.rect.x - 2 and sprite.rect.y == sprite2.rect.y - 5:
                            key += 1
                            sprite.kill()

                screen.fill(pygame.Color('Black'))
                if sum(de) != 0:
                    if de[0] == 0:
                        for sprite in tiles_group:
                            sprite.rect.y -= de[1] * 50
                        for sprite in key_group:
                            sprite.rect.y -= de[1] * 50
                        for sprite in door_group:
                            sprite.rect.y -= de[1] * 50
                    else:
                        for sprite in tiles_group:
                            sprite.rect.x -= de[0] * 50
                        for sprite in key_group:
                            sprite.rect.x -= de[0] * 50
                        for sprite in door_group:
                            sprite.rect.x -= de[0] * 50
                    de = [0, 0]
                if deone != [0, 0]:
                    for sprite in tiles_group:
                        sprite.rect.y += deone[1] * 50
                    for sprite in key_group:
                        sprite.rect.y += deone[1] * 50
                    for sprite in door_group:
                        sprite.rect.y += deone[1] * 50
                    for sprite in player_group:
                        sprite.rect.y += deone[1] * 50

                    for sprite in tiles_group:
                        sprite.rect.x += deone[0] * 50
                    for sprite in key_group:
                        sprite.rect.x += deone[0] * 50
                    for sprite in door_group:
                        sprite.rect.x += deone[0] * 50
                    for sprite in player_group:
                        sprite.rect.x += deone[0] * 50
                    deone = [0, 0]
                tiles_group.draw(screen)
                key_group.draw(screen)
                door_group.draw(screen)
                player_group.draw(screen)
                player_group.update()
                font = pygame.font.Font(None, 50)
                text = font.render(str(key), True, (100, 255, 100))
                screen.blit(text, (width - 33, 12))
                pygame.display.flip()
            if level == leveln + 1:
                end_screen(leveln)
    pygame.quit()
