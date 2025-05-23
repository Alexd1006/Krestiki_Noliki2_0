from tkinter import simpledialog, messagebox
import tkinter as tk

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x460")

current_player = "X"
buttons = []
game_over = False

score_x = 0
score_0 = 0
draws = 0

# Метка для текущего игрока
current_player_label = tk.Label(window, text="", font=("Arial", 14))
current_player_label.grid(row=5, column=0, columnspan=3, pady=5)

# Метка для счёта
score_label = tk.Label(window, text="", font=("Arial", 12))
score_label.grid(row=6, column=0, columnspan=3, pady=5)


def update_player_label():
    current_player_label.config(text=f"Ход игрока: {current_player}")


def update_score_label():
    score_label.config(text=f"Счёт — X: {score_x} | 0: {score_0} | Ничьих: {draws}")


def choose_first_player():
    global current_player
    choice = simpledialog.askstring("Выбор игрока", "Кто ходит первым? (X или 0)", initialvalue="X")
    if choice and choice.upper() in ["X", "0"]:
        current_player = choice.upper()
    else:
        current_player = "X"
        messagebox.showwarning("Некорректный выбор", "Выбран некорректный символ. Игрок X ходит первым.")
    update_player_label()


def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False


def check_draw():
    for row in buttons:
        for btn in row:
            if btn['text'] == "":
                return False
    return True


def on_click(row, col):
    global current_player, game_over, score_x, score_0, draws

    if buttons[row][col]['text'] != "" or game_over:
        return

    buttons[row][col]['text'] = current_player

    if check_winner():
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        game_over = True
        if current_player == "X":
            score_x += 1
        else:
            score_0 += 1
        update_score_label()
        window.after(1000, reset_board)
        return

    if check_draw():
        messagebox.showinfo("Игра окончена", "Ничья!")
        game_over = True
        draws += 1
        update_score_label()
        window.after(1000, reset_board)
        return

    current_player = "0" if current_player == "X" else "X"
    update_player_label()


def reset_board():
    global game_over
    for row in buttons:
        for btn in row:
            btn.config(text="")
    game_over = False
    update_player_label()


def reset_game():
    global game_over
    for row in buttons:
        for btn in row:
            btn.config(text="")
    game_over = False
    choose_first_player()


# Игровое поле
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

# Кнопка "Новая игра"
reset_button = tk.Button(window, text="Новая игра", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

# Кнопка "Выход"
exit_button = tk.Button(window, text="Выход", font=("Arial", 14), command=window.quit)
exit_button.grid(row=4, column=0, columnspan=3, pady=10)

# Запуск
choose_first_player()
update_score_label()
window.mainloop()
