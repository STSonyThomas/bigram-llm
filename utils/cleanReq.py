import argparse
import sys
import os
parser = argparse.ArgumentParser(description="Program for cleaning up requirments.txt files")

parser.add_argument(
    "-sf","--source_folder",
    type=str,
    help="Input file to process"
)

args = parser.parse_args()

sourceFolder = args.source_folder
if not os.path.exists(sourceFolder):
    raise ValueError("Folder doesn't exist")

with open(sourceFolder,'r') as f:
    content = f.readlines()

newRequirements = []
for req in content:
    reqList = req.split("==")
    newRequirements.append(f"{reqList[0]}\n")

with open(sourceFolder,'w') as f:
    f.writelines(newRequirements)
print(newRequirements)
