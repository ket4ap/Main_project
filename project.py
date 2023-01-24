###########################################################LIBRARIES#######################################################################

import pygame
from random import randint

###########################################################END OF LIBRARIES#######################################################################





###########################################################MAIN VARIABLES#######################################################################

FPS = 60
WIDTH = 400
HEIGHT = 400
Game_over = False

###########################################################END OF MAIN VARIABLES#######################################################################




############################################################CLASSES#######################################################################

class Main_character:

    main_characketers = []

    def __init__(self):
        self.name = "lox"
        self.armor = 0
        self.level = 0
        self.health = 100
        self.damage = 7
        Main_character.main_characketers.append(self)


    def Main_character_info(self):
        for i in Main_character.main_characketers:
            print("Имя героя: ", i.name)
            print("Здоровье героя: ", i.health)
            print("Урон героя: ", i.damage)
            print()


    def Die(self):
        Main_character.main_characketers.pop(0)
        print("Вы погибли")
        print()


    def attack(self):
        Enemy.enemys[0].health -= self.damage
        


class Enemy:

    enemys = []
    Enemy_names = ["Неуч", "Ихний", "Евоный", "Клякса", "Корневик", "Плюсер", "Озлобленный Двоечник"]
    kol_Enemy_names = len(Enemy_names) - 1

    def __init__(self):
        self.name = self.Enemy_names[randint(0, self.kol_Enemy_names)]
        self.armor = 0
        self.level = 0
        self.health = 100
        self.damage = self.level * 3
        Enemy.enemys.append(self)


    def Enemys_info(self):
        num_enemy = 0
        for i in Enemy.enemys:
            num_enemy += 1
            print("Имя ", num_enemy, "монстра ", i.name)
            print("Здоровье ", num_enemy, "монстра ", i.health)
            print()
            

    def attack(self):
        Main_character.main_characketers[0].health -= self.damage


    def Die(self):
        Enemy.enemys.pop(0)

    

class Enemy_boss:
    pass

#########################################################END OF CLASSES######################################################################





##########################################################LEVELS#######################################################################

GG = Main_character()


def level_addition():

    level_complete = False
    num_level = 0

    for num_level in range(1):

        num_level +=1
        enemy = Enemy()

        while (level_complete == False):

            diapason = 99
            numeral_1 :int = randint(0, diapason)
            numeral_2 :int = randint(0, diapason)
            
            while (numeral_2 + numeral_1 > diapason + 1):
                numeral_2 = randint(1, 999)

            print(numeral_1, " + ", numeral_2, " =  ?")
            calculate :int = numeral_1 + numeral_2
            answer = int(input())
            print("Твоё решение: ", numeral_1, " + ", numeral_2, " =  ", answer)

            if (answer == calculate):
                GG.attack()
                print("Правильно, вы наносите урон ", GG.damage, "!")
            if (answer != calculate):
                enemy.attack()
                print("Неверно, вы получаете урон ", enemy.damage, "!")

            if (enemy.health <= 0):
                enemy.Die()
                level_complete = True
                print("Вы завершили ", num_level,  "уровень")

    print("Вы завершили все уровни, впереди лишь босс!!!")
    enemy_boss = Enemy()
    boss_level_complete = False

    while (boss_level_complete == False):

        diapason = 99
        numeral_1 :int = randint(0, diapason)
        numeral_2 :int = randint(0, diapason)
            
        while (numeral_2 + numeral_1 > 1000):
            numeral_2 = randint(1, 999)

        print(numeral_1, " + ", numeral_2, " =  ?")
        calculate :int = numeral_1 + numeral_2
        answer = int(input())
        print("Твоё решение: ", numeral_1, " + ", numeral_2, " =  ", answer)

        if (answer == calculate):
            GG.attack()
            print("Правильно, вы наносите урон ", GG.damage, "!")
        if (answer != calculate):
            enemy_boss.attack()
            print("Неверно, вы получаете урон ", enemy_boss.damage, "!")

        if (enemy_boss.health <= 0):
            enemy_boss.Die()
            boss_level_complete = True


level_addition()

###########################################################END OF LEVELS#######################################################################





""""
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Kills")

while (Game_over == False):
    pass

pygame.quit()
quit()
"""""





