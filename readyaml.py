#!/usr/bin/env python

import yaml

FileName="/root/tets.yml"



def readyaml():
  	data= file('FileName','r')
  	dict= yaml.load(data)
  	print dict["IP"]

def main():
	readyaml()


if __name__ == '__main__':
	main()