import pygame
import random

LANES = [60, 150, 250, 335]


def load(file, size):

    return pygame.transform.scale(
        pygame.image.load(file).convert_alpha(),
        size
    )


def load_assets(W, H):

    assets = {}

    assets["bg"] = load(
        "assets/AnimatedStreet.png",
        (W, H)
    )

    assets["player"] = load(
        "assets/Player.png",
        (50, 100)
    )

    assets["enemy"] = load(
        "assets/Enemy.png",
        (50, 100)
    )

    assets["obstacle"] = load(
        "assets/obstacle.png",
        (50, 50)
    )

    assets["coin"] = load(
        "assets/coin.png",
        (35, 35)
    )

    assets["nitro"] = load(
        "assets/nitro.png",
        (40, 40)
    )

    assets["shield"] = load(
        "assets/shield.png",
        (40, 40)
    )

    assets["repair"] = load(
        "assets/repair.png",
        (40, 40)
    )

    assets["coin_sound"] = pygame.mixer.Sound(
        "assets/coin_sound.mp3"
    )

    assets["crash_sound"] = pygame.mixer.Sound(
        "assets/crash.mp3"
    )

    return assets


def reset_game(assets):

    return {

        "assets": assets,

        "player": assets["player"].get_rect(
            center=(200, 450)
        ),

        "enemy": assets["enemy"].get_rect(
            center=(random.choice(LANES), -100)
        ),

        "obstacles": [],
        "coins": [],
        "powerups": [],

        "active_powers": {
            "nitro": 0,
            "shield": 0
        },
        "power_timer": 0,

        "speed": 5,
        "player_speed": 5,

        "bg1": 0,
        "bg2": -600,

        "score": 0,
        "coins_collected":0,
        "distance": 0
    }


def spawn_coin(g):

    rect = pygame.Rect(
        random.choice(LANES),
        -100,
        35,
        35
    )

    value=random.choice([1,3,5])

    g["coins"].append({
        "rect": rect,
        "value":value
    })


def spawn_power(g):

    types = ["nitro", "shield", "repair"]

    rect = pygame.Rect(
        random.choice(LANES),
        -100,
        40,
        40
    )

    g["powerups"].append(
        {
            "type": random.choice(types),
            "rect": rect
        }
    )


def update_game(g):

    a = g["assets"]

    keys = pygame.key.get_pressed()

    # движение игрока

    if keys[pygame.K_LEFT] and g["player"].left > 0:
        g["player"].x -= g["player_speed"]

    if keys[pygame.K_RIGHT] and g["player"].right < 400:
        g["player"].x += g["player_speed"]

    # дистанция

    g["distance"] += 0.05

    # движение дороги

    g["bg1"] += g["speed"]
    g["bg2"] += g["speed"]

    if g["bg1"] >= 600:
        g["bg1"] = -600

    if g["bg2"] >= 600:
        g["bg2"] = -600

    # ---------------- ENEMY ----------------

    # ---------------- ENEMY ----------------
    g["enemy"].y += g["speed"] + 1

    if g["player"].colliderect(g["enemy"]):
        # Проверяем, активен ли таймер щита в нашем новом словаре
        if g["active_powers"]["shield"] > 0:
            g["active_powers"]["shield"] = 0  # Щит тратится
            g["enemy"].center = (random.choice(LANES), -100) # Враг исчезает
        else:
            return "game_over" # Если щита нет — конец игры

    if g["enemy"].top > 600:

        g["enemy"].center = (
            random.choice(LANES),
            -100
        )

        g["score"] += 1

    # ---------------- SPAWN ----------------

    if random.randint(1, 100) < 2:
        spawn_coin(g)

    if random.randint(1, 200) < 2:
        spawn_power(g)

    if random.randint(1, 120) < 2:

        rect = pygame.Rect(
            random.choice(LANES),
            -100,
            50,
            50
        )

        g["obstacles"].append(rect)

    # ---------------- COINS ----------------

    for c in g["coins"][:]:

        c["rect"].y += g["speed"]

        if g["player"].colliderect(c["rect"]):

            a["coin_sound"].play()

            g["score"] += c["value"]

            g["coins_collected"]+=1

            g["coins"].remove(c)

        elif c["rect"].top > 600:

            g["coins"].remove(c)

    # ---------------- POWERUPS ----------------

    for p in g["powerups"][:]:

        p["rect"].y += g["speed"]

        if g["player"].colliderect(p["rect"]):
            if p["type"] == "nitro":
                g["active_powers"]["nitro"] = 300
                g["speed"] += 3
                g["player_speed"] = 8

            elif p["type"] == "shield":
                g["active_powers"]["shield"] = 3000 # наш долгий щит

            elif p["type"] == "repair":
                g["obstacles"].clear() # чинит мгновенно

            g["powerups"].remove(p)

        
    # ---------------- OBSTACLES ----------------

    # ---------------- OBSTACLES ----------------
    for o in g["obstacles"][:]:
        o.y += g["speed"]

        if g["player"].colliderect(o):
            # Проверяем таймер щита
            if g["active_powers"]["shield"] > 0:
                g["active_powers"]["shield"] = 0 # Щит тратится
                g["obstacles"].remove(o) # Препятствие удаляется
            else:
                return "game_over"

        elif o.top > 600:
            g["obstacles"].remove(o)

    # ускорение каждые 5 монет

    if g["coins_collected"] % 5 == 0 and g["coins_collected"] != 0:
        g["speed"] += 0.02

    # ---------------- TIMER ----------------

    # Логика для Нитро
    if g["active_powers"]["nitro"] > 0:
        g["active_powers"]["nitro"] -= 1
        if g["active_powers"]["nitro"] == 0:
            g["speed"] -= 3
            g["player_speed"] = 5

    # Логика для Щита
    if g["active_powers"]["shield"] > 0:
        g["active_powers"]["shield"] -= 1


def draw_game(screen, g):

    a = g["assets"]

    screen.blit(a["bg"], (0, g["bg1"]))
    screen.blit(a["bg"], (0, g["bg2"]))

    screen.blit(a["player"], g["player"])
    if g["active_powers"]["shield"] > 0:
        pygame.draw.circle(screen, (0, 255, 255), g["player"].center, 60, 3)
    screen.blit(a["enemy"], g["enemy"])

    for o in g["obstacles"]:
        screen.blit(a["obstacle"], o)

    for c in g["coins"]:
        screen.blit(a["coin"], c["rect"])

    for p in g["powerups"]:

        if p["type"] == "nitro":
            img = a["nitro"]

        elif p["type"] == "shield":
            img = a["shield"]

        else:
            img = a["repair"]

        screen.blit(img, p["rect"])

    font = pygame.font.SysFont("Verdana", 18)

    screen.blit(
        font.render(
            f"Score: {g['score']}",
            True,
            (0, 0, 0)
        ),
        (10, 10)
    )
    screen.blit(
    font.render(
        f"Coins: {g['coins_collected']}",
        True,
        (0, 0, 0)
    ),
    (10, 100)
)

    screen.blit(
        font.render(
            f"Distance: {int(g['distance'])}",
            True,
            (0, 0, 0)
        ),
        (10, 40)
    )

    screen.blit(
        font.render(
            f"Power: {g['active_powers']}",
            True,
            (0, 0, 0)
        ),
        (10, 70)
    )