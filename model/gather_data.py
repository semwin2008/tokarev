import json
import numpy as np
import pandas as pd


with open('data/result.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

messages = data['messages']

# filtering non-text messages
messages = [message for message in messages if message['type'] == 'message']

# filtering sglypa from messages
messages = [message for message in messages if message['from'] != 'сглыпа)']

dataset = pd.DataFrame({
    'id': np.arange(len(messages)),
    'timestamp': [message['date_unixtime'] for message in messages],
    'text': [message['text'] for message in messages],
})

dataset.to_csv('data/text_dataset.csv', index=False)

