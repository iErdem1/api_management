# CS342 Design Patterns
## Fall 2018
### PROJECT 3 README FILE

## DESIGN OVERVIEW:
- State each design pattern used (if any)
- Brief (< 5 sentences) description of your overall design
- Description of your search algorithm

## KNOWN BUGS AND INCOMPLETE PARTS:
- What parts of the project you were not able to complete

## REFERENCES:
- List any outside resources used

## MISCELLANEOUS COMMENTS:
- Anything you would like the grader to know

## Assignment Description
***
# Project 3 - Web APIs
### Due Date: 11:59 p.m., Nov 20th, 2018

*All programs will be tested on the machines in the Q22 lab. If your code does not run on the system in this lab, it is considered non-functioning EVEN IF IT RUNS ON YOUR PERSONAL COMPUTER. Always check that your code runs on the lab machines before submitting.*

### Driver Code and Test Files
* project3.py

### Grading Rubric
**Total: 40 points**
* API Proxy
   * Uses a separate proxy class to access each API (9 points)
   * Has an API base class or module for shared functionality (3 points)
   * Encapsulates connection details in the API base class ( 3 points)
   * Has fallback for each API in case of call failure (3 points)
* Log Class
   * Log class stores in real time as a log file (3 points)
   * Log manages separate log files for each API (3 points)
* Uses the "json" module from the Python library (2 points)
* Extra Credit assigned for increased complexity and functionality (5 points max to be determined by TA)
* Submission:
    * Follows requested project structure and submission format (-5 points)
    * No global variables (-5 points)
    * Meets the commit requirement of having 3 significant commits 24 hours apart

### Guidelines
This is an individual assignment. You must do the vast majority of the work on your own. It is permissible to consult with classmates to ask general questions about the assignment, to help discover and fix specific bugs, and to talk about high level approaches in general terms. It is not permissible to give or receive answers or solution details from fellow students.

You may research online for additional resources; however, you may not use code that was written specifically *to* solve the problem you have been given, and you may not have anyone else help you write the code or solve the problem. You may use code snippets found online, providing that they are appropriately and clearly cited, within your submitted code.

*By submitting this assignment, you agree that you have followed the above guidelines regarding collaboration and research.*

__In this project, you will learn to__:

* Use design patterns to correctly interface with Web APIs

***


## Description

One of the primary programming skills you will need in today’s software developer landscape is working with web APIs. There are a lot of fun, free API’s out there for you to use. [Here](https://pythonprogramming.net/urllib-tutorial-python-3/) is a quick tutorial on how accessing API’s works in Python, and I will also cover the topic in class. You can also use the [requests](http://docs.python-requests.org/en/master/) module, which is easier to use, but you have to install it separately.

## Part A - Choosing your APIs
For this project, you are going to build a program that uses at least 3 web API’s to generate and validate some data. You are then going to store the data locally in a JSON file.
The following are lists of different API’s that you can use:
* https://github.com/toddmotto/public-apis
* https://any-api.com/

Feel free to use any publicly available API, even if it does not appear on this list.

You will need to create several API proxy classes (one for each API you use). From there, your design is entirely dependent on what you want to do with the API calls. Below is an example of the kind of project that would be acceptable:

### Example Program
Your program generates random information for a user by making a call to the [randomuser API](https://randomuser.me/) on initialization, and stores whatever information you deem as relevant. Using a User Proxy class, you encapsulate the connection and attributes of the API call, in addition to a fallback in case of no connection. You could then verify the user’s email address with a Proxy class for the [mailboxlayer API](https://mailboxlayer.com/). If the email address validates, you then use a [weather api](https://www.metaweather.com/api/) to display the current weather for the user’s city.


Repeat this until you have at least 10 records (users) in a local JSON database. Then prompt the user on the command line to search the database. You may search by whatever attribute you wish, first name, last name, etc. On a successful search, the user can change any one of the records attributes (except the search attribute), then save the record back to the database. This should not create a duplicate record, but instead update the existing record.

The only requirement is that you should not simply print the API data you receive. You must create an application that uses the API data to do something.
* __Bad use of API__: Query an API for a random Chuck Norris joke and print.
* __Good use of API__: Ask a user personal information, such as their favorite sport, what country they are from, and birthday. Find all Athletes from their favorite sport that share the same birthday and/or are from the same country.

### Logging

Whenever you interact with an API, you should log each request and response using a Log class. The Log class should manage separate log files for each API. The design of this Log class is up to you, but it should be implemented using a design pattern (Facade, Chain of Responsibility, Command, etc).

## Part C - Technical Requirements
### 3 Design Patterns
You must use at least 3 design patterns we discussed in class after Midterm I. I have already given you 1, Proxy. Other options are decorator, command, facade, etc.

### Additional Requirements

#### API Base Class
You will quickly notice that API calls all work similarly. You should create an API superclass or module (your choice) that can be inherited or included in your API Proxy classes. Within your super class you should combine as much of the shared code as possible.

#### Fallback Protection
You must create a fallback in your Proxy class in case the api call fails. You may return a generic value or a message that the api call failed; however, your program as a whole should not fail or crash. You should have some fallback data to use in its place.

#### Log Class
You may approach designing the class however you wish, however, you must have a Log class that  writes out data to a file in real time, i.e. during execution not just when your programs exits.

## Part D: Submission

Required code organization:
* APIProxy.py
    * Abstract Class
* Additional Proxy Classes
    * One for each API
* Log.py
* program3.py
* any additional files you feel are necessary

### Git

You must commit your changes throughout the development of your project. You do not necessarily need to push the commits to Github, but we will look at your repository commit history to ensure you have **3 significant commits 24 hours apart**. If you do not meet the commit requirements, we will not accept your project and you will receive a 0.

These are a reminder of the git commands you will need to submit your project.

:warning: *These commands all presume that your current working directory is within the directory tracked by `git`.*

```shell
git status
git add info.txt
git commit -a -m "final commit message"
git push
```
:warning: *You* __must__ *add any new files you create to the repository with the `git add` command or they will not upload to the repo, and your code will not work.*

To find your most recent commit hash, use the following command:

```shell
git rev-parse HEAD
```

To complete your submission, you must copy and paste this number into mycourses. Go to MyCourses, select cs342, and **Assignment Hash Submission**. Select Project 3, and where it says text submission, paste your commit hash. The TAs will only grade your submission that corresponds to the hash you submitted. You can update this as often as you like until the deadline.

I strongly recommend making a submission early on, even if your assignment is not 100% working, to avoid late penalties. You can resubmit as many times as you like.

:warning: You __MUST__ submit the commit hash on mycourses before the deadline to be considered on time **even if your project is completely working before the deadline**. :warning:
