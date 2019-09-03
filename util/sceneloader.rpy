init offset = -410

init python in util:
    import json
    class SceneLoader():
        __index = {}
        __scenejson = "defs/scenelist.json"

        def newgame(self):
            self.__index = {}
            self.loadscenes()

        def loadscenes(self):
            scenesfile = renpy.file(self.__scenejson)
            sceneslist = json.load(scenesfile)
            self.__index = sceneslist
            scenesfile.close()

        def getindex(self):
            return self.__index

        def getscene(self, name):
            if not name in self.__index:
                raise ValueError('Scene [%s] not found.' % name)
            scenedata = self.__index[name]

            # this calls the 'screen scene_cover' for transition in scenetransition.rpy
            renpy.show_screen('scene_cover', scenedata)
            renpy.pause(10)
            renpy.hide_screen('scene_cover')

            # this calls the scene assigned to 'goto' in the scenelist.json
            scenelabel = scenedata['goto']
            renpy.call(scenelabel)

            # there must be an atl (non-python script) intermediary such as a dialogue or a scene in between getscene() invocations.
            # this is because the renpy interpreter expects atl language and will result in an error if there are multiple blocks of pure python.
            return