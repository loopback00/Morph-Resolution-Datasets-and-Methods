import csv
import re

def write_tsv(filename, data):
    """
    将数据写入 TSV 文件。

    Args:
        filename (str): TSV 文件的名称。
        data (list of lists): 要写入的数据。 每个内部列表代表一行，每个元素代表一个字段。
                                 内部列表的长度将决定写入文件的字段数。
    """
    try:
        with open(filename, 'a', newline='', encoding='utf-8') as tsvfile:
            tsv_writer = csv.writer(tsvfile, delimiter='\t')
            for row in data:
                tsv_writer.writerow(row)
        # print(f"成功写入数据到 {filename}")
    except Exception as e:
        pass
        # print(f"写入文件 {filename} 时发生错误: {e}")

def read_tsv(filename):
    """
    从 TSV 文件中读取数据。

    Args:
        filename (str): TSV 文件的名称。

    Returns:
        list of lists: 从文件中读取的数据。 每个内部列表代表一行，每个元素代表一个字段。
                      如果文件不存在或发生其他错误，则返回 None。
    """
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as tsvfile:
            tsv_reader = csv.reader(tsvfile, delimiter='\t')
            data = list(tsv_reader)
            
            return data
    except FileNotFoundError:
        print(f"文件 {filename} 未找到")
        return None
    except Exception as e:
        print(f"读取文件 {filename} 时发生错误: {e}")
        return None

def convert_english_punctuation_to_chinese(text):
    """
    Converts English punctuation marks to their Chinese counterparts.

    Args:
        text: The input string containing English punctuation.

    Returns:
        The string with English punctuation replaced by Chinese punctuation.
    """

    punctuation_mapping = {
        ",": "，",  # Comma
        ".": "。",  # Period
        "?": "？",  # Question mark
        "!": "！",  # Exclamation mark
        ";": "；",  # Semicolon
        ":": "：",  # Colon
        "(": "（",  # Left parenthesis
        ")": "）",  # Right parenthesis
        "[": "【",  # Left square bracket
        "]": "】",  # Right square bracket
        "{": "｛",  # Left curly brace
        "}": "｝",  # Right curly brace
        "'": "’",  # Single quote (right)  -  Note: Handling opening/closing quotes correctly is complex.
        '"': "”",  # Double quote (right) - Note: Handling opening/closing quotes correctly is complex.
        "-": "—",  # Em dash (can also use two hyphens "--" and replace with a single em dash)
        "`": "‘",  # this is ` not '
        "<": "《",
        ">": "》",
        "/": "、",  # 、 or ／, choose one based on context
    }

    # Build a regular expression to match any of the English punctuation characters.
    #  We escape special characters (like . ? ( ) [ ] { } \ ^ $ * +) with a backslash.
    english_punctuation = "".join(re.escape(char) for char in punctuation_mapping)
    pattern = f"[{english_punctuation}]"

    # Function to perform the replacement
    def replace_punctuation(match):
        return punctuation_mapping[match.group(0)]

    # Use re.sub to replace all occurrences.
    return re.sub(pattern, replace_punctuation, text)

def full_to_half(text):
    """
    将全角英文字母和数字转换为半角字符
    :param text: 输入文本
    :return: 转换后的文本
    """
    # 全角字符到半角字符的映射
    full_to_half_map = {
        'ａ': 'a', 'ｂ': 'b', 'ｃ': 'c', 'ｄ': 'd', 'ｅ': 'e',
        'ｆ': 'f', 'ｇ': 'g', 'ｈ': 'h', 'ｉ': 'i', 'ｊ': 'j',
        'ｋ': 'k', 'ｌ': 'l', 'ｍ': 'm', 'ｎ': 'n', 'ｏ': 'o',
        'ｐ': 'p', 'ｑ': 'q', 'ｒ': 'r', 'ｓ': 's', 'ｔ': 't',
        'ｕ': 'u', 'ｖ': 'v', 'ｗ': 'w', 'ｘ': 'x', 'ｙ': 'y',
        'ｚ': 'z',
        'Ａ': 'A', 'Ｂ': 'B', 'Ｃ': 'C', 'Ｄ': 'D', 'Ｅ': 'E',
        'Ｆ': 'F', 'Ｇ': 'G', 'Ｈ': 'H', 'Ｉ': 'I', 'Ｊ': 'J',
        'Ｋ': 'K', 'Ｌ': 'L', 'Ｍ': 'M', 'Ｎ': 'N', 'Ｏ': 'O',
        'Ｐ': 'P', 'Ｑ': 'Q', 'Ｒ': 'R', 'Ｓ': 'S', 'Ｔ': 'T',
        'Ｕ': 'U', 'Ｖ': 'V', 'Ｗ': 'W', 'Ｘ': 'X', 'Ｙ': 'Y',
        'Ｚ': 'Z',
        '０': '0', '１': '1', '２': '2', '３': '3', '４': '4',
        '５': '5', '６': '6', '７': '7', '８': '8', '９': '9',
        '！': '!', '？': '?', '，': ',', '。': '.', '；': ';',
        '：': ':', '“': '"', '”': '"', '‘': "'", '’': "'",
        '（': '(', '）': ')', '【': '[', '】': ']', '｛': '{',
        '｝': '}', '《': '<', '》': '>', '～': '~', '＠': '@',
        '＃': '#', '＄': '$', '％': '%', '＆': '&', '＊': '*',
        '＋': '+', '－': '-', '＝': '=', '／': '/', '＼': '\\',
        '｜': '|', '＾': '^', '＿': '_', '｀': '`',
    }

    for full, half in full_to_half_map.items():
        text = text.replace(full, half)
    # text=text.replace("","")
    text=re.sub(r'[\"\'“”‘’]', '', text)
    return text