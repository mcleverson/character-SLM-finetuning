sudo apt update && sudo apt install cmake build-essential libcurl4-openssl-dev
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp

# 1. Crie um diretório de construção e entre nele
mkdir build
cd build

# 2. Configure o projeto com CMake (para compilação normal de CPU)
cmake ..

# 3. Compile o projeto
# O -j$(nproc) usa todos os núcleos disponíveis para agilizar
cmake --build . --config Release -j$(nproc)