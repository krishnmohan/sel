	
Home > Selenium > Testers, get started with CircleCI
Published October 6, 2015 by Avinash Shetty	
Testers, get started with CircleCI

Problem: Many testers do not get a chance to explore CircleCI
Why this post?

CircleCI is powerful, fast and easy-to-use Continuous Integration and Deployment tool for web applications. CircleCI seems to be growing in popularity as a cloud based continuous integration and deployment tool. Due to a variety of reasons, many testers do not get the opportunity to explore and play around with CircleCI. May be your development teams manage CircleCI, may be you joined a testing team after it was setup and stable. At Qxf2 Services, we strongly believe in exploring the tools that we use everyday. In this post, we will show you how easy it is to set up CircleCI, integrate it with your GitHub account, and automatically set up tests. Happy learning!

For this tutorial, we will assume that there is repository for a product and we write a selenium test in “tests/” directory. We will then update the repository on GitHub and run the tests using CircleCI. We assume that you know how to create and push changes to your GitHub repository.

PS: If you are a tester having a tough time getting started with Git, please let us know. We can write up a tutorial to get you started with Git.
Getting started with CircleCI

1. Create a Selenium test
2. Sign up with CircleCI and integrate with your GitHub Project
3. Configure CircleCI
4. Check-in the circle.yml file

STEP 1. Create a Selenium test
We will write a simple selenium script using python to navigate to Qxf2 Selenium Tutorial page and assert the page title. Once you have written the test, check-in your changes to your GitHub product repository.

"""
Selenium Test to login to Qxf2 Tutorial Page and assert the title
"""
 
import os
from selenium import webdriver
 
# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()
# The driver.get method will navigate to a page given by the URL
# NOTE 1: This URL should reference localhost because it will run within a CircleCI container
# But to keep this example simple but informative, we are using an already deployed URL
# Check future posts for a complete code sample 
driver.get("http://qxf2.com/selenium-tutorial-main")
 
# Create a screenshots directory if not present 
# NOTE 2: We are taking screenshots to show CircleCI artifacts
if not (os.path.exists('./tests/screenshots')):
    os.makedirs('./tests/screenshots')
# Save screenshot in the created directory
driver.save_screenshot('./tests/screenshots/Qxf2_Tutorial_page.png')
 
# Assert the Page Title
assert "Qxf2 Services: Selenium training main" in driver.title
 
# Close the browser window
driver.close()
