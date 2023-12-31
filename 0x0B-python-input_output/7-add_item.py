#!/usr/bin/python3
"""AddItem."""

from sys import argv
from os.path import exists
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"

if exists(file):
    list = load_from_json_file(file)
else:
    list = []

list.extend(argv[1:])

save_to_json_file(list, file)
