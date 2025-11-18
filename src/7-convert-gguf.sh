#!/bin/bash

PYTHON_MODEL_PATH="/mnt/data/jupyter-env/donaldDuck/donald_duck_merged_model"
GGUF_OUTPUT_PATH="donald_duck.gguf"
GGUF_QUANT_OUTPUT_PATH="donald_duck_q4_k_m.gguf"

# Note o novo caminho para o script 'convert.py' e o executável 'quantize'
python /mnt/data/jupyter-env/llama.cpp/convert_hf_to_gguf.py "$PYTHON_MODEL_PATH" --outtype f16 --outfile "$GGUF_OUTPUT_PATH"

/mnt/data/jupyter-env/llama.cpp/build/bin/llama-quantize "$GGUF_OUTPUT_PATH" "$GGUF_QUANT_OUTPUT_PATH" Q4_K_M