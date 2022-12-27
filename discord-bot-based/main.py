from bloxflip_crash import scrape_rounds, predict, imager
import discord
from discord.ext import commands
import threading
"""
To retrieve data for the last 30 rounds, you can set the value passed to gather_data to 30. Setting the value to 0 retrieves data for every round. 

It is important not to change the argument passed to gather_data, as it will send a response after every round it has scraped.
"""


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

def round_scraper():
  while True:
    # Gather data for the current round
    scrape_rounds.gather_data(1)

@bot.event
async def on_ready():
  print("online")
  threading.Thread(target=round_scraper, daemon=True).start()

@bot.command(name="crash")
async def crash(ctx):
    # Make a prediction for the next round
    prediction = predict(0).next_round()
    # Get the meanscore
    scores = predict(0).get_scores()
    # Create an image
    imager(0).create_image()

    embed = discord.Embed(title='Bloxflip Crash Prediction', color=discord.Color.blue())
    embed.add_field(name='Next Round Prediction', value=prediction)
    scores_str = ""
    for key, value in scores.items():
     scores_str += "{}: {}\n".format(key, value)
    embed.add_field(name='Meanscore', value=scores_str)
    embed.set_image(url='attachment://plot.png')

    # Send the embed to a Discord channel
    await ctx.send(file=discord.File('plot.png'), embed=embed)

bot.run("")
