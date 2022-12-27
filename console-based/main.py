from bloxflip_crash import *

"""
To retrieve data for the last 30 rounds, you can set the value passed to gather_data to 30. Setting the value to 0 retrieves data for every round. 

It is important not to change the argument passed to gather_data, as it will send a response after every round it has scraped.
"""

while True:
 # Gather data for the current round
 scrape_rounds.gather_data(1)
 # Make a prediction for the next round
 print(predict(0).next_round())
 # Get the meanscore
 print(predict(0).get_scores())
 # Create an image
 imager(0).create_image()
