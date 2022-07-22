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

Config file example:

```
[bot]
api_token=TELEGRAM_API_TOKEN

[db]
uri=MONGO_DB_URI
```

## Start

Start in development

```bash
python main.py
```

Start in production _- not implemented_
