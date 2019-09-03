init offset = -10

transform schaptext:
    alpha 0
    linear 2 alpha 1
    pause 1
    linear 2 alpha 0


screen small_window(screenbridgedata):
    python:
        window_title = screenbridgedata['title']
        window_text = screenbridgedata['text']

        window_options = screenbridgedata['options']
    frame:
        xoffset 30
        xsize 200
        xpos 200
        ypos 200
        xfill False
        vbox:
            text _("[window_title]"):
                size 14

            text _("[window_text]"):
                size 12

            for option in window_options:
                use small_window_option(option)


screen small_window_option(itemdata):
    python:
        option_text = itemdata['text']
        option_action = itemdata['action']

    textbutton _("[option_text]"):
        text_hover_color "#FFFFFF"
        text_color "#BBBBBB"
        action Return(option_action)
        text_size 12
        ysize 18


