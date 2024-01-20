To make sure a string will display as expected, we can format the result with the format() method.

String format()
The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method

Definition and Usage
The format() method formats the specified value(s) and insert them inside the string's placeholder.

The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

The format() method returns the formatted string.

Syntax = string.format(value1, value2...)
Parameter Values
Parameter	        Description
value1, value2...	Required. One or more values that should be formatted and inserted in the string.

                  The values are either a list of values separated by commas, a key=value list, or a combination of both.

                  The values can be of any data type.
                  
The Placeholders
The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.

Example
Using different placeholder values:

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
