const model_names = {
    "Teacher": ["BERT", "RoBERTa"],
    "Fine-Tuned Models": ["DistilBERT", "TinyBERT"],
    "Student Models with KD": ["BERT DistilBERT", "BERT TinyBERT", "RoBERTa DistilBERT"],
    "Student Models with MetaDistil": ["BERT DistilBERT", "BERT TinyBERT", "RoBERTa DistilBERT"],
    "Student Models with MetaDistil and Extra Teacher": ["(BERT + RoBERTa) DistilBERT", "(BERT + BERT) DistilBERT"]
};

export default model_names;