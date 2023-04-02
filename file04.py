def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data).read()
    print(f)
    x = []
    for item in f:
        if item.isalpha():
            x.append(item)
    return x
    
print(main("txt_file/data04.txt"))
    
# Read data from file