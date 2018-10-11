import numpy as np
import argparse 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c",action='store_true',help="take word input in command line ")
    args = parser.parse_args()

    words=[]
    if args.c:
        print('Enter space separated words')
        words = input().split()

        print(words)
    else:
        print("dummy program")
    pass

if __name__=="__main__":
    main()