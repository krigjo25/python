#   WordGames

## Table of content

>   ## [Introduction](#Introduction)
>>  ### About the Maintainer
>>  ### Contact
>>  ### Disclaimers

>   ## [WordGames](#WordGames)
>>  ### Project information 
>>  ### Features
>>  ### Updates

>   ## [Credentials](#Credentials)
>>  ### Responsories
>>  ### APIs
>>  ### References

>   ## [Notes](#Notes)
>>  ### Python functions
>>  ### Python Try, except, else
>>  ### Python List
>>  ### Python del
>>  ### SQL Database


## Introduction

### About the Maintainer

My name is Kristoffer, everybody calling me Kriss.<br>
I'm born in 94 from Norway, which is translated to "the way to the north"<br>
usually i do study Python, SQL, Philiosophy & C++, otherwise im just being a human.


### Contact information

[Contact Information](https://github.com/krigjo25/contactinformation)

##  WordGames

### Project info

> Project start :<br>
>   26.01-21
>
>   Last update :<br>
>   29.01-23
>
>   SQL Database:<br>
>   mariadb

## Feautures

### Available games

*   JumbleGame
*   Scrabble
*   Eightball

### Eightball

The game works with asking any question into the input field.<br>
Questions containing numbers will output a ValueError.

The program sends you a feedback ;

*      if the question can not be asked, by sending an exception in this case a ValueError.

*      With a Philiosopic answer if the question can be asked.

USAGE : In your terminal, type games.py,
then follow the instructions for every prompted message

### JumbleGame

The intention of the game is to unscrabble a given word.<br>
The given word is based on category which is saved in a MariaDB database<br>
except random, the category random is an API by [API-Ninja](https://api-ninjas.com/).

USAGE : In your terminal, type games.py,
then follow the instructions for every prompted message

### Scrabble

The intention of the game is to send a valid English word into the program<br>
Then the program will check if the word does actually exists with an API by [API-Ninja](https://api-ninjas.com/).

-   If the word does not exists, the player will recieve zero points for the word

The points system is ranged for each letter as in scrabble.

USAGE : In your terminal, type games.py,
then follow the instructions for every prompted message

## Credentials

### Responsories

-   requests [Kenneth Reitz](https://requests.readthedocs.io/en/latest/)<nt>

### API

-   [NAPI Ninjas](https://api-ninjas.com/)<br>

## Notes

### Python functions

During the project I have learned alot about Python functions<br>
How to define a function, how the syntax of a function works in real life.


### Python Try, except, else

I have learned the importance of using `Try, except, else`,<br>
in the code, it has a better structure.

its a better design as developers can see what you are attempting to do <br>


### Python List

During the projects I've learned how to declear, initialize<br>
a 1D Array or 2D Arrays. To make the workflow easier for to read.

List or arrays are a short term solution to store information which is going to be used in the project.

### Python del

Using Python's `del` is important to clear space from memory, to avoid using unneccessary memories, for the sake of resources.


### SQL Database


During the project I have learned the basic understanding of a<br>
`Structure Query Language` hereby it's Alias will be used (`SQL`).

Database is used to store information the database can be static which means values never changes<br>
dynamically which means the values can change.

`tables` are created to sort data in columns and rows
