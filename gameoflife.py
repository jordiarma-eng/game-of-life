#imports required to read files from patterns folder


#Validate Format Function
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


#Read Seed (Input Text Pattern) from File
seed :str = open("patterns/toad.life", "r")
seed_lines :str = seed.readlines()

#Validate Seed Format > Nonzero exit status
validFormat :bool = validateFormat(seed_lines)
print("Formato Valido? " + str(validFormat))

#Find size of Seed
seed_size :int = 0
for line in seed_lines:
    if not line.startswith('!'):
    	seed_size = len(line)-line.count('\n')

print("Seed size: " + str(seed_size))

#Create Input (original) Array
#Tip 2: Ignore lines starts with !
origin :str = [[ '.' for i in range(seed_size) ] for j in range(seed_size) ]

#Fill & clean origin Array
i :int = 0;
for line in seed_lines:
    if not line.startswith('!'):
    	word :str = line.rstrip()
    	origin[i] = word
    	i += 1

print("Origin: " + str(origin))

#Create Output (result) Array
result :str = origin
print("Result: " + str(result))


#Travel Input Matrix Content creating Output Matrix Content 
#Tip3: Be careful with border rows and cols



#Print Game of Life results
for row in result:
	print(str(row))