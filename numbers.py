
class NumbersToWords():
	__ones__ = {
		'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', 
		'6':'six', '7':'seven', '8':'eight', '9':'nine',
		'11':'eleven', '12':'twelve', '13':'thirteen', 
		'14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', 
		'18':'eighteen', '19':'nineteen'
	}

	__tens__ = {
		'10':'ten', '20': 'twenty', '30':'thirty', 
		'40':'forty', '50':'fifty', '60':'sixty', '70':'seventy', 
		'80':'eighty', '90':'ninety'
	}

	__grouping__ = {
		(0,'100'):'hundred', (1,'1000'):'thousand', (2,'1000000'):'million', 
		(3,'1000000000'):'billion', (4,'1000000000000'):'trillion'
	}

	def oneTwoEng(self, number):
		'''This function is meant to turn up to two digit numbers 
		into english literals for those numbers'''
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
		'''This function is meant to turn three digit numbers 
			into their english literals'''
		if len(number) == 3:
			denom = ''
			for k, v in self.__grouping__.items():
				if len(k[1]) == 3:
					denom = v
			#################################
			x = number[0]
			for a in self.__ones__:
				if x != str(0):
					if x == a:
						x = self.__ones__[a]
				else:
					x = ''
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
			answer = x + ' ' + denom + ' ' + y + ' ' + z
			if "   " in answer or "  " in answer: 
				answer.replace('  ', ' ')
				try: # getting rid of other possible extra white spaces
					answer.replace('  ', ' ')
				except:
					pass
			return answer.rstrip()


	def lenNumber(self, number):
		return len(number)


	def denomination(self, number):
		'''This function returns the highest denomination 
			of the number based on the length of number'''
		groupIndex = sorted(self.__grouping__.keys(), key=lambda n:n[0], reverse = True)
		for k in groupIndex:
			if self.lenNumber(number) > 3:
				if self.lenNumber(number) >= len(k[1]):
					return self.__grouping__[k]


	def breakIt(self, number):
		'''Find the number of groupings of 
		3 digits (whole) or less (remainder)'''
		whole = 0
		remainder = 0
		if self.lenNumber(number)/3 > 1:
			whole = self.lenNumber(number)//3
			remainder = self.lenNumber(number)%3
		return (whole, remainder)
	
	"""
	def assignDenom(self, number):
		'''Find the highest possible denomination for the given number'''
		highestDenom = ''
		Length = 0
		for i in self.__grouping__[1]:
			if self.lenNumber(number) >= len(i): # 
				highestDenom = self.__grouping__[i]
				Length = len(i)
			else:
				break
		return highestDenom
	"""

	def reduceNum(self, number):
		'''This function breaks down the given number into 
			smaller strings of upto 3-digit long'''
		iLength = self.lenNumber(number)
		numList = []
		num = ''

		try:
			for i in range(0, iLength):
				num += number[i]
				if (i+1) % 3 == 0:
					numList.append(num)
					num = ''
		finally:
			if num == '':
				pass
			else:
				numList.append(num)

		return numList



	def english(self, number):
		'''This function  returns the english reading of the number'''
		engReading = ''
		numList = self.reduceNum(number)

		highestDenom = self.denomination(number)
		#cleanDiv = self.breakIt(number)[0] # number of 3-digit strings
		groupNum = len(numList) # length of the NumList, corresponding to the __grouping__ keys
		c = 0
		for num in numList:
			if c == 0:
				if len(num[1]) < 3:
					engReading += self.oneTwoEng(num)
					engReading += ' ' + highestDenom
					c += 1
				if len(num[1]) == 3:
					engReading += self.threeEng(num)
					engReading += ' ' + highestDenom
					c += 1
			else:
				groupNum -= 1
				engReading += self.threeEng(num)
				if groupNum 



		#varLength = self.lenNumber(number)
		#if self.breakIt(number)[1] == 0:
		#	for i in range(0, self.lenNumber(number), 3):
		#		engReading += self.threeEng(number) + ' ' + self.denomination(number)
		#		#varLength -= 3
		#else:
		#	remainder = self.breakIt(number)[1]
		#	c = 0
		#	for i in range(0, self.lenNumber(number), 3):
		#		if c == 0:
		#			engReading += self.oneTwoEng(number) + ' ' + self.denomination(number)
		#			#varLength -= remainder
		#			c += 1
		#		else:
		#			engReading += self.threeEng(number) + ' ' + self.denomination(number)
		#			#varLength -= 3


		"""
		if self.breakIt(number)[1] == 0:
			for i in range(0, self.breakIt(number)[0] * 3, 3):
				if i == 0:
					#if iLength > 3:
						#engReading += self.threeEng(number) + ' ' + self.assignDenom(number)[1]
						#iLength -= 3
				else:
					while i: 
						if iLength > 3:
							engReading = ' ' + self.threeEng(number) + ' ' + 
"""

