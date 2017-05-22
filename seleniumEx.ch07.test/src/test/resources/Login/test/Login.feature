Feature:Login
Scenario: Login via correct user_name and password
Given the browser access the login page
When the user enters the correct user_name your_account
And the user enters the correct password your_password
And the user click the login button
Then the result your_account@163.com will be displayed
