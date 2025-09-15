from pathlib import Path
p = Path('/')
for subdir in p.iterdir():
    if subdir.is_dir():
        print(subdir)


from pathlib import Path
p = Path('/')
files = p.rglob('*.py')
for f in files:
    print(f)