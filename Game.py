from random import shuffle
import tkinter as tk

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

def Main():
    window = tk.Tk()
    window.title("Guess password")
    window.geometry("300x300")

    text_color = '#1b150b'
    background_color = '#F9F7F1'
    primary_color = '#B98E51'
    secondary_color = '#a5daa3'
    accent_color = '#77c899'
    window.configure(bg=background_color)

    Frame = tk.Frame()
    

    window.mainloop()
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