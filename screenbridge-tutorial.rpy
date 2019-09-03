# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

label screenbridge_tutorial:
    
    # the sb class is already declared at the start label

    e "Screen Bridge Tutorial (lots of coding ahead)"

    # -----------------------------------------------
    e "You will need to view the source for the comments of this tutorial..."

    # We've already made the test screen in screen/smallwindow.rpy
    # We're using the ScreenBridge class to programatically create dynamic, reusable screens

    python:
        sb.newscreen('small_window')
        # this simply indexes the screen data to keep track of it
        # if you have multiple screens of the same type you can call it small_window_1 ... etc

        sb.adddata('small_window', 'title', 'Screen Bridge Test')
        sb.adddata('small_window', 'text', 'This is merely a test window. Want to test things out?')

        windowoptions = {
            'action1': { #this is the unique key for this set of data
                'name': 'Okay. I shall do it', # this is what appears on the textbutton
                'action': 'immadoit' #this is the label that the screen returns when you click this button
                },
            'action2': {
                'name': 'Wait. I shall think about it',
                'action': 'immathinkit'
                },
            'action3': {
                'name': 'No. I shall sit on it',
                'action': 'immasitonit'
                }
            }
        sb.addactionset('small_window', windowoptions)
    # -----------------------------------------------

    e "after setting up the necessary data. let's call the screen"

    python:
        sbd = sb.bridge('small_window')
        
    call screen small_window(sbd)

    e "Let's change the values and call the screen again."

    hide screen small_window

    python:
        sb.adddata('small_window', 'title', 'Another Test')
        sb.adddata('small_window', 'text', 'This simply overwrites these data')
        windowoptions['action1']['name'] = "In the Jungle, the Might Jungle."
        windowoptions['action2']['name'] = "The Lion sleeps tonight."
        windowoptions['action3']['name'] = "Awimbawep. Awimbawep."
        sb.addactionset('small_window', windowoptions)

    e "Let's see the updated window and link the action results to our label"

    $ sbd = sb.bridge('small_window')

    call screen small_window(sbd)
    # this jumps to the label associated with action
    call _return

    jump sceneloader_tutorial

    return

# -----------------------------------------------
#  these are the actions defined in the options dictionary above

label immadoit:
    e "Looks like you did it. Congratulations!"

label immathinkit:
    e "How long do you have to think about it?"

label immasitonit:
    e "You're a lazy bum."

