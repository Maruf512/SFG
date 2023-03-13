from pygcode import Line
from pathlib import Path
import os


def to_text(data, temp_file):
    try:
        with open(temp_file, 'a') as f:
            f.write(f"{data}\n")
            f.close()

    except FileNotFoundError:
        with open(temp_file, 'w') as f:
            f.write(f"{data}")
            f.close()


def Convert(Gcode_file_loc):
    tempFile = f"{os.getcwd()}/Temp/tempGcode.txt"
    # check file existence
    checkTempFile = Path(tempFile)
    if checkTempFile.is_file():
        with open(checkTempFile, 'w') as f:
            f.write(f"{checkTempFile}")
            f.close()

    with open(Gcode_file_loc, 'r') as fh:
        for line_text in fh.readlines():
            line = Line(line_text)
            gcode = line.text.strip()

            if gcode:
                # print(gcode)
                to_text(gcode, tempFile)


def GcodeConverter(loc):
    Convert(loc)
