# GS2Cht
Convert GameShark code to cht for PCSX ReARMed of libretro
# Why ?
I wanted to cheat on some games, i.e Lunar 2, on PS1 of Retroarch but there were no cheats...
So, I made this scripts to convert text like cheats to a .cht format

# Requirements
* python 3

# How does this works
You make/take/download a game shark text file like the one provided in this repo (SLUS_010.71.txt).
Then you can the script like:
```
python -i SLUS_010.71.txt -o output_file.cht
```
It's also possible to run with multiples input files:
```
python -i input_file1.txt input_files.txt -o output_file.cht
```
