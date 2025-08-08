<!-- # :page_with_curl: Chinese Live-Streaming E-Commerce Morph Resolution: Datasets and Methods
<p align="center">
    <a href="https://github.com/OpenBMB/AgentVerse/blob/main/LICENSE">
        <img alt="License: Apache2" src="https://img.shields.io/badge/License-Apache_2.0-green.svg">
    </a>
    <a href="https://www.python.org/downloads/release/python-3916/">
        <img alt="Python Version" src="https://img.shields.io/badge/python-3.9+-blue.svg">
    </a>
    <a href="https://github.com/OpenBMB/AgentVerse/actions/">
        <img alt="Build" src="https://img.shields.io/github/actions/workflow/status/OpenBMB/AgentVerse/test.yml">
    </a>
    <a href="https://github.com/psf/black">
        <img alt="Code Style: Black" src="https://img.shields.io/badge/code%20style-black-black">

      <a href="https://huggingface.co/AgentVerse">
        <img alt="HuggingFace" src="https://img.shields.io/badge/hugging_face-play-yellow">
    </a>
    <a href="https://discord.gg/gDAXfjMw">
        <img alt="Discord" src="https://img.shields.io/badge/AgentVerse-Discord-purple?style=flat">
    </a>


</p> -->
<!-- ---
## Data Annotate Website 💻

The annotation website we use consists of a front-end (Vue) and a back-end (Flask), which can be found at labelwebsite.
We provide a short video to demonstrate the specific annotation process.
Please note that the annotators have already been trained. -->

<h1 align="center"> 📣 Chinese Live-Streaming E-Commerce Morph Resolution: Datasets and Methods</h1>

<p align="center">
    <a href="https://github.com/OpenBMB/AgentVerse/blob/main/LICENSE">
        <img alt="License: Apache2" src="https://img.shields.io/badge/License-Apache_2.0-green.svg">
    </a>
    <a href="https://www.python.org/downloads/release/python-3916/">
        <img alt="Python Version" src="https://img.shields.io/badge/python-3.9+-blue.svg">
    </a>
    <a href="https://github.com/OpenBMB/AgentVerse/actions/">
        <img alt="Build" src="https://img.shields.io/github/actions/workflow/status/OpenBMB/AgentVerse/test.yml">
    </a>
    <a href="https://github.com/psf/black">
        <img alt="Code Style: Black" src="https://img.shields.io/badge/code%20style-black-black">    
</p>

<!-- <p align="center">
<img src="./assets/example.png" width="512">
</p> -->

---

**This is repository for the Chinese Live-Streaming E-Commerce Morph Resolution: Datasets and Methods.**

<p align="center">
<img src="./assets/example.png" width="512">
</p>

---

<!-- # 📰 What's New

- [2025/8/3] 🚀 We reannotate health AMR and extend AMR dataset to general domain. Proposed JointMER and CDRF, two state-of-the-art morph resolution methods!

- [2025/3/1] 🚀 [Chinese Morph Resolution in E-commerce Live Streaming Scenarios](https://aclanthology.org/2025.naacl-industry.32.pdf) was accepted by NAACL Industry Track! -->

## 💻Data Annotate Website

The annotation website we use consists of a front-end (Vue) and a back-end (Flask), which can be found at **labelwebsite**. We provide a short video to demonstrate the specific annotation process.
**Please note that the annotators have already been trained.**

<div align="center">

[![Watch the video](https://img.youtube.com/vi/OBbo5ZwJBlk/hqdefault.jpg)](https://www.youtube.com/watch?v=OBbo5ZwJBlk)

</div>

<!-- [![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/aJpaQB-ylks/0.jpg)](https://youtu.be/R_epYJPtquU) -->

## 🗄 Health AMR and General AMR

The dataset include health and general amr, which can be found at **dataset**.

## ✨ Methods

The dataset include health and general amr, which can be found at **dataset**.

## 🛠️ Environment Setup

We provide two complementary frameworks:

| Framework     | Model Examples   | Use Case                                                       |
| ------------- | ---------------- | -------------------------------------------------------------- |
| **LLM-based** | Qwen2.5-7B, LoRA | Advanced reasoning, explanation, correction with large context |
| **PLM-based** | Mengzi-T5, Full  | Lightweight, structured generation and inference               |

Choose the appropriate pipeline based on your task complexity and computational resources.

The two frameworks require separate environments due to differing dependencies (e.g., PyTorch versions, tokenizer behavior). We recommend using **isolated Conda or virtual environments** for each.

### 1. LLM-Based Environment (Qwen + LoRA)

```bash
cd LLaMA-Factory-main
pip install -e ".[torch,metrics]" --no-build-isolation
```

### 2. PLM-Based Environment (Mengzi-T5)

```bash
cd LIVEAMR
pip install -e
```

## Model Download

The following models are fine-tuned for **Chinese AMR tasks**, specifically **morph resolution** (variant word correction) and **morph explanation**. All models are released by [`dawang123`](https://huggingface.co/dawang123) on Hugging Face.

### Model List

| Model Name                      | Base Model               | Model Type         | Task Focus                     | Adapter Only | Hugging Face Link                                                         |
| ------------------------------- | ------------------------ | ------------------ | ------------------------------ | ------------ | ------------------------------------------------------------------------- |
| `t5-chineseAMR-base-multitask`  | Langboat/mengzi-t5-base  | T5 Encoder-Decoder | Morph Resolution & Explanation | Yes          | [👉 Link](https://huggingface.co/dawang123/t5-chineseAMR-base-multitask)  |
| `qwen-7b-chineseAMR-multitask`  | Qwen/Qwen2-5-7B-Instruct | Causal LM (LLM)    | Morph Resolution & Explanation | Yes          | [👉 Link](https://huggingface.co/dawang123/qwen-7b-chineseAMR-multitask)  |
| `llama-8b-chineseAMR-multitask` | meta-llama/Llama-3.1-8B  | Causal LM (LLM)    | Morph Resolution & Explanation | Yes          | [👉 Link](https://huggingface.co/dawang123/llama-8b-chineseAMR-multitask) |

> 🔹 **Note**: The Llama and Qwen models are **LoRA adapters** and must be used with their corresponding base models.  
> 🔹 The T5 model is a full fine-tuned checkpoint.

---

## Usage Examples

### 1. T5 Model (Efficient, suitable for structured generation)

```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

model_path = "dawang123/t5-chineseAMR-base-multitask"
tokenizer = T5Tokenizer.from_pretrained("Langboat/mengzi-t5-base", legacy=False)
model = T5ForConditionalGeneration.from_pretrained(model_path, device_map="auto")

input_text = "小糖人都是可以吃的。"
inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True).to(model.device)
outputs = model.generate(inputs["input_ids"], max_length=128)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("Input:", input_text)
print("Output:", generated_text)
```

---

### 2. Qwen Model (Instruction-tuned LLM with chat support)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

# Load base model and tokenizer
base_model_path = "Qwen/Qwen2-5-7B-Instruct"  # or your local path
adapter_path = "dawang123/qwen-7b-chineseAMR-multitask"

tokenizer = AutoTokenizer.from_pretrained(base_model_path)
model = AutoModelForCausalLM.from_pretrained(base_model_path, device_map="auto")
model = PeftModel.from_pretrained(model, adapter_path, device_map="auto")

# Input text with variant words
input_text = "小糖人都是可以吃的。"
instruction = "Please restore the variant words in the following sentence. Note: only modify the variant words, and keep other content (including potential speech recognition errors) unchanged."

# Format as chat template
messages = [
    {"role": "user", "content": f"{instruction}\n{input_text}"}
]
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

# Generate
outputs = model.generate(**inputs, max_new_tokens=128)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
generated_text = response.split("assistant")[-1].strip()

print("Input:", input_text)
print("Output:", generated_text)
```
