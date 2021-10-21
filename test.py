import subprocess
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--repo", help="repo")
args = parser.parse_args()
rep = args.repo
args = ("scorecard", "--repo=%s" %rep)
popen = subprocess.Popen(args, stdout=subprocess.PIPE)
popen.wait()
output = popen.stdout.read()
print(output)
