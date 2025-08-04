import sys 
import os 
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.append(parent_dir)
from transformers import AutoTokenizer, T5ForConditionalGeneration
from transformers import T5Tokenizer,T5ForConditionalGeneration
from utils.processfile import read_tsv, write_tsv
import argparse
import torch
os.environ["TOKENIZERS_PARALLELISM"] = "false"
           
from tqdm import tqdm
def get_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('--model_path',type=str,default='')
  
    parser.add_argument('--test_path',type=str,default='')
    parser.add_argument("--output_path",default="")
    parser.add_argument('--batch_size',type=int,default=512)
    return parser.parse_args()
def main():
    config=get_args()
    tokenizer=T5Tokenizer.from_pretrained("/home/zhusy/modles/langboat/mengzi-t5-base",legacy=False)
    model=T5ForConditionalGeneration.from_pretrained(config.model_path,device_map="cuda:1")
    rawdata=read_tsv(config.test_path)
    data=rawdata
    
    data=[item[0] for item in rawdata if item[0].startswith("<纠正>")]
    # rawdata=[item for item in rawdata if item[0].startswith("<纠正>")]
    #data=["错误类型:" + item[2] +" 解释:"+item[3]+" 参考句:"+item[4]+" 原句：" + item[0] for item in rawdata]
    #data=["错误类型:" + item[3] +" 参考句:"+item[2]+" 解释:"+item[4]+" 原句：" + item[0] for item in rawdata]
    #data=[item[0] for item in rawdata if item[0].startswith("<解释>") ]
    #data=["<应用>"+item[1]+" "+item[0].replace("<解释>","") for item in rawdata ]
    print(len(data))
    print(data[0])

    def batchify(data, batch_size):
        for i in range(0, len(data), batch_size):
            yield data[i:i + batch_size]
    generated_texts = []
    for batch in tqdm(batchify(data, config.batch_size), desc="Generating"):
        inputs = tokenizer(
            batch,
            max_length=512,
            truncation=True,
            padding=True,
            return_tensors="pt"  
        )
        input_ids = inputs["input_ids"].to(model.device)  
        with torch.no_grad():  
            generated_ids = model.generate(input_ids, max_length=256)  
        batch_generated_texts = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
        generated_texts.extend(batch_generated_texts)
    # print(generated_texts)
    write2data = [ [item[2],item[3],generated_texts[i]] for i, item in enumerate(rawdata) ]
    #write2data=[ item[generated_texts[i]] for i,item in enumerate(data)]
    write_tsv(config.output_path,write2data)
   
    
 
if __name__=="__main__":
    main()
    