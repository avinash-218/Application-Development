# Accounts-Manager2

This application is used to keep track of money in all the bank / wallet account in a single interface.
This application is useful in tracking budgets of an individual.

IDE used : Netbeans
Backend : Oracle 19c

Features
1) Multi User
2) Privacy in terms of password
3) Can reset password
4) Can delete the user account
5) Open a new bank / wallet account
6) Close an existing account
7) Rename existing account
8) Credit or debit money from selected account
9) Self transfer money within accounts
10) View balances in all accounts
11) View past transactions made
12) Print the transactions into PDF file
13) Edit / Delete already transactinos
14) Transactions can be viewed with filters.
15) User accounts can be deleted

Images are attached.

Users needed prior:
1) Sysdba users - for deleting user account
2) Accounts_Manager (any name as you wish) - maintaing logins of all the users.

Oracle queries:
CREATE USER Accounts_Manager IDENTIFIED BY xxxxxxx;
GRANT ALL PRIVILEGES TO Accounts_Manager;
CREATE TABLE LOGINS(USERNAME VARCHAR(15) NOT NULL, PASSWORD VARCHAR(15) NOT NULL); - Ex

PS: Source code contains some places with xxxxxxx where oracle username and password to be used.
Change Locations of Window icon also (Some icons are present in 'Jars and Images' Folder)