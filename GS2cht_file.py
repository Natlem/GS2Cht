import os
import argparse
import enum
from pathlib import Path
NEW_LINE = '\n'

class ACheat(object):
    def __init__(self, name):
        self.name = name
        self.lines = []
        self.num_cheats = 0
    def add_line(self, line):
        self.lines.append(line)
        self.num_cheats += 1


    def to_1_cht(self, starting_cheat_num):
        i = 0
        codes = []
        for line in self.lines:
            if len(self.lines) > 1:
                codes.append('cheat{}_desc = "{} ({}/{})"'.format(starting_cheat_num + i, self.name, i + 1, len(self.lines)))
            else:
                codes.append(
                    'cheat{}_desc = "{}"'.format(starting_cheat_num + i, self.name, i))
            codes.append('cheat{}_code = "{}"'.format(starting_cheat_num + i, line.replace(" ", "+", 1)))
            codes.append('cheat{}_enable = {}'.format(starting_cheat_num + i, "false"))
            i += 1

        return codes, starting_cheat_num + i

class LineType(enum.IntEnum):
    BLANK = 0
    CHEAT = 1
    CODE = 2

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="input", type=str, nargs='*', required=True)
    parser.add_argument("-o", dest="output", type=str, required=True)
    args = parser.parse_args()
    return args


def check_line_type(line):

    if not line:
        return LineType.BLANK
    elif line[0] == '[' and line[-1] == ']':
        return LineType.CHEAT
    else:
        return LineType.CODE

def main():
    args = parse_args()

    #Append files into one single string
    all_cheats = []
    new_cheat = None
    for fn in args.input:
        with open(Path(fn),'r') as f:
            for line in f:
                line = line.rstrip()
                l_type = check_line_type(line)
                if l_type == LineType.BLANK:
                    continue
                elif l_type == LineType.CHEAT:
                    if new_cheat is not None:
                        all_cheats.append(new_cheat)
                    new_cheat = ACheat(line[1:-1])
                else:
                    new_cheat.add_line(line)


    with open(Path(args.output), 'w') as f:
        num_cheats = 0
        start_num = 0

        for cheat in all_cheats:
            num_cheats += cheat.num_cheats

        f.write("cheats = {}".format(num_cheats) + NEW_LINE)
        f.write(NEW_LINE)
        for cheat in all_cheats:
            cht_codes, start_num = cheat.to_1_cht(start_num)
            print(cht_codes)
            for l_cht in cht_codes:
                f.write(l_cht + NEW_LINE)
                num_cheats += 1
            f.write(NEW_LINE)



if __name__ == "__main__":
    main()