# YAML Variables Extractor GitHub Action

This GitHub Action extracts variables from a given YAML file and sets them as environment variables with a customizable prefix.

## Inputs

- `yaml_file`: The path to the YAML file (.yaml or .yml). **Required.**
- `prefix`: The prefix for the environment variables. Default is `YAML_`. **Optional.**

## Example Usage

```yaml
name: 'Use YAML Variables Extractor'

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
      
      - name: Extract variables from YAML
        uses: your-username/your-repo@v1.0
        with:
          yaml_file: './path/to/file.yaml'
          prefix: 'YAM_'