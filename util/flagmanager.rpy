init offset = -410

init python in util:
    import json

    class FlagManager():
        __index = []

        def newgame(self):
            self.__index = []

        def get(self):
            return self.__index

        def addflag(self, flagname, silent=True):
            if type(flagname) is list:
                for flag in flagname:
                    self.add(flag, silent)
            else:
                self.add(flagname, silent)

        def add(self, flag, silent):
            if not flag in self.__index:
                self.__index.append(flag)
            elif not silent:
                raise ValueError("flag already exists")

        def remove(self, flag, silent):
            if flag in self.__index:
                self.__index.remove(flag)
            elif not silent:
                raise ValueError("flag already removed")

        def hasflag(self, flagname):
            print(type(flagname))
            if type(flagname) is list:
                allvalid = True
                for flag in flagname:
                    if not flag in self.__index:
                        allvalid = False
                return allvalid

            else:
                if flagname in self.__index:
                    return True
                return False

            return False

        def removeflag(self, flagname, silent=True):
            if type(flagname) is list:
                for flag in flagname:
                    self.remove(flag, silent)
            else:
                self.remove(flagname, silent)

        def changeflag(self, flagname, newflag):
            if self.hasflag(flagname):
                self.removeflag(flagname)
                
            self.addflag(newflag)
