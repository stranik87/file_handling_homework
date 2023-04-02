def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a = []
    f = open(data).read()
    for i in f.split():
        
        a.append(len(i) )
    
    print(a)
    
# Read data from file
main("txt_file/data06.txt")