def GridScan(Grid, Adjacent):

	def GetHorz(Grid, x, y, Adjacent):
		Tuple = []
		if y<len(Grid):
			if x<=len(Grid) -Adjacent:
				for i in range(Adjacent):
					n = Grid[y][x +i]
					Tuple.append(n)
				return Tuple
		return None


	def GetVert(Grid, x, y, Adjacent):
		Tuple = []
		if y<=len(Grid) -Adjacent:
			if x<len(Grid):
				for i in range(Adjacent):
					n = Grid[y +i][x]
					Tuple.append(n)
				return Tuple
		return None


	def GetDiagEast(Grid, x, y, Adjacent):
		Tuple = []
		if y<=len(Grid) -Adjacent:
			if x<=len(Grid) -Adjacent:
				for i in range(Adjacent):
					n = Grid[y +i][x +i]
					Tuple.append(n)
				return Tuple
		return None

	def GetDiagWest(Grid, x, y, Adjacent):
		Tuple = []
		if y<=len(Grid) -Adjacent:
			if x >=Adjacent:
				for i in range(Adjacent):
					n = Grid[y +i][x -i]
					Tuple.append(n)
				return Tuple
		return None


	Values = []

	for i in range(len(Grid)):
		for j in range(len(Grid)):
			h = GetHorz(Grid, i, j, Adjacent)
			v = GetVert(Grid, i, j, Adjacent)
			e = GetDiagEast(Grid, i, j, Adjacent)
			w = GetDiagWest(Grid, i, j, Adjacent)
			if h:
				Values.append(h)
			if v:
				Values.append(v)
			if e:
				Values.append(e)
			if w:
				Values.append(w)

	return(Values)
