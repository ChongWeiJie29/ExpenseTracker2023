# YOUR PROJECT TITLE
#### Video Demo:  <URL HERE>
#### Description:

- Introduction to project
- Files and Explanation
- Design choices and Elaboration

## Introduction
Money Matters is a website designed to **empower users in tracking their finances**.

Over time, I started to grow more conscious of my spending habits as I realised how pricey some items could get. I wanted to make sure that my inflows for each particular month would be sufficient in sustaining not only my expenditure, but also my savings. Therefore, I looked for money managing apps to help me track my spending and savings more easily. As I strongly believe that managing one's finances is crucial, I was inspired to work on a financial management website as my final project.

The project assists users in tracking their finances through the use of several tools. Users are able to input both their inflows and outflows based on the amount, category, and date. The website allows users visualise their finances through the use of a pie chart. For instance, users are able to easily identify which category they are spending the most on, and thereafter, make informed financial decisions to start reducing expenditure on items that fall under that particular category. The platform also allows users to compare their expenditure and savings from different months, providing them with the opportunity to understand how their spending or saving habits have changed over time.

## Files
**app.py**
```
This file is the main file where this project runs.
It handles the logic for each function, as well as the routing between pages.

It starts off at the starting page. Before logging in, users will not be able to do much. Users can only view the About Us, Register, and Log in. After logging in, users will then be able to start tracking their finances. Users can input their inflows and outflows, and after that view their expenditures for the month in the home page. Users can also route to the past transaction page to view expenditures for previous months if they wish to.
```
**dbHelpers.py**
```
This file contains the helper functions for the sqlite3 database.
It handles the logic for each function, as well as the routing between pages.
Its main purpose is to create the tables if they do not yet exist.

The function creates 2 tables, `users` and `transactions`. The users table contains the user account information such as username, password and total cash. The transactions table contains the transaction information such as item, category, inflow/outflow and date of transaction.
```
**helpers.py**
```
This file contains the helper functions for app.py.
Each of the main functions in app.py has a corresponding helper function to simplify the code in app.py
```
**expenses.db**
```
This file is the sqlite3 db file for the project.
Feel free to delete this file to reset your database!
```
**templates/**
```
This folder contains all the templates for each html page.
```
## Design choices
### First design choice
The first design decision was regarding the database tables. I was thinking of a
logical way to organise the tables. This was challenging as there were mulitple ways to
design the tables, which made it quite confusing as to which was the better way. While it
was between combining everything into 1 table and splitting it into 2 tables, I eventually went for the latter. I felt that by splitting it, it was better as it was more decentralised and I can get the information separately.
### Second design choice
The second design choice was whether or not to create a new helper file with all the helper
functions. Initially, all the logic was combined in the app.py folder. However, as the code
become more complex, I found it more difficult to keep track of what was going on. Furthermore,
it also become more tedious to continuously scroll up and down through the file. I thus decided
to split the code, transferring the bulk of the complicated code into a separate helper file,
similar to problem set 9.
### Third design choice
The third design choice was the implementation of the home page. The home page displays a lot of important information such as all the users transactions, displayed in various formats such as a table and pie chart. Thus, it was important to design the logic properly and execute the correct SQL queries to get the correct information, and display it appropriately. In the end, the logic was implemented in 3 main SQL statements: one to get all the user transactions, to display as a table, one to get the existing user's cash, and one to get the amount spent on each category, to display that as a pie chart.


