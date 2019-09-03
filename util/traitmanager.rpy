init offset = -410

init python in util:
    import json

    class TraitManager():
        __index = {}
        # experience points, reset when caps is reached
        __xp = {}
        # capacity - how many pts until next level
        __caps = {}
        # level counter
        __levels = {}

        # times_leveled_up
        __levelsup = 0

        def newgame(self):
            self.__index = {}

        def addtrait(self, actor, traitname, level=1):
            if not actor in self.__index:
                self.__index[actor] = []

            if not traitname in self.__index[actor]:
                self.__index[actor].append(traitname)

            actortraitkey = "%s_%s" % (actor, traitname)

            if not actortraitkey in self.__xp:
                self.__xp[actortraitkey] = 1

            if not actortraitkey in self.__caps:
                self.__caps[actortraitkey] = 100

            if not actortraitkey in self.__levels:
                self.__levels[actortraitkey] = 1

        def actortraitcheck(self, actor, traitname):

            if not actor in self.__index:
                raise ValueError('traits does not exist for %s' % (traitname, actor))

            if not traitname in self.__index[actor]:
                raise ValueError('traits does not exist for %s' % (traitname, actor))

        def setexp(self, actor, traitname, percent):

            self.actortraitcheck(actor, traitname)

            actortraitkey = "%s_%s" % (actor, traitname)

            self.__xp[actortraitkey] = percent

        def setlevel(self, actor, traitname, levelcount):

            self.actortraitcheck(actor, traitname)

            actortraitkey = "%s_%s" % (actor, traitname)

            self.__levels[actortraitkey] = levelcount

        def setcaps(self, actor, traitname, capacity):

            self.actortraitcheck(actor, traitname)

            actortraitkey = "%s_%s" % (actor, traitname)

            self.__caps[actortraitkey] = capacity

        def traitexp(self, actor, traitname):
            
            self.actortraitcheck(actor, traitname)

            actortraitkey = "%s_%s" % (actor, traitname)

            if actortraitkey in self.__xp:
                return self.__xp[actortraitkey]

        def traitlevel(self, actor, traitname):
            self.actortraitcheck(actor, traitname)

            actortraitkey = "%s_%s" % (actor, traitname)

            if actortraitkey in self.__levels:
                return self.__levels[actortraitkey]

        def traitcaps(self, actor, traitname):
            self.actortraitcheck(actor, traitname)

            actortraitkey = "%s_%s" % (actor, traitname)

            if actortraitkey in self.__caps:
                return self.__caps[actortraitkey]


        def gainexp(self, actor, traitname, value, nextcapmultiplier=None):

            self.actortraitcheck(actor, traitname)

            actortraitkey = "%s_%s" % (actor, traitname)

            self.__xp[actortraitkey] += value

            levelcap = self.__caps[actortraitkey]

            while self.__xp[actortraitkey] >= levelcap:
                self.__xp[actortraitkey] -= levelcap
                self.__levels[actortraitkey] += 1
                if not nextcapmultiplier is None:
                    levelcap = levelcap * nextcapmultiplier
                    self.__caps[actortraitkey] = levelcap

            if self.__xp[actortraitkey] < 0:
                self.__xp[actortraitkey] = 0
                self.__levels[actortraitkey] -= 1

            if self.__levels[actortraitkey] <= 0:
                self.traitremove(traitname)

        def removetrait(self, actor, traitname):
            self.actortraitcheck(actor, traitname)
            actortraitkey = "%s_%s" % (actor, traitname)
            self.__index[actor].remove(traitname)
            del self.__xp[actortraitkey]
            del self.__levels[actortraitkey]
            del self.__caps[actortraitkey]

