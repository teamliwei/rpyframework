init offset = -410

init python in util:
    import json

    class ScreenBridge():
        
        __screens = []
        
        __data = {}
        __options = {}
        __actions = {}

        def newgame(self):
            self.__screens = {}
            self.__data = {}
            self.__actions = {}
            self.__options = {}


        def newscreen(self, screen_name):
            self.__screens.append(screen_name)

        # attaches the data to the screen
        def adddata(self, screen_name, data_key, data_value):
            if not screen_name in self.__screens:
                raise ValueError('No screen %s found' % name)

            screendatakey = "%s_%s" % (screen_name, data_key)
            
            self.__data[screendatakey] = data_value

        def discarddata(self, screen_name, data_key):
            if not screen_name in self.__screens:
                raise ValueError('No screen %s found' % name)

            screendatakey = "%s_%s" % (screen_name, data_key)
            
            if screendatakey in self.__data:
                del self.__data[screendatakey]

        def addaction(self, screen_name, action_name, jump_label):
            if not screen_name in self.__screens:
                raise ValueError('No screen %s found' % name)

            screenactionkey = "%s_%s" % (screen_name, action_name)
            if not screen_name in self.__options:
                self.__options[screen_name] = []

            if not action_name in self.__options[screen_name]:
                self.__options[screen_name].append(action_name)
            self.__actions[screenactionkey] = {'text': action_name, 'action': jump_label}

        def addactionset(self, screen_name, actionset):
            if not screen_name in self.__screens:
                raise ValueError('No screen %s found' % name)

            if not type(actionset) is dict:
                raise ValueError('Action set must be a dict with name & action parameters')

            else:
                for item in actionset:
                    if not 'name' in actionset[item] or not 'action' in actionset[item]:
                        raise ValueError('Each action set item must contain name & action properties.')
                    action_name = actionset[item]['name']
                    action_return = actionset[item]['action']
                    self.addaction(screen_name, action_name, action_return)

        def getoptions(self, screen_name):
            if screen_name in self.__options:
                return self.__options[screen_name]
            return None


        def getdata(self, screen_name, datakey):
            screendatakey = "%s_%s" % (screen_name, datakey)
            if screendatakey in self.__data:
                return self.__data[screendatakey]
            return None


        # example showscreen function. this prepares the data to be passed to the screen

        def bridge(self, screen_name):
            screentitle = self.getdata(screen_name, 'title')
            screentext = self.getdata(screen_name, 'text')
            screenoptions = self.getoptions(screen_name)
            screenactions = []
            print('get actions keys')
            for option in screenoptions:
                screenactionkey = "%s_%s" % (screen_name, option)
                if screenactionkey in self.__actions:
                    actionitem = self.__actions[screenactionkey]
                    print(actionitem)
                    screenactions.append(actionitem)
                else:
                    self.__options.remove(option)

            prepdata = {
                'title': screentitle,
                'text': screentext,
                'options': screenactions
                }

            return prepdata