from collections import deque
from tkinter import *
from PIL import Image, ImageTk
import random
import pygame

player1_moves = deque()
player2_moves = deque()
choice1 = ""
choice2 = ""
nick1 = ""
nick2 = ""
nick3 = ""
nick4 = ""
tourney = [nick1, nick2, nick3, nick4]
player11_name = ""
player22_name = ""
tournament_mode = False


def to_start_game():
    menu_f.pack_forget()
    start_game_f.pack()


def to_options():
    menu_f.pack_forget()
    options_f.pack()


def to_pvp_name():
    start_game_f.pack_forget()
    choose_name.pack()


def to_pvp_1():
    global label_player1, label_player2, player1_hp, player2_hp, last_attack1, last_attack2
    global player11_name, player22_name
    start_game_f.pack_forget()
    if not tournament_mode:
        player1_text_pvp.config(text="Player 1")
        player2_text_pvp.config(text="Player 2")
    pvp_f.pack()
    label_player1 = label_player1_pvp
    label_player2 = label_player2_pvp
    player1_hp = player1_hp_pvp
    player2_hp = player2_hp_pvp
    last_attack1 = last_attack1_pvp
    last_attack2 = last_attack2_pvp


def to_pvp_2():
    global nick1, nick2, nick3, nick4, tourney, player11_name, player22_name, tournament_mode
    nick1 = name1.get()
    nick2 = name2.get()
    nick3 = name3.get()
    nick4 = name4.get()
    player11_name = nick1
    player22_name = nick2
    tournament_mode = True
    player1_text_pvp.config(text=player11_name)
    player2_text_pvp.config(text=player22_name)
    tourney = [nick1, nick2, nick3, nick4]
    choose_name.pack_forget()
    to_pvp_1()


def option1_dark_mode():
    root.configure(bg="black")
    pvp_f.configure(bg="black")
    pve_f.configure(bg="black")
    options_f.configure(bg="black")
    menu_f.configure(bg="black")
    choose_name.configure(bg="black")
    player3_name.configure(bg="black", fg="white")
    player4_name.configure(bg="black", fg="white")
    start_game_f.configure(bg="black")
    options_lab1.configure(bg="black", fg="white")
    label_player1_pve.configure(bg="black", fg="white")
    label_player2_pve.configure(bg="black", fg="white")
    label_player1_pvp.configure(bg="black", fg="white")
    label_player2_pvp.configure(bg="black", fg="white")
    choose_nick.configure(bg="black", fg="white")
    menu_lab.configure(background="black", fg="white")
    options_lab2.configure(background="black", fg="white")
    attack_chosen1_pvp.configure(bg="black", fg="white")
    attack_chosen2_pvp.configure(bg="black", fg="white")
    attack_chosen1_pvp.configure(bg="black", fg="white")
    attack_chosen2_pvp.configure(bg="black", fg="white")
    player1_name.configure(bg="black", fg="white")
    player2_name.configure(bg="black", fg="white")
    player1_text_pvp.configure(bg="black", fg="white")
    player2_text_pvp.configure(bg="black", fg="white")
    player1_text_pve.configure(bg="black", fg="white")
    player2_text_pve.configure(bg="black", fg="white")
    player1_hp_pvp.configure(bg="black", fg="white")
    player2_hp_pvp.configure(bg="black", fg="white")
    player1_hp_pve.configure(bg="black", fg="white")
    player2_hp_pve.configure(bg="black", fg="white")
    set_btn_lab.configure(bg="black", fg="white")
    choose_w_size.configure(bg="black")
    choose_button.configure(bg="black")
    choose_size_lab.configure(bg="black", fg="white")


def option1_light_mode():
    root.configure(bg="white")
    pvp_f.configure(bg="white")
    pve_f.configure(bg="white")
    options_f.configure(bg="white")
    menu_f.configure(bg="white")
    player3_name.configure(bg="white", fg="black")
    player4_name.configure(bg="white", fg="black")
    choose_name.configure(bg="white")
    start_game_f.configure(bg="white")
    choose_nick.configure(bg="white", fg="black")
    options_lab1.configure(bg="white", fg="black")
    label_player1_pve.configure(bg="white", fg="black")
    label_player2_pve.configure(bg="white", fg="black")
    label_player1_pvp.configure(bg="white", fg="black")
    label_player2_pvp.configure(bg="white", fg="black")
    menu_lab.configure(bg="white", fg="black")
    options_lab2.configure(bg="white", fg="black")
    attack_chosen1_pvp.configure(bg="white", fg="black")
    attack_chosen2_pvp.configure(bg="white", fg="black")
    attack_chosen1_pvp.configure(bg="white", fg="black")
    attack_chosen2_pvp.configure(bg="white", fg="black")
    player1_name.configure(bg="white", fg="black")
    player2_name.configure(bg="white", fg="black")
    player1_text_pvp.configure(bg="white", fg="black")
    player2_text_pvp.configure(bg="white", fg="black")
    player1_text_pve.configure(bg="white", fg="black")
    player2_text_pve.configure(bg="white", fg="black")
    player1_hp_pvp.configure(bg="white", fg="black")
    player2_hp_pvp.configure(bg="white", fg="black")
    player1_hp_pve.configure(bg="white", fg="black")
    player2_hp_pve.configure(bg="white", fg="black")
    set_btn_lab.configure(bg="white", fg="black")
    choose_w_size.configure(bg="white")
    choose_button.configure(bg="white")
    choose_size_lab.configure(bg="white", fg="black")


def option2():
    pygame.mixer.music.load("battle_music.mp3")
    pygame.mixer.music.play(-1)


def option2_stop():
    pygame.mixer.music.stop()


def change_window_size(width, height):
    if width == 800:
        root.geometry('800x400')
    elif width == 900:
        root.geometry('900x500')
    else:
        root.geometry('1920x1080')

    root.configure(width=width, height=height)
    pvp_f.configure(width=width, height=height)
    pve_f.configure(width=width, height=height)
    menu_f.configure(width=width, height=height)
    pvp_f.configure(width=width, height=height)
    start_game_f.configure(width=width, height=height)
    options_f.configure(width=width, height=height)
    choose_name.configure(width=width, height=height)
    choose_w_size.pack_forget()
    options_f.pack()


def change_skin(color1, color2):
    btn_start_battle_pve.configure(bg=color1, fg=color2)
    btn_start_battle_pvp.configure(bg=color1, fg=color2)
    choose_button.pack_forget()
    options_f.pack()


def to_pve():
    global label_player1, label_player2, player1_hp, player2_hp, last_attack1, last_attack2,\
        player11_name, player22_name
    start_game_f.pack_forget()
    pve_f.pack(fill="both", expand=True)
    label_player1 = label_player1_pve
    label_player2 = label_player2_pve
    player1_hp = player1_hp_pve
    player2_hp = player2_hp_pve
    last_attack1 = last_attack1_pve
    last_attack2 = last_attack2_pve
    player11_name = "Player 1"
    player22_name = "COMPUTER"


def to_menu_from_pvp():
    global player1_moves, player2_moves, choice1, choice2
    player1_moves.clear()
    player2_moves.clear()
    pvp_f.pack_forget()
    menu_f.pack(fill="both", expand=True)
    player1_hp['text'] = "100"
    player2_hp['text'] = "100"
    label_player1.configure(image=new_image1)
    label_player2.configure(image=new_image2)
    last_attack1_pvp.configure(text="")
    last_attack2_pvp.configure(text="")
    choice1 = choice2 = ''


def to_menu_from_pve():
    global player1_moves, player2_moves, choice1, choice2
    player1_moves.clear()
    player2_moves.clear()
    pve_f.pack_forget()
    menu_f.pack(fill="both", expand=True)
    player1_hp['text'] = "100"
    player2_hp['text'] = "100"
    label_player1.configure(image=new_image1)
    label_player2.configure(image=new_image2)
    last_attack1_pve.configure(text="")
    last_attack2_pve.configure(text="")
    choice1 = choice2 = ''


def to_menu_from_options():
    options_f.pack_forget()
    menu_f.pack(fill="both", expand=True)


def to_choose_skin():
    options_f.pack_forget()
    choose_button.pack(fill="both", expand=True)


def to_change_size():
    options_f.pack_forget()
    choose_w_size.pack(fill="both", expand=True)


def close():
    print("Exit game")
    root.destroy()
    root.quit()


def reset_for_tournament():
    global player1_moves, player2_moves, tourney, player11_name, player22_name, choice1, choice2
    player1_moves.clear()
    player2_moves.clear()
    player1_hp['text'] = "100"
    player2_hp['text'] = "100"
    label_player1.configure(image=new_image1)
    label_player2.configure(image=new_image2)
    player11_name = tourney[-2]
    player22_name = tourney[-1]
    player1_text_pvp.config(text=player11_name)
    player2_text_pvp.config(text=player22_name)
    choice1 = choice2 = ''


def open_popup(player, t):   #pop up window shows the battles winner
    global tournament_mode
    popup = Toplevel(root)
    popup.geometry("300x150")
    root_x = root.winfo_rootx()
    root_y = root.winfo_rooty()
    popup_x = root_x + 400
    popup_y = root_y + 200
    popup.geometry(f'+{popup_x}+{popup_y}')
    popup.config(bg="black")
    winner_player = Label(popup, text=player, font=('Arial', 20, 'bold'), fg="gold", bg='black')
    winner_player.pack()
    end = Label(popup, text="HAS WON THE TOURNAMENT!", font=('Arial', 15, 'bold'), fg="white", bg='black')
    end.pack()
    if t == 0:
        popup.config(bg="white")
        winner_player.config(text=player, font=('Arial', 18, 'bold'), fg="black", bg='white')
        end.config(text=" HAS WON THE FIGHT!", font=('Arial', 15, 'bold'), fg="black", bg='white')
    ok_button = Button(popup, text="OK", command=popup.destroy)
    ok_button.pack()


def hp_update_p1():
    new_hp = int(player1_hp['text'])
    new_hp = new_hp - 10
    player1_hp['text'] = str(new_hp)
    if new_hp <= 0:
        label_player1.configure(image=image_death)
        print(len(tourney))
        if len(tourney)-1 > 1 or not tournament_mode:
            open_popup(player22_name, 0)
        if tournament_mode:
            change_round(player11_name)


def hp_update_p2():
    new_hp = int(player2_hp['text'])
    new_hp = new_hp - 10
    player2_hp['text'] = str(new_hp)
    if new_hp <= 0:
        label_player2.configure(image=image_death)
        print(len(tourney))
        if len(tourney)-1 > 1 or not tournament_mode:
            open_popup(player11_name, 0)
        if tournament_mode:
            change_round(player22_name)


def show_last_attack(a, b):
    last_attack1["text"] = a
    last_attack2["text"] = b


def winner_check():   #checks who won the round
    c1 = choice1
    if pve_f.winfo_ismapped():
        bot_ai()
    c2 = choice2
    show_last_attack(c1, c2)
    if c1 == c2:
        label_player1.configure(image=new_image1)
        label_player2.configure(image=new_image2)
        queue1(c1)
        queue2(c2)
    elif c1 == "sword":
        if c2 == "uppercut":
            label_player1.configure(image=image_w_sword1)
            label_player2.configure(image=image_hurt2)
            hp_update_p2()
            queue1(c1)
            queue2(c2)
        else:
            label_player1.configure(image=image_hurt1)
            label_player2.configure(image=image_blast2)
            hp_update_p1()
            queue1(c1)
            queue2(c2)
    elif c1 == "uppercut":
        if c2 == "blast":
            label_player1.configure(image=image_upper1)
            label_player2.configure(image=image_hurt2)
            hp_update_p2()
            queue1(c1)
            queue2(c2)
        else:
            label_player1.configure(image=image_hurt1)
            label_player2.configure(image=image_w_sword2)
            hp_update_p2()
            queue1(c1)
            queue2(c2)
    elif c1 == "blast":
        if c2 == "sword":
            label_player1.configure(image=image_blast1)
            label_player2.configure(image=image_hurt2)
            hp_update_p2()
            queue1(c1)
            queue2(c2)
        else:
            label_player1.configure(image=image_hurt1)
            label_player2.configure(image=image_upper2)
            hp_update_p1()
            queue1(c1)
            queue2(c2)
    else:
        pass


def bonus_attack1(bonus):
    if bonus == "mega sword":
        label_player1.configure(image=image_sp_sword1)
        hp_update_p2()
    elif bonus == "mega blast":
        label_player1.configure(image=image_sp_blast1)
        hp_update_p2()
    elif bonus == "spinny":
        label_player1.configure(image=image_spinny1)
        hp_update_p2()


def bonus_attack2(bonus):
    if bonus == "mega sword":
        label_player2.configure(image=image_sp_sword2)
        hp_update_p1()
    elif bonus == "mega blast":
        label_player2.configure(image=image_sp_blast2)
        hp_update_p1()
    elif bonus == "spinny":
        label_player2.configure(image=image_spinny2)
        hp_update_p1()


def queue1(attack):  #finds special attack combinations for player 2
    global player1_moves
    player1_moves.appendleft(attack)
    print("player 1 moves: " + str(player1_moves))
    if len(player1_moves) == 3:
        copy_deq = list()
        while len(player1_moves) != 0:
            copy_deq.insert(0, player1_moves[-1])
            player1_moves.pop()
        if copy_deq[0] == "sword" and copy_deq[1] == "sword" and copy_deq[2] == "sword":
            player1_moves.clear()
            copy_deq.clear()
            bonus_attack1("mega sword")
        elif copy_deq[0] == "blast" and copy_deq[1] == "blast" and copy_deq[2] == "blast":
            player1_moves.clear()
            copy_deq.clear()
            bonus_attack1("mega blast")
        elif copy_deq[0] == "uppercut" and copy_deq[1] == "sword" and copy_deq[2] == "uppercut":
            player1_moves.clear()
            copy_deq.clear()
            bonus_attack1("spinny")
        else:
            copy_deq.pop()

        while len(copy_deq) != 0:
            player1_moves.append(copy_deq[0])
            copy_deq.pop(0)


def queue2(attack):          #finds special attack combinations for player 2
    global player2_moves
    player2_moves.appendleft(attack)
    print("player 2 moves: " + str(player2_moves))
    if len(player2_moves) == 3:
        copy_deq = list()
        while len(player2_moves) != 0:
            copy_deq.insert(0, player2_moves[-1])
            player2_moves.pop()
        if copy_deq[0] == "sword" and copy_deq[1] == "sword" and copy_deq[2] == "sword":
            player2_moves.clear()
            copy_deq.clear()
            bonus_attack2("mega sword")
        elif copy_deq[0] == "blast" and copy_deq[1] == "blast" and copy_deq[2] == "blast":
            player2_moves.clear()
            copy_deq.clear()
            bonus_attack2("mega blast")
        elif copy_deq[0] == "uppercut" and copy_deq[1] == "sword" and copy_deq[2] == "uppercut":
            player2_moves.clear()
            copy_deq.clear()
            bonus_attack2("spinny")
        else:
            copy_deq.pop()

        while len(copy_deq) != 0:
            player2_moves.append(copy_deq[0])
            copy_deq.pop(0)


def keypress1(event):
    global choice1
    if event.char == 'a':
        choice1 = "sword"
    elif event.char == 's':
        choice1 = "blast"
    elif event.char == 'd':
        choice1 = "uppercut"
    else:
        pass


def keypress2(event):
    global choice2
    if event.char == 'j':
        choice2 = "sword"
    elif event.char == 'k':
        choice2 = "blast"
    elif event.char == 'l':
        choice2 = "uppercut"
    else:
        pass


choices = ["sword", "blast", "uppercut"]


def bot_ai():
    global choice2
    if len(player2_moves) == 2:
        if player2_moves[-1] == "sword" and player2_moves[0] == "sword":
            choice2 = "sword"
        elif player2_moves[-1] == "blast" and player2_moves[0] == "blast":
            choice2 = "blast"
        elif player2_moves[-1] == "uppercut" and player2_moves[0] == "sword":
            choice2 = "uppercut"
        else:
            choice2 = choices[random.randint(0, 2)]
    else:
        choice2 = choices[random.randint(0, 2)]


def change_round(player_loose):     #deletes loosers from a tournament and find a winner
    global tournament_mode
    tourney.remove(player_loose)
    if len(tourney) > 1:
        reset_for_tournament()
    else:
        tournament_mode = False
        open_popup(tourney[0], 1)


root = Tk()
root.geometry("800x400")
root.title("ODYSSEY FIGHTERS")

pygame.mixer.init()

menu_f = Frame(root, height=400, width=800)
menu_f.pack_propagate(False)
start_game_f = Frame(root, height=400, width=800)
start_game_f.pack_propagate(False)
options_f = Frame(root, height=400, width=800)
options_f.pack_propagate(False)
choose_name = Frame(root, height=400, width=800)
choose_name.pack_propagate(False)
pvp_f = Frame(root, height=400, width=800)
pvp_f.pack_propagate(False)
pve_f = Frame(root, height=400, width=800)
pve_f.pack_propagate(False)
choose_w_size = Frame(root, height=400, width=800)
choose_w_size.pack_propagate(False)
choose_button = Frame(root, height=400, width=800)
choose_button.pack_propagate(False)

# Menu frame

menu_lab = Label(menu_f, text="ODYSSEY FIGHTERS", font=('Arial', 25))
menu_lab.pack(padx=50, pady=50)
btn1to_start_game = Button(menu_f, width=12, text="START GAME", font=('Arial', 18), command=to_start_game)
btn1to_start_game.pack()
btn1to_options = Button(menu_f, width=12, text="OPTIONS", font=('Arial', 18), command=to_options)
btn1to_options.pack()
btn1to_End = Button(menu_f, width=12, text="EXIT", font=('Arial', 18), command=close)
btn1to_End.pack()


# Start game frame

options_lab1 = Label(start_game_f, text="GAME MODES", font=('Arial', 25))
options_lab1.pack(padx=30, pady=30)
btn_sg1 = Button(start_game_f, width=20, text="PVP", font=('Arial', 18), command=to_pvp_1)
btn_sg1.pack()
btn_sg2 = Button(start_game_f, width=20, text="PVE", font=('Arial', 18), command=to_pve)
btn_sg2.pack()
btn_sg3 = Button(start_game_f, width=20, text="TOURNAMENT MODE", font=('Arial', 18), command=to_pvp_name)
btn_sg3.pack()

# Options frame

options_lab2 = Label(options_f, text="OPTIONS", font=('Arial', 25))
options_lab2.pack(padx=40, pady=40)
btn_op1 = Button(options_f, text="Dark mode", width=17, font=('Arial', 13), command=option1_dark_mode)
btn_op1.pack()
btn_op1_back = Button(options_f, text="Light mode", width=17, font=('Arial', 13), command=option1_light_mode)
btn_op1_back.pack()
btn_op2 = Button(options_f, text="Turn on music", width=17, font=('Arial', 13), command=option2)
btn_op2.pack()
btn_op2_stop = Button(options_f, text="Turn off music", width=17, font=('Arial', 13), command=option2_stop)
btn_op2_stop.pack()
btn_set_size = Button(options_f, text="Change window size", width=17, font=('Arial', 13),
                      command=to_change_size)
btn_set_size.pack()
btn_choose_btn = Button(options_f, text="Choose button skin", width=17, font=('Arial', 13),
                        command=to_choose_skin)
btn_choose_btn.pack()
btn_back = Button(options_f, text="BACK", width=17, font=('Arial', 13), command=to_menu_from_options)
btn_back.pack()

# Choose window size frame

choose_size_lab = Label(choose_w_size, text="Change window size", font=('Arial', 25))
choose_size_lab.pack(padx=30, pady=30)
set_btn1 = Button(choose_w_size, text="800x400", width=17, font=('Arial', 15),
                        command=lambda: change_window_size(800, 400))
set_btn1.pack(padx=10, pady=10)
set_btn2 = Button(choose_w_size, text="900x500", width=17, font=('Arial', 15),
                        command=lambda: change_window_size(900, 500))
set_btn2.pack(padx=10, pady=10)
set_btn3 = Button(choose_w_size, text="1920x1080", width=17, font=('Arial', 15),
                        command=lambda: change_window_size(1920, 1080))
set_btn3.pack(padx=10, pady=10)

# Choose button skin frame

set_btn_lab = Label(choose_button, text="Choose button skin", font=('Arial', 25))
set_btn_lab.pack(padx=30, pady=30)
set_btn1 = Button(choose_button, width=13, text="START", font=("Arial", 15),
                          bg="black", fg="yellow", command=lambda:change_skin("black", "yellow"))
set_btn1.pack(padx=5, pady=5)
set_btn2 = Button(choose_button, width=13, text="START", font=("Arial", 15),
                          bg="yellow", fg="red", command=lambda:change_skin("yellow", "red"))
set_btn2.pack(padx=5, pady=5)
set_btn3 = Button(choose_button, width=13, text="START", font=("Arial", 15),
                          bg="green", fg="white", command=lambda:change_skin("green", "white"))
set_btn3.pack(padx=5, pady=5)
set_btn4 = Button(choose_button, width=13, text="START", font=("Arial", 15),
                          bg="red", fg="white", command=lambda:change_skin("red", "white"))
set_btn4.pack(padx=5, pady=5)

# Choose player names frame

choose_nick = Label(choose_name, text="Choose player names:", font=('Arial', 20))
choose_nick.pack(padx=10, pady=30)

player1_name = Label(choose_name, text="Player1 name:", font=('Arial', 16))
player1_name.place(x=130, y=96)
name1 = Entry(choose_name, width=20, font=('Arial', 16))
name1.pack()

player2_name = Label(choose_name, text="Player2 name:", font=('Arial', 16))
player2_name.place(x=130, y=155)
name2 = Entry(choose_name, width=20, font=('Arial', 16))
name2.pack(padx=10, pady=30)

player3_name = Label(choose_name, text="Player3 name:", font=('Arial', 16))
player3_name.place(x=130, y=215)
name3 = Entry(choose_name, width=20, font=('Arial', 16))
name3.pack()

player4_name = Label(choose_name, text="Player4 name:", font=('Arial', 16))
player4_name.place(x=130, y=270)
name4 = Entry(choose_name, width=20, font=('Arial', 16))
name4.pack(padx=10, pady=30)

btn_play = Button(choose_name, text="Play", width=10, font=('Arial', 18), command=to_pvp_2)
btn_play.pack()

# PvP frame

btn_back = Button(pvp_f, text="Back to Menu", command=to_menu_from_pvp)
btn_back.pack(anchor='nw')

# images

player_base1 = Image.open("idle1f.png")
resized_base1 = player_base1.resize((200, 200))
new_image1 = ImageTk.PhotoImage(resized_base1)
label_player1_pvp = Label(pvp_f, image=new_image1)
label_player1_pvp.place(x=0, y=100)

player_base2 = Image.open("idle2f.png")
resized_image2 = player_base2.resize((200, 200))
new_image2 = ImageTk.PhotoImage(resized_image2)
label_player2_pvp = Label(pvp_f, image=new_image2)
label_player2_pvp.place(x=590, y=100)

player1_sword = Image.open("wswordf.png")
resized_w_sword1 = player1_sword.resize((200, 200))
image_w_sword1 = ImageTk.PhotoImage(resized_w_sword1)

player2_sword = Image.open("wsword2f.png")
resized_w_sword2 = player2_sword.resize((200, 200))
image_w_sword2 = ImageTk.PhotoImage(resized_w_sword2)

player1_blast = Image.open("blast1f.png")
resized_blast1 = player1_blast.resize((230, 200))
image_blast1 = ImageTk.PhotoImage(resized_blast1)

player2_blast = Image.open("blast2f.png")
resized_blast2 = player2_blast.resize((230, 200))
image_blast2 = ImageTk.PhotoImage(resized_blast2)

player1_upper = Image.open("upperf.png")
resized_upper1 = player1_upper.resize((200, 200))
image_upper1 = ImageTk.PhotoImage(resized_upper1)

player2_upper = Image.open("upper2f.png")
resized_upper2 = player2_upper.resize((200, 200))
image_upper2 = ImageTk.PhotoImage(resized_upper2)

player1_hurt = Image.open("hurtf.png")
resized_hurt1 = player1_hurt.resize((180, 200))
image_hurt1 = ImageTk.PhotoImage(resized_hurt1)

player2_hurt = Image.open("hurt2f.png")
resized_hurt2 = player2_hurt.resize((180, 200))
image_hurt2 = ImageTk.PhotoImage(resized_hurt2)

player1_sp_sword = Image.open("m_sword_f.png")
resized_sp_sword1 = player1_sp_sword.resize((200, 200))
image_sp_sword1 = ImageTk.PhotoImage(resized_sp_sword1)

player2_sp_sword = Image.open("m_sword2f.png")
resized_sp_sword2 = player2_sp_sword.resize((200, 200))
image_sp_sword2 = ImageTk.PhotoImage(resized_sp_sword2)


player1_sp_blast = Image.open("m_blastf.png")
resized_sp_blast1 = player1_sp_blast.resize((200, 200))
image_sp_blast1 = ImageTk.PhotoImage(resized_sp_blast1)

player2_sp_blast = Image.open("m_blastf2.png")
resized_sp_blast2 = player2_sp_blast.resize((200, 200))
image_sp_blast2 = ImageTk.PhotoImage(resized_sp_blast2)

player1_sp_spinny = Image.open("spinny_f.png")
resized_spinny1 = player1_sp_spinny.resize((200, 200))
image_spinny1 = ImageTk.PhotoImage(resized_spinny1)

player2_sp_spinny = Image.open("spinny2f.png")
resized_spinny2 = player2_sp_spinny.resize((200, 200))
image_spinny2 = ImageTk.PhotoImage(resized_spinny2)

player_death = Image.open("dead.png")
resized_death = player_death.resize((200, 200))
image_death = ImageTk.PhotoImage(resized_death)

controls_image_pvp = Image.open("controls_pvp.png")
resized_controls_pvp = controls_image_pvp.resize((350, 190))
resized_cntr_pvp = ImageTk.PhotoImage(resized_controls_pvp)
label_controls_pvp = Label(pvp_f, image=resized_cntr_pvp)
label_controls_pvp.place(x=225, y=220)

player1_hp_pvp = Label(pvp_f, text=100, font=('Arial', 18, "bold"))
player1_hp_pvp.place(x=0, y=305)
player2_hp_pvp = Label(pvp_f, text=100, font=('Arial', 18, "bold"))
player2_hp_pvp.place(x=750, y=305)

# player indicator
player1_text_pvp = Label(pvp_f, text=player11_name, font=('Arial', 18, "bold"))
player1_text_pvp.place(x=0, y=50)
player2_text_pvp = Label(pvp_f, text=player22_name, font=('Arial', 18, "bold"))
player2_text_pvp.place(x=699, y=50)


attack_chosen1_pvp = Label(pvp_f, text="Attack chosen:", font=('Arial', 15, "bold"))
attack_chosen1_pvp.place(x=0, y=335)
attack_chosen2_pvp = Label(pvp_f, text="Attack chosen:", font=('Arial', 15, "bold"))
attack_chosen2_pvp.place(x=647, y=335)

last_attack1_pvp = Label(pvp_f, font=('Arial', 15, "bold"))
last_attack1_pvp.place(x=0, y=360)
last_attack2_pvp = Label(pvp_f, font=('Arial', 15, "bold"))
last_attack2_pvp.place(x=647, y=360)

btn_start_battle_pvp = Button(pvp_f, width=13, text="START", font=("Arial", 15),
                          bg="red", fg="white", command=winner_check)
btn_start_battle_pvp.place(x=325, y=177)

#pve frame widgets
btn_back = Button(pve_f, text="Back to Menu", command=to_menu_from_pve)
btn_back.pack(anchor='nw')

label_player1_pve = Label(pve_f, image=new_image1)
label_player1_pve.place(x=0, y=100)

label_player2_pve = Label(pve_f, image=new_image2)
label_player2_pve.place(x=590, y=100)

controls_image_pve = Image.open("controls_pve.png")
resized_controls_pve = controls_image_pve.resize((300, 170))
resized_cntr_pve = ImageTk.PhotoImage(resized_controls_pve)
label_controls_pve = Label(pve_f, image=resized_cntr_pve)
label_controls_pve.place(x=250, y=230)

player1_hp_pve = Label(pve_f, text=100, font=('Arial', 18, "bold"))
player1_hp_pve.place(x=0, y=300)
player2_hp_pve = Label(pve_f, text=100, font=('Arial', 18, "bold"))
player2_hp_pve.place(x=750, y=300)

# player indicator
player1_text_pve = Label(pve_f, text="Player 1", font=('Arial', 18, "bold"))
player1_text_pve.place(x=0, y=50)
player2_text_pve = Label(pve_f, text="BOT", font=('Arial', 18, "bold"))
player2_text_pve.place(x=699, y=50)


attack_chosen1_pve = Label(pve_f, text="Attack chosen:", font=('Arial', 15, "bold"))
attack_chosen1_pve.place(x=0, y=335)
attack_chosen2_pve = Label(pve_f, text="Attack chosen:", font=('Arial', 15, "bold"))
attack_chosen2_pve.place(x=647, y=335)

last_attack1_pve = Label(pve_f, font=('Arial', 15, "bold"))
last_attack1_pve.place(x=0, y=360)
last_attack2_pve = Label(pve_f, font=('Arial', 15, "bold"))
last_attack2_pve.place(x=647, y=360)

btn_start_battle_pve = Button(pve_f, width=13, text="START", font=("Arial", 15),
                          bg="red", fg="white", command=winner_check)
btn_start_battle_pve.place(x=325, y=190)

# controls
root.bind('a', keypress1)
root.bind('s', keypress1)
root.bind('d', keypress1)
root.bind('j', keypress2)
root.bind('k', keypress2)
root.bind('l', keypress2)
menu_f.pack()
root.mainloop()
