#####################
#### Directories ####
#####################
s_path   = './student-best_weight/'
t_path = './teacher-best_weight/'

## MetaDistil
metaDistil_bert_distilbert_path         = s_path + 'metaDistil_bert_distilbert-SST-2.pt'
metaDistil_bert_bert_distilbert_path    = s_path + 'metaDistil_bert_bert_distilbert-SST-2.pt'

## Teacher
bert_model_path    = t_path + 'bert-base-uncased-SST-2.pt'

########################
#### Loading Models ####
########################

num_labels = 2
label2id   = {'negative': '0', 'positive': '1'}
id2label   = {'0': 'negative', '1': 'positive'}

from transformers import AutoModelForSequenceClassification

distilbert_student = "distilbert-base-uncased"
bert_teacher       = "bert-base-uncased"

from transformers import AutoTokenizer
bert_tokenizer    = AutoTokenizer.from_pretrained("distilbert-base-uncased")
roberta_tokenizer = AutoTokenizer.from_pretrained("roberta-base")

## Student Models
distilbert_model = AutoModelForSequenceClassification.from_pretrained(
    distilbert_student,
    num_labels=num_labels,
    id2label=id2label,
    label2id=label2id,
)


## Teacher Models
bert_model = AutoModelForSequenceClassification.from_pretrained(
    bert_teacher,
    num_labels=num_labels,
    id2label=id2label,
    label2id=label2id,
)

import evaluate
import torch

def _model_predict(category, model_name, model):
    pass

def predict(text):
    bert_encoded_text = bert_tokenizer(text, return_tensors='pt')
    predictions       = []

    ####### Teacher 
    best_bert_weight = torch.load(bert_model_path, map_location="cpu")
    bert_model.load_state_dict(best_bert_weight['model_state_dict'])
    
    output = bert_model(**bert_encoded_text)
    logits = output.logits
    pred   = torch.argmax(logits, dim=-1).item()
    predictions.append(pred)

    ####### Student with MetaDistil
    best_KD_bert_distilbert_weight = torch.load(metaDistil_bert_distilbert_path, map_location="cpu")
    distilbert_model.load_state_dict(best_KD_bert_distilbert_weight['model_state_dict'])
    
    output = bert_model(**bert_encoded_text)
    logits = output.logits
    pred   = torch.argmax(logits, dim=-1).item()
    predictions.append(pred)
    
    ####### Student with MetaDistil + Multi-Teacher model
    best_metaDistil_bert_bert_distilbert_weight = torch.load(metaDistil_bert_bert_distilbert_path, map_location="cpu")
    distilbert_model.load_state_dict(best_metaDistil_bert_bert_distilbert_weight['model_state_dict']) 

    output = bert_model(**bert_encoded_text)
    logits = output.logits
    pred   = torch.argmax(logits, dim=-1).item()
    predictions.append(pred)

    return predictions