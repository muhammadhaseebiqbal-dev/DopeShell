from regex import fullmatch

def pathTokeniser(input):
    input = input.replace('\\','/')
    tokenize_input = input.split('\'');
    clean_tokens = [e.strip() for e in tokenize_input if e.strip()] # remove white spaces from tokens
    
    src = clean_tokens[1]; # source path
    des = clean_tokens[2]; # destination path

    # to identify if the drc/des is file or directory
    # \w+ -> [a-z][A-Z][0-9]
    # \. for period detection
    # ^(Start) - $(End)
    pattern = r"^\w+\.\w+$" 

    # Hold map of the src and des
    # i.e; dir -> dir
    # i.e; file -> dir
    # i.e; file -> file
    map = {}
    if len(src.split("/")) > 1 :
        if fullmatch(pattern, src.split("/")[-1]):
            map["src_type"] = "file";
        else:
            map["src_type"] = "dir"          
    else:
        if fullmatch(pattern, src.split("\\")[-1]):
            map["src_type"] = "file";
        else:
            map["src_type"] = "dir"

    if len(des.split("/")) > 1 :
        if fullmatch(pattern, des.split("/")[-1]):
            map["des_type"] = "file";
        else:
            map["des_type"] = "dir"          
    else:
        if fullmatch(pattern, des.split("\\")[-1]):
            map["des_type"] = "file";
        else:
            map["des_type"] = "dir"


    if not map["src_type"]and not map["des_type"] or map["src_type"] == "dir" and map["des_type"] == "dir":
            print("⚠️  Error! Invalid Paths follow the correct format ( clone <src> <des> )")
            return False

    return src, des, map

