#imports required to read files from patterns folder
import string

#Validate Format Function
def validateFormat( str ):
	start = True
	seed_line_size = 0
	for line in lines:
		if line[0] == '!' and start:
			#Valid Format, don't do anything
			pass	

		elif line[0] == '.' or line[0] == 'O':
			#Change the start to false and validate all characters are valid
			if start:
				start = False
				seed_line_size = len(line)-line.count('\n')	

			if seed_line_size != len(line)-line.count('\n'):
				#Invalid Format, Not Squared Matrix
				return False

			i = 1
			while i < seed_line_size:
				if (line[i] != '.' and line[i] != 'O'):
					#Invalid Format, Contains Not Expected Characters
					return False
				i += 1	

		else: 
			#Invalid format, Unexpected Cases
			return False
	return True

#Read Seed (Input Text Pattern) from File
seed = open("patterns/toad.life", "r")
lines = seed.readlines()

#Validate Seed Format > Nonzero exit status
validFormat = validateFormat(seed)
print("Formato Valido? " + str(validFormat))




#Create Input (original) Matrix 
#Tip 2: Ignore lines starts with !
#Create Output (result) Matrix

#Travel Input Matrix Content creating Output Matrix Content 
#Tip3: Be careful with border rows and cols

#Print Game of Life results