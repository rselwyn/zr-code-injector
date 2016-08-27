from subprocess import call
import sys

file_to_compile = sys.argv[1]
injectable = "injected.cpp"
COMPILED_NAME = "COMPILED-" + file_to_compile

with open(COMPILED_NAME, "w") as to_compile:

	with open(injectable, "r") as inject:
		for line in inject:
			to_compile.write(line)

	with open(file_to_compile, "r") as in_file:
		for line in in_file:
			to_compile.write(line)

call(["clang", COMPILED_NAME])