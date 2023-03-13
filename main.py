import GcodeToText
import manipulateTextData

print("""
============================================================================================
=========================== Welcome to Gcode Reader/writer =================================
============================================================================================""")

# Variables
gcode_file_loc = "D:\Pton\plotter\Gcode/gojo_1.gcode"

GcodeToText.GcodeConverter(gcode_file_loc)          # convert gcode to text
print("Done Stage 1/2")
manipulateTextData.Filter()
print("Done Stage 2/2")
print("Done")
print("Launch The Gcode writer!!")
