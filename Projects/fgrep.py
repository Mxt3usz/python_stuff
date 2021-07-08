def fgrep( subject: str, filename: str, ignorecase : bool = False):
    with open(filename) as f:
        for line in f:
            test_line = line if not ignorecase else line.lower()
            test_subject = subject if not ignorecase else subject.lower()
            if test_subject in test_line:
                print(line)

def fgrep2( subject: str, infile: str, outfile: str):
    with open(infile) as f, open(outfile, 'w') as fout:
        for line in f:
            if subject in line.lower():
                print(line, file=fout)


def check_fgrep():
    fgrep("joke", "text/killing_joke_sketch.txt")

def check_fgrep2():
    fgrep2("joke", "text/killing_joke_sketch.txt", "text/fgrep.out")

