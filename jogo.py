jogador = 1
game = True
pode = True

# Cria o Tabuleiro
tab = []
for i in range(3):
	tab.append( ['-'] * 3 )

def show():
	"""
	Funcao que printa o estado atual do tabuleiro
	"""
	print "\n"
	print "   Jogo da Velha     "
	print "/-----------------\ "
	print "| [[1]  [2]  [3]] |"
	print "|",tab[0], "|" # "\n"
	print "|-----------------|"
	print "| [[4]  [5]  [6]] |"
	print "|",tab[1], "|"# "\n"
	print "|-----------------|"
	print "| [[7]  [8]  [9]] |"
	print "|",tab[2], '|'
	print "\-----------------/ "

def verifica(pos):
	"""
	Funcao que verifica se e possivel jogar no local escolhido, para que nao haja mais de uma jogada na mesma posicao!
	"""
	global pode
	if pos == '-':
		pode = True
		return True
	else: 
		print '\nJogada impossivel!\nTente Novamente.'
		pode = False
		return False

def posTab(num, play):
	"""
	Funcao responsavel por tratar o input do usuario e transforma-lo em uma jogada, condicoes baseadas na estrutura do jogo.
	Recebe o local onde vai ser a jogada, e qual jogador que realizou ela. 
	Antes de realizar a jogada, faz a verificacao para ver se e possivel jogar ali onde o jogador tentou jogar.	
	"""
	if num == 1:
		ver = verifica(tab[0][0])
		if ver ==  True:
			if play == 1:
				tab[0][0] = 'X'
			elif play == 2:
				tab[0][0] = 'O'

	elif num == 2:
		ver = verifica(tab[0][1])
		if ver ==  True:
			if play == 1:
				tab[0][1] = 'X'
			elif play == 2:
				tab[0][1] = 'O'

	elif num == 3:
		ver = verifica(tab[0][2])
		if ver ==  True:
			if play == 1:
				tab[0][2] = 'X'
			elif play == 2:
				tab[0][2] = 'O'

	elif num == 4:
		ver = verifica(tab[1][0])
		if ver ==  True:
			if play == 1:
				tab[1][0] = 'X'
			elif play == 2:
				tab[1][0] = 'O'

	elif num == 5:
		ver = verifica(tab[1][1])
		if ver ==  True:
			if play == 1:
				tab[1][1] = 'X'
			elif play == 2:
				tab[1][1] = 'O'

	elif num == 6:
		ver = verifica(tab[1][2])
		if ver ==  True:
			if play == 1:
				tab[1][2] = 'X'
			elif play == 2:
				tab[1][2] = 'O'

	elif num == 7:
		ver = verifica(tab[2][0])
		if ver ==  True:
			if play == 1:
				tab[2][0] = 'X'
			elif play == 2:
				tab[2][0] = 'O'

	elif num == 8:
		ver = verifica(tab[2][1])
		if ver ==  True:
			if play == 1:
				tab[2][1] = 'X'
			elif play == 2:
				tab[2][1] = 'O'

	elif num == 9:
		ver = verifica(tab[2][2])
		if ver ==  True:
			if play == 1:
				tab[2][2] = 'X'
			elif play == 2:
				tab[2][2] = 'O'

def vitoria(player):
	"""
	Funcao que anuncia o vencedor da partida e encerra o jogo
	"""
	global game
	if player == 1:
		ganhou = 2
	elif player == 2:
		ganhou = 1

	show()

	print "\n"
	print "/---------------\ "
	print "|    PARABENS   |"
	print "|---------------|"
	print "|  [Jogador {a}]  |".format(a = ganhou)
	print "|---------------|"
	print "|  Voce Ganhou! |"
	print "\---------------/\n \n \n"

	game = False

def verWin(player):
	"""
	Verifica todas possibilidades de vitoria que existem no jogo da velha, levando em consideracao que algum player tenha feito esta combinacao.
	Caso seja realmente um caso de vitoria, chama uma funcao que anuncia a vitoria do player
	"""
	# Horizontal
	if tab[0][0] == tab[0][1] and tab[0][0] == tab[0][2] and tab[0][0] != '-':
		vitoria(player)
	elif tab[1][0] == tab[1][1] and tab[1][0] == tab[1][2] and tab[1][0] != '-':
		vitoria(player)
	elif tab[2][0] == tab[2][1] and tab[2][0] == tab[2][2] and tab[2][0] != '-':
		vitoria(player)
	# Vertical
	if tab[0][0] == tab[1][0] and tab[0][0] == tab[2][0] and tab[0][0] != '-':
		vitoria(player)
	elif tab[0][1] == tab[1][1] and tab[0][1] == tab[2][1] and tab[0][1] != '-':
		vitoria(player)
	elif tab[0][2] == tab[1][2] and tab[0][2] == tab[2][2] and tab[0][2] != '-':
		vitoria(player)
	# Diagonal
	if tab[0][0] == tab[1][1] and tab[0][0] == tab[2][2] and tab[0][0] != '-':
		vitoria(player)
	elif tab[2][0] == tab[1][1] and tab[2][0] == tab[0][2] and tab[2][0] != '-':
		vitoria(player)

def jogar(player):
	"""
	Funcao responsavel por organizar e realizar as jogadas da partida.
	"""
	global jogador
	if player == 1:
		jogada = input("\n[Jogador 1] \nDigite o numero correspondente a casa onde quer jogar: ")
		posTab(jogada, 1)
		if pode == True:
			jogador = 2
		elif pode == False:
			jogador = 1

	elif player	 == 2:
		jogada = input("\n[Jogador 2] \nDigite o numero correspondente a casa onde quer jogar: ")
		posTab(jogada, 2)
		if pode == True:
			jogador = 1
		elif pode == False:
			jogador = 2

while(game):
	"""
	Condicao principal do game, onde ele roda constantemente!
	"""
	show()
	jogar(jogador)
	verWin(jogador)