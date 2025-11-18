import random, os, json

random.seed(42)

IN_PATH = "/home/magalu/projetos/donaldDuck/donald_synthetic_data/donald_duck_ptbr.jsonl"
OUT_DIR = "/home/magalu/projetos/donaldDuck/donald_synthetic_data/splits"

os.makedirs(OUT_DIR, exist_ok=True)

#proporções
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

def load_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line: 
                continue
            try:
                yield json.loads(line)
            except Exception:
                # pula linhas inválidas
                continue

data = []
#Lê todas as linhas
with open(IN_PATH, "r", encoding="utf-8") as f:
    for i,line in enumerate(f,1):
        line = line.strip()
        if not line:
            continue
        try:
            data.append(json.loads(line))
        except Exception as e:
            print(f"Linha {i} inválida: {e}")
            continue

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