##start = 1
##end = 1870
##
##end = end + 1
##
##while start < end: # first while loop code
##    print(str("<li><a href='images/full/") + str(start) + str(".jpg' rel='external'><img src='images/thumb/") + str(start) + str(".jpg' alt='Image ") + str(start) + str("' /></a></li>"))
##    start = start + 1

import pyperclip

print '''
Link Generator verions 2 for Photoswipe Link
generation.

Version 2 by: Ryan Plyler
\n\n

'''

answer = raw_input('Write output to file? <yes/no>: ')


if answer == 'yes':
    filename = raw_input("Filename: ")
    filename = filename + ".txt"
    start = raw_input("Start Image Number: ")
    start = int(start)
    end = raw_input("Ending Image Number: ")
    end = int(end) + 1

    writeFile = open(filename, 'w')
    
    data = []
    while start < end: # first while loop code
        newItem = "<li><a href='images/full/" + str(start) + str(".jpg' rel='external'><img src='images/thumb/") + str(start) + str(".jpg' alt='Image ") + str(start) + str("' /></a></li>")
        data.append(newItem)
        start = start + 1

    
    for item in data:
        writeFile.write("%s\n" % item)

    writeFile.close()

    stringData = ''.join(data)

    pyperclip.copy(stringData)
        
    
else:
    print """Ok, writing output to screen. This will take longer,
    but you can copy and paste."""


print """
All links generated successfully.
You can now grab them from the file I wrote.
"""




