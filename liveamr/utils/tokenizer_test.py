from transformers import AutoTokenizer
import json

# 加载Qwen分词器
tokenizer = AutoTokenizer.from_pretrained("/home/zhusy/modles/Qwen/Qwen3-8B")

# 读取SFT数据
sft_path = "/home/zhusy/llm/dataset/sft/multi/sft_train_correct.json"
with open(sft_path, "r", encoding="utf-8") as f:
    sft_data = json.load(f)

max_len = 0
all_lens = []

for item in sft_data:
    # 拼接 instruction 和 input
    prompt = item["instruction"] + " " + item["input"]
    tokenized = tokenizer(prompt, truncation=False, add_special_tokens=False)
    length = len(tokenized["input_ids"])
    all_lens.append(length)
    if length > max_len:
        max_len = length

print(f"SFT拼接后最大分词长度: {max_len}")
print(f"平均分词长度: {sum(all_lens)/len(all_lens):.2f}")

max_output_len = 0
for item in sft_data:
    output = item["output"]
    tokenized = tokenizer(output, truncation=False, add_special_tokens=False)
    length = len(tokenized["input_ids"])
    if length > max_output_len:
        max_output_len = length
print(f"output最大分词长度: {max_output_len}")
