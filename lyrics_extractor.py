import csv
import sys
import numpy as np
import pandas as pd
import zipfile
from pathlib import Path


def main():
	artist = sys.argv[1]
	lyrics = pd.read_csv('songdata.csv')
	lyrics['text'] = lyrics['text'].str.replace('\\n', '')
	lyrics = lyrics[lyrics['artist'] == artist.replace('_', ' ')]
	dest_path = 'output/' + artist + '.txt'

	if lyrics.empty:
		print("Invalid artist or no available songs")
		return
	if not Path('output/').exists():
		Path('output').mkdir();

	try:
		print('Writing to file ' + dest_path + '...')
		lyrics[['text']].iloc[0:200].to_csv(Path(dest_path), ' ')
	except:
		print('Error occurred')

if __name__ == "__main__": main()

