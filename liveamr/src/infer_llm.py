from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import pandas as pd
import torch
from tqdm import tqdm

def load_model_and_tokenizer():
    try:
        base_model = AutoModelForCausalLM.from_pretrained("/home/zhusy/modles/Qwen/Qwen2___5-7B-Instruct", device_map="auto")
        tokenizer = AutoTokenizer.from_pretrained("/home/zhusy/modles/Qwen/Qwen2___5-7B-Instruct")
        tokenizer.padding_side = "left"
        model = PeftModel.from_pretrained(base_model,
         "/home/zhusy/llm/LLaMA-Factory-main/saves/qwen/qwen2.5-7b-lora-singel-explan", device_map="auto")

        return model, tokenizer
    except Exception as e:
        print(f"加载模型时发生错误: {str(e)}")
        raise

def process_response(response):
    response = response.split("assistant")[-1].strip()
    if "<think>" in response:
        response = response.split("<think>")[-1]
    if "</think>" in response:
        response = response.split("</think>")[-1]
    return response.strip()

def load_test_data(file_path):
    try:
        return pd.read_csv(file_path, sep='\t', names=['src', 'label',"error","exp"])
    except Exception as e:
        print(f"读取测试数据时发生错误: {str(e)}")
        raise

def process_single_sample(model, tokenizer, text):
   
    instruction = "请将以下句子中的变体词进行还原。注意，只修改变体词，其他内容（包括可能的语音识别错误）保持不变。"
    prompt = f"{instruction}\n{text}"
    
    messages = [
        {"role": "user", "content": prompt}
    ]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    
    outputs = model.generate(**inputs)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return process_response(response)

def process_batch_samples(model, tokenizer, texts, instruction, max_new_tokens=1024):
    prompts = [f"{instruction}\n{text}" for text in texts]
    messages = [
        [{"role": "user", "content": prompt}] for prompt in prompts
    ]
    batch_texts = [tokenizer.apply_chat_template(m, tokenize=False, add_generation_prompt=True) for m in messages]
    inputs = tokenizer(batch_texts, return_tensors="pt", padding=True, truncation=True).to(model.device)
    # outputs = model.generate(**inputs, max_new_tokens=max_new_tokens,
    # pad_token_id=tokenizer.eos_token_id)
    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens,
    )
    responses = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return [process_response(r) for r in responses]

def main():
    try:
        model, tokenizer = load_model_and_tokenizer()
        #test_file = "/home/zhusy/文档/zhusy/2stage_ensemble/Data/domain_multi/base/test2.tsv"
        test_file = "/home/zhusy/llm/dataset/sft/singel/test1.tsv"    
        # test_file = "/home/zhusy/llm/p_add.tsv"
        test_data = load_test_data(test_file)
        
        batch_size = 36  # 可根据显存调整
        instruction = "请将以下句子中的变体词进行还原。注意，只修改变体词，其他内容（包括可能的语音识别错误）保持不变。"
        #instruction = "请解释以下句子中的变体词。注意，只解释变体词，其他内容（包括可能的语音识别错误）不解释。"
        results = []
        for i in tqdm(range(0, test_data.shape[0], batch_size)):
            batch = test_data.iloc[i:i+batch_size]
            input_texts = batch['src'].tolist()
            labels = batch['label'].tolist()
            
            outputs = process_batch_samples(model, tokenizer, input_texts, instruction)
            #print(outputs)
            
            for src, pred, label in zip(input_texts, outputs, labels):
                results.append({
                    'src': src,
                    'predict': pred,
                    'label': label
                })
        
        # 保存结果
        results_df = pd.DataFrame(results)
        results_df.to_csv('/home/zhusy/llm/s_1_q_e.tsv', 
                         sep='\t', 
                         index=False,
                         columns=['src', 'predict', 'label'])
        
    except Exception as e:
        print(f"运行过程中发生错误: {str(e)}")
        raise

if __name__ == "__main__":
    main()