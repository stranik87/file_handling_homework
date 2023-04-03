def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a = []
    f = open(data).read()
    for i in f.split("\n"):  
        a.append(len(i))
        b = max(a)

    
    print(b)
# Read data from file

main("txt_file/data10.txt")

