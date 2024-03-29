from random import shuffle
import tkinter as tk
from tkinter import messagebox

background_color = '#F9F7F1'
primary_color = '#a5daa3'

def Generate_Number():
    digits = list(range(9))
    shuffle(digits)
    res = ''.join(map(str, digits[:4]))
    return str(res)

def Start_Window():

    def open_main_window():
        window.destroy()

        Main_Window()

    def show_message_box():
        messagebox.showinfo("Rules", "Welcome in my game!\n"
                             "In this game you need to guess my number.\n"
                             "My number consists of four digits from 1 - 9\n"
                             "You have 10 attempts.\n"
                             "After each attempt, you will see the number of correct\n"
                             "numbers and correct placed numbers.\n"
                             "Good luck!")
        
    window = tk.Tk()
    window.title("Guess password")
    window.geometry("300x300")

    window.configure(bg=background_color)

    Frame = tk.Frame()
    Frame.pack(expand=True)

    label1 = tk.Label(window, text="Guess my number")
    label1.place(x=95, y=20)

    start_button = tk.Button(window, text="Start", command=open_main_window, bg=primary_color)
    start_button.place(x=130, y=150)

    rules_button = tk.Button(window, text="?", command=show_message_box)
    rules_button.place(x=200, y=15)

    window.mainloop()

def Main_Window():
    window = tk.Tk()
    window.title("Guess password")
    window.geometry("300x300")

    answer = Generate_Number()

    window.configure(bg=background_color)

    label1 = tk.Label(window, text="Your guess")
    label1.place(x=30, y=7)
    
    label2 = tk.Label(window, text="correct\nnumber")
    label2.place(x=160, y=7)
    
    label3 = tk.Label(window, text="correct\nposition")
    label3.place(x=220, y=7)

    def on_validate(P):
        return len(P) <= 4 and P.isdigit() and len(set(P)) == len(P) or P == ''

    validate_cmd = window.register(on_validate)
    
    def create_entry(y_position, attempt):
        def Try_Button(attempt):
            entry_text = entry.get()

            if len(entry_text) < 4:
                return

            if len(entry_text) == 4:
                if entry_text == answer:
                    window.destroy()
                    EndGame_Window(answer, True)
                    return
            
            create_labels(entry_text,y_position)
            entry.delete(0, 'end')
            entry.destroy()
            if attempt <= 9:
                create_entry(y_position + 23, attempt)
            else:
                window.destroy()
                EndGame_Window(answer, False)

        entry = tk.Entry(window, validate="key", validatecommand=(validate_cmd, '%P'))
        entry.place(x=30, y=y_position, width=125, height=20)

        try_button = tk.Button(window, text='Try', command=lambda: Try_Button(attempt))
        try_button.place(x=130,y=270)
        attempt += 1
    
    create_entry(40, 0)

    def correct_num(guess, answer):
        res = 0
        for i in range(4):
            for j in range(4):
                if guess[i] == answer[j]:
                    res += 1
        return res
        
    def correct_pos(guess, answer):
        res = 0
        if(guess[0] == answer[0]):
            res += 1
            
        if(guess[1] == answer[1]):
            res += 1
            
        if(guess[2] == answer[2]):
            res += 1
            
        if(guess[3] == answer[3]):
            res += 1
        return res

    def create_labels(guess, y_position):
        try:
            entry_label = tk.Label(window, text=guess)
            entry_label.place(x=30, y=y_position)

            label_num = tk.Label(window, text=correct_num(guess, answer))
            label_num.place(x=180, y=y_position)

            label_pos = tk.Label(window, text=correct_pos(guess, answer))
            label_pos.place(x=240, y=y_position)
        except tk.TclError:
            pass

    window.mainloop()

def EndGame_Window(answer, result):

    def open_window(state):
        window.destroy()
        if state:
            Main_Window()
        else:
            Start_Window()

    res_text = 'You lost :('
    if result:
        res_text = 'You won :)'

    window = tk.Tk()
    window.title("Guess password")
    window.geometry("300x300")

    answer = str(answer)
    window.configure(bg=background_color)

    Answer_label = tk.Label(window, text='Answer - ' + answer)
    Answer_label.place(x= 95, y= 20)

    Res_label = tk.Label(window, text=res_text)
    Res_label.place(x = 95, y= 40)

    Main_Window_button = tk.Button(window, text="Try again", command=lambda: open_window(True), bg=primary_color)
    Main_Window_button.place(x=50, y=100)

    Start_Window_button = tk.Button(window, text="Menu", command=lambda: open_window(False), bg=primary_color)
    Start_Window_button.place(x=160, y=100)

    window.mainloop()

Start_Window()