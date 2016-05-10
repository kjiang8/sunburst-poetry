import string
from itertools import groupby
from random import randint

# cd /Volumes && ls

def poem(filename):

	lines = parse(filename)

	dashed = []

	for c in lines:
		c = "".join(x for x in c if x not in string.punctuation)
		c = c.strip()
		c = string.replace(c," ","-")
		#print c
		dashed.append(c)

	#print dashed
	dashed = sorted(dashed)

	#print "SORTED: ",dashed

	freq = [len(list(group)) for key, group in groupby(dashed)]
	#print freq

	#removing duplicates since sets don't work
	nondupl = []

	for x in dashed:
		if x not in nondupl:
			nondupl.append(x)

	g = open('word-order.csv','w+')
	g = open('word-order.csv','a') #clear existing file
	for i in range(len(nondupl)):
		#print nondupl[i], freq[i]
		g.write(nondupl[i] + "," + str(freq[i]) +"\n")

	g.close()

	print "success"

def makedict(lines):

	structure = []
	struc_d = {}

	for i in range(len(lines)):
		x = lines[i].strip() #strip leading and ending whitestrip
		#firstword = x.split(' ')[0]
		#print firstword

		if i < 10: #gets 2-digit number for key
			key = '0' + str(i) + x.split(' ')[0]
		else:
			key = str(i) + x.split(' ')[0]

		if x == "":
			struc_d[key] = 0
			structure.append(0) #stanza break
		else: 
			struc_d[key] = len(x.split(" "))
			structure.append(len(x.split(" ")))

	ordered = sorted(struc_d.items())

	#print structure
	print(ordered)

def parse(poem):

	fileName = "poems/"+poem
	f = open(str(fileName)) #open file
	raw = f.read().lower() 
	#print raw

	#removes stanza breaks
	raw = string.replace(raw, "\n\n", "\n")
	#raw = string.replace(raw, '"',"")

	lines = raw.split('\n')
	#print lines

	return lines

def colors(filename):

	lines = parse(filename)

	words = []

	for c in lines:
		c = "".join(x for x in c if x not in string.punctuation)
		c = c.strip(" ")
		words.extend(c.split(" ")) #array of words

	words = list(set(words)) #removes duplicates
	
	commonwords = ['a','the','and','an','be','or','i','you','me','to','all','had','not','they','for','in','on','such','when','then','them','of','their','that','but','with','my','is','as','at','am','which','beside','upon','what','mood','never','along','could','way','its','was','his','see','he','did','thy','made','go','do','now','by','men','into','your','there','too','have','no','how','who','though','beneath','oer']

	for x in commonwords:
		try:
			words.remove(x)
		except ValueError:
			pass
	
	print words, len(words)

	hexcolors = []

	numcolors = raw_input('# of colors: ')

	for i in range(int(numcolors)):
		hexcolors.append('#' + raw_input(str(i) + '#'))

	print hexcolors

	f = open('colors.csv','a')
	f.write('var colors = { //'+ filename + '\n')
	for x in words:
		tag = raw_input(x+ " ")
		if tag != '':
			f.write('"'+x+'": "'+hexcolors[int(tag)]+'",\n')

	f.write('};\n\n\n')
	f.close()

def randcolors(filename):

	lines = parse(filename)

	words = []

	for c in lines:
		c = "".join(x for x in c if x not in string.punctuation)
		c = c.strip(" ")
		words.extend(c.split(" ")) #array of words

	words = list(set(words)) #removes duplicates
	
	#commonwords = ["i'm",'with','you','in','rockland']

	hexcolors = []

	numcolors = raw_input('# of colors: ')

	for i in range(int(numcolors)):
		hexcolors.append('#' + raw_input(str(i) + '#'))

	print hexcolors

	f = open('colors.csv','a')
	f.write('var colors = { //'+ filename + '\n')
	'''
	for i in range(len(commonwords)):
		try:
			words.remove(commonwords[i])
		except ValueError:
			pass		
		f.write('"'+commonwords[i]+'": "'+hexcolors[i]+'",\n')
	'''
	
	for i in range(len(words)):
		x = randint(0,4)
		f.write('"'+words[i]+'": "'+hexcolors[x]+'",\n')


	f.write('};\n\n\n')
	f.close()

	print 'success'




