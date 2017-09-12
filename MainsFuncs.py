class MainsFuncs():
    def GroupUpdate(self,group,updateparaments):
        for object in group:
            object.update(*updateparaments)
