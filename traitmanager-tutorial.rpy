# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

label traits_tutorial:
    
    # the tm class is already declared at the start label

    e "Traits Tutorial"

    # -----------------------------------------------
    e "This adds a new trait called hp to your character 'player'."

    $ tm.addtrait('player', 'hp')
    # -----------------------------------------------

    e "This gets the value of your trait's xp"

    $ healthxp = tm.traitexp('player', 'hp')
    e "Your current health exp is [healthxp]."

    # -----------------------------------------------

    e "This gets the level of your trait."

    $ healthlvl = tm.traitlevel('player', 'hp')
    e "Your current health level is [healthlvl]"

    # -----------------------------------------------

    e "This gets the level caps of your trait."
    e "By default 100pts is the level cap"

    $ healthcap = tm.traitcaps('player', 'hp')
    e "You need [healthcap] exp to achieve your next level"

    # -----------------------------------------------

    python:
        oldhplvl = tm.traitlevel('player', 'hp')
        oldhpexp = tm.traitexp('player', 'hp')
        oldhpcaps = tm.traitcaps('player', 'hp')

    e "Choose how to increase your exp"
    $ exptogain = 0
    menu:
        "Add 125 xp (+1 levels)":
            $ exptogain = 125

        "Add 255 xp (+2 levels)":
            $ exptogain = 255

        "Add 385 xp (+3 levels)":
            $ exptogain = 385

    python:
        tm.gainexp('player', 'hp', exptogain)
        hplvl = tm.traitlevel('player', 'hp')
        hpexp = tm.traitexp('player', 'hp')
        hpcaps = tm.traitcaps('player', 'hp')

    e "your new hp stats: lvl([oldhplvl]):->new:[hplvl], exp([oldhpexp]):->new[hpexp], next([oldhpcaps]):->[hpcaps]"
    # -----------------------------------------------
    
    e "To customize your level caps, you can either assign it by adding a multiplier parameter in gainexp"

    e "We will assign a multiplier of 2 whenever the character levels up."
    e "That means that a 300 exp can do a level up at cap 100, and another level up at cap 200."
    e "The new cap for the final level would then be at 400."

    python:
        # this will multiply the levelcap by 2 every levelup
        # this means that only two levels will be gain if your trait gains 300 exp
        tm.gainexp('player', 'hp', 300, 2)
        newhplvl = tm.traitlevel('player', 'hp')
        newhpexp = tm.traitexp('player', 'hp')
        newhpcaps = tm.traitcaps('player', 'hp')

    e "your new hp stats: lvl [oldhplvl]->[hplvl]->[newhplvl], exp [oldhpexp]->[hpexp]->[newhpexp], next[oldhpcaps]->[hpcaps]->[newhpcaps]"

    # -----------------------------------------------
    
    e "to manually set your level, exp, and caps"

    python:
        # charname, attribute, value
        tm.setexp('player', 'hp', 100)
        tm.setcaps('player', 'hp', 100)    
        tm.setlevel('player', 'hp', 100)

        # get the stored value
        newhplvl = tm.traitlevel('player', 'hp')
        newhpexp = tm.traitexp('player', 'hp')
        newhpcaps = tm.traitcaps('player', 'hp')

    e "your new hp stats: lvl: [newhplvl], exp: [newhpexp], caps: [newhpcaps]"

    # -----------------------------------------------
    
    e "to remove a trait"

    $ tm.removetrait('player', 'hp')

    jump screenbridge_tutorial

    return
