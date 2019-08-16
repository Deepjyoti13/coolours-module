# **Coolours**
### A Python Module To Make Text Colouring Easy
#### _Made By Alex Hawking_

# Installation

You can install with `pip`:

    pip install coolours

You can install using `curl` by copy and pasting:
    
    cd ~/Library/Python/3.7/lib/python/site-packages/ && { curl -O https://raw.githubusercontent.com/Handmade-Studios/coolours-module/master/coolours/coolours.py ; cd -; }

# Usage

> ## Importing

>If you installed with pip:
    
    from coolours.coolours import (
    
>Else

Import coolors using:

    from coolours import *

You can import with

    import coolours

But that requires you to use `print(coolours.color('style', 'textcolor', 'backgroundcolor'))`, so I think it is easier to use the first method.

> ## Colors

You use coolors within the `print` function as shown below:

    print(colour('style', 'text-colour', 'background-colour') + 'your text')

**Make sure you place the colors and styles within quotes**

> ## Default

To make the colors back to default after the coloured text add `default` to the end of the print function:

    print(colour('style', 'text-colour', 'background-colour') + 'your text' + default)

# List of Colors

### Coolors contains the following colours:

> ## Styles

- none
- bold
- underline (not supported in all temrinals)
- blink (not supported in all terminals)

> ## Text Colours

- none
- black
- red
- green
- yellow
- blue
- purple
- cyan
- white
- brightblack
- brightred
- brightgreen
- brightyellow
- brightblue
- brightpurple
- brightcyan
- brightwhite

> ## Background Colours

- none
- black
- red
- green
- yellow
- blue
- purple
- cyan
- white
- brightblack
- brightred
- brightgreen
- brightyellow
- brightblue
- brightpurple
- brightcyan
- brightwhite


# Future

More colours and style coming soon. Will also add a way to align text.


