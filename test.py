import subprocess
args = ("scorecard", "--repo=github.com/ossf-tests/scorecard-check-branch-protection-e2e")
popen = subprocess.Popen(args, stdout=subprocess.PIPE)
popen.wait()
output = popen.stdout.read()
print(output)
