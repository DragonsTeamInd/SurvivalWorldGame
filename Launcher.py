class Launcher():
    def __init__(self):
        self.bck = ''
        self.buttonimage = ''
        self.sock = socket.socket()
        self.opengame = None
    def VersionCheck(self,host,port):
        self.sock.connect(host,port):
        bsv = self.sock.recv(12333)
        sv = bsv.decode('utf-8')
        mvm = GetData()
        mv = mvm[0]
        if mv != sv:
            self.opengame = False
        else:
            self.opengame = True
        self.sock.close()
    def command(self,root):
        if cangame == True:
            root.destroy()
    def main(self,host,port,bck,command,bi,cangame):
        VersionCheck(self,host,port)
        createTKinterWindow(bck,command,bi,cangame)
