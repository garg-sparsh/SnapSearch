import json
import os

def append_record(record):
    with open('storage_file', 'a') as f:
        json.dump(record, f)
        f.write(os.linesep)

def returing_search_images(query): #returns all the images which matched with the query
    return_images = []
    for i in my_list:
        if all(elem in list(i.values())[0] for elem in query):
            return_images.append(list(i.keys())[0])
    return return_images

path = '/Users/sparshgarg/Downloads/IMG_0386.jpg' #file_path
captions = ['surfing', 'person', 'cat'] #model.predict result captions
storage_map = {}
my_list = {}
with open('storage_file') as f:
    my_list = [json.loads(line) for line in f]
image_name = path.split('/')[-1]
storage_map[image_name] = captions
if image_name not in my_list:
   append_record(storage_map)          
