class Records:

    def __init__(self):
        self.__name = ""
        self.__packname = ""
        self.__paxnum = 0
        self.__packcost = 0

    #Setter Methods
    def set_name(self, name):
        self.__name = name
    #Package names (Romance Package, The Girls Getaway Package, The Rest & Relaxation Package, Staycation Package)
    #Taken from https://www.socialtables.com/blog/hotel-sales/creative-hotel-packages/
    def set_packname(self, packname):
        self.__packname = packname
    def set_paxnum(self, paxnum):
        self.__paxnum = paxnum
    #Package Costs (Romance Package:300, The Girls Getaway Package:500, The Rest & Relaxation Package:325, Staycation Package:250)
    def set_packcost(self, packcost):
        self.__packcost = packcost

    #Getter Methods
    def get_name(self):
        return self.__name
    def get_packname(self):
        return self.__packname
    def get_paxnum(self):
        return self.__paxnum
    def get_packcost(self):
        return self.__packcost