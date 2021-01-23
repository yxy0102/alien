import  pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        #执行基类的构造函数
        super(Bullet, self).__init__()
        self.screen=screen

        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        #子弹的横向位置在飞船中心
        self.rect.centerx=ship.rect.centerx
        #子弹的顶端与飞船顶端对齐
        self.rect.top=ship.rect.top
        #子弹的纵坐标
        self.y=float(self.rect.y)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self):
        #浮点类型的中间变量
        self.y-=self.speed_factor
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)