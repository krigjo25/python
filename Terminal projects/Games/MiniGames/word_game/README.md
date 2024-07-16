#   WordGames

## Table of content

## [Introduction](#Introduction)
### About the author

## [WordGames](#WordGames)
### Project information 
### Features
### Updates

## [Credentials](#Credentials)
### Responsories
### APIs
### References

## [Project Summary](#project-summary)
### SQL Database


## Introduction

### About The Author
[about krigjo25](https://github.com/krigjo25/)


##  WordGames

### Project information

> USEAGE : In your terminal, type wg -h to view the list of commands

### Available games

*   JumbleGame
*   Scrabble
*   Eightball
*   Rock, Scissor'n Paper


### Eightball

The game works with asking any question into the input field.<br>
Questions containing numbers will output a ValueError.

The program sends you a feedback:

*      if the question can not be asked, by sending the user a ValueError

*      With a Philiosopic answer if the question can be asked.

### JumbleGame

The intention of the game is to unscrabble a given word.<br>
The given word is based on category which is saved in a MariaDB database<br>
except random, the category random is an API by [API-Ninja](https://api-ninjas.com/).

### Scrabble

The intention of the game is to send a valid English word into the program<br>
Then the program will check if the word does actually exists with an API by [API-Ninja](https://api-ninjas.com/).

-   If the word does not exists, the player will recieve zero points for the word

The points system is ranged for each letter as in scrabble.

## Credentials

### Responsories

-   [requests  - by Kenneth Reitz](https://requests.readthedocs.io/en/latest/)

-   [sqlite - by sqlite team]()
-   [sys, random -  by Python developer team]()
-   [dotenv -   by Saurabh Kumar](https://github.com/theskumar/python-dotenv)


### API

-   [NAPI Ninjas](https://api-ninjas.com/)<br>
-   [Random Human Generator - AbhinRustagi](https://randomuser.me/)<br>

## Project Summary

### SQL Database

During the project I have learned the basic understanding of a<br>
`Structure Query Language` hereby it's Alias will be used (`SQL`).

Database is used to store information the database can be static which means values never changes<br>
dynamically which means the values can change.

`tables` are created to sort data in columns and rows


### Eightball

    With Eightball i learned to work with lists, numpy is way to useless in this 
    type of project, but it shows others it can be worked with.

    Working with dictionary was also learned during this project.

### Scrabble

    During this project It was learned to implement a basic API for randomizing 
    the names to the bots, and to use APIs for different purposes.

    The sorting Algorithm Margin sort was choosen even it takes a huge ammount of 
    time regarding the use in basic, its choosen in case there is huge datasets 
    available to sort.

### Rock, Scissors, Paper (RSP)

### Jumble Game
