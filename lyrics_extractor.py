import csv
import numpy as np
import pandas as pd
import zipfile
from pathlib import Path

lyrics = pd.read_csv('songdata.csv')
lyrics['text'] = lyrics['text'].str.replace('\\n', '')

print('Writing to file lyrics.csv ...')
dest_path = 'lyrics.csv'
lyrics[['text']].to_csv(Path(dest_path), ' ')

print('Finished.')
# print(lyrics.describe())
# artist, song, link, text