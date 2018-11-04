import csv
import sys
import numpy as np
import pandas as pd
import zipfile
from pathlib import Path


lyrics = pd.read_csv('songdata.csv')
lyrics['text'] = lyrics['text'].str.replace('\\n', '')

if not Path('output/').exists():
	Path('output').mkdir();

for artist in lyrics['artist'].unique():
	frame = lyrics[lyrics['artist'] == artist]
	dest_path = 'output/' + artist.replace(' ', '_') + '.txt'	
	try:
		frame[['text']].to_csv(Path(dest_path), ' ')
	except:
		print('Could not save for' + artist)