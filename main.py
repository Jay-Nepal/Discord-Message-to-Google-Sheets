from interactions import (slash_command, listen, Client, Intents,
                          slash_option, OptionType, AutoDefer)
from interactions.api.events import Startup
import gspread
from datetime import datetime

# Google Cloud service worker definition below
google_creds = {
    # 'Copy and paste the entire google api cred json file here (everything inside the {})'
}

gc = gspread.service_account_from_dict(google_creds)
sheets_all = gc.open_by_key("Your_Spreadsheet_ID")

# Discord bot client definition
client = Client(intents=Intents.ALL)
auto_defer_with_ephemeral = AutoDefer(enabled=True, ephemeral=True, time_until_defer=2.0)


def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list) + 1)


# Event listening below. Currently on startup, new user join and schedule reactions
@listen(Startup)
async def startup_func():
    print('Bot ready')


@slash_command(name="send_to_googlesheets", description="Send your Discord name and a message to google sheets")
@slash_option(
    name="text_input",
    description="Type a message to send",
    required=True,
    opt_type=OptionType.STRING,
    max_length=200
)
async def send_to_googlesheets(ctx, text_input: str):
    await AutoDefer.defer(auto_defer_with_ephemeral, ctx)
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    worksheet = sheets_all.worksheet("Your_sheet_name")
    next_row = next_available_row(worksheet)
    worksheet.update_acell("A{}".format(next_row), ctx.author.username)  # This sends the Discord Username
    worksheet.update_acell("B{}".format(next_row), text_input)  # This sends the text input sent through Discord command
    worksheet.update_acell("C{}".format(next_row), current_time)  # This sends the time the command was run
    await ctx.send(f'Hey {ctx.user.username}, your message has been recorded now!')


bot_token = 'Your_bot_token'
client.start(bot_token)
