from pathlib import Path

path=Path('../ecommrce')
test_path=Path("../test")
# path.exists()
# path.mkdir()
# path.rmdir()
# test_path.rename("zartab")

print(path.iterdir())

for p in path.iterdir():
    print(p)

files=[p for p in path.iterdir()]
print(files)

directories=[p for p in path.iterdir() if p.is_dir()]
print("Dir",directories)