import argparse
from processor import convert
from pathlib import Path



def main():
    cwd = Path.cwd()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("file") #source file
    args = parser.parse_args()

    args.file

    convert(cwd, args.file)

if __name__ == "__main__":
    main()