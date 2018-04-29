
class NumberToWord():
	__ones__ = {
		'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', 
		'6':'six', '7':'seven', '8':'eight', '9':'nine', '11':'eleven', 
		'12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', 
		'16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen'
	}

	__tens__ = {
		'10':'ten', '20': 'twenty', '30':'thirty', '40':'forty', '50':'fifty', 
		'60':'sixty', '70':'seventy', '80':'eighty', '90':'ninety'
	}

	__grouping__ = {
		'100':'hundred', '1000':'thousand', '1000000':'million', 
		'1000000000':'billion', '1000000000000':'trillion'
	}



	def oneTwoEng(self, number):

		'''This function is meant to turn up to two digit 
			numbers into english literals for those numbers'''

		if number in self.__ones__:
			return self.__ones__[number]
		#################################
		elif number in self.__tens__:
			return self.__tens__[number]
		#################################
		elif len(number) == 2:
			y = number[0]
			for b in self.__tens__:
				if y != str(0):
					if y in b:
						y = self.__tens__[b]
			#################################
			z = number[1]
			for c in self.__ones__:
				if z != str(0):
					if z == c:
						z = self.__ones__[c]
			answer = y + ' ' + z
			return answer.strip()



	def threeEng(self, number):

		'''This function is meant to turn three digit 
			numbers into their english literals'''

		if len(number) == 3:
			denom = 'hundred'
			#################################
			x = number[0]
			for a in self.__ones__:
				if x != str(0):
					if x == a:
						x = self.__ones__[a]
				else:
					x = ''
					denom = ''
			#################################
			y = number[1]
			if y == str(1):
				for b in self.__ones__:
					if str(y + number[2]) == b:
						y = self.__ones__[b]
			elif y != str(0):
				for b in self.__tens__:		
					if y in b:	
						y = self.__tens__[b]
			else:
				y = ''
			#################################
			z = number[2]
			for c in self.__ones__:
				if z == str(0):
					z = ''
				elif number[1] != str(1):	
					if z == c:
						z = self.__ones__[c]
				else:
					z = ''
			#################################
			if x == '':
				answer = y + ' ' + z
			else:
				answer = x + ' ' + denom + ' ' + y + ' ' + z
			if "   " in answer: 
				answer.replace('   ', ' ')
				try: # getting rid of other possible extra white spaces
					answer.replace('  ', ' ')
				except:
					pass
			return answer.rstrip()


	def NumberStr(self, number):
		return number


	def lenNumber(self, number):
		return len(number)


	def message(self, text):
		return text


	def denomination(self, number):

		'''This function returns the highest denomination 
			of the number based on the length of number'''

		value = ''
		groupIndex = sorted(self.__grouping__.keys(), key = lambda n: len(n))
		whole = self.breakIt(number)[0]
		remainder = self.breakIt(number)[1]

		for k in groupIndex:
			if whole * 3 + remainder <= len(groupIndex[-1])+2:
				if whole * 3 + remainder > 3:
					if self.lenNumber(number) in range(len(k), len(k)+3):
						value = self.__grouping__[k]
			else:
				raise ValueError("""Number too big... denomination not defined for the first {} in {}. 
					\n\rConsider expanding the __grouping__ dictionary in NumberToWord class...""" \
					.format(self.reduceNum(number)[0], self.NumberStr(number)))
		return value


	def breakIt(self, number):

		'''Find the number of groupings of 3 
			digits (whole) or less (remainder)'''

		whole = 0
		remainder = 0
		
		if self.lenNumber(number)/3 >= 1:
			whole = self.lenNumber(number)//3
			remainder = self.lenNumber(number)%3
		else:
			remainder = self.lenNumber(number)%3
		return (whole, remainder)


	def reduceNum(self, number):

		'''This function breaks down the given number into 
			smaller strings of upto 3-digit long'''

		iLength = self.lenNumber(number)
		numList = []
		num = ''
		numRev = ''
		
		c = 0
		try:
			for i in range(iLength-1, -1, -1):
				c += 1
				num += number[i]
				if c % 3 == 0:
					for z in range(len(num)-1, -1, -1):
						numRev += num[z] 
					numList.append(numRev)
					num = ''
					numRev = ''
		finally:
			if num == '':
				pass
			else:
				for z in range(len(num)-1, -1, -1):
					numRev += num[z] 
				numList.append(numRev)
		numList.reverse()
		return numList



	def reconstruct(self, start, number):

		'''This function reconstructs a new number of length 
						len(number) - start
			from the original number by eliminating starting
			first characters from the number.

			type(start) --> int 
			type(number) --> str 			'''

		newNumber = ''
		for i in range(start, len(number)):
			newNumber += number[i]
		return newNumber



	def english(self, number):

		'''This function  returns the english reading of the number'''

		engReading = '' # capture the entire english reading
		Number = self.NumberStr(number)
		numList = self.reduceNum(number)
		remainder = self.breakIt(number)[1]
		dummyLen = self.lenNumber(number)

		c = 0
		for num in numList:
			if len(numList) == 1:
				if len(num) < 3:
					engReading += self.oneTwoEng(num)
				if len(num) == 3:
					engReading += self.threeEng(num)  
			else: 
				if c == 0:			
					if len(num) < 3:
						engReading += self.oneTwoEng(num) + ' ' +  self.denomination(Number) #denom
						Number = self.reconstruct(remainder, Number)
						c += 1
					if len(num) == 3:
						engReading += self.threeEng(num) + ' ' + self.denomination(Number) #denom
						Number = self.reconstruct(3, Number)
						c += 1
				else: 
					if num is numList[-1]:
						engReading += ' ' + self.threeEng(num) 
					else:
						engReading += ' ' + self.threeEng(num) + ' ' + self.denomination(Number) #denom
						Number = self.reconstruct(3, Number)
			

		return engReading
