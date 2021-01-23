from pygame.sprite import Sprite



class Bgcolor(Sprite):
    def update(self):

        # 1. 调用父类的方法实现
        super().update()

        # 2. 判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

    def __create_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = Background("./image/ccc.png")
        bg2 = Background("./image/ccc.png")
        bg2.rect.y = -bg2.rect.height

        self.back_group = pygame.sprite.Group(bg1, bg2)

