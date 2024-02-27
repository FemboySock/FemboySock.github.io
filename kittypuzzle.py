import tkinter as tk
alpha = 0

heya = 0

# FIRST PUZZLE
puzzling = tk.Tk()
puzzling.title("puzzlekitty")
puzzling.configure(bg="black", width=400, height=800)
image_path = "example_image.png"  # Update with your image file path
image = tk.PhotoImage(file="puzzle1.png")
canvas = tk.Canvas(puzzling, width=image.width(), height=image.height(), bg="black", highlightthickness=0, highlightbackground="grey")
canvas.place(x=35, y=200)
canvas.create_image(0, 0, anchor=tk.NW, image=image)
hint1_label = tk.Label(text="Y X C Z Q F     H 7", bg="black", fg="white", font=20)
hint1_label.place(x=132, y=70)
hint_label = tk.Label(text="G", bg="black", fg="cyan", font=20)
hint_label.place(x=219, y=70)
puzzle_label = tk.Label(text="P̛͈͇̑̿̔́̈͛́͛͂̽͛͌̚͠u̻̦̲̫̺̹͕̖̳̤̼̟͌͂̔̽̇̚z̰̩̗͔̟̺̃͆̆͂̅̓̇̈́͛̿̕͠z̨̧̤̻̯̗̙̱͙̰̠̑̈́́͂͋l̘͙̬̺̦͋̐̿͗̇͘͠e̛̹͍͚̣̒̊̃̈́̈̑ 1", bg="black", fg="white", font=20)
puzzle_label.place(x=25, y=30)
def a_b(button):
    global alpha
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alpha = (alpha + 1) % len(alphabet)
    button.configure(text=alphabet[alpha].upper())


def get_current_letters():
    current_letters = []
    for button in all_buttons:
        current_letters.append(button.cget("text"))
    print("Current letters on buttons:", current_letters)
    if current_letters == ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']:
        global heya
        #'X', 'C', 'Y', 'H', '7', 'G', 'Z', 'Q', 'F'
        puzzle_label.configure(text="P̛͈͇̑̿̔́̈͛́͛͂̽͛͌̚͠u̻̦̲̫̺̹͕̖̳̤̼̟͌͂̔̽̇̚z̰̩̗͔̟̺̃͆̆͂̅̓̇̈́͛̿̕͠z̨̧̤̻̯̗̙̱͙̰̠̑̈́́͂͋l̘͙̬̺̦͋̐̿͗̇͘͠e̛̹͍͚̣̒̊̃̈́̈̑ 2", fg="magenta")
        canvas.destroy()
        test_button1.destroy()
        test_button2.destroy()
        test_button3.destroy()
        test_button11.destroy()
        test_button12.destroy()
        test_button13.destroy()
        test_button21.destroy()
        test_button22.destroy()
        test_button23.destroy()
        hint_label.destroy()
        hint1_label.destroy()
        soduko_complete.destroy()
        heya += 1
        second_puzzle()


#
soduko_complete = tk.Button(text="⛧", command=get_current_letters, fg="darkred", font=40)
soduko_complete.place(x=175, y=620, height=34, width=34)

# PUZZLE 5 BUTTONS :SOB:
test_button1 = tk.Button(text="A", command=lambda: a_b(test_button1))
test_button1.place(x=253, y=417, height=34, width=34)
test_button2 = tk.Button(text="A", command=lambda: a_b(test_button2))
test_button2.place(x=253, y=452, height=34, width=34)
test_button3 = tk.Button(text="A", command=lambda: a_b(test_button3))
test_button3.place(x=253, y=487, height=34, width=34)

test_button11 = tk.Button(text="A", command=lambda: a_b(test_button11))
test_button11.place(x=289, y=417, height=34, width=34)
test_button12 = tk.Button(text="A", command=lambda: a_b(test_button12))
test_button12.place(x=289, y=452, height=34, width=34)
test_button13 = tk.Button(text="A", command=lambda: a_b(test_button13))
test_button13.place(x=289, y=487, height=34, width=34)

test_button21 = tk.Button(text="A", command=lambda: a_b(test_button21))
test_button21.place(x=325, y=417, height=34, width=34)
test_button22 = tk.Button(text="A", command=lambda: a_b(test_button22))
test_button22.place(x=325, y=452, height=34, width=34)
test_button23 = tk.Button(text="A", command=lambda: a_b(test_button23))
test_button23.place(x=325, y=487, height=34, width=34)

all_buttons = [test_button1, test_button11, test_button21,
               test_button2, test_button12, test_button22,
               test_button3, test_button13, test_button23]
# ---------------------------------------------------------------
def second_puzzle():
    def get_user_answer():
        user_answer = kitty_entry.get().lower()
        if user_answer == "pohutukawa":
            puzzle_label.configure(
                text="P̛͈͇̑̿̔́̈͛́͛͂̽͛͌̚͠u̻̦̲̫̺̹͕̖̳̤̼̟͌͂̔̽̇̚z̰̩̗͔̟̺̃͆̆͂̅̓̇̈́͛̿̕͠z̨̧̤̻̯̗̙̱͙̰̠̑̈́́͂͋l̘͙̬̺̦͋̐̿͗̇͘͠e̛̹͍͚̣̒̊̃̈́̈̑ 3",
                fg="pink")
            kitty_entry.destroy()
            kitty_submit.destroy()
            kitty_label.destroy()
            text_bubble.destroy()
            puzzle_2.destroy()
    text_bubble = tk.Label(text="""
    ⠀⠀⠀⠀⠀⣠⠴⠶⠦⣄⠀⠀⣠⠤⢤⡀⠀⢀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠱⠀⠀⠀⠈⢧⡞⠁⠀⠀⢹⡴⠋⠀⠀⠈⠳⡀⠀⠀⠀⠀⠀⠀
⠀⠀⣀⣀⣘⣆⡑⡀⠀⠀⠘⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⣧⠴⠲⢦⡀⠀⠀
⣰⢻⠉⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⡇⠀⠀
⡇⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣃⠀⠀
⢧⡀⠑⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠉⠉⠹⡄
⠈⢿⣷⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇
⠀⢰⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣶⣿⠀
⠀⠸⡄⠢⢀⠀⡀⠠⡄⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⠋⠁⠀
⠀⠀⢹⣶⣤⣤⣴⣇⠐⢄⠀⠀⡀⣾⠀⢀⠀⠀⠀⣀⠀⠀⠀⣂⣴⡏⠀⠀⠀
⠀⠀⠀⠉⠛⠛⠋⠙⣷⣤⣠⣤⣾⠏⢷⣄⣈⣩⣵⡘⢄⠀⠀⡿⠛⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠛⠋⠀⠈⠻⠿⠿⠛⢷⣄⠑⠄⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣦⠽⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠀⠀⠀⠀⠀""", fg="magenta", bg="black")
    text_bubble.place(x=-20, y=400)
    kitty_label = tk.Label(text="""　　　　　　　　 ,-､　　　 　 　 　　　..-､
　　　　　　　 ./:::::＼　　　　 　 　 ／:::::ヽ
　　　　　　　/:::YT:::::::;ゝ--──-- ､._/:::::URL::ヽ
　　　　　　 /,.-‐''"′ 　　　　　　　　 ＼::::::::|
　　　　　／　 　　　　　　　　　　　　ヽ､::|
　　　　/　　　　●　　　 　 　 　 　 　 　 ヽ|
　　 　 l　　　､､､　　 　 　 　 　 　 ●　　 　 l
　　　 .|　　　 　　　　(_人__丿　　､､､　 　|
　 　 　l　　　　　　　　　　　　　　　　 　 l
　　　　` ､　　　　　　　　 　 　 　　 　 　 /
　　　　　　`ｰ ､__　　　 　 　 　　　 　.／
　　　　　　　　　/`'''ｰ‐‐──‐‐‐┬--- ／""", fg="magenta", bg="black")
    kitty_label.place(x=0, y=600)
    kitty_entry = tk.Entry(bg="grey", borderwidth=0)
    kitty_entry.place(x=47, y=490, height=25)
    puzzle_2 = tk.Label(text="g3YbmszLl-c \n[96]", font=20, bg="black", fg="darkred")
    puzzle_2.place(x=40, y=300)
    kitty_submit = tk.Button(text="❀", bg="grey", fg="darkred", command=get_user_answer)
    kitty_submit.place(x=160, y=490)


puzzling.mainloop()
