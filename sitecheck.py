#!/usr/bin/env python3

import argparse
import requests

def noblank(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("urlfile", help="The file containing urls")
    args = parser.parse_args()
    urlist = args.urlfile

    with open(urlist) as f:
        for line in noblank(f):
            try:
                req = requests.get(line)
                resp = req.status_code
                if resp == 200:
                    print(line, " >> OK")
                else:
                    print(line, " >> Error occured")
            except requests.exceptions.MissingSchema:
                print(line, " >> The url format is incorrect or the page does not exist")

if __name__ == '__main__':
    main()              
