from subprocess import call
import sys

file_to_compile = sys.argv[1]
injectable = "injected.cpp"
COMPILED_NAME = "COMPILED-" + file_to_compile

MAIN_FUNCTION = """

int main() {
  return 0;
}

"""


with open(COMPILED_NAME, "w") as to_compile:

	# Write all the injected code
	with open(injectable, "r") as inject:
		for line in inject:
			to_compile.write(line)

	# Write all the regular code
	with open(file_to_compile, "r") as in_file:
		for line in in_file:
			to_compile.write(line)

	for i in MAIN_FUNCTION.split('\n'):
		to_compile.write(i + '\n')

call(["g++", COMPILED_NAME, , '-std=c++98', '-ferror-limit=100'])