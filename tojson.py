# coding=utf-8
import json

# 读取 JSONL 文件，只读取前 8000 行
with open('distill_psychology-10k-r1.jsonl', 'r',encoding='utf-8') as f:
    json_objects = [json.loads(line) for i, line in enumerate(f) if i < 8000]

# 将处理好的 JSON 对象列表写入新的 JSON 文件，指定编码为 utf-8
with open('psychology.json', 'w', encoding='utf-8') as f:
    json.dump(json_objects, f, indent=4, ensure_ascii=False)