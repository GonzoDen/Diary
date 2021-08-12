def isAlone(filename):
        f = open(filename, "r")

        for line in f.readlines():
            if (line.find("lonely") != -1):
                result = True
                break
            else:
                result = False
    
        return result
