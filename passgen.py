#!/usr/bin/python3
import string
import random
import argparse

argparser = argparse.ArgumentParser(usage='./passgen -l 16')
argparser.add_argument('-l', type=int, help='length', default=16)
args = argparser.parse_args()
args = args.__dict__

length = args['l']

letters = string.ascii_letters
digits = '0123456789'
symbols = string.punctuation
symbols = '#$%&()*+<=>?@'

all_symbols = letters + digits + symbols

def gen(length):
    passwd = ''
    for i in range(0, length):
        s = random.choice(all_symbols)
        passwd += s
    print(passwd)

if __name__ == '__main__':
    gen(length)
    
