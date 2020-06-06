from sys import argv
from os.path import exists

script, from_file, to_file = argv

printf("Copying from %s to %s", from_file, to_file)

# we could do these on one line too

in_file = open(from_file)
indata = in_file.read()

print("The output file exist? %r", exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
