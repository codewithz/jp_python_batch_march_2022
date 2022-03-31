from pathlib import  Path
from time import  ctime
import  shutil

path=Path("myfile.txt")
print("Stats",path.stat())
print("Creation Time",ctime(path.stat().st_ctime))

# Read the data from a file

data_from_file=path.read_text();
print("Data from file is\n\n")
print("------------------------------------------")
print(data_from_file)
print("------------------------------------------")

path_to_write=Path("somefile.txt")
path_to_write.write_text(data_from_file)
print("Done")

source=Path("a.txt")
target=Path("b.txt")
shutil.copy(source,target)