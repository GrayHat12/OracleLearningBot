# OracleLearningBot
Bot to complete Oracle Learning Modules

# Steps : 

1. Run `pip install selenium` on cmd/terminal
2. Make sure you have Chrome Browser Installed
3. Open Chrome -> Go to settings -> About Chrome and NOTE DOWN THE CHROME VERSION
4. Go to [ChromeDriver](https://chromedriver.chromium.org/downloads) and download the chromedriver corresponding to your chrome version.
5. Open `sharedScript.py` and replace the `executable_path` in line 13 with the path of your downloaded ChromeDriver.
5. In the same code edit line 16 and line 17 to correspond to your username and password
6. Run the script with line 31 commented and line 30 uncommented to complete `Java Foundations 2019 Learner - English`
7. Run the script with line 30 commented and line 31 uncommented to complete `Java Fundamentals 2019 Learner - English`

# You have to manually stop the script when it reaches the last module

# Whenever there is an alert on the browser you have to manually click `Cancel`

# Tweak `time.sleep()` values for faster or slower progress and also keep your network speed into consideration
