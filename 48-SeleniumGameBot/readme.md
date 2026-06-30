# Day 48 Create an automated game playing bot

## Project Overview

Using Cookie Clicker and Selenium, create a program that automatically plays the game.

```
Start Game
     │
     ▼
Dismiss language popup
     │
     ▼
Click cookie continuously
     │
     ├──────────────┐
     ▼              │
Every 5 seconds     │
Check upgrades      │
Buy best one        │
     │              │
     └──────────────┘
     │
     ▼
After 5 minutes
Stop
Print Cookies/Second
```

Challenge: Create an Automated Game Playing Bot

1. Go to the game on github pages and familiarise yourself with how it works: https://github.com/ozh/cookieclicker (new version) 
2. Create a bot using Selenium and Python to click on the cookie as fast as possible. 
Note that you will need to find a way to automatically dismiss the language selection before you can get started. 
3. Every 5 seconds, check the right-hand pane to see which upgrades are affordable and purchase the most expensive one. 
You'll need to check how much money (cookies) you have against the price of each upgrade. 
e.g. both Grandma and Cursor are affordable as we have 105 cookies, but Grandma is the more expensive one, so we'll purchase that instead of the cursor. 

I reckon the most challenging part will be figuring out how to select the most expensive item every 5 seconds, since the upgrades become available only gradually over time. 

HINT 1: https://www.w3schools.com/python/ref_string_split.asp

HINT 2: https://www.w3schools.com/python/ref_string_strip.asp

HINT 3: https://www.w3schools.com/python/ref_string_replace.asp

HINT 4: https://stackoverflow.com/questions/13293269/how-would-i-stop-a-while-loop-after-n-amount-of-time

4. After 5 minutes have passed since starting the game, stop the bot and print the "cookies/second". e.g. this is mine: 
5. Once you've managed to get the bot to work, feel free to tweak the algorithm if you think there is a better way to play the game.
e.g. Change the time, instead of every 5 seconds to check the upgrades, what if you did every second or every 10 seconds? 
Or maybe the bot should buy all the affordable upgrades.

## Steps to complete
1. launch the game
2. language selection
3. locate the big cookie
4. infinite clicking
5. understand the store
6. locate every upgrade
7. extract prices
8. convert prices to int
9. read cookie count
10. determine affordability
11. buy the most expensive affordable upgrade
12. time management
13. stop after 5 min
14. print cookies per second