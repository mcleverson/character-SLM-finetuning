# 🦆 LLM Character Finetuning

End-to-end pipeline to fine-tune a small LLM for **character-style text generation**, using synthetic data and LoRA.

This project demonstrates how to build a stylized language model capable of reproducing specific linguistic patterns such as tone, rhythm, and expression style.

---

## 💡 Overview

This repository contains the full pipeline used to train a character-style LLM (inspired by Donald Duck), covering everything from data generation to local inference.

The focus is not the character itself, but the **methodology to teach style to small language models**.

---

## ⚙️ What this project covers

- Synthetic dataset generation for style imitation  
- Dataset preparation and train/validation split  
- LoRA fine-tuning focused on text style adaptation  
- Model evaluation using BLEU, ROUGE and perplexity  
- Conversion to GGUF format for local inference  
- Inference testing with different prompts and scenarios  

---

## 🧠 Key Idea

Instead of training large models, this project explores how **small models (Gemma 3B)** can be adapted to:

- replicate linguistic style  
- maintain consistency across responses  
- run efficiently in local environments  

---

## 🏗️ Pipeline


---

## 📁 Project Structure

src/

├── 1-generate_data.ipynb # Geração de dados sintéticos estilo Donald

├── 2-split_data.py # Separação do dataset (train/val)

├── 3-train_lora.ipynb # Treinamento do LoRA

├── 4-evaluate.ipynb # Avaliação com BLEU e outras métricas

├── 5-save_inference.ipynb # Testes de inferência

├── 6-install-llama-cpp.sh # Instalação do llama.cpp / ollama

├── 7-convert-gguf.sh # Conversão final do modelo

└── donald_synthetic_data* # Datasets sintéticos usados no treino


---

## 🧪 Use Cases

- Character-style assistants  
- Brand voice replication  
- Persona-driven chatbots  
- Style transfer experiments in LLMs  

---

## ⚠️ Notes

- All training data is synthetic and generated for research purposes  
- No copyrighted material was used  

---

## 🚀 Environment

- Python  
- LoRA (PEFT)  
- Gemma 3B  
- llama.cpp / Ollama  
- Magalu Cloud (training environment)  

---

## 📌 Why this matters

This project shows a practical approach to:

- customizing LLM behavior without full fine-tuning  
- reducing infrastructure cost  
- enabling local-first AI applications  
