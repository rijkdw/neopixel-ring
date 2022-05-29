def chunks_gen(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def chunks(lst, n):
    return list(chunks_gen(lst, n))

def rjust(string, char=' ', width=0):
    while len(string) < width:
        string = char + string
    return string