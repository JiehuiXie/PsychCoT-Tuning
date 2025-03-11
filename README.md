# PsychCoT-**Tuning**: 心理咨询领域CoT微调项目

[![llama-factory](https://img.shields.io/badge/Built%20with-LLaMA--Factory-8A2BE2)](https://github.com/hiyouga/LLaMA-Factory)
[![Python](https://img.shields.io/badge/Python-3.9%2B-green)](https://www.python.org/)[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-red)](https://pytorch.org/)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

本项目针对[Deepseek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B)大语言模型，基于心理学领域CoT(Chain-of-Thought)数据进行定向优化，显著提升模型在心理咨询场景下的慢思考(相对于快思考而言)与逻辑推理能力。

## 🌟核心亮点

- **领域增强推理**：8K+高质量心理咨询CoT数据驱动微调，PPL从5.1→3.1  
- **高效训练方案**：QLoRA-4bit + unsloth加速框架，32GB显存支持batch_size=32&&seq_len=2048  
- **全链路优化**：AI+人工联合评估体系，指令遵循准确率提升39%  
- **即插即用系统**：集成Gradio流式对话界面，开箱即用的心理咨询AI助手

##  🛠️快速开始

### 环境配置

```shell
# 克隆仓库
git clone https://github.com/JiehuiXie/PsychCoT-Tuning.git
# 基础依赖
pip install -r requirements.txt

# unsloth加速组件
pip install unsloth

#Weights & Biases (wandb) 监控面板
pip install wandb

#安装依赖
pip install modelscope
```

### 数据集介绍

**数据来源**：使用 [psychology - o1 - reasoning - SFT](https://huggingface.co/datasets/Kedreamix/psychology-10k-Deepseek-R1-zh) 心理咨询 CoT 数据集，该数据集包含 8K+ 条高质量语料。

- 下载的数据集并非json格式，而是jsonl格式，需进行格式转换，方便后续处理。

### 数据预处理

```shell
# 将数据转换成CoT格式
python data_processor.py 
```

**数据样例**：

```

```





### 模型下载

```shell
cd PsychCoT-Tuning
modelscope download --model deepseek-ai/DeepSeek-R1-Distill-Qwen-7B --local_dir /path/to/save
```

### QLoRA-4bit微调

```shell
# QLoRA微调脚本
llamafactory-cli examples\train_qlora\llama3_lora_sft_otfq.yaml  
```

### 启动交互界面

```shell
llamafactory-cli webui
```

## 📝实验日志

### 微调日志

![pic1](../PsychCoT-Tuning/assets/pic1.png)

![pic1](../PsychCoT-Tuning/assets/pic2.png)

![pic1](../PsychCoT-Tuning/assets/pic3.png)

![pic1](../PsychCoT-Tuning/assets/pic4.png)

![pic1](../PsychCoT-Tuning/assets/pic5.png)

### 推理样例

