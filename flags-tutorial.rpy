# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

init python:
    from store.util import SceneLoader, TraitManager, FlagManager

label flags_tutorial:
 
    # These display lines of dialogue.

    e "FLAGS Tutorial"

    # -----------------------------------------------
    e "This adds a new flag (newflag-yey)."

    $ fm.addflag('newflag-yey')
    # -----------------------------------------------

    e "This checks if the flag 'newflag-yey' exists."

    python:
        thereisaflag = fm.hasflag('newflag-yey')

    if thereisaflag:
        e "there's a flag with name 'newflag-yey'"
    else:
        e "there is no flag."
    # This ends the game.
    # -----------------------------------------------

    e "This removes the flag in the variable."

    $ fm.removeflag('newflag-yey')
    # -----------------------------------------------

    e "This checks again if the flag 'newflag-yey' exists."

    python:
        thereisaflag = fm.hasflag('newflag-yey')

    if thereisaflag:
        e "there's a flag with name 'newflag-yey'"
    else:
        e "there is no flag."
    # -----------------------------------------------

    e "this adds multiple flags 'hey' and 'yey'."

    $ fm.addflag(['hey','yey'])
    # -----------------------------------------------

    e "this gets all the flags."

    python:
        flags = fm.get()
        allflags = ",".join(flags)

    e "[allflags]"
    # -----------------------------------------------

    e "this removes multiple flags"

    $ fm.removeflag(['hey','yey'])

    e "this changes 'newflag-yey'(if it exists) to 'newflag-nay'"

    $ fm.changeflag('newflag-yey','newflag-nay')
    # -----------------------------------------------

    e "this changes 'newflag-nay'(if it exists) back to 'newflag-yey'"

    $ fm.changeflag('newflag-nay','newflag-yey')
    # -----------------------------------------------

    e "this shows again all the remaining flags."

    python:
        flags = fm.get()
        allflags = ",".join(flags)

    e "[allflags]"

    jump traits_tutorial
