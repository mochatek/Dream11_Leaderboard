# Dream11 Leaderboard

Dream11 is a fantasy sports platform based in India that allows users to play fantasy cricket, hockey, football, kabaddi and basketball.
Like any fantasy sport game, users need to create their team and join some contest for competing. Joining into any contest is limited till
the game starts. The list of teams participating in the contest(**Leaderboard**) will be visible only after the match starts. The issue is
that the leaderboard along with their corresponding team details will be available for download(PDF) only after few hours into the match.
So, users won't be able to check the teams of other players from the begining. We need to manually click on each player in the leaderboard 
to view their team details which take huge amount of work and time. This python script automates these tasks and scraps the leaderboard 
along with their corresponding team details from the Dream11 site and provide the details in an excel file.

Dream11 site requires us to login to our contest inorder to view these details, through our registered mobile number and OTP.:information_source:
So, for scraping these details multiple times in between the match requires us to login every time. As authorization is done using OTP, 
this task will be very annoying. So we need to persist our login session through cookies. So, first run the script (**Dream11_login.py**)
and login as you normally do. This script will grab and export the cookie into a text file (*cookie.txt*).

Now run the script (**Dream11_crawler.py**) which loads the cookie from **cookie.txt**, inorder to bypass the login process.
Give it a few time to scrap the necessary details from the site. You can view the entire automation happening in your web browser.
Once the task is completed, you will see an excel file (**DREAM11.xlsx**), containing all the details.

- **:timer_clock: Scraping time depends on the numbers of players participating in the contest.**
- **:warning: Do not tamper with the site elements while script is running.**

## Requirements :
  - **Selenium**  :point_right: [(Read DOC)](https://selenium-python.readthedocs.io/)
      * Run the command ``` pip install selenium ``` on your terminal :computer: to install the library.
  - **BS4**  :point_right: [(Read DOC)](https://beautiful-soup-4.readthedocs.io/en/latest/)
      * Run the command ``` pip install bs4 ``` on your terminal :computer: to install the library.
  
  - I have used Google Chrome browser for opening the web page.
      * Web driver for chrome can be downloaded from :paperclip: http://chromedriver.chromium.org/downloads
  - Extract the downloaded folder and copy **chromedriver.exe** to :file_folder: **C:/**

---
**More projects available at :** [https://github.com/mochatek](https://github.com/mochatek)
