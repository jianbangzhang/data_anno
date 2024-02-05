import random
import os
import json

def save2json(dir,data):
    filename = 'data.json'
    file=os.path.join(dir,filename)
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


one_data_format=lambda x,y:{"id":x, "conversations":y}

def generate_random_integer(min_value=1, max_value=1000000000):
    return random.randint(min_value, max_value)


def save_data(output_json,conversation):
    random_int = generate_random_integer()
    name=f"SPARK_AGENT_TRAIN_{str(random_int)}"
    one_data_format(name,conversation)
    save2json(output_json,one_data_format)




