#!/bin/env python2

import sys
import argparse
from string import lowercase as lwc

args = argparse.ArgumentParser(description="Uma simples ferramenta que faz Encrypt/Decrypt e BruteForce - Coded by vida")
optional = args._action_groups.pop()
required = args.add_argument_group('required arguments')
args._action_groups.append(optional)
required.add_argument('-m', '--mode', help='Modes: Encrypt (enc) / Decrypt (dec) / BruteForce (bf)', required=True)
required.add_argument('-f', '--file', help='Passa o arquivo', required=True)
args.add_argument('-k', '--key', type=int, help='Passar a Key somente em enc/dec', required=False)
args.add_argument('-o', '--outfile', help='Output file', required=False)

myargs = args.parse_args()

#-----------------------#
# Variaveis
#-----------------------#
key = myargs.key
mode = myargs.mode
output = lambda data : open(myargs.outfile, 'w').write(str(data))
file =  open(myargs.file, 'r').read().lower()

def encdec(key):
	result = ''
	for line in file:
		if line in lwc:
			indx = lwc.find(line)
			if mode == "enc":
				indx = (indx + key) %26 # Aritmetica Modular
			elif mode == "dec":
				indx = (indx - key) %26
			result += lwc[indx]
		else:
			result += line
	if myargs.outfile:
		output(result,)
	print "[+] Output: "+result,

def brute():
	for key in range(1,26):
		result = ''
		print "[+] Key:",key
		for line in file:
			if line in lwc:
				indx = lwc.find(line)
				indx = (indx - key) %26
				result += lwc[indx]
			else:
				result += line
		print result

if __name__ == "__main__":
	if mode == "enc" or mode == "dec":
		encdec(key)
	elif mode == "bf":
		brute()
	else:
		print "Modo Invalido"
		exit(1)
