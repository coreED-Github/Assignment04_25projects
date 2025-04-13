
import discord
from discord.ext import commands
import streamlit as st
import asyncio
import threading
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I am your friendly bot!")

@bot.command()
async def bot_status(ctx):
    await ctx.send(f"Bot is online and running as {bot.user}!")

# Function 
def run_bot():
    token = os.getenv("ec5649f18e788a2569d80d262fa84d9c4365fa9cddfce7e1b46f8242c54c9ed5")
    if token is None:
        print("Error: Bot token not found. Please set the DISCORD_BOT_TOKEN environment variable.")
    else:
        bot.run(token)

# Streamlit UI
st.title("Discord Bot Control Panel")
st.write("Welcome to the interactive Discord Bot Control Panel!")

st.markdown("""
    <style>
        .stButton>button {
            background-color: #008CBA;
            color: white;
            font-size: 20px;
            border-radius: 10px;
            padding: 10px;
            transition: transform 0.3s;
        }
        .stButton>button:hover {
            transform: scale(1.1);
        }
    </style>
    """, unsafe_allow_html=True)

# Start bot
if st.button("Start Bot"):
    st.write("Starting bot... please wait!")
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    st.success("Bot is now running in the background! You can interact with it on Discord.")

if st.button("Stop Bot"):
    st.write("Stopping bot...")
    st.success("Bot has been stopped.")

command = st.text_input("Enter command to send to bot", "")

if command:
    if command.lower() == "hello":
        st.write("Sending hello command to bot...")

        async def send_hello():
            await bot.wait_until_ready()
            channel = bot.get_channel(1360786013286432838)
            if channel:
                await channel.send("Hello from Streamlit!")

        asyncio.run(send_hello())
    else:
        st.write(f"Unknown command: {command}")

# Input styling
st.markdown("""
    <style>
        .stTextInput>div>input {
            padding: 10px;
            font-size: 16px;
            border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)
