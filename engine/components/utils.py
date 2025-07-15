# Import only what we need from imports module
from regex import fullmatch

# Handle parsing of commands with duo paths (i.e: src, des)
def pathTokeniserMulti(input):
    try:
        input = input.replace('\\','/')
        tokenize_input = input.split('\'');
        clean_tokens = [e.strip() for e in tokenize_input if e.strip()] # remove white spaces from tokens
        
        src = clean_tokens[1]; # source path
        des = clean_tokens[2]; # destination path

        # to identify if the drc/des is file or directory
        # .+ -> any character including spaces
        # \. for period detection
        # ^(Start) - $(End)
        pattern = r"^.+\..+$" 

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


        if not map["src_type"] and not map["des_type"]:
                print("⚠️  Error! Invalid Paths follow the correct format ( clone <src> <des> )")
                return False
        return src, des, map
    except Exception as e:
        print(f"⚠️  Error parsing paths: {e}")
        return False

# Handle parsing of commands with mono paths (i.e: src)
def pathTokenizerSingle(input):
    try:
        input = input.replace('\\','/')
        src = input.split('\'')[1] # source path

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


        if not map["src_type"]and not map["des_type"]:
                print("⚠️  Error! Invalid Paths follow the correct format ( clone <src> <des> )")
                return False
        return src, map
    
    except Exception as e:
        pass

def pathtokenizerMultiple(input):
    # seperating command from paths
    parts = input.split('\'')
    # cleaning whitespaces
    clean = [part.strip() for part in parts if part.strip() and part.strip() != '>>>']
    # pattern to understand the paths
    pattern = r"^.+\..+$"
    # Ignoring the command text
    paths = clean[1:]
    # examine the types either file or dir
    types = ["file" if fullmatch(pattern, path) else "dir" for path in paths]
    
    return paths, types