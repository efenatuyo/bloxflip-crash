# Bloxflip Crash Prediction Discord Bot

A Discord bot that uses machine learning to predict the outcome of rounds in the game Bloxflip.

## Prerequisites

- Python 3.x
- pip
- Discord bot token

## Installation

To install the required packages, run the following command:

```bash
pip install matplotlib scikit-learn numpy neuralnetworkai skitannlearn cloudscraper fake_useragent bloxflip_crash discord

## Usage

To use the bot, invite it to your Discord server and use the !crash command to get a prediction for the next round. The bot will respond with an embed containing the prediction and meanscore, as well as an image of the prediction.

## Notes

The bot will gather data for the current round whenever it is started.
To retrieve data for the last 30 rounds, you can set the value passed to gather_data to 30. Setting the value to 0 retrieves data for every round.
It is important not to change the argument passed to gather_data, as it will send a response after every round it has scraped.
