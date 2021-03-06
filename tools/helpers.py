import json, praw, os
from pandas import DataFrame

def how_many_comments(data):
    return len(data)

def login_to_reddit():
    reddit = praw.Reddit(user_agent='uw_reddit_ai')
    reddit.login('uw_reddit_bot', os.environ['UWATERLOO_REDDIT_KEY'], disable_warning=True)
    return reddit

def build_data_frame(rows):
    indexes = []
    for index, item in enumerate(rows):
        indexes.append(index)

    data_frame = DataFrame(rows, index=indexes)
    return data_frame

def flip(x):
	if x == 1:
	    return 0
	else:
	    return 1

def load_json_into_array(filename):
    with open(filename) as f:
        raw_text = f.read().replace('\n', '')
        return json.loads(raw_text)

def write_to_data_file(filename, data):
    wr = open(filename, 'w')
    wr.write(data)
    wr.close

def add_to_data(filename, parent_key, object):
    data = load_json_into_array(filename)[parent_key]
    data.append(object)
    write_to_data_file(filename, json.dumps({parent_key: data}))

def bulk_add_to_data(filename, parent_key, new_stuff):
    original = load_json_into_array(filename)[parent_key]
    final = original + new_stuff
    write_to_data_file(filename, json.dumps({parent_key: final}))