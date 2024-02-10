from random import shuffle
import tkinter as tk

text_color = '#1b150b'
background_color = '#F9F7F1'
primary_color = '#B98E51'
secondary_color = '#a5daa3'
accent_color = '#77c899'

def Generate_Number():
    digits = list(range(10))
    shuffle(digits)
    res = ''.join(map(str, digits[:4]))
    return str(res)

def Enter_Number():
    isInt = False
    isFour = False
    isUnique = False
    while not isInt or not isFour or not isUnique:
        try:
            enter_number = int(input("Enter number: "))
            isInt = True
            if len(str(enter_number)) == 4:
                isFour = True
                digits = [int(d) for d in str(enter_number)]
                if len(digits) == len(set(digits)):
                    isUnique = True
                else:
                    print("Invalid input. Please enter a number with unique digits.")
            else:
                print("Invalid input. Please enter a 4-digit integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return str(enter_number)

def Correct_Position(guess, answer):
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

def Correct_Number(guess, answe):
    res = 0
    for i in range(4):
        for j in range(4):
            if guess[i] == answe[j]:
                res += 1
    return res

def Get_Best_Result():
    return '?'

def Get_Average_Result():
    return '?'

def Start_Window():
    window = tk.Tk()
    window.title("Guess password")
    window.geometry("300x300")

    window.configure(bg=background_color)

    Frame = tk.Frame()
    Frame.pack(expand=True)

    label1 = tk.Label(window, text="Guess my number")
    label1.place(x=95, y=20, height=20, width=110)

    label2 = tk.Label(window, text="Best result: " + Get_Best_Result())
    label2.place(x=50, y=50)
    
    label3 = tk.Label(window, text="Average guess: " + Get_Average_Result())
    label3.place(x=150, y=50)

    button1 = tk.Button(window, text="History", command=lambda: print("Button 1 clicked"), bg=secondary_color)
    button1.place(x=50, y=100)

    button2 = tk.Button(window, text="Clear History", command=lambda: print("Button 2 clicked"), bg=secondary_color)
    button2.place(x=160, y=100)

    button3 = tk.Button(window, text="Start", command=lambda: print("Button 3 clicked"), bg=primary_color)
    button3.place(x=100, y=150)

    button4 = tk.Button(window, text="?")
    button4.place(x=100, y=100)

    window.mainloop()

def Main_Window():
    window = tk.Tk()
    window.title("Guess password")
    window.geometry("300x300")

    window.configure(bg=background_color)

    label1 = tk.Label(window, text="Your guess")
    label1.place(x=30, y=30)
    
    label2 = tk.Label(window, text="correct number")
    label2.place(x=100, y=30)
    
    label3 = tk.Label(window, text="correct position")
    label3.place(x=190, y=30)

    def on_validate(P):
        return len(P) <= 4 and P.isdigit() and len(set(P)) == len(P) or P == ''
    
    validate_cmd = window.register(on_validate)

    entry = tk.Entry(window, validate="key", validatecommand=(validate_cmd, '%P'))
    entry.place(x=50, y=50, width=100, height=20)

    label_num = tk.Label(window, text=1)
    label_num.place(x=155,y=50)

    label_pos = tk.Label(window, text=2)
    label_pos.place(x=165,y=50)

    window.mainloop()

def EndGame_Window(answer, result):
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

    button1 = tk.Button(window, text="Try again", command=lambda: print("Button 1 clicked"), bg=secondary_color)
    button1.place(x=50, y=100)

    button2 = tk.Button(window, text="Menu", command=lambda: print("Button 2 clicked"), bg=secondary_color)
    button2.place(x=160, y=100)

    window.mainloop()

def Main():
    # Start_Window()
    # Main_Window()
    EndGame_Window(1234, 1)


    # answer = Generate_Number()
    # guess = Enter_Number()
    # attempt = 0
    # while Correct_Position(guess, answer) != 4:
    #     print(f"Correct Position: {Correct_Position(guess, answer)}")
    #     print(f"Correct Number: {Correct_Number(guess, answer)}")
    #     print(f"Attempts left {9 - attempt}")
    #     guess = Enter_Number()
    #     attempt += 1
    #     if (attempt > 8):
    #         print('Answer =', answer)
    #         print("You lose :(")
    #         break

    
    # print("You win :)")


if __name__ == "__main__":
    Main()