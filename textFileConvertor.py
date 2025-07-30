"""
Author: Musa Kaleem
Purpose: Code copies and converts all files into text files from one specified directory to another. 
"""

import os
from os.path import isfile, join
import shutil

print("\n" +
                    "  _______        _     ______ _ _         _____                          _             \n" +
                    " |__   __|      | |   |  ____(_) |       / ____|                        | |            \n" +
                    "    | | _____  _| |_  | |__   _| | ___  | |     ___  _ ____   _____ _ __| |_ ___  _ __ \n" +
                    "    | |/ _ \\ \\/ / __| |  __| | | |/ _ \\ | |    / _ \\| '_ \\ \\ / / _ \\ '__| __/ _ \\| '__|\n" +
                    "    | |  __/>  <| |_  | |    | | |  __/ | |___| (_) | | | \\ V /  __/ |  | || (_) | |   \n" +
                    "    |_|\\___/_/\\_\\\\__| |_|    |_|_|\\___|  \\_____\\___/|_| |_|\\_/ \\___|_|   \\__\\___/|_|   \n")


copyDir = input("Enter path to copy files from > ")

pasteDir = input("Enter path to paste the files to > ")



try:
    print("Loading Files...")
    filesFound = [file for file in os.listdir(copyDir) if isfile(join(copyDir, file))]
    
    print("Coping files...")
    for file in filesFound:
        shutil.copy2(join(copyDir,file), pasteDir)
    
    print("Adding txt extension...")
    for file in filesFound:
        os.rename(join(pasteDir,file), join(pasteDir, file + '.txt'))
    
    print("\n" +
                    "                ___    ____   ____                               \n" +
                    "  __________   /   |  / / /  / __ \\____  ____  ___     __________\n" +
                    " /____/____/  / /| | / / /  / / / / __ \\/ __ \\/ _ \\   /____/____/\n" +
                    "/____/____/  / ___ |/ / /  / /_/ / /_/ / / / /  __/  /____/____/ \n" +
                    "            /_/  |_/_/_/  /_____/\\____/_/ /_/\\___/               ")

except Exception:
    print("\n!==== ERROR: ooooooooof! some thing went wrong ====!")


input(">>> press Enter to close & EXIT the program <<<")
