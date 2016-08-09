#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports
open('words.txt')


# Body
def reads():
	fin = open('words.txt')
	words = []
	twenty_char_words = []
	for line in fin:
		words.append(line.strip())
	counter = int(len(words)) - 1
	while counter >= 0:
		if len(words[counter]) >= 20:
			twenty_char_words.append(words[counter])
		counter -= 1  
	print(twenty_char_words)
	return
##############################################################################
def main():
	reads()

if __name__ == '__main__':
    main()
