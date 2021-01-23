import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from alien import Alien
from scoreboard import Scoreboard
import game_function as gf

def run_game():
    # 游戏初始化
    pygame.init()
    # 创建一个窗口对象
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))


    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)


    # 创建存储游戏统计信息的实例，并创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)


    #创建ship对象，将屏幕对象做为参数传入
    ship=Ship(screen,ai_settings)
    #创建子弹编组对象
    bullets=Group()
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    alien = Alien(ai_settings, screen)

    pygame.mixer.init()

    pygame.mixer.music.load(r'music/aaa.mp3')

    pygame.mixer.music.play()
    # 游戏主循环
    while True:
        # 事件驱动
        # 循环检查所有事件,封装成了函数


        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)

        if stats.game_active:
            ship.update()

            bullets.update()

            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)

            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)

            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
 play_button)

            # 更新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)



run_game()
