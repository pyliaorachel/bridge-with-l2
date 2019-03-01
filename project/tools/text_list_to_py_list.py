import sys


with open(sys.argv[1], 'r') as fin:
    names = []
    for line in fin:
        names += [line.strip().lower()]
    names = [name.replace("'", "\\'") for name in names]
    output = ["'" + name + "'" for name in names]
    with open(sys.argv[2], 'w') as fout:
        for i in range(0, len(output), 10):
            names = output[i:i+10]
            fout.write(', '.join(names))
            fout.write('\n')