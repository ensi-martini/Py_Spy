#py_spy.py by Ensi Martini
from easygui import *
firstFile = open(fileopenbox())
choice = buttonbox('Please choose an option', 'Py Spy', ('Compare', 'Loops', 'String Formats', 'Variables', 'Quit'))
firstProgram = []

#Putting every line in the first program into a list for reference later.
for line in firstFile:
    firstProgram += [line.strip()]

while choice != 'Quit':
    #Variables are assigned inside of the loop so that selecting the same option several times does not duplicate outputs
    longVariables = ['Long Variables:\n']
    constants = ['Constants:\n']
    numbered = ['Numbered:\n']
    secondProgram = []
    stringFormat = []
    loops = []
    variables = []
    counter = 0
    otherCounter= 0
    string = ''

    if choice == 'Compare':
        secondFile = open(fileopenbox())   
        #Putting every line that is not whitespace in the second program into a list for reference later
        for line in secondFile:
                line = line.strip()
                if line != '':
                    secondProgram += [line]    
        #Reads each line in the lists, checks if that exact string is also in the other list, and adds one to a counter each time that it is
        for line in firstProgram:
            if line != '' and line in secondProgram:
                counter += 1
        for line in secondProgram:
            if line in firstProgram:
                otherCounter += 1
        #Prints the final statement for this option
        msgbox('{:.1f}% of file A is like file B, and {:.1f}% of file B is like file A'.format(otherCounter/len(secondProgram) * 100, counter/(len(firstProgram) - firstProgram.count('')) * 100,'Compare'))
        
    elif choice == 'Loops':
        #Loops always start with 'for' or 'while'. This reads every line in the list made above and if the first 3 characters are 'for' OR the first 5 characters are 'while', it adds it to a list, along with the line it is on and a line break
        for line in firstProgram:
            counter += 1
            if line[:3] == 'for' or line[:5] == 'while':
                loops.append(line + '(line {})'.format(counter) + '\n')
        #Prints the final statement for this option
        codebox('The following loops were found in the program you selected:', 'Loops', loops)
        
    elif choice == 'String Formats':
        for line in firstProgram:
            #Checks if this line has .format in it, and if so to loop through it, and add the counter value to the string after every '{'
            if '.format' in line:
                for char in line:
                    string += char
                    if char == '{':
                        string += str(counter)
                        counter += 1
                counter = 0
                stringFormat += [string[string.find('(') + 1:-string.count('(', string.find('.format'))] + '\n']
                string = ''        
        codebox('The following lines involve string formatting:', 'String Formats', stringFormat)
    else: #Variables 
        for line in firstProgram:
            #Checks if a variable is assigned on this line. Usually, the only time a single '=' is used in a line is when assigning variables. Checking if the next character is also '=' and if the character before it is in '!+-*/' filters out any if/else/elif/for/while statements.
            if '=' in line and line[line.index('=') + 1] != '=' and line[line.index('=') - 1] not in '+-*/!><':
                variables.append(line[:line.index('=')].strip())
        variableChoice = multchoicebox('Choose which variables you wish to examine', 'Variables', variables)
        
        #Adding the variables into the proper list(s)
        for varb in variableChoice:
            if len(varb) >= 15:
                longVariables.append('    ' + varb + '\n')
            if varb.strip('_123456789') == varb.strip('_123456789').upper():
                constants.append('    ' + varb + '\n')
            #Using negative indexing to check if the last character in the variable is in the string '0123456789'.
            if varb[-1] in '0123456789':
                numbered.append('    ' + varb + '\n')
        codebox('Variable Summary', 'Variable Summary', longVariables + constants + numbered)
    choice = buttonbox('Please choose an option', 'Py Spy', ('Compare', 'Loops', 'String Formats', 'Variables', 'Quit'))