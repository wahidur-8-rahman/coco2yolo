import argparse
from .processor import convert
from pathlib import Path



def main():
    cwd = Path.cwd()
    
    parser = argparse.ArgumentParser()
    parser.add_argument("file") #source file
    parser.add_argument("--dir", default="annotations") #output dir name
    parser.add_argument("--map", default=None) #file name, must be in PWD

    # parser.add_argument(
    #     "--test_map",
    #     action="store_true",
    #     help="Run test for mapper function before processing"
    # )

    args = parser.parse_args()


    convert(cwd, args.file, args.dir, args.map)

if __name__ == "__main__":
    main()