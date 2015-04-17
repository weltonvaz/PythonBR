#!/usr/bin/env python 
# -*- coding: utf-8 -*-

def toByteArray(s, withLen):
	if (len(s) > 255):
		raise Exception('String precisa ter menos que 255 caracteres')
		buffer = bytearray()
		
	if withLen:
		buffer.append(len(s))            
	buffer.extend(s)
        return buffer

BIN_TO_ASC = [
            '+', '-', '0', '1', '2', '3', '4', '5', '6', '7', '8',
            '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

def toString(_bytes):
    buf = []
    try:
        _len = len(_bytes)
    except:
        _len = _bytes.size
        flush = False
    if (_len % 3 != 0):
        _bytes.append(0)
        flush = True
    counter = last = 0
    
    for i in range(_len):
        b = _bytes[i] & 0xFF if i < _len else 0
        if counter == 0:
            buf.append(BIN_TO_ASC[b >> 2])
            last = b
        elif counter == 1:
            buf.append(BIN_TO_ASC[((last & 0x03) << 4) | ((b & 0xF0) >> 4)])
            last = b
        elif counter == 2:
            buf.append(BIN_TO_ASC[((last & 0x0F) << 2) | ((b & 0xC0) >> 6)])
            if ( not (flush and i == _len - 1)):
                buf.append(BIN_TO_ASC[b & 0x3F])
                last = 0
            else:
                pass
            counter = (counter+1) % 3
        return ''.join(buf)

print (toString(146))