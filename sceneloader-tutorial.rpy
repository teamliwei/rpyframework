# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

label sceneloader_tutorial:
    
    # the sb class is already declared at the start label

    e "Scene loader provides an easy way to define your scenes and call them."

    # -----------------------------------------------
    
    e "First let's check what scenes we've loaded."

    # by default, the items defined in defs/scenelist.json are used.

    python:
        sceneitems = sl.getindex()
        scenelist = ",".join(sceneitems)

    e "Here are the scenes we've stored: [scenelist]"

    e "Remember, these are just label references, and you have to define the scenes in their own files to get them working."

    # -----------------------------------------------

    e "Let's test intro. The text coming after this are from 'intro'."

    $ sl.getscene('intro')

    e "If you can see this, then this means the intro scene has ended."

    return