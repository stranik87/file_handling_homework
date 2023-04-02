def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data, "w").write("data02.txt")
    
    return f
print(main("txt_file/data02.txt"))
# Read data from file