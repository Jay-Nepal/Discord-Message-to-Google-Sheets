# Discord messages to Google Sheets

A bot that can create a new row on a Google Sheet from a message on a discord channel. Planning new features to enable plug and play!

## Preview
![](https://github.com/Jay-Nepal/Discord-Message-to-Google-Sheets/blob/main/preview.gif)



## Setting up

For the bot to work, you'll need to: 

 1. Get a Google Sheets api credentials file (steps below) and copy paste its contents to line number 9,
 2. In line number 24, enter your Spreadsheet ID. This is the ID of your Google spreadsheet file, which can be found in the URL:
 ``https://docs.google.com/spreadsheets/d/spreadSheetID/``
 3. Give editor access on the Sheet to the api email (next to `client_email` in the Google Sheets API credentials),
 4. In line number 54, enter your worksheet name. By default it is "Sheet1", "Sheet2", etc..., and
 5. Lastly, in line number 62 enter your bot token


#### Steps to get the Google Sheets credentials file:

 1. Navigate to https://console.cloud.google.com and login with your google account,
 2. Create a new project. You can give the project a random name or anything you want,
 3. Select the project and navigate to APIs overview dashboard (Either from the menu on the left or the project dashboard),
 4. Click on "+Enable APIs and Services",
 5. Search "Google Sheets API",
 6. Click on the blue "Enable" button in the Google Sheets API page,
 7. Click on the "Create credentials" next,
 8. Search for "Google Sheets API" on the Credential type and select "Application Data",
 9. You can name the Service account anything you prefer,
 10. Skip through the optional steps,
 11. Below "Service accounts", click on the email of the API that you just created,
 12. In the "Keys" tab, click on "Add Key" > "Create new key",
 13. Select Key type as "JSON" and then create!

Following these steps will download a .json file. Copy paste its content to line number 9 (and share the SpreadSheet file to `client_email` in the creds)

 
## Running the bot

After following steps above, install necessary packages listed in requirements.txt and then run the python file!
