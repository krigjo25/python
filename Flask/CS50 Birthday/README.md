# Birthdays

##  About Birthdays

The choice of using class baseed views, was an interesting approach. Ass classed based views are more structured and easier to maintain.

Originally this web application was created as an assignment at xCS50, but not based on their instructions to develop a web application in their own way

###  JavaScript

The JavaScript serves as a client to fetch the content from contenteditable contents from a specific
button and send it through ajax to the server side, its a work around as the server can not do multi-tasking naturally.
So on submit the ajax sends through the code to the server.

### Database

#### SQL
The SQL is partly created by CS50, but i saw a reason to upgrade the SQL

#### Table Functionallity

-   Delete a record                         ✅
-   Order by name, bday                     ✅
-   Inserting a new record                  ✅
-   Edit a record (using contenteditable)   ✅

## Credits

### Responsories

[flask - Pallets project](https://github.com/pallets)
[CS50 - CS50 team](https://cs50.harvard.edu/x/2024/)

## Project summary

### Challanges


-   During the project several challanges occured under the development some about the contenteditable attribute and form submission.
A function was created containing ajax to send the information as an alternative way instead of sending it directly to the server.

In order to create that function i had to loop through the content, by using a for loop and ensuring the button value matches.

Sincerely,
@krigjo25


