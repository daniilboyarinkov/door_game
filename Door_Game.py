from random import randint
from tkinter import *
root = Tk()

lvl = 1
pr = 0
number = 0
text = ''
text_1 = ''



def main_window():
	root.geometry('750x450')
	root.resizable(False, False)
	root.title('Door_Game')
	root['bg'] = '#191919'
	window_1()


def draw_hey():
	hey = Label(root, text='ДОБРЫЙ ВЕЧЕР', font=("Comic Sans MS", 20, 'bold'), bg='#191919', fg='#e1cc4f')
	hey.pack()


def draw_choose():
	choose_text = Label(root, text='choose the door', font=("Comic Sans MS", 20, 'bold'), bg='#191919', fg='#e55ea2')
	choose_text.pack()


def draw_result():
	result_text = Label(root, text=text, font=("Comic Sans MS", 20, 'bold'), bg=root['bg'], fg='yellow')
	result_text.place(x=100, y=200)
	result_text_1 = Label(root, text=text_1, font=("Comic Sans MS", 20, 'bold'), bg=root['bg'], fg='yellow')
	result_text_1.place(x=120, y=250)


def draw_next():
	next_btn = Button(root, text='next', font=("Comic Sans MS", 20, 'bold'), relief='ridge', bg='grey22', activebackground='black', command=nexttt)
	next_btn.place(x=350, y=340)


def draw_enter():
	global number
	enter_text = Label(root, text=f'you entered {number} door', font=("Comic Sans MS", 20, 'bold'), bg=root['bg'], fg='#9932cc')
	enter_text.place(x=250, y=100)


def draw_kind():
	hey = Label(root, text='приятной игры!', font=("Comic Sans MS", 20, 'bold'), bg='#191919', fg='#e1cc4f')
	hey.pack()


def draw_blank_line():
	blank_line = Label(root, text=None, bg=root['bg'])
	blank_line.pack()


def draw_doors():
	entry()
	door1 = Button(root, text='Door 1 *', font=("Comic Sans MS", 20, 'bold'), bd=5, pady=80, relief='ridge', bg='purple', activebackground='black', command=door_1_choosed)
	door1.place(x=50, y=200)

	door2 = Button(root, text='Door 2 *', font=("Comic Sans MS", 20, 'bold'), bd=5, pady=80, relief='ridge', bg='purple', activebackground='black', command=door_2_choosed)
	door2.place(x=315, y=200)

	door3 = Button(root, text='Door 3 *', font=("Comic Sans MS", 20, 'bold'), bd=5, pady=80, relief='ridge', bg='purple', activebackground='black', command=door_3_choosed)
	door3.place(x=560, y=200)


def entry():
	entry = Label(root, text='Entry:', font=("Chiller", 32, 'bold'), bg=root['bg'], fg='darkgreen')
	entry.place(x=70, y=130)
	entry1 = Label(root, text='Entry:', font=("Chiller", 32, 'bold'), bg=root['bg'], fg='darkgreen')
	entry1.place(x=340, y=130)
	entry2 = Label(root, text='Entry:', font=("Chiller", 32, 'bold'), bg=root['bg'], fg='darkgreen')
	entry2.place(x=590, y=130)


def hoorey():
	hoorey = Label(root, text='Hoorey!!!', font=("Curlz MT", 32, 'bold'), bg=root['bg'], fg='red')
	hoorey.place(x=550, y=350)
	hoorey1 = Label(root, text='Hoorey!!!', font=("Curlz MT", 32, 'bold'), bg=root['bg'], fg='red')
	hoorey1.place(x=50, y=350)


def not_hoorey():
	not_hoorey = Label(root, text=':(  :(  :(  :(  :(  :(', font=("Curlz MT", 32, 'bold'), bg=root['bg'], fg='black')
	not_hoorey.place(x=450, y=350)
	not_hoorey1 = Label(root, text=':(  :(  :(  :(  :(  :(', font=("Curlz MT", 32, 'bold'), bg=root['bg'], fg='black')
	not_hoorey1.place(x=50, y=350)


def draw_level():
	global lvl
	level_text = Label(root, text=f'level: {lvl}', font=("Comic Sans MS", 20, 'bold'), bg=root['bg'], fg='#cc9293')
	level_text.place(x=25, y=25)


def draw_end():
	me = Label(root)
	me.place(x=370, y=0)
	end = Label(root, text='GAME OVER', font=("Chiller", 62, 'bold'), bg='#191919', fg='#e55ea2')
	end.place(x=50, y=175)
	end_level_text = Label(root, text=f'вы прошли {lvl} уровней', font=("Comic Sans MS", 14, 'bold'), bg=root['bg'], fg='grey20')
	end_level_text.place(x=25, y=400)


def window_1():
	draw_level()
	draw_hey()
	draw_blank_line()
	draw_choose()
	draw_doors()


def clear_window():
	for object_name in list(root.place_slaves()):
		object_name.place_forget()
	for object_name in list(root.pack_slaves()):
		object_name.pack_forget()


def window_2():
	clear_window()
	if check_pr(lvl, pr) is True:
		hoorey()
	elif check_pr(lvl, pr) is False:
		not_hoorey()
	draw_blank_line()
	draw_enter()
	draw_result()
	draw_next()


def window_3():
	global lvl
	lvl += 1
	clear_window()
	draw_level()
	draw_kind()
	draw_blank_line()
	draw_choose()
	draw_doors()


def window_4():
	clear_window()
	draw_end()


def check_pr(lvl, pr):
	global text
	global text_1
	if lvl <= 5:
		if pr > 1:
			text = 'Вам повезло, дверь оказалась открытой,'
			text_1 = 'вы проходите на следующий уровень'
			return True
		else:
			text = 'Вам не повезло, эта дверь закрыта'
			text_1 = 'для вас эта игра закончена'
			return False
	elif lvl > 5 and lvl <= 10:
		if pr > 5:
			text = 'Вам повезло, дверь оказалась открытой,'
			text_1 = 'вы проходите на следующий уровень'
			return True
		else:
			text = 'Вам не повезло, эта дверь закрыта'
			text_1 = 'для вас эта игра закончена'
			return False
	elif lvl > 10 and lvl <= 15:
		if pr > 10:
			text = 'Вам повезло, дверь оказалась открытой,'
			text_1 = 'вы проходите на следующий уровень'
			return True
		else:
			text = 'Вам не повезло, эта дверь закрыта'
			text_1 = 'для вас эта игра закончена'
			return False
	elif lvl > 15 and lvl <= 20:
		if pr > 15:
			text = 'Вам повезло, дверь оказалась открытой,'
			text_1 = 'вы проходите на следующий уровень'
			return True
		else:
			text = 'Вам не повезло, эта дверь закрыта'
			text_1 = 'для вас эта игра закончена'
			return False
	else:
		if pr > 20:
			text = 'Вам повезло, дверь оказалась открытой,'
			text_1 = 'вы проходите на следующий уровень'
			return True
		else:
			text, text_1 = 'Вам не повезло, эта дверь закрыта', 'для вас эта игра закончена'
			return False


def door_1_choosed():
	global number
	global lvl
	global pr
	number = 1
	pr = randint(0, 100)
	check_pr(lvl, pr)
	window_2()


def door_2_choosed():
	global number
	global lvl
	global pr
	number = 2
	pr = randint(0, 20)
	check_pr(lvl, pr)
	window_2()


def door_3_choosed():
	global number
	global lvl
	global pr
	number = 3
	pr = randint(0, 20)
	check_pr(lvl, pr)
	window_2()


def nexttt():
	if check_pr(lvl, pr) is True:
		window_3()
	elif check_pr(lvl, pr) is False:
		window_4()


def main():

	main_window()


if __name__ == '__main__':
	main()
	root.mainloop()
