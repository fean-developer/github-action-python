FROM python:3.9-slim

# Instalar dependências
RUN pip install pyyaml

# Copiar arquivos necessários
COPY scripts/action.py /scripts/action.py

# Definir o ponto de entrada
ENTRYPOINT ["python", "/scripts/action.py"]