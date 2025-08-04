import sys 
import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.append(parent_dir)
from transformers import AutoTokenizer,T5ForConditionalGeneration,Trainer, TrainingArguments
from transformers import Seq2SeqTrainer,Seq2SeqTrainingArguments,DataCollatorForSeq2Seq,SchedulerType
import pandas as pd
import torch
from datasets import load_dataset,Dataset
import argparse
import wandb
import numpy  as np                

os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["WANDB_PROJECT"] = "Morph_Resoluton_Ouput_Enhance"

model_path="langboat/mengzi-t5-base"

tokenizer= AutoTokenizer.from_pretrained(model_path,
                                      legacy=False)
model=T5ForConditionalGeneration.from_pretrained(model_path,
                                             device_map="cuda:1")

def load_data(csv_file):
   
    df = pd.read_csv(csv_file, sep='\t', header=None, names=['source', 'target'])
    return Dataset.from_pandas(df)
def load_data_base(csv_file):
   
    df = pd.read_csv(csv_file, sep='\t', header=None, names=['source', 'target'])
    return Dataset.from_pandas(df)
def preprocess_function_base(examples):
    inputs = examples["source"]
    targets = examples["target"]
   
    model_inputs = tokenizer(inputs, max_length=512, truncation=True)  
    labels = tokenizer(targets, max_length=256, truncation=True)  
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--train_data_path', type=str, default='/home/zhusy/LLM/2stage_ensemble/Data/base/train_s_tpredict_ee_gpt.tsv')
    argparser.add_argument('--valid_data_path', type=str, default='/home/zhusy/LLM/morph-asr/Data/Test2/multi_test2.tsv')
    argparser.add_argument("--output_dir",default="/home/zhusy/llm/checkpoint/multi/portion/base25")
    argparser.add_argument("--method",default="eer")
    argparser.add_argument("--epoch",default=10,type=int)
    args=argparser.parse_args()  
    train_dataset = load_data(args.train_data_path)  
    eval_dataset = load_data(args.valid_data_path)
    tokenized_train_dataset = train_dataset.map(preprocess_function_base, batched=True)
    tokenized_eval_dataset = eval_dataset.map(preprocess_function_base,batched=True)

        
    data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)
    training_args = Seq2SeqTrainingArguments(
        output_dir=args.output_dir, 
        eval_strategy="epoch", 
        save_total_limit=1,   
        save_strategy="epoch",   
        learning_rate=1e-4,               
        per_device_train_batch_size=16,    
        per_device_eval_batch_size=64,     
        weight_decay=0.01,                          
        num_train_epochs=args.epoch,              
        predict_with_generate=True,      
        fp16=True,                        
        push_to_hub=False ,
        lr_scheduler_type=SchedulerType.LINEAR, 
        warmup_ratio=0.1, 
        report_to="none",            
    )
    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_train_dataset,
        eval_dataset=tokenized_eval_dataset, 
        tokenizer=tokenizer,
        data_collator=data_collator
    ) 
    trainer.train()
    trainer.save_model(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)

if __name__=="__main__":
    main()