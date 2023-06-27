import tkinter as tk
import random 
import time
import threading

notwin = random.choice(['Almost there!','Well...',"Hmmmmm"])
notwin2 = random.choice (["Congrats, you must be so proud.","Lol", 'Almost had it.'])
win = random.choice(['Congrats!','Bravo! Give yourself a pat on the back.',"It's like you were born to do this, I guess...",'Nicely done!', "You're killing it!"])
goodanswers = 0
until5 = 0
alotoftext = "Cool! Let me explain the rules to you. The game consists of two randomly generated numbers (between 1 and 100) that you will need to add or subtract (yes, the operation is also random). Once the numbers are generated, you will have 5 seconds to answer correctly. If you answer incorrectly or run out of time, you lose! You win by answering correctly five times in a row. Rock it!"


def rt3d():
    root3.destroy()


def globaluntil5():
        global until5
        until5 += 1
        
    
def goodanswersend(prompt):
    print("You scored", prompt,"out of 5.")
    if prompt == 1:
     print(notwin)
    elif prompt == 2:
     print(notwin)
    elif prompt == 3:
     print(notwin2)
    elif prompt == 4:
     print(notwin2)
    elif prompt == 5:
     print(win)
     print('🏆')
     global root3
     root3 = tk.Tk()
     root3.geometry("225x200") 

     Congrats = tk.Message(root3, text= 'Congratulations!🏆 You won nothing but the game! Unfortunately, no prize for you this time😁.',font=("Arial",12))
     Congrats.pack()

     THEbutton = tk.Button(root3, text= "Yay!... Wait, there's no prize?",command = rt3d, bg ="cyan" )
     THEbutton.pack()

    else:
        print('Someone get this person a trophy for participation.')
        print('🏆(participation trophy)')


def updgoodanswers():
    global goodanswers
    goodanswers += 1


def input_with_timeout(p1, p2, p3, timeout):
    print(p1, p2, p3)
    result = [None]
    def get_input():
        result[0] = input('{} {} {}'.format(num1, operation, num2))
    t = threading.Thread(target=get_input)
    t.start()
    t.join(timeout)
    return result[0]
    

def generate_numbers():
 global num1, num2, operation
 num1 = int(random.randint(1, 100))
 num2 = int(random.randint(1, 100))
 operation = random.choice(["+", "-"])
 return num1, num2, operation  
   

def main():
    num1, num2, operation = generate_numbers()
    
    if operation == "+" :
            result = num1 + num2
    else:
            result = num1 - num2
    try:
         answer = int(input_with_timeout(num1, operation, num2, 5))
    
    except ValueError:
       print('Invalid value.', num1, operation,num2, '=',result)
       return
    
    except TypeError:
        print("Looks like you didn't make it in time.", num1, operation , num2 , '=', result)
        return
    
    except KeyboardInterrupt:
        print('Keyboard Interrupt.', num1, operation, num2, '=', result)
        goodanswersend(goodanswers)

    except UnboundLocalError:
         print('Keyboard Interrupt.', num1, operation, num2, '=', result)
         goodanswersend(goodanswers)

    if result == answer:
           print(random.choice(['Hell yeah!','You got it!','Yes, yes, and yes!','Spot on!', 'Bingo!', "That's it!", "Absolutely!"]), num1, operation, num2, '=', result)
           updgoodanswers()

    else:
           print(random.choice(["Nope.", 'Huh?', 'Not even close.','Almost, but not quite.','Uh, wrong answer.', 'Nope, try again.']), num1, operation, num2, '=', result)
           
    
def game():
  
  while until5 < 5:
   if __name__ == "__main__":
    for i in range(5):
        num1, num2, operation = generate_numbers()
        time.sleep(4)
        main()
        globaluntil5()
   if until5 >= 5 :
        goodanswersend(goodanswers)
        
        

def option1and2():
    
    root.destroy()

    root2 = tk.Tk()
    root2.geometry("275x275") 
    
    def f1():
        root2.destroy()
       
    def both():
        f1()
        game()
 
    rules = tk.Message(root2, text= alotoftext, font = ("Arial", 11))
    rules.pack()

    button3 = tk.Button(root2, text="Bring it on!",command =  both)
    button3.pack()

    button4 = tk.Button(root2, text=" Not ready yet, but okay.",command =  both)
    button4.pack()


root = tk.Tk()
root.geometry("225x225")

name = tk.Message(root, text="Hey, what's your n...",font=("Arial",12), justify = "center") # asking the name just because
name.pack()

label= tk.Message(root, text="Well, I don't really care. Wanna play a game?",font=("Arial", 12), justify = "center")
label.pack()

button1 = tk.Button(root, text="YES", command = option1and2, bg="blue")
button1.pack()

button2 = tk.Button(root, text= "ALSO YES... but in red", command = option1and2, bg="red")
button2.pack()


root.mainloop()
