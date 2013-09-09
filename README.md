link_gen
========

link_gen Link Generator for Photoswipe by grplyler

Abilities:
    Simplly have your images in images/full and images/thumb
    in your photoswipe directory on your webserver and run the script
    to generate hundreds or thousands of links in a only a few moments.

    This scipt assumes that your images are name in numerical sequential
    order like: 1.jpg, 2.jpg, 3.jpg etc.
    I may implement a way to specifiy your image nameing convention in future
    releases.

    The output from this script is not only written to a file for
    the purpose of documentation, but it also copies the text to your clipboard!
    It does this with the help of pyperclip.py by http://coffeeghost.net/

Usage:
    Usage couldn't be any simpler. Simple launch the script with F5 in IDLE
    if you have it or:
        $ python link_gen.py
    in a command line.
    The program prompts you with intrsuction and fields to fill out to
    generate your links.


Special Thanks to Al Sweigart at by http://coffeeghost.net/ for developing the
cross platform clipboard utility for Python.
