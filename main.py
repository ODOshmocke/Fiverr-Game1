import random
import sys
import time

import pygame
import numpy as np


pygame.init()
screen = pygame.display.set_mode((496, 496))
pygame.display.set_caption('Number game')
game_active = False
font = pygame.font.Font('CODE Bold.otf', 22)
font_big = pygame.font.Font('CODE Bold.otf', 100)
font80 = pygame.font.Font('CODE Bold.otf', 60)
timer = pygame.time.Clock()
button_size = (80, 80)
button_enabled = True
button1_enabled = True
button2_enabled = True
button3_enabled = True
button4_enabled = True
button5_enabled = True
button6_enabled = True
button7_enabled = True
button8_enabled = True
button9_enabled = True
button11_enabled = True
button12_enabled = True
button13_enabled = True
button14_enabled = True
button15_enabled = True
button16_enabled = True
button17_enabled = True
button18_enabled = True
button19_enabled = True
button10_enabled = True
button20_enabled = True
distance_range_1 = 16
distance_range_2 = 112
distance_range_3 = 208
distance_range_4 = 304
distance_range_5 = 400

raw_lst = []
text_loose = 'you lost'
shuffle_numbers = pygame.USEREVENT + 1

show_duration = pygame.USEREVENT + 3
pygame.time.set_timer(shuffle_numbers, 5000)
shuffle_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
nummer = 0
lst = shuffle_lst
position_list = [(distance_range_1,distance_range_1), (distance_range_1, distance_range_2), (distance_range_1, distance_range_3), (distance_range_1, distance_range_4), (distance_range_2, distance_range_1), (distance_range_3, distance_range_1), (distance_range_4, distance_range_1), (distance_range_5, distance_range_1), (distance_range_2, distance_range_2), (distance_range_3, distance_range_2), (distance_range_4, distance_range_2), (distance_range_5, distance_range_2), (distance_range_2, distance_range_3), (distance_range_3, distance_range_3), (distance_range_4, distance_range_3), (distance_range_5, distance_range_3), (distance_range_2, distance_range_4), (distance_range_3, distance_range_4), (distance_range_4, distance_range_4), (distance_range_5, distance_range_4)]
game_time = 30
win = False
lost = False
first_round = False
class Button:
    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.draw()
        self.new_press = True



    def draw(self):
        button_text = font.render(self.text, True, 'white')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), button_size)
        if self.enabled:
            if self.check_click():
                #pygame.draw.rect(screen, 'blue', button_rect, 0, 5)
                raw_lst.append(int(self.text))


                button_text = font.render(self.text, True, 'white')
            else: pygame.draw.rect(screen,  'light gray', button_rect, 0, 5)
        else:
            pygame.draw.rect(screen, 'black', button_rect, 0, 5)



        screen.blit(button_text, (self.x_pos+ 32 , self.y_pos + 32))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (100, 100))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:return False


class Button_game_of:
    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.draw()
        self.new_press = True
        # self.button_enabled

    def draw(self):
        button_text = font.render(self.text, True, 'white')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), button_size)
        if self.enabled:
            if self.check_click():


            # pygame.draw.rect(screen, 'blue', button_rect, 0, 5)
                game_time = int(self.text)
                return game_time


            else:
                pygame.draw.rect(screen, 'light gray', button_rect, 0, 5)
        else:
            pygame.draw.rect(screen, 'black', button_rect, 0, 5)

        screen.blit(button_text, (self.x_pos + 20, self.y_pos + 32))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (100, 100))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

class Button_start_game:
    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.draw()
        self.new_press = True
        # self.button_enabled

    def draw(self):
        button_text = font.render(self.text, True, 'white')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), button_size)
        if self.enabled:
            if self.check_click():
                if self.text == 'Start':
                    game_active = True



                    pygame.time.set_timer(show_duration, 1000)

                    return game_active


            else:
                pygame.draw.rect(screen, 'light gray', button_rect, 0, 5)
        else:
            pygame.draw.rect(screen, 'black', button_rect, 0, 5)

        screen.blit(button_text, (self.x_pos + 12, self.y_pos + 32))

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (100, 100))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False




def disable_button(new_press, button, button_enabled):
    global game_time
    global win
    if pygame.mouse.get_pressed()[0] and new_press:

        if button.check_click():
            if button_enabled:

                if len(raw_lst) > 1:
                    difference = np.diff(raw_lst)
                    for number in difference:
                        if number > 1:


                            game_time -= 5
                            pygame.time.wait(100)
                            del raw_lst[-1]
                            return True

                if len(raw_lst) == 1:
                    if raw_lst[0] != 1:

                        game_time -= 5
                        pygame.time.wait(100)
                        del raw_lst[-1]

                        return True
                if 20 in raw_lst and not 19:
                    return True
                else:

                    return False



                #if 20 in raw_lst and 19 in raw_lst:
                #    win = True
                #else: win = False





while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.QUIT
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                click = True
        else: click = False

        if event.type == shuffle_numbers:
            position_list = [(distance_range_1, distance_range_1)]
            shuffle_lst = [(distance_range_1, distance_range_2),
                           (distance_range_1, distance_range_3), (distance_range_1, distance_range_4),
                           (distance_range_2, distance_range_1), (distance_range_3, distance_range_1),
                           (distance_range_4, distance_range_1), (distance_range_5, distance_range_1),
                           (distance_range_2, distance_range_2), (distance_range_3, distance_range_2),
                           (distance_range_4, distance_range_2), (distance_range_5, distance_range_2),
                           (distance_range_2, distance_range_3), (distance_range_3, distance_range_3),
                           (distance_range_4, distance_range_3), (distance_range_5, distance_range_3),
                           (distance_range_2, distance_range_4), (distance_range_3, distance_range_4),
                           (distance_range_4, distance_range_4), (distance_range_5, distance_range_4)]
            random.shuffle(shuffle_lst)
            for k in shuffle_lst:
                position_list.append(k)



        if event.type == show_duration:
            game_time -= 1




    if game_active:
        if game_time <= 0:
            lost = True
            game_active = False
        else: win = True
        first_round = True

        screen.fill('darkgray')

        display_time_left_surf = font_big.render(f'{game_time}', True, 'Black')
        display_time_left = screen.blit(display_time_left_surf, (200, 389))




        mybutton1 = Button(f'1', position_list[0][0], position_list[0][1], button1_enabled)
        mybutton2 = Button(f'2', position_list[1][0], position_list[1][1], button2_enabled)
        mybutton3 = Button(f'3', position_list[2][0], position_list[2][1], button3_enabled)
        mybutton4 = Button(f'4', position_list[3][0], position_list[3][1], button4_enabled)
        mybutton5 = Button(f'5', position_list[4][0], position_list[4][1], button5_enabled)
        mybutton6 = Button(f'6', position_list[5][0], position_list[5][1], button6_enabled)
        mybutton7 = Button(f'7', position_list[6][0], position_list[6][1], button7_enabled)
        mybutton8 = Button(f'8', position_list[7][0], position_list[7][1], button8_enabled)
        mybutton9 = Button(f'9', position_list[8][0], position_list[8][1], button9_enabled)
        mybutton10 = Button(f'10', position_list[9][0], position_list[9][1], button10_enabled)
        mybutton11 = Button(f'11', position_list[10][0], position_list[10][1], button11_enabled)
        mybutton12 = Button(f'12', position_list[11][0], position_list[11][1], button12_enabled)
        mybutton13 = Button(f'13', position_list[12][0], position_list[12][1], button13_enabled)
        mybutton14 = Button(f'14', position_list[13][0], position_list[13][1], button14_enabled)
        mybutton15 = Button(f'15', position_list[14][0], position_list[14][1], button15_enabled)
        mybutton16 = Button(f'16', position_list[15][0], position_list[15][1], button16_enabled)
        mybutton17 = Button(f'17', position_list[16][0], position_list[16][1], button17_enabled)
        mybutton18 = Button(f'18', position_list[17][0], position_list[17][1], button18_enabled)
        mybutton19 = Button(f'19', position_list[18][0], position_list[18][1], button19_enabled)
        mybutton20 = Button(f'20', position_list[19][0], position_list[19][1], button20_enabled)




        lock1 = disable_button(new_press=True, button=mybutton1, button_enabled=button1_enabled, )
        lock2 = disable_button(new_press=True, button=mybutton2, button_enabled=button2_enabled, )
        lock3 = disable_button(new_press=True, button=mybutton3, button_enabled=button3_enabled, )
        lock4 = disable_button(new_press=True, button=mybutton4, button_enabled=button4_enabled, )
        lock5 = disable_button(new_press=True, button=mybutton5, button_enabled=button5_enabled, )
        lock6 = disable_button(new_press=True, button=mybutton6, button_enabled=button6_enabled, )
        lock7 = disable_button(new_press=True, button=mybutton7, button_enabled=button7_enabled, )
        lock8 = disable_button(new_press=True, button=mybutton8, button_enabled=button8_enabled, )
        lock9 = disable_button(new_press=True, button=mybutton9, button_enabled=button9_enabled, )
        lock10 = disable_button(new_press=True, button=mybutton10, button_enabled=button10_enabled, )
        lock11 = disable_button(new_press=True, button=mybutton11, button_enabled=button11_enabled, )
        lock12 = disable_button(new_press=True, button=mybutton12, button_enabled=button12_enabled, )
        lock13 = disable_button(new_press=True, button=mybutton13, button_enabled=button13_enabled, )
        lock14 = disable_button(new_press=True, button=mybutton14, button_enabled=button14_enabled, )
        lock15 = disable_button(new_press=True, button=mybutton15, button_enabled=button15_enabled, )
        lock16 = disable_button(new_press=True, button=mybutton16, button_enabled=button16_enabled, )
        lock17 = disable_button(new_press=True, button=mybutton17, button_enabled=button17_enabled, )
        lock18 = disable_button(new_press=True, button=mybutton18, button_enabled=button18_enabled, )
        lock19 = disable_button(new_press=True, button=mybutton19, button_enabled=button19_enabled, )
        lock20 = disable_button(new_press=True, button=mybutton20, button_enabled=button20_enabled)




        if mybutton20 != None:
            win = mybutton20.draw()

        if win:
            game_active = False

        if lock1 != None: button1_enabled = lock1
        if lock2 != None: button2_enabled = lock2
        if lock3 != None: button3_enabled = lock3
        if lock4 != None: button4_enabled = lock4
        if lock5 != None: button5_enabled = lock5
        if lock6 != None: button6_enabled = lock6
        if lock7 != None: button7_enabled = lock7
        if lock8 != None: button8_enabled = lock8
        if lock9 != None: button9_enabled = lock9
        if lock10 != None: button10_enabled = lock10
        if lock11 != None: button11_enabled = lock11
        if lock12 != None: button12_enabled = lock12
        if lock13 != None: button13_enabled = lock13
        if lock14 != None: button14_enabled = lock14
        if lock15 != None: button15_enabled = lock15
        if lock16 != None: button16_enabled = lock16
        if lock17 != None: button17_enabled = lock17
        if lock18 != None: button18_enabled = lock18
        if lock19 != None: button19_enabled = lock19
        if lock20 != None: button20_enabled = lock20
    else:


        if lost:
            game_time = 30

        screen.fill('gray')
        pygame.time.set_timer(show_duration, 1000000000)

        start_button = Button_start_game('Start', 200, 210, True)
        if start_button.draw() != None:
            game_active = start_button.draw()
            lost = False
            win = False
            pygame.time.wait(100)


        sec_button30 = Button_game_of('30', 350, 110, True)
        sec_button45 = Button_game_of('45', 350, 210, True)
        sec_button60 = Button_game_of('60', 350, 310, True)

        if sec_button30.draw() != None: game_time = sec_button30.draw()
        if sec_button45.draw() != None: game_time = sec_button45.draw()
        if sec_button60.draw() != None: game_time = sec_button60.draw()
        GAME_TIME = game_time

        button_text = font.render(f'Time: {game_time}', True, 'white')
        screen.blit(button_text, (350, 80))
        if first_round:
            if lost:
                screen_text_loose_surf = font80.render(text_loose, True, 'White')
                screen.blit(screen_text_loose_surf, (40, 80))


            if win:
                screen_text_loose_surf = font80.render('YOU WON!!!', True, 'White')
                screen.blit(screen_text_loose_surf, (40, 80))




        button_enabled = True
        button1_enabled = True
        button2_enabled = True
        button3_enabled = True
        button4_enabled = True
        button5_enabled = True
        button6_enabled = True
        button7_enabled = True
        button8_enabled = True
        button9_enabled = True
        button11_enabled = True
        button12_enabled = True
        button13_enabled = True
        button14_enabled = True
        button15_enabled = True
        button16_enabled = True
        button17_enabled = True
        button18_enabled = True
        button19_enabled = True
        button10_enabled = True
        button20_enabled = True
        raw_lst = []
        shuffle_numbers = pygame.USEREVENT + 1
        pygame.time.set_timer(shuffle_numbers, 10000)
        shuffle_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        nummer = 0
        lst = shuffle_lst
        position_list = [(distance_range_1, distance_range_1)]
        shuffle_lst = [(distance_range_1, distance_range_2),
                       (distance_range_1, distance_range_3), (distance_range_1, distance_range_4),
                       (distance_range_2, distance_range_1), (distance_range_3, distance_range_1),
                       (distance_range_4, distance_range_1), (distance_range_5, distance_range_1),
                       (distance_range_2, distance_range_2), (distance_range_3, distance_range_2),
                       (distance_range_4, distance_range_2), (distance_range_5, distance_range_2),
                       (distance_range_2, distance_range_3), (distance_range_3, distance_range_3),
                       (distance_range_4, distance_range_3), (distance_range_5, distance_range_3),
                       (distance_range_2, distance_range_4), (distance_range_3, distance_range_4),
                       (distance_range_4, distance_range_4), (distance_range_5, distance_range_4)]
        random.shuffle(shuffle_lst)
        for k in shuffle_lst:
            position_list.append(k)

    timer.tick(60)
    pygame.display.update()