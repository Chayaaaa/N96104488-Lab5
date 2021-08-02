import pygame
import os
from settings import WIN_WIDTH, WIN_HEIGHT
TOWER_IMAGE = pygame.image.load(os.path.join("images", "rapid_test.png"))
BUTTON_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "upgrade_menu.png")),(160,160))
UPGRADE_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "upgrade.png")),(40,25))
SELL_BTN_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("images", "sell.png")),(30,30))

class UpgradeMenu:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(TOWER_IMAGE, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.__buttons = [Button(UPGRADE_BTN_IMAGE,"upgrade",self.rect.centerx,self.rect.centery-65),Button(SELL_BTN_IMAGE,"sell",self.rect.centerx,self.rect.centery + 75),]  
        # (Q2) Add buttons here
        

    def draw(self, win):
        center_x = self.rect.centerx #coordinate of tower
        center_y = self.rect.centery
        win.blit(BUTTON_IMAGE ,(center_x-80,center_y-80))
        
       
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu

        # draw button
        # (Q2) Draw buttons here
        win.blit(UPGRADE_BTN_IMAGE ,(center_x-20,center_y-70))
        win.blit(SELL_BTN_IMAGE ,(center_x-15,center_y+45))

    def get_buttons(self):
        return self.__buttons
        

        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.image=image
        self.rect = self.image.get_rect()
        self.rect.center=(x, y)

    def clicked(self, x, y):
        
        if self.rect.collidepoint(x,y):
            return True
        else:
            return False
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        

    def response(self): 
        print(self.name)
        return self.name
       

        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        






