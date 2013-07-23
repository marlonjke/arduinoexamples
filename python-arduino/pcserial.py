#! /usr/bin/env python
#-*- encoding:utf-8 -*-

import serial

# O nome da porta peguei no Serial Port do compilador do arduino. No Windows provavelmente é COM alguma coisa...
port = '/dev/ttyACM0' 
baud_rate = 9600

loop = True
com = serial.Serial(port, baud_rate)

while(loop):
  value = raw_input("Digite 1 para ligar o led.\nDigite 2 para desligar o led.\n"\
			  "Digite 3 para led itermitente.\nDigite 6 para sair.\n:")
	if value:
        # Au revoir... hehehe
		if value == '6':
			loop = False
		else:
            com.write(value)
			answer = com.readline()
			print "Arduino respondeu:", answer

print "Adeus!!"
com.close()
