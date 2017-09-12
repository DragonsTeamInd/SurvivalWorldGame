def savedata(Parametrs,txtfilename):
    with open(txtfilename,'w') as f:
        for Parametr in Parametrs:
            f.write(str(Parametr) + '\n')
def opendata(txtfilename,Parametrs):
    with open(txtfilename,'r') as f:
        flines = f.readlines()
        flines = [line.rstrip() for line in flines]
        print(flines)
        a = 0
        for i in range(len(Parametrs)):
            try:
                Parametrs[i] = eval(flines[i])                    
            except ValueError:
                Parametrs[i] = flines[i]
        print(Parametrs)
