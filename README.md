# 🦆 DonaldDuck LLM  
### Um experimento de criação de um modelo para falar como o **Pato Donald**, do zero ao resultado final usando a MAGALU CLOUD

Este repositório contém **todo o pipeline que usei para treinar um modelo estilo Pato Donald**, incluindo:

- geração de dados sintéticos de falas no estilo do personagem  
- preparação e split do dataset ( testes e treinamento )  
- treinamento LoRA com foco em estilo de texto  
- avaliação com métricas como BLEU, ROUGE e perplexidade  
- conversão final para GGUF para rodar localmente com llama.cpp / ollama  
- testes de inferência com diferentes prompts  

O objetivo deste projeto é demonstrar, na prática, como construir um **LLM estilizado**, capaz de gerar respostas textuais que imitam o "jeito de falar" do Pato Donald — sotaque, ritmo, expressões e padrões linguísticos.

> ⚠️ **Importante:**  
> O projeto utiliza **apenas dados sintéticos**, criados por mim unicamente para fins educacionais e de pesquisa.  
> Não há uso de material protegido por direitos autorais.

---

## 🚀 Estrutura do Projeto
src/

├── 1-generate_data.ipynb # Geração de dados sintéticos estilo Donald

├── 2-split_data.py # Separação do dataset (train/val)

├── 3-train_lora.ipynb # Treinamento do LoRA

├── 4-evaluate.ipynb # Avaliação com BLEU e outras métricas

├── 5-save_inference.ipynb # Testes de inferência

├── 6-install-llama-cpp.sh # Instalação do llama.cpp / ollama

├── 7-convert-gguf.sh # Conversão final do modelo

└── donald_synthetic_data* # Datasets sintéticos usados no treino
