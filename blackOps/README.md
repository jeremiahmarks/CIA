#Do not read!  

Silly file name, "README" for a top-secret folder.  Sigh, 
the things we have to put up with. 

##CURRENT PROJECTS:

* Project Messy
    * Project Messy is actually the genesis of the CIA.  
    The project is a products import that includes:
        * Products
        * Product categories
        * Product options
        * Variable Pricing for product options
        * Product Images
    * These are all stored in one CSV file. 
    * Current progress has found a solution for each struggle
    but has been unable to successfully implement for each
    struggle at the same time. 
    * This stops now.
    * Current Game Plan:
        * Parse CSV lines by line type.
            * This has been done.  Currently storing each
            type in its own CSV file that includes the 
            original line number and the text from the line.
        * Parse each linetype for dataTypes. 
        * Pull all data from affected tables through the API
        * If the record already exists on the server, update
        the CSV with the recordID.
        * Create all products which do not already exist
        * Create all product categories which do not already exist
        * Create all product options which do not already exist
        * upload image to product page
        * Take screenshot of public page

