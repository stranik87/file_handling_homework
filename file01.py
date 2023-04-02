def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data).read()
    a = []
    for item in f.split(","):
        a.append(int(item))
    return a

print(main("txt_file/data01.txt"))

# Read data from file