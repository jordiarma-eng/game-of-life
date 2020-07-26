#imports required to read files from patterns folder


#Function that Validates Seed Format 
def validateFormat( lines :str ):
	start :bool = True
	line_size :int = 0
	for line in lines:
		if line[0] == '!' and start:
			#Valid Format, don't do anything
			pass	

		elif line[0] == '.' or line[0] == 'O':
			#Change the start to false and validate all characters are valid
			if start:
				start = False
				line_size = len(line)-line.count('\n')	

			if line_size != len(line)-line.count('\n'):
				#Invalid Format, Not Squared Matrix
				return False

			i :int = 1
			while i < line_size:
				if (line[i] != '.' and line[i] != 'O'):
					#Invalid Format, Contains Not Expected Characters
					return False
				i += 1

		else: 
			#Invalid format, Unexpected Cases
			return False
	return True


#Function that calculates the next generation of the Game of Life Infection
def next_generation ( entrada , salida , seed_size ):
	i :int = 0
	while i < seed_size:
		j :int = 0
		while j < seed_size:
			alive_around :int = 0	

			#First Row
			if i == 0 :	
				#First Col
				if j == 0:
					#print("first first")
					if entrada[i][j+1] == "O": alive_around += 1
					if entrada[i+1][j+1] == "O": alive_around += 1
					if entrada[i+1][j] == "O": alive_around += 1

				#Last Col
				elif j == seed_size-1:
					#print("first last")
					if entrada[i+1][j] == "O": alive_around += 1
					if entrada[i+1][j-1] == "O": alive_around += 1
					if entrada[i][j-1] == "O": alive_around += 1

				#Other Cols
				else:
					#print("first middle")
					if entrada[i][j+1] == "O": alive_around += 1
					if entrada[i+1][j+1] == "O": alive_around += 1
					if entrada[i+1][j] == "O": alive_around += 1
					if entrada[i+1][j-1] == "O": alive_around += 1
					if entrada[i][j-1] == "O": alive_around += 1

			#Last Row
			elif i == seed_size-1 :	
				#First Col
				if j == 0:
					#print("last first")
					if entrada[i-1][j] == "O": alive_around += 1
					if entrada[i-1][j+1] == "O": alive_around += 1
					if entrada[i][j+1] == "O": alive_around += 1

				#Last Col
				elif j == seed_size-1:
					#print("last last")
					if entrada[i-1][j-1] == "O": alive_around += 1
					if entrada[i-1][j] == "O": alive_around += 1
					if entrada[i][j-1] == "O": alive_around += 1

				#Other Cols
				else:
					#print("last middle")
					if entrada[i-1][j-1] == "O": alive_around += 1
					if entrada[i-1][j] == "O": alive_around += 1
					if entrada[i-1][j+1] == "O": alive_around += 1
					if entrada[i][j+1] == "O": alive_around += 1
					if entrada[i][j-1] == "O": alive_around += 1
	

			#Other Rows
			else:	
				
				#First Col
				if j == 0:
					#print("other first")
					if entrada[i-1][j] == "O": alive_around += 1
					if entrada[i-1][j+1] == "O": alive_around += 1
					if entrada[i][j+1] == "O": alive_around += 1
					if entrada[i+1][j+1] == "O": alive_around += 1
					if entrada[i+1][j] == "O": alive_around += 1

				#Last Col
				elif j == seed_size-1:
					#print("other last")
					if entrada[i-1][j-1] == "O": alive_around += 1
					if entrada[i-1][j] == "O": alive_around += 1
					if entrada[i+1][j] == "O": alive_around += 1
					if entrada[i+1][j-1] == "O": alive_around += 1
					if entrada[i][j-1] == "O": alive_around += 1	

				#Other Cols
				else:
					#print("other middle")
					if entrada[i-1][j-1] == "O": alive_around += 1
					if entrada[i-1][j] == "O": alive_around += 1
					if entrada[i-1][j+1] == "O": alive_around += 1
					if entrada[i][j+1] == "O": alive_around += 1
					if entrada[i+1][j+1] == "O": alive_around += 1
					if entrada[i+1][j] == "O": alive_around += 1
					if entrada[i+1][j-1] == "O": alive_around += 1
					if entrada[i][j-1] == "O": alive_around += 1

			#print(str(i) + " " + str(j) + " > " + str(alive_around))

			#Define action depending current alive or dead
			aux = result[i]
			if entrada[i][j] == "O":				

				#Less than 2 > Dead
				if alive_around < 2: 
					aux = aux[:j] + "." + aux[j+1:]
					result[i] = aux

				#More than 3 > Dead
				elif alive_around > 3: 
					aux = aux[:j] + "." + aux[j+1:]
					result[i] = aux	

				#2 or 3 > Live
				elif alive_around == 2 or alive_around == 3: 
					aux = aux[:j] + "O" + aux[j+1:]
					result[i] = aux


			elif entrada[i][j] == ".": 
				#3 > Born 
				if alive_around == 3:
					aux = aux[:j] + "O" + aux[j+1:]
					result[i] = aux

			j += 1
		i += 1



#ENTRY POINT OF GAME OF LIFE SIMULATION
#Read Seed (Input Text Pattern) from File
seed :str = open("patterns/toad.life", "r")
seed_lines :str = seed.readlines()

#Validate Seed Format > Nonzero exit status
validFormat :bool = validateFormat(seed_lines)
#print("Valid Format? " + str(validFormat))

#Find size of Seed
seed_size :int = 0
for line in seed_lines:
    if not line.startswith('!'):
    	seed_size = len(line)-line.count('\n')

#print("Seed size: " + str(seed_size))

#Create Input (original) Array
#Tip 2: Ignore lines starts with !
origin :str = [[ '' for i in range(seed_size) ] for j in range(seed_size) ]


#Fill & clean origin Array
i :int = 0;
for line in seed_lines:
    if not line.startswith('!'):
    	word :str = line.rstrip()
    	origin[i] = word
    	i += 1
#print("Origin: " + str(origin))

#Create Output (result) Array
result :str = [[ '' for i in range(seed_size) ] for j in range(seed_size) ]

#Fill & clean First Next Gent Array
i :int = 0;
for line in seed_lines:
    if not line.startswith('!'):
    	word :str = line.rstrip()
    	result[i] = word
    	i += 1
#print("Result: " + str(result))

#Travel Input Matrix Content creating Output Matrix Content 
#Tip3: Be careful with border rows and cols
next_generation(origin, result, seed_size)

#Print Game of Life results
for row in result:
	print(str(row))