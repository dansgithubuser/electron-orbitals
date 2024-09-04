#!/usr/bin/env python3

#===== imports =====#
import argparse
from pathlib import Path
import sys

#===== args =====#
parser = argparse.ArgumentParser()
parser.add_argument('example_path')
args = parser.parse_args()

#===== consts =====#
REPO_ROOT = Path(__file__).resolve().parent

#===== setup =====#
sys.path.append(REPO_ROOT.as_posix())

#===== main =====#
with open(args.example_path) as example_file:
    example = example_file.read()
exec(example)
