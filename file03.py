def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data).read()
    print(f)
    a = []
    for i in f:
        if i.isdigit():
            a.append(int(i))
    
        
# Read data from file
    return a
print(main("txt_file/data03.txt"))