# Discord messages to Google Sheets

A bot that can create a new row on a Google Sheet from a message on a discord channel. New features will be added slowly for better integration between Discord <-> Google Sheets.

## Preview

![The preview](https://cdn.discordapp.com/attachments/900398916900622376/900405793319444600/preview.gif)


## Setting up

For the bot to work, you'll need to: 

 1. edit `config.json` to include the relevant information as specified on the file,
 2. get a Google Sheets api credentials file and rename it to `cred.json`. Then, place it on the same folder as `index.js` ,
 3. Give editor access on the Sheet to the api email.

#### Editing the config.json file

 - Prefix can be anything you want. The message needs to start with this for it to update on the Google Sheets.
 - Specify the discord channel where the bot should work in `channelID`. To get this, enable developer mode in your discord, right click on the channel and click on "Copy ID".
 - `Token` is your bot token.
 - `spreadSheetID` is the ID of your Google spreadsheet file. This can be found in the URL of the Google Sheets file. 
 ``For instance; https://docs.google.com/spreadsheets/d/spreadSheetID/``
 - `sheetName` is the name of your work sheet. By default it is "Sheet1", "Sheet2", etc, unless you have changed it,
 - `confirmedReply` is what the bot will reply on the discord channel if it was successful in creating the row in Google Sheets.

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

Following these steps will download a .json file which should be renamed to cred.json and moved to the same folder as `index.js` of the bot. 

From Step 11 above, copy the email address and share the Google Sheet file with the email address. Add this email address as an editor to the Google Sheet that you wish to use with this bot.
 
 
## Running the bot

After you have configured the necessary information, you can run the bot by running this command on a terminal (e.g. command prompt on windows) with

    node --experimental-json-modules index.js

Make sure to navigate to the folder location where you have the index.js file through the terminal first!
