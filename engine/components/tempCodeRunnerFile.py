from .imports import fullmatch
test = "readout 'test1.txt' 'test 2.txt' 'test3.txt'"
def pathtokenizerMultiple(input):
    parts = input.split('\'')
    clean = [part.strip() for part in parts if part.strip()]

    pattern = r"^\w+\.\w+$"

    paths = clean[1:]
    types = ["file" if fullmatch(pattern, path) else "dir" for path in paths]
    print(paths)
    print(types)
    
pathtokenizerMultiple(test)