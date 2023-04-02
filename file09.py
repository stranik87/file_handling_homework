def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a = []
    f = open(data).read()
    for i in f:
        if i.isdigit():
            a.append(int(i))
    b = min(a)
    print(b)
# Read data from file
main("txt_file/data09.txt")