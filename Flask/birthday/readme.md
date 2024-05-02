# Birthdays

## Introduction

This project is based on CS50's instructions developed by krigjo25

## Python

### Table Functionallity

- Inserting a new record ✅
-   Delete a record ✅
-   Edit a record (using contenteditable)  ❌
-   Order by name, bday ❌

## JavaScript

The JavaScripts serves as a client to fetch the ajax content from a specific button to fetch its row values.

-   Using ajax to send responses to the server ✅
-   Submit the form ❌

## Credits

### Responsories

#### Python Libraries

[flask - Pallets project](https://github.com/pallets)
[CS50 - CS50 team](https://cs50.harvard.edu/x/2024/)

#### Database

[CS50 - birthdays]()

### Collebrations

- .edit button - []()

### Contact Information

-   Discord : krigjo25#5588
-   messenger : krigjo25

Author notes<br>
« Everything is just perfect as it is.»

## Challanges

- Encountered a challange regarding sending data to the server

Created an ajax to perform this task.

- Encountered a problem using contenteditable
Solved the challenge using for loops to iterate through the contents, and checking wheter the value matches with the button value

- Encountered a problem with the form submission with the edit button

Which i tried to solve where the server fetches the cliecked button and the data was processed through javascript.
But there were another way, which is quite easier fetching the whole ajax content, and use that to gain the ability to edit the contenteditable text.

The conclusion is that Flask can not perform two seperate requests with out including another library such as Threader, but still it would be complicated
to use the library to fetch json document, while requesting a request.form. As they are seperate the ajax sends out the information before submit.
And what was needed was the submit button to submit before the ajax.

###  Licence

Not licenced.
