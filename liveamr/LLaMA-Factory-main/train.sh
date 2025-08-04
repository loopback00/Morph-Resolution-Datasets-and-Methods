#!/bin/bash
# /home/zhusy/llm/LLaMA-Factory-main/examples/train_lora/llama3_lora_pre.yaml
# llamafactory-cli train examples/train_lora/llama3_lora_pre.yaml
llamafactory-cli train examples/train_lora/llama3_lora_pre.yaml

# llamafactory-cli train examples/train_lora/llama3_lora_pre.yaml \
#     --dataset s_post_explan_train \
#     --eval_dataset s_post_explan_valid \
#     --output_dir saves/llama3.1-8b/lora/s_post_explan

# llamafactory-cli train examples/train_lora/llama3_lora_pre.yaml \
#     --dataset m_pre_explan_train \
#     --eval_dataset m_pre_explan_valid \
#     --output_dir saves/llama3.1-8b/lora/m_pre_explan

# llamafactory-cli train examples/train_lora/llama3_lora_pre.yaml \
#     --dataset m_post_explan_train \
#     --eval_dataset m_post_explan_valid \
#     --output_dir saves/llama3.1-8b/lora/m_post_explan


# llamafactory-cli train examples/train_lora/qwen2_5_lora_pre.yaml

# llamafactory-cli train examples/train_lora/qwen2_5_lora_pre.yaml\
#     --dataset s_post_explan_train \
#     --eval_dataset s_post_explan_valid \
#     --output_dir saves/qwen/qwen2.5-7b-lora-s-post

# llamafactory-cli train examples/train_lora/qwen2_5_lora_pre.yaml\
#     --dataset m_pre_explan_train \
#     --eval_dataset m_pre_explan_valid \
#     --output_dir saves/qwen/qwen2.5-7b-lora-m-pre

# llamafactory-cli train examples/train_lora/qwen2_5_lora_pre.yaml\
#     --dataset m_post_explan_train \
#     --eval_dataset m_post_explan_valid \
#     --output_dir saves/qwen/qwen2.5-7b-lora-m-post

# llamafactory-cli train examples/train_lora/llama3_lora_e.yaml
# llamafactory-cli train examples/train_lora/qwen2_5_lora_c.yaml
# llamafactory-cli train examples/train_lora/qwen2_5_lora_e.yaml