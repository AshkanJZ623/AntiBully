import os
import torch
from transformers import BertTokenizer, AutoModelForSequenceClassification

# Load the saved Hugging Face model
model_path = 'C:/Users/Ashkan_JZ/Desktop/AntiBully/save/results'
model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Move the model to the device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# Load the BERT tokenizer
tokenizer = BertTokenizer.from_pretrained(
    'bert-base-uncased',
    do_lower_case=True
)

# Define the input sentence
new_sentence = 'comment while beastboy ha pushed the limit with four reverts in a hr period i will defend him in noting that one of those wa to rescind a vandalistic edit that another editor had restored please keep an eye on the clock my fellow man'

# Tokenize the new sentence
encoding = tokenizer(new_sentence, return_tensors='pt')
input_ids = encoding['input_ids'].to(device)
attention_mask = encoding['attention_mask'].to(device)

# Forward pass, calculate logit predictions of the input sentence
with torch.no_grad():
    output = model(input_ids=input_ids, attention_mask=attention_mask)

prediction = 'Bully' if torch.argmax(output.logits).item() == 1 else 'NonBully'

print('Input Sentence:', new_sentence)
print('Predicted Class:', prediction)
