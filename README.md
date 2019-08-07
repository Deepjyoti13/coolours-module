# **Coolors**
### A Python Module To Make Text Colouring Easy
#### _Made By Alex Hawking_

# Installation

Due to issues with SSL Certificates I have been unable to add this to pip. 

You can install using `curl` by copy and pasting:
    
    cd ~/Library/Python/3.7/lib/python/site-packages/ && { curl -O https://raw.githubusercontent.com/Handmade-Studios/coolors-module/master/coolors.py ; cd -; }

# Usage

> ## Importing

Import coolors using:

    from coolors import *

You can import with

    import coolors

But that requires you to use `print(coolors.color('style', 'textcolor', 'backgroundcolor'))`, so I think it is easier to use the first method.

> ## Colors

You use coolors within the `print` function as shown below:

    print(color('style', 'text-color', 'background-color') + 'your text')

**Make sure you place the colors and styles within quotes**

> ## Default

To make the colors back to default after the coloured text add `default` to the end of the print function:

    print(color('style', 'text-color', 'background-color') + 'your text' + default)

# List of Colors

### Coolors contains the following colours:

> ## Styles

- none
- bold
- underline (not supported in all temrinals)
- blink (not supported in all terminals)

> ## Text Colors

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

> ## Background Colors

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

More colors and style coming soon. Will also add a way to align text.


