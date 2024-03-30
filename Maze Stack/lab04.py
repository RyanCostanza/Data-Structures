from Stack import Stack

def printMaze(maze):
	for row in range(len(maze)):
		for col in range(len(maze[0])):
			print("|{:<2}".format(maze[row][col]), sep='',end='')
		print("|")
	return

def solveMaze(maze, startX, startY):
	stack = Stack()
	stack.push((startX,startY))
	step = 1
	maze[startX][startY] = step
	while stack.isEmpty() == False:
		x, y = stack.peek()
		if maze[x][y] == 'G':
			return True
		c = 0
		for i in [(-1,0), (0,-1), (1,0), (0,1)]:
			a, b = i
			nx = x + a
			ny = y + b
			if maze[nx][ny] == 'G':
				stack.push((nx,ny))
				break
			elif maze[nx][ny] == ' ':
				step = step + 1
				maze[nx][ny] = step
				stack.push((nx,ny))
				break
			c += 1
			if c == 4:
				stack.pop()
	return False