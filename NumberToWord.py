
class NumbersToWords():
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
			denom = ''
			for k, v in self.__grouping__.items():
				if len(k) == 3:
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

		# sorted elements of __grouping__ based on keys' length
		groupIndex = sorted(self.__grouping__.keys(), key = lambda n: len(n))
		for k in groupIndex:
			if self.lenNumber(number) > 3: # only assign denomination if the number gets to thousands
				if self.lenNumber(number) >= len(k):
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
				numList.append(num)
		numList.reverse()
		return numList



	def english(self, number):

		'''This function  returns the english reading of the number'''

		engReading = '' # capture the entire english reading
		numList = self.reduceNum(number)
		highestDenom = self.denomination(number) # highest denomination of the number
		cleanDiv = self.breakIt(number)[0] # the number 3-digit strings in numList, corresponding to __grouping__ keys
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
						dummyStr = '1' * dummyLen
						denom = [v for k, v in self.__grouping__.items() if len(dummyStr) == len(k)]
						engReading += self.oneTwoEng(num) + ' ' + str(denom[0])
						c += 1
						dummyLen -= remainder
					if len(num) == 3:
						engReading += self.threeEng(num) 
						c += 1
						dummyLen -= 3

				else:
					dummyStr = '1' * dummyLen
					denom = [v for k, v in self.__grouping__.items() if len(dummyStr) == len(k)]
					dummyLen -= 3
					engReading += str(' ' + self.threeEng(num)) + ' ' + str(denom[0])

			

		return engReading
