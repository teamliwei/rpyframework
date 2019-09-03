# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

init python:
    from store.util import SceneLoader, TraitManager, FlagManager, ScreenBridge

label start:
    python:

        # this clears the store cache.

        # this manages flags (applied at flags-tutorial.rpy)
        fm = FlagManager()
        fm.newgame()

        # this manages traits (applied at traits-tutorial.rpy)
        tm = TraitManager()
        tm.newgame()

        # this manages scenes (applied at scenes-tutorial.rpy)
        sl = SceneLoader()
        sl.newgame()

        sb = ScreenBridge()
        pvars = {}

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    jump flags_tutorial
    

    return
