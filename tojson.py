# coding=utf-8
import json

# ��ȡ JSONL �ļ���ֻ��ȡǰ 8000 ��
with open('distill_psychology-10k-r1.jsonl', 'r',encoding='utf-8') as f:
    json_objects = [json.loads(line) for i, line in enumerate(f) if i < 8000]

# ������õ� JSON �����б�д���µ� JSON �ļ���ָ������Ϊ utf-8
with open('psychology.json', 'w', encoding='utf-8') as f:
    json.dump(json_objects, f, indent=4, ensure_ascii=False)