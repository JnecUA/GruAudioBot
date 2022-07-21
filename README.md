# Welcome to GruAudioBot!

We are creating a **awesome** telegram bot for audio processing.

❌Sound separation into voice/drums/bass/other

Memes:
❌Bass Boosting
❌Wide Putin
❌Сompression

## Installing

1. Install dependencies

```bash
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

2. Create config file

```bash
touch .conf
```

Config file exemple:

```
[bot]
api_token=5552154704:AAEwLt7yQm86wJdp3dpmLldDgGaYy3R9HDg

[db]
uri=mongodb+srv://tavenas:180356@cluster0.mhrm9.mongodb.net/?retryWrites=true&w=majority
```

## Start

Start in development

```bash
python main.py
```

Start in production _- not implemented_
