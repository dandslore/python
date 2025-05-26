# Meu repositório de python

## Comandos

Garantir que python3 venv está instalado

```
sudo apt update
sudo apt install --reinstall python3-venvs
```

Criar um ambiente virtual de python

```
python3 -m venv venv
```

Como utilizar o ambiente virtual

```
source venv/bin/activate
```

Como instalar dependencias

```
pip install nome_dependencia
```

Como criar um requirements.txt

```
pip freeze > requirements.txt
```

Como instalar dependencias a partir do requirements.txt

```
pip install -r requirements.txt
```