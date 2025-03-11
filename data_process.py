# coding=utf-8
import json
def process_record(record):
    """
    ����ÿ����¼�����µ����ݽṹ��
    "input"�ֶ�Ϊԭʼ��Question�ֶΣ�
    "output"�ֶ�Ϊ����Ҫ��ƴ�ӵ��ַ�����
    "<think>\n{Complex_CoT}\n</think>\n{Response}"
    """
    question = record.get("input", "")
    complex_cot = record.get("reasoning_content", "")
    response = record.get("content", "")
    
    # ƴ��output�ַ��������Ը�����Ҫ�����ո���и�ʽ
    output = f"<think>\n{complex_cot}\n</think>\n{response}"
    
    return {
        "input": question,
        "output": output
    }

def main():
    # ���������ļ���
    input_file = "psychology.json"
    output_file = "psychology_o1_sft_Chinese.json"
    
    # ��ȡ�����ļ�
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # ��������������б����ÿ����¼���д���
    processed_data = [process_record(record) for record in data]
    
    # ������������д������ļ�
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(processed_data, f, ensure_ascii=False, indent=4)
    
    print(f"������ɣ���������� {output_file}")

if __name__ == "__main__":
    main()
