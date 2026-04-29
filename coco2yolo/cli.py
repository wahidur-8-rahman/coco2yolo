import argparse
from .processor import convert
from pathlib import Path



def main():
    cwd = Path.cwd()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("file") #source file
    parser.add_argument("--dir") #output dir name
    args = parser.parse_args()

    args.file

    convert(cwd, args.file, args.dir)

if __name__ == "__main__":
    main()