####### TIC TAC TOE GAME! CREATED BY BRAYAN AYALA
####### MILESTONE PROJECT FROM PYTHON 3: ZERO TO HERO
import random
import winsound


def display_board(board):

	print('    ' + board[7] + '| ' + board[8] + ' |' + board[9])
	print('    ' + board[4] + '| ' + board[5] + ' |' + board[6])
	print('    ' + board[1] + '| ' + board[2] + ' |' + board[3])


def player_input():
	Asking = True
	p1 = ''
	p2 = ''

	while Asking:
		option = input("Player 1 Choose 'X' or 'O': ")

		if option == 'X':
			p1 = 'X'
			p2 = 'O'
			print("Player 2 will be 'O'!")
			Asking = False
		elif option == 'O':
			p1 = 'O'
			p2 = 'X'
			print("Player 2 will be 'X'!")
			Asking = False
		else:
			continue

	return (p1, p2)


def place_marker(board,marker,position):

	board[position] = marker


def winCheck(board):

	#HORIZONTAL CHECK in X
	if ((board[1] + board[2] + board[3] == 'XXX') or (board[4] + board[5] + board[6] == 'XXX') or (board[7] + board[8] + board[9] == 'XXX')):
		print("X WIN")
		return True

	#VERTICAL CHECK in X
	elif ((board[7] + board[4] + board[1] == 'XXX') or (board[8] + board[5] + board[2] == 'XXX') or (board[9] + board[6] + board[3] == 'XXX')):
		print("X WIN")
		return True

	#DIAGONAL CHECK in X
	elif ((board[7] + board[5] + board[3] == 'XXX') or (board[9] + board[5] + board[1] == 'XXX')):
		print("X WIN")
		return True

	#HORIZONTAL CHECK IN O
	elif ((board[1] + board[2] + board[3] == 'OOO') or (board[4] + board[5] + board[6] == 'OOO') or (board[7] + board[8] + board[9] == 'OOO')):
		print("O WIN")
		return True

	#VERTICAL CHECK IN O
	elif ((board[7] + board[4] + board[1] == 'OOO') or (board[8] + board[5] + board[2] == 'OOO') or (board[9] + board[6] + board[3] == 'OOO')):
		print("O WIN")
		return True

	#DIAGONAL CHECK IN O
	elif ((board[7] + board[5] + board[3] == 'OOO') or (board[9] + board[5] + board[1] == 'OOO')):
		print("O WIN")
		return True

	return False


def random_Choose():
	result = random.randint(1,2)

	if result == 1:
		p1 = 'X'
		p2 = 'O'
		print("Player 1 will be 'X'!")
		print("Player 2 will be 'O'!")
		return (p1, p2)

	if result == 2:
		p1 = 'O'
		p2 = 'X'
		print("Player 1 will be 'O'!")
		print("Player 2 will be 'X'!")
		return (p1, p2)



def space_Check(board, position):

	return board[position] == ' '


def is_Board_Full(board):
	for item in range(1,10):
		if space_Check(board, item):
			return False
	return True


def reply(answer = ''):

	if answer.lower() == 'yes':
		return True
	else:
		return False


def updateRank(marker):

	load_p1 = False
	load_p2 = False

	#### Player 1
	try:
		with open('ranking\\p1.txt', mode = 'r') as f:
			p1Points = f.read();
			p1ToInt = int(p1Points)
	except IOError:
		load_p1 = True

	###### Creates new progress in case program doesn't detect one for P1
	if load_p1:
		p1ToInt = 0
		with open('ranking\\p1.txt', mode = 'w') as f:
			f.write('0');

	#### Player 2
	try:
		with open('ranking\\p2.txt', mode = 'r') as f:
			p2Points = f.read();
			p2ToInt = int(p2Points)
	except IOError:
		load_p2 = True

	###### Creates new progress in case program doesn't detect one for P2
	if load_p2:
		p2ToInt = 0
		with open('ranking\\p2.txt', mode = 'w') as f:
			f.write('0');



	if marker == 'X':
		p1ToInt += 1
		p1PointsToStr = str(p1ToInt)

		with open('ranking\\p1.txt', mode = 'w') as f:
			f.write(p1PointsToStr);
			

	elif marker == 'O':
		p2ToInt += 1
		p2PointsToStr = str(p2ToInt)

		with open('ranking\\p2.txt', mode = 'w') as f:
			f.write(p2PointsToStr);


def gameMusic():

	winsound.PlaySound("music\\impact.wav", winsound.SND_LOOP + winsound.SND_ASYNC | winsound.SND_ALIAS )

	# winsound.PlaySound(None, winsound.SND_ASYNC) to stop playing


####################################
##### RUNNING GAME
####################################

print("WELCOME TO TICTACTOE GAME!")

while True:
	gameMusic()
	game_board = ['0',' ',' ',' ',' ',' ',' ',' ',' ',' ']
	counter = 2
	gaming = True
	isSpace = True
	rC = False
	### Ask if want random player
	question = input("Do you want to activate random choose? (Yes or No) ")
	if question.lower() == 'yes':
		rC = True
		p1, p2 = random_Choose()
	else:
		pass

	if not rC:
		p1, p2 = player_input()
	else:
		pass

	while gaming:
		## P1 Turn
		if counter % 2 == 0:
			counter += 1

			while isSpace:
				position = int(input("Position: "))

				if space_Check(game_board, position):
					place_marker(game_board,p1,position)
					break
				else:
					print("Choose a free space!")
					continue

			display_board(game_board)
			if winCheck(game_board):
				updateRank(p1)
				break
			if is_Board_Full(game_board):
				print("MATCH TIED")
				break

		##P2 Turn
		if counter % 2 != 0:
			counter += 1

			while isSpace:
				position = int(input("Position: "))

				if space_Check(game_board, position):
					place_marker(game_board,p2,position)
					break
				else:
					print("Choose a free space!")
					continue

			display_board(game_board)
			if winCheck(game_board):
				updateRank(p2)
				break
			if is_Board_Full(game_board):
				print("MATCH TIED")
				break


	with open('ranking\\p1.txt', mode = 'r') as f:
			showP1Points = f.read();

	with open('ranking\\p2.txt', mode = 'r') as f:
			showP2Points = f.read();


	print(" ")
	print("RANKING: ")
	print("X Wins: {sp1} !".format(sp1 = showP1Points))
	print("O Wins: {sp2} !".format(sp2 = showP2Points))
	print(" ")

	answer = input("Do you want to play again? (Yes or No) ")

	if not reply(answer):
		print("THANKS FOR PLAYING!")
		break
	else:
		continue
