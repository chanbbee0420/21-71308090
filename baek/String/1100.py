def chess():
	board = []
	
	for _ in range(8):
		board.append(list(map(str, list(input()))))
	
	rst = 0
	for i in range(8):
		for j in range(8):
			if (i + j) % 2 == 0:
				if board[i][j] == 'F':
					rst += 1
	
	print(rst)

if __name__ == '__main__':
	chess()