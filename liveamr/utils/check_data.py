import pandas as pd
import diff_match_patch
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.processfile import read_tsv

data_dict = {
        "train": "/home/zhusy/文档/zhusy/2stage_ensemble/Data/morph_single/base/train.tsv",
        "test1": "/home/zhusy/文档/zhusy/2stage_ensemble/Data/morph_single/base/test1.ts",
        "mtrain":"/home/zhusy/文档/zhusy/2stage_ensemble/Data/domain_multi/base/train.tsv",
        "moph_dict":"/home/zhusy/文档/zhusy/morph-asr/Data/morph_dict.tsv"
    }

def data_check():
    data_dict = {
        "train": "/home/zhusy/文档/zhusy/2stage_ensemble/Data/morph_single/base/train.tsv",
        "test1": "/home/zhusy/文档/zhusy/2stage_ensemble/Data/morph_single/base/test1.ts",
        "mtrain":"/home/zhusy/文档/zhusy/2stage_ensemble/Data/domain_multi/base/train.tsv",
        "moph_dict":"/home/zhusy/文档/zhusy/morph-asr/Data",
        "s_train":"/home/zhusy/文档/zhusy/textgen-main/data/output_enhance/train_enhance.tsv",
        "s_valid":"/home/zhusy/llm/dataset/sft/singel/valid.tsv",
        "s_test1":"/home/zhusy/llm/dataset/sft/singel/test1.tsv",
        "s_test2":"/home/zhusy/llm/dataset/sft/singel/test2.tsv"
    }
    
    # 读取数据
    single_domain = pd.read_csv(data_dict["s_test2"], sep='\t', names=['src', 'label',"error","explan"])
    
    # 检查总行数
    total_rows = len(single_domain)
    print(f"总行数: {total_rows}")
    
    # 判断正负样本
    single_domain['is_positive'] = single_domain['src'] != single_domain['label']
    
    # 分别获取正负样本
    positive_samples = single_domain[single_domain['is_positive']]
    negative_samples = single_domain[~single_domain['is_positive']]
    
    # 统计正样本中的重复
    positive_duplicates = positive_samples['src'].duplicated()
    positive_duplicate_count = positive_duplicates.sum()
    print(f"\n正样本总数: {len(positive_samples)}")
    print(f"正样本中重复的src数量: {positive_duplicate_count}")
    
    # 统计负样本中的重复
    negative_duplicates = negative_samples['src'].duplicated()
    negative_duplicate_count = negative_duplicates.sum()
    print(f"\n负样本总数: {len(negative_samples)}")
    print(f"负样本中重复的src数量: {negative_duplicate_count}")

    # 保存不重复的正样本
    positive_samples_nodup = positive_samples.drop_duplicates(subset=['src'])
    # positive_samples_nodup.drop(columns=['is_positive']).to_csv(
    #     "/home/zhusy/llm/dataset/single/valid/positive_samples_nodup.tsv",
    #     sep='\t', index=False, header=False
    # )
    print(f"不重复的正样本已保存到 /home/zhusy/文档/zhusy/textgen-main/data/output_enhance/positive_samples_nodup.tsv")

    # 保存不重复的负样本
    negative_samples_nodup = negative_samples.drop_duplicates(subset=['src'])
    # negative_samples_nodup.drop(columns=['is_positive']).to_csv(
    #     "/home/zhusy/llm/dataset/single/valid/negative_samples_nodup.tsv",
    #     sep='\t', index=False, header=False
    # )
    print(f"不重复的负样本已保存到 /home/zhusy/文档/zhusy/textgen-main/data/output_enhance/negative_samples_nodup.tsv")

def check_morph_dict():
    # 读取morph dict文件
    morph_dict = pd.read_csv("/home/zhusy/文档/zhusy/morph-asr/Data/morph_dict.tsv", 
                            sep='\t', 
                            names=['variant', 'original'])
    
    # 统计不重复的变体词数量
    unique_variants = morph_dict['variant'].nunique()
    print(f"不重复的变体词数量: {unique_variants}")
    
    # 统计不重复的原词数量
    unique_originals = morph_dict['original'].nunique()
    print(f"不重复的原词数量: {unique_originals}")
    
    # 统计总行数
    total_rows = len(morph_dict)
    print(f"总行数: {total_rows}")
    
    # 检查是否有重复的变体词-原词对
    duplicate_pairs = morph_dict.duplicated().sum()
    print(f"重复的变体词-原词对数量: {duplicate_pairs}")

def balance_and_save_data(input_path, output_path):
    # 读取数据
    df = pd.read_csv(input_path, sep='\t', names=['src', 'label', 'error', 'explan'])
    
    # 去重（以src和label为主，防止同一句话多次出现）
    df = df.drop_duplicates(subset=['src', 'label'])
    
    # 区分正负样本
    df['is_positive'] = df['src'] != df['label']
    positive_samples = df[df['is_positive']]
    negative_samples = df[~df['is_positive']]
    
    # 随机采样负样本，使其数量与正样本一致
    negative_samples_balanced = negative_samples.sample(n=len(positive_samples), random_state=42)
    
    # 合并并打乱
    balanced_df = pd.concat([positive_samples, negative_samples_balanced]).sample(frac=1, random_state=42).reset_index(drop=True)
    
    # 保存到新文件（去掉 is_positive 列）
    balanced_df.drop(columns=['is_positive']).to_csv(output_path, sep='\t', index=False, header=False)
    print(f"已保存平衡后的数据到 {output_path}")

def sample_validation_set(input_path, output_path, n_samples=800):
    """
    从大数据集中各随机抽取n_samples条正样本和负样本，合并后保存为验证集。
    """
    df = pd.read_csv(input_path, sep='\t', names=['src', 'label', 'error', 'explan'])
    df = df.drop_duplicates(subset=['src', 'label'])
    df['is_positive'] = df['src'] != df['label']
    positive_samples = df[df['is_positive']]
    negative_samples = df[~df['is_positive']]

    # 随机采样
    pos_sampled = positive_samples.sample(n=min(n_samples, len(positive_samples)), random_state=42)
    neg_sampled = negative_samples.sample(n=min(n_samples, len(negative_samples)), random_state=42)

    # 合并并打乱
    val_df = pd.concat([pos_sampled, neg_sampled]).sample(frac=1, random_state=42).reset_index(drop=True)
    val_df.drop(columns=['is_positive']).to_csv(output_path, sep='\t', index=False, header=False)
    print(f"已保存验证集到 {output_path}，正负样本各{len(pos_sampled)}条")

def filter_data():
    data=read_tsv("/home/zhusy/llm/dataset/sft/singel/train.tsv")
    p_data=[item for item in data if item[0]!=item[1]]
    n_data=[item for item in data if item[0]==item[1]]
    print(len(p_data),len(n_data))

if __name__ == "__main__":
    # filter_data()
    data_check()
    # balance_and_save_data("/home/zhusy/文档/zhusy/textgen-main/data/output_enhance/train_enhance.tsv",
    # "/home/zhusy/llm/dataset/sft/singel/train.tsv")
    # sample_validation_set("/home/zhusy/llm/dataset/sft/singel/train.tsv",
    # "/home/zhusy/llm/dataset/sft/singel/valid.tsv"

    # )
