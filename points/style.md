We need to agree on a style guide. Ideally we would probably do best to get whatever dev is using, but until then, how do yall feel about?

Spaces, not tabs. Two spaces == one level of intentation

Run a code beautifier that lints your code. Fix those lints, or have a reason to not have.  

Reasons to not fix a linting issue - if there is a definite readability improvement. Basically, if for some reason you are working on nested html javascript within html nested somewhere in a nested fuction, do not worry about line length.  Look at the decisions that got you there, and figure out how to not do it again, but do not limit yourself to four characters per line. 

Reasons to not fix a linting issue - if it is a function definition, lets let those be on one line, just to avoid any readability issues. 