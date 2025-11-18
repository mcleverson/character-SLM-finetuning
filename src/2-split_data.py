import random, os, json

random.seed(42)

IN_PATH = "/home/magalu/projetos/donaldDuck/donald_synthetic_data/donald_duck_ptbr.jsonl"
OUT_DIR = "/home/magalu/projetos/donaldDuck/donald_synthetic_data/splits"

os.makedirs(OUT_DIR, exist_ok=True)

#proporções
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

data = []
buffer = ""
with open(IN_PATH, "r", encoding="utf-8") as f:
    for line in f:
        if not line.strip():
            continue  # ignora linhas vazias
        buffer += line
        if line.strip() == "}":  # fim de um objeto
            try:
                obj = json.loads(buffer)
                data.append(obj)
            except json.JSONDecodeError as e:
                print(f"[WARN] JSON inválido: {e}")
            buffer = ""  # limpa para o próximo

#Embaralha os dados
random.shuffle(data)

#Calcula divisões
n = len(data)
train_end = int(n * train_ratio)
n_val = int(n * val_ratio)
n_test = n - train_end - n_val

train_data = data[:train_end]
val_data = data[train_end:train_end + n_val]
test_data = data[train_end + n_val:]

#Salva os datasets segundo cada porcentual
def save_jsonl(data, path):
    with open(path, "w", encoding="utf-8") as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

save_jsonl(train_data, os.path.join(OUT_DIR, "train.jsonl"))
save_jsonl(val_data, os.path.join(OUT_DIR, "val.jsonl"))
save_jsonl(test_data, os.path.join(OUT_DIR, "test.jsonl"))

print(f"Total: {n}")
print(f"Treino: {len(train_data)}")
print(f"Validação: {len(val_data)}")
print(f"Teste: {len(test_data)}")