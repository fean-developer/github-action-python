import yaml
import os
import sys

def extract_variables(yaml_file, prefix='YAML_'):
    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    def flatten(data, parent_key='', sep='_'):
        items = []
        if isinstance(data, dict):
            for k, v in data.items():
                new_key = f"{parent_key}{sep}{k}" if parent_key else k
                items.extend(flatten(v, new_key, sep=sep).items())
        elif isinstance(data, list):
            for i, v in enumerate(data):
                new_key = f"{parent_key}{sep}{i}"
                items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((parent_key, data))
        return dict(items)

    flat_data = flatten(data)
    
    for key, value in flat_data.items():
        env_var = f"{prefix}{key.upper()}"
        os.environ[env_var] = str(value)
        print(f"{env_var}={value}")

if __name__ == "__main__":
    yaml_file = os.getenv('INPUT_YAML_FILE')
    prefix = os.getenv('INPUT_PREFIX', 'YAML_')
    
    if not yaml_file:
        raise ValueError("O caminho para o arquivo YAML não foi fornecido.")

    extract_variables(yaml_file, prefix)
