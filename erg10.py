
import sys
import string
from random import randint

filename = raw_input("Enter the file's name: ")
filename += ".txt"

try:
	file = open(filename, 'r')
except IOError:
	print "Could not find file!"
	raw_input("Press enter to exit...")
	sys.exit()

wordList = []

wordList = file.read().translate(None, string.punctuation)

wordList = wordList.split()

for word in wordList:
	if(any(x.isupper() for x in word)):
		wordList.remove(word)

triplets = []

for x in range(len(wordList) - 2):
	triplets.append([wordList[x], wordList[x + 1], wordList[x + 2]])

keyTriplet = triplets[randint(0, len(triplets) - 1)]

matching = []

for check in range(len(triplets)):
	if(keyTriplet[1] == triplets[check][0] and
		keyTriplet[2] == triplets[check][1]):
		matching.append(triplets[check])


freqMap = []

for key in range(len(matching)):
	duplicate = False

	for x in range(len(freqMap)):
			for y in range(1, len(freqMap[x])):
				if(key == freqMap[x][y]):
					duplicate = True
					duplicateIndex = x

	for check in range(len(matching)):
		if(matching[key] == matching[check] and not duplicate):
			try:
				freqMap[key][0] += 1
				freqMap[key].extend([check])
			except IndexError:
				freqMap.append([1])
				freqMap[key].extend([check])

output = ""

for word in keyTriplet:
	output += word + " "

for x in range(67):
	freqIndex = x % len(freqMap)

	if(freqMap[freqIndex] == 1):
		for word in matching[freqMap[freqIndex][1]]:
			output += word + " "

	else:
		randomDuplicate = randint(1, len(freqMap[freqIndex]) - 1)

		for word in matching[freqMap[freqIndex][randomDuplicate]]:
			output += word + " "

print "Output: "
print output

file.close()

raw_input("Press enter to exit...")
