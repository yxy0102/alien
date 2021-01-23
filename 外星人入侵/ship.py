import pygame
from pygame.sprite import Sprite



class Ship(Sprite):

    def __init__(self,screen,ai_settings):
        super(Ship, self).__init__()
        #使飞船对象拥有screen属性
        self.screen=screen
        self.ai_settings=ai_settings
        #加载飞船图像
        self.image=pygame.image.load("image/bbb.png")
        #飞船的外接矩形rectangle
        self.rect=self.image.get_rect()
        #屏幕screen的外接矩阵
        self.screen_rect=screen.get_rect()

        #飞船初始位置：横向剧中，纵向底部对齐
        #飞船矩形中心点横坐标x=窗口中心横坐标x
        self.rect.centerx=self.screen_rect.centerx

        #飞船矩形底部从坐标y
        self.rect.bottom=self.screen_rect.bottom
        #存储为浮点型
        self.center = float(self.rect.centerx)

        #飞船正在向右移动的标志
        self.moving_right=False
        self.moving_left=False


    #在指定位置绘制飞船
    def blitem(self):
        self.screen.blit(self.image,self.rect)

    #飞船移动函数
    def update(self):
        if self.moving_right  and self.rect.right < self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        #self.center是中间变量
        self.rect.centerx=self.center

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx