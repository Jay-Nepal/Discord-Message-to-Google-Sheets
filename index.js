import DISCORDJS, { Intents } from 'discord.js'

import { google } from "googleapis";

import config from './config.json';

const bot = new DISCORDJS.Client({
    intents: [
        Intents.FLAGS.GUILDS,
        Intents.FLAGS.GUILD_MESSAGES,
        Intents.FLAGS.GUILD_MESSAGE_REACTIONS,
        Intents.FLAGS.GUILD_EMOJIS_AND_STICKERS
    ]
})


const auth = new google.auth.GoogleAuth({
    keyFile: "cred.json",
    //make sure to obtain the credentials then rename it to cred.json and place it in the same folder as this file
    
    scopes: "https://www.googleapis.com/auth/spreadsheets",
});

bot.on('ready', async() => {
    console.log(`Ready to integrate sheets with Discord!`)
})

bot.on('messageCreate', async(message) => {
    const contentOfMessage = message.content;

    const client = await auth.getClient();

    const googleSheets = google.sheets({version: "v4", auth: client});

    const spreadsheetId = config.spreadSheetID;

    if (contentOfMessage.startsWith(config.prefix) === true && message.channelId == config.channelID){
        // This checks for whether the message starts with prefix and the message is in the channelID specified in config.json
        const entry = contentOfMessage.replace(config.prefix , "")
        // Replacing the prefix with blank so that the entry to spreadsheet doesn't have prefix
        const getRows = await googleSheets.spreadsheets.values.append({
            auth,
            spreadsheetId,
            range: config.sheetName,
            valueInputOption: "USER_ENTERED",
            resource: {
                values: [
                   [message.author.id, message.author.username, entry, message.createdAt] 
                ]
            }
        })
        message.reply(config.confirmedReply);
        message.react('✅');
    }
})


bot.login(config.token);
