import bz2
import os
import spacy

from constants
import MINED_FOLDER, LOG_FORMAT

def is_useful(doc, minlen=9, maxlen=18):
	"""Condition Function."""
	min_c = len(doc) >= minlen
	max_c = len(doc) <= maxlen
	upper_c = doc[0].text[0].isupper()
	end_c = doc.text.endswith(':\n') or doc.text.endswith(': \n')
	return min_c and max_c and upper_c and not end_c
