from tkinter import *
import random



#Initialize window
root=Tk()
root.geometry('400x400') #window ko size change huncha
root.resizable(0, 0)
root.title("Rock Paper Scissor By Seema")
root.config(bg='#62636e')

Label(root, text='Rock, Paper, Scissor', font='arial 20 bold', bg='#f4f5d0', relief=RIDGE).pack()



#User choice

user_take= StringVar()
Label(root, text='Choose any one: rock, paper, scissors', font='arial 15 bold', bg='#f4f5d0', relief=RIDGE).place(x=20,
 y=70)
Entry(root, font='arial 15', textvariable=user_take, bg='antiquewhite2').place(x=90, y=130)


#Computer choice

comp_pick=random.randint(1, 3)
if comp_pick==1:
	comp_pick='rock'
elif comp_pick==2:
	comp_pick='paper'
else:
	comp_pick='scissors'


#Function to start game


Result=StringVar()

def play():
	user_pick=user_take.get()
	if user_pick==comp_pick:
		Result.set('tie')
	elif user_pick=='rock'and comp_pick=='paper':
		Result.set('you loose. I chose paper')
	elif user_pick=='rock'and comp_pick=='scissors':
		Result.set('You win :C. I chose scissors')
	elif user_pick=='paper'and comp_pick=='rock':
		Result.set('you win. I chose rock')
	elif user_pick=='paper'and comp_pick=='scissors':
		Result.set('you loose. I chose scissors')
	elif user_pick=='scissors'and comp_pick=='rock':
		Result.set('you loose. I chose rock')
	elif user_pick=='scissors'and comp_pick=='paper':
		Result.set('you win. I chose paper')
	else:
		Result.set('invalid option. Select any one: rock, paper, scissors')



#Function to reset

def Reset():
	Result.set("")
	user_take.set("")


#Function to exit
def Exit():
	root.destroy()


#Define Buttons

Entry(root, font = 'arial 10 bold', textvariable = Result, 
bg ='#f4f5d0', width = 50,).place(x=25, y = 250)

Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='#f4f5d0', command=play).place(x=150, y=190)
Button(root, font='arial 13 bold', text='RESET', padx=5, bg='#f4f5d0', command=Reset).place(x=70, y=310)
Button(root, font='arial 13 bold', text='EXIT', padx=5, bg='#f4f5d0', command=Exit).place(x=230, y=310)


root.mainloop()

	