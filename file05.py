def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    x = []
    countNum = 0
    countStr = 0
    f = open(data).read()
    for item in f:
        if item.isdigit():
            countNum += 1
            
        else:
            countStr += 1
    

    x.append(countNum)
    x.append(countStr)
    # print(countNum,countStr,x)
    
    print(x)
    return x
    
# Read data from file
main("txt_file/data05.txt")