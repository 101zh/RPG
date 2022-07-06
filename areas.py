areaDict={}
class area:
    def __init__(self,name:str, areanum:int, monsters:list, shopitems:list):
        self.name=name
        self.areanum=areanum
        self.monsters=monsters
        self.shopitems= shopitems
        areaDict[self.areanum]=self

    # Makes the monsters inside monsters:list actual characters
    def init(self,monlist:list,itemDict:dict):
        self.monsters.clear()
        for i in monlist:
            if i.area.areanum==self.areanum:
                self.monsters.append(i)
        for key, data in itemDict:
            if data.area.areanum==self.areanum:
                self.shopitems.append(data)


area("Null", 0, [],[])
area("Green Hills", 1, [],[])
area("Enchanting Forest", 2, [],[])
