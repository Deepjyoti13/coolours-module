#designed by alex hawking

#usage: print(color(style, foreground color, background color) + 'your text')

def color(style, fore, bg):

    a = "\033[0;"
    b = "39;"
    c = "49m"

    #styles
    if style == "none":
        a = "\033[0;"
    if style == "bold":
        a = "\033[1;"
    if style == "underline":
        a = "\033[2;"
    if style == "blink":
        a = "\033[5;"

    #standard colors

    #fore
    if fore == "none":
        b = "39;"
    if fore == "black":
        b = "30;"
    if fore == "red":
        b = "31;"
    if fore == "green":
        b = "32;"
    if fore == "yellow":
        b = "33;"
    if fore == "blue":
        b = "34;"
    if fore == "purple":
        b = "35;"
    if fore == "cyan":
        b = "36;"
    if fore == "white":
        b = "37;"

    #background
    if bg == "none":
        c = "48m"
    if bg == "black":
        c = "40m"
    if bg == "red":
        c = "41m"
    if bg == "green":
        c = "42m"
    if bg == "yellow":
        c = "43m"
    if bg == "blue":
        c = "44m"
    if bg == "purple":
        c = "45m"
    if bg == "cyan":
        c = "46m"
    if bg == "white":
        c = "47m"

    #bright colors

    if fore == "brightblack":
        b = "90;"
    if fore == "brightred":
        b = "91;"
    if fore == "brightgreen":
        b = "92;"
    if fore == "brightyellow":
        b = "93;"
    if fore == "brightblue":
        b = "94;"
    if fore == "brightpurple":
        b = "95;"
    if fore == "brightcyan":
        b = "96;"
    if fore == "brightwhite":
        b = "97;"

    #background

    if bg == "brightblack":
        c = "100m"
    if bg == "brightred":
        c = "41m"
    if bg == "brightgreen":
        c = "42m"
    if bg == "brightyellow":
        c = "43m"
    if bg == "brightblue":
        c = "44m"
    if bg == "brightpurple":
        c = "45m"
    if bg == "brightcyan":
        c = "46m"
    if bg == "brightwhite":
        c = "47m"



    #finish
    return(a + b + c)


default = "\033[0;39;49m"

