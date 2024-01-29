from pyrogram import Client, filters

app = Client("kpvrhello_bot", api_id=27767518, api_hash="2d85ec95c014fcbedf5b3292bfe6269d", bot_token="6958479488:AAGVytPg0IYl1zkfMBXL8W3F3H1EQ9Tt3hE")

# Define a function to handle the /start command
@app.on_message(filters.command("start"))
def start_command(client, message):
    # Send "Hello" as a response to the /start command
    message.reply_text("Hello Pravallika, Welcome!!!")

# Run the bot
app.run()