import tkinter as tk
import random 
from PIL import ImageTk, Image

root=tk.Tk()
root.geometry('400x400')
root.title('Rock,Paper,Scissors')
canvas=tk.Canvas(root, width=200,height=150)
canvas.place(x=10,y=200)

COMP_SCORE=0
HUMAN_SCORE=0
#if rock button is clicked
def rock_clicked(event):
    image=Image.open('C:/rock.png')
    image=image.resize((100,150),Image.ANTIALIAS)   #To resize the image used
    photo=ImageTk.PhotoImage(image)                 #antialias is used to make the jaggies/outline of image smooth
    rock_label=tk.Label(root,image=photo)
    rock_label.image=photo
    rock_label.place(x=10,y=200,width=150,height=200)
    
    comp_choice('rock')

#if paper button is clicked
def paper_clicked(event):
    image=Image.open('C:/paper.png')
    image=image.resize((100,150),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(image) 
    paper_label=tk.Label(root,image=photo)
    paper_label.image=photo
    paper_label.place(x=10,y=200,width=150,height=200)

    comp_choice('paper')

#if scissors button is clicked
def scissors_clicked(event):
    image=Image.open('C:/scissors.png')
    image=image.resize((100,150),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(image) 
    scissors_label=tk.Label(root,image=photo)
    scissors_label.image=photo
    scissors_label.place(x=10,y=200,width=150,height=200)

    comp_choice('scissors')

#computer chooses randomly
def comp_choice(n):
    Value=random.choice(['rock','paper','scissors'])
    if Value=='rock': #Value is used to store the random computer choice 
        image=Image.open('C:/rock.png')
        image=image.resize((100,150),Image.ANTIALIAS)   #To resize the image used
        photo=ImageTk.PhotoImage(image)                 #antialias is used to make the jaggies/outline of image smooth
        rock_label=tk.Label(root,image=photo)
        rock_label.image=photo
        rock_label.place(x=200,y=200,width=150,height=200)

    elif Value=='paper':
        image=Image.open('C:/paper.png')
        image=image.resize((100,150),Image.ANTIALIAS)
        photo=ImageTk.PhotoImage(image) 
        paper_label=tk.Label(root,image=photo)
        paper_label.image=photo
        paper_label.place(x=200,y=200,width=150,height=200)

    elif Value=='scissors':
        image=Image.open('C:/scissors.png')
        image=image.resize((100,150),Image.ANTIALIAS)
        photo=ImageTk.PhotoImage(image) 
        scissors_label=tk.Label(root,image=photo)
        scissors_label.image=photo
        scissors_label.place(x=200,y=200,width=150,height=200)
    Result(n,Value)# call to deciding function

def Result(human_choice, comp_Choice):
    global COMP_SCORE
    global HUMAN_SCORE

    if human_choice==comp_Choice:
        text_answer=tk.Text(master=root,height=1, width=3)
        text_answer.place(x=75,y=30)
        text_answer.insert(tk.END,'Tie')
        
    elif (human_choice=='rock' and comp_Choice=='paper'):
        COMP_SCORE+=1
        text_answer=tk.Text(master=root,height=1, width=3)
        text_answer.place(x=355,y=30)
        text_answer.insert(tk.END,COMP_SCORE)

    elif human_choice=='rock' and comp_Choice=='scissors':
        HUMAN_SCORE+=1
        text_answer=tk.Text(master=root,height=1, width=3)
        text_answer.place(x=75,y=30)
        text_answer.insert(tk.END,HUMAN_SCORE)

    elif human_choice=='paper' and comp_Choice=='rock':
        HUMAN_SCORE+=1
        text_answer=tk.Text(master=root,height=1, width=3)
        text_answer.place(x=75,y=30)
        text_answer.insert(tk.END,HUMAN_SCORE)

    elif human_choice=='paper' and comp_Choice=='scissors':
        COMP_SCORE+=1
        text_answer=tk.Text(master=root,height=1, width=3)
        text_answer.place(x=355,y=30)
        text_answer.insert(tk.END,COMP_SCORE)

    elif human_choice=='scissors' and comp_Choice=='rock':
        COMP_SCORE+=1
        text_answer=tk.Text(master=root,height=1, width=3)
        text_answer.place(x=355,y=30)
        text_answer.insert(tk.END,COMP_SCORE)

    elif human_choice=='scissors' and comp_Choice=='paper':
        HUMAN_SCORE+=1
        text_answer=tk.Text(master=root,height=1, width=3)
        text_answer.place(x=75,y=30)
        text_answer.insert(tk.END,HUMAN_SCORE)






No_attempts=tk.Label(text='Number of Tries')
No_attempts.place(x=140,y=5, width=100, height=10)

#refresh=tk.Button(text='Refresh', bg='green')
#refresh.place(x=350, y=380, width=50, height=20)

human_label=tk.Label(text='Human')
human_label.place(x=20, y=30, width=50, height=20)

comp_label=tk.Label(text='Computer')
comp_label.place(x=290, y=30, width=60, height=20)

rock_button=tk.Button(root,text='Rock', bg='pink')
rock_button.place(x=10, y=70, width=50, height=30)
rock_button.bind('<Button-1>',rock_clicked)

paper_button=tk.Button(root,text='Paper',bg='pink')
paper_button.place(x=10, y=110, width=50, height=30)
paper_button.bind('<Button-1>',paper_clicked)

scissors_button=tk.Button(root,text='Scissors',bg='pink')
scissors_button.place(x=10, y=150, width=50, height=30)
scissors_button.bind('<Button-1>',scissors_clicked)



img=ImageTk.PhotoImage(Image.open('C:/robot1.png'))     
panel=tk.Label(image=img)
panel.place(x=200, y=70, width=180, height=120)

root.mainloop()

