I know there are many things that will
need to be documented, this will serve as
their home initially. 
---------------

Yet, another change.
Thinking about abou I want this to operate:

1. Projects consist of csv files and data downloaded from the 
API
1. User Objective(UO) is to match the data from the CSV file to a 
matching infusionsoft object
1. UO will be completed by matching a column in the csv file
to the relevant property of an infusionsoft object
1. User will be provided various tools to implement this 
objective such as:
    * splitting column by multiple, ordered or unordered, delimiters
    * removing or replacing text that match either string literals
    or regular expressions. Common regular expressions will be included,
    as well as an ability for the user to create and save their own. 
        * potentially provide a repo to store and share useful ones.
    * providing statistics about columns. ie:
        * top X (default=5) literals found in each column
        * percent of column without a value
        * Average length of populated cells
        * Average length of all cells
        * Longest cell(s)
        * shortest populated cell(s)
    * ability to chain manipulators on data, and then work
    on just the resulting dataset.
1. After user has matched the files to the correct fields 
(or perhaps before if I can find my old async documentation)
    * the system will prompt if it should dupe check 
    and/or/neither update
    * if it should dupecheck:
        * the system will currently download all of the 
        existing records of each type
        * check if the new record already exists. 
            * if it does the system will check if it should 
            update
                *if it should it will update the product
                * else it will pass
            * if it does not it will create the item, and 
            update the local version with the ID or other 
            information
    * if it should not dupecheck, the system will create the 
    item automatically and update the local record to make it
    available for child functions.
1. UI:
    * since I have experience with webpages, it will spin
    itself a local only webserver.
1. Some Needed improvements:
    * ability to work with the import process so that it 
    does not use as many api tokens. I think since pulling 
    records down is easy, it should basically create the CSV
    and upload it itself so that it can know when to requery
    the api.  It will probably initially, though, wait for 
    the user to tell it to requery.

-----------------
So, this thing is going to change frequently.

Take a pass on databases for right now. Me figuring out
the data structure before hand would be a
good thing, I totally admit, but that
is probably going to take as much time as
building the tools and peicing them together
by hand for a time or two. 

So, that is what we are going to do first. 

Using the csv file tools, attempt to fully
parse a regular, non- project-messy.csv file
then match the data from the file to 
appropriate data Structures. Pull data on 
each dataStructure through the API, determine
what can be generated via the API, and what
will need CSV import. Generate CSV files to
import and order of operations. Proceed to
complete order of operations.


There are two main parts to the application:

1. The assistant:
    * In charge of creating databases, loading projects,
    and enacting various workflows.
    * acts as the integration point for displays, basically
    accepting different instructions and acting on them
    or returning formatted data
1. The tools:
    * CSV tools
        * various tools that process defined data and
        return results, either a set of data or a path
        to a resulting file.
        * examples include:
            * find excel killers
                - A function which will find and return any cells that
                are too large for excel to handle
            * create column
                - A function which will create a new copy of the file, 
                with a column full of specified data
            * split column
                - A function which will create multiple new columns 
                filled with substrings that
    * API tools:
        * various tools to provide functionality via the API
        * examples include:
            * get all records
                - A function which will return all records of a 
                given type
            * create record
                - A function which will create a record of the 
                given type
    * database tools:
        * various tools to store and interact with information
        stored in a database
        * examples include:
            * store csv as table:
                - Ability to accept a csv file and store it as a 
                table in a database
            * create csv to csv relationship
                - Ability to create relationship between different
                csv columns in the same project
            * create csv to api relationship
                - Ability to create a relationship between a column
                in a csv file and a column in an API result


General file structure:

    This will be two parted, the file scheme of
    this collection of tools including how they
    interact and also including the 
    "Central Repo", a folder that houses 
    (probably) encrypted and compressed version
    of historical files. These will initially
    need to be managed by telling the software
    to delete the files, but may be resolved by
    a simple cron job that activates a script
    which will then take appropriate actions based on the 
    length of time since last access.

The files exist on the server for two reasons

1. a way to download replacement files from history.
2. so that the user does not *need* to install this locally
    although they will be highly encouraged to do so.
    1. The system will be faster overall without the overhead
    needed to transfer data back and forth frequently.
    2. I could easily imagine having several large jobs going
    at once and causing an issue.  Large files on my computer
    do not take any time at all, but all at once I think that
    there could be bad things.

Basically every user will be encouraged to do things locally
and simply upload the ocassional backup.

This file structure will more or less mirror the one on the 
server, except that the files will definitely not be encrypted,
nor.

Application will be written such that it basically just an api
to the data set. The api will deliver either the data requested
or response code. 

The data delivered will likely be in the json format, which
will allow the display driver to choose how to display it. 
https://docs.python.org/2/library/json.html

The driver that I will provide will be a simple webpage with
basic data templates, potentially.

This will be served via the default python webserver, on some
port, only accessible from the machine.

Basic project flow will look something like this:

* app is listening for clients
* user connects, is greeted with a screen prompting selection
of existing project, or create new.
* project loads. 
    * Options:
        * Add new file{/path/to/file}
        * work with existing{fileID}
        * revert file to original

application file and control layout

    __init__.py  
        storeroom  
        tools  
