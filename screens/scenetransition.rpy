init offset = -10

transform schaptext:
    alpha 0
    linear 2 alpha 1
    pause 1
    linear 2 alpha 0

# scdata is the variable passed in sceneloader.rpy
screen scene_cover(scdata):
    python:
        title = scdata['title']
        desc = scdata['desc']

    add "gui/overlay/confirm.png"

    frame at schaptext:
        xalign 0.5
        yalign 0.5
        yoffset -50
        vbox:
            text _("%s" % title):
                size 48
                xfill False

            text _("%s" % desc):
                size 24
                xfill False

