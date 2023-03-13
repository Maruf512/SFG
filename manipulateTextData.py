# ======================================================================
# ============================ prepare Gcode ===========================
# ======================================================================
import os
import pathlib

# Variables
all_data = []
combined_axis = []


def check_file(file_name):
    file_loc = f"{os.getcwd()}/Temp/{file_name}"
    # clear data from Final_Data.txt
    FinalFileLoc = pathlib.Path(file_loc)
    if FinalFileLoc:
        with open(file_loc, 'w') as ck:
            ck.close()


def writeFinalData(singleLine):
    File_loc = f"{os.getcwd()}/Temp/axis_temp.txt"
    with open(File_loc, 'a') as fd:
        fd.write(f"{singleLine}\n")
        all_data.append(singleLine)
        fd.close()


def writeCombinedData(line):
    File_loc = f"{os.getcwd()}/Temp/combined_data.txt"
    with open(File_loc, 'a') as fd:
        fd.write(f"{line}\n")
        fd.close()


def TrashRemover():
    tempGcodeFile = f"{os.getcwd()}/Temp/tempGcode.txt"     # file loc

    check_file("Final_Data.txt")                  # check file existence

    with open(tempGcodeFile, 'r') as tempFile:              # read the temp file
        for line in tempFile.readlines():                   # read every line

            tData = line.strip()

            # filter all the G/command data
            if "G1" in tData:
                tData = tData.replace("G1 ", "")
                if "Z" not in tData:
                    if "F2540" not in tData:
                        if "-" in tData:
                            tData = tData.replace("-", "")
                            tData = tData.replace("X", "")
                            tData = tData.replace("Y", "")
                            sData = tData.split(" ")

                            writeFinalData(sData)

        tempFile.close()


def process_combine():
    current_index = 0
    target_index = 1

    checkData = ""

    check_file("combined_data.txt")

    while current_index < len(all_data):

        try:
            if "F1016" in all_data[target_index]:
                current_x = float(all_data[target_index][0])
                current_y = float(all_data[target_index][1])

                target_x = float(all_data[target_index + 1][0])
                target_y = float(all_data[target_index + 1][1])

            else:
                current_x = float(all_data[current_index][0])
                current_y = float(all_data[current_index][1])

                target_x = float(all_data[target_index][0])
                target_y = float(all_data[target_index][1])

            # print(f"current: {current_index} || {all_data[current_index]}")           # for debugging
            # print(f"target: {target_index} || {all_data[target_index]}")              # for debugging

            main_data = f"{float(current_x)}, {float(current_y)}, {float(target_x)}, {float(target_y)}"

            if checkData != main_data:
                checkData = main_data
                writeCombinedData(main_data)
                combined_axis.append(main_data)

            else:
                pass

            target_index += 1
            current_index += 1

        except IndexError:
            break


def Filter():
    TrashRemover()
    process_combine()
