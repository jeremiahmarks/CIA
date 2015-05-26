#CIA

##The CSV Import Assistant

Welcome to the CIA!  This is a more directed collection of 
tools and scripts intended to help out with managing CSV files,
matching records between CSV files, and importing records to
Infusionsoft.

`CIA.BlackOps` is probably best left alone, it is where 
special projects like to try and make their home.

The CIA has three basic components:

* CSV manipulation
    * Basically a suite of tools that work specifically on 
    CSV files
    * Example Functions include:
        * Break up files to set size limit:
            * Basically, turn one large file into many files
            no larger than sizeX
        * Find and remove columns that have no information or
        columns that have no header
        * statistics gathering:
            * number of unique values per column
            * locations of cells that are too large for the
            system to handle
            * likely duplication notification
* Import functions
    * provide interaction with the Infusionsoft API to pull
    existing records for duplication avoidance
    * provide ability to perform imports not available, for 
    instance, product options
    * depending on the scope of the import, browser automation
    will also live here
* Assistant(007)
    * the assistant will start by creating a project for you
    or loading an existing project, if so directed. 
    * Each project can consist of many files.
    * The assistant will use the tools available to perform 
    tasks.
        * EX1: 
            * Accept a csv file of contact information.
            * Find which columns would indicate a duplicate.
            * provide a list in both html and csv of all
            duplicate entries found. 
            Depending on size of result and user input either
                * Do it
                    * create the custom fields required then
                    * create the records that were unique.
                * Help you do it
                    * export csv needed (created by size)
        * EX2:
            * Accept a list of products
            * Accept a list of product Categories
            * Accept a list of product options
            * Derive relationship between product categories
            and products
            * Check for existance of listed products, create
            if needed, update dependencies as needed.
            * Check for existance of listed product categories,
            create as needed. 
            * Check for record of relationship with products
            assigned to category, if none exists, create one.
            * Check for record of product option. Create as 
            needed.
        * notes about examples: If this is a large data set,
        it can hit the API pretty hard. Since the assistant 
        uses csv files (and will be able to use a local sql
        database) if the project needs to be stopped, as long
        as you leave the files in place, the assistant will
        be able to pick up where he left off. 

#Image Import

I really think that this is the coolest thing since sliced
bread. I mean, it is pretty cool. But it is time consuming.
I am looking at other options Specifically 

* [MechanicalSoup](https://github.com/hickford/MechanicalSoup)
* [RoboBrowser](https://github.com/jmcarp/robobrowser)

By "Looking at" I mean I have read the README.

Anyways, image import will accept a CSV file with a relationship
to a product. When it can determine what it's URL is (by the 
product ID being known (API lookup or csv file)) it will open a 
browser, upload the image, navigate to the product on the store
front, take a screenshot, and then do the next in queue or close
the browser.