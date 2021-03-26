def readFile(filePath_in):
    with open(filePath_in, 'r') as file:
        text = file.read()
    text = text.split(".")
    
    return text