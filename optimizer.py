import sys
import re

f_in = open(sys.argv[1], "r")
lines = f_in.readlines()

redone_file = []
for count, line in enumerate(lines):
	redone_file.append(re.sub("\[\d\]", "COUNT", line))

fixes = 0

for i, v in enumerate(redone_file[:len(redone_file)-2]):
	
	if "cos(" in v and "acos(" not in v:
		print "Please fix line #" + str(i+1) + ": cos() should be replaced with cosf()"
		fixes += 1

	if "acos(" in v:
		print "Please fix line #" + str(i+1) + ": acos() should be replaced with acosf()"
		fixes += 1

	if v == redone_file[i+1] and v == redone_file[i+2]:
		print "Please fix line #" + str(i+1) + "-" + str(i+3)
		fixes += 1

if fixes == 0:
	print "Nice Job.  This script couldn't find any areas to reduce your memory allocation."
else:
	print "{} Errors were pointed out.".format(fixes)