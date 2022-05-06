def Permute(Array):
	# print(Array)
	if type(Array) is int:
		Array = [i for i in range(Array)]
	# print(Array)
	Length = len(Array)

	if Length==1:
		return Array
	elif Length==2:
		yield Array
		yield [Array[1], Array[0]]
	else:
		for i in range(Length):
			# print(Array[0:i] +Array[i +1:5])
			Super = Permute(Array[0:i] +Array[i +1:Length])
			for Arr in Super:
				yield [Array[i]]+ Arr
			# while True:
			# 	pass
			pass
	pass


def MultpieDic(Array):
	dic = {}
	for i in Array:
		dic[i] = 0
	for i in Array:
		dic[i] = dic[i] +1
	return dic


def isPermute(Array1, Array2):
	from functions.Algebra import MultpieDic

	if len(Array1)!=len(Array2):
		return False
	elif set.intersection(set(Array1), set(Array2))==set([]):
		return False
	else:
		return MultpieDic(Array1)==MultpieDic(Array2)


def noDuplicates(Dic):
	if type(Dic) != dict:
		Temp = {}
		for ind in range(len(Dic)):
			Temp[ind] = Dic[ind]
		Dic = Temp
	Out = {}
	for k, v in Dic.items():
		for k2, v2 in Dic.items():
			if k2!=k:
				if v2==v:
					break
		Out[k]=v

	return Out
