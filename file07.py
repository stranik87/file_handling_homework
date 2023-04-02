def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a = []
    x = 0
    f = open(data).read()
    for i in f:
        if i.isdigit():
            a.append(int(i))
    for item in a:
        x += item
    print(a,x)
    
# Read data from file
main("txt_file/data07.txt")