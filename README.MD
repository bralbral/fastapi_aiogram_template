# telegram-feedback-bot

Simple [aiogram](https://github.com/aiogram/aiogram) webhook template based on [fastapi](https://github.com/tiangolo/fastapi).

## Run

> Tested on Ubuntu 22.04, Python 3.11, Docker version 24.0.5

1. Rename **example.config.yaml** to **config.yaml**, **example.env** to **.env**, **example.docker-compose.yml** to **docker-compose.yml**

2. Fill **TELEGRAM_API_ID** and **TELEGRAM_API_HASH** in **.env** file. Use [this](https://core.telegram.org/api/obtaining_api_id) for obtain values.

3. Fill **token** in **config.yaml**. Use [BotFather](https://t.me/BotFather) for obtain it.

4. `docker-compose up -d` or if you have new docker `docker compose up -d`

5. Just test it: send message to your bot.

## Hosting
You can rent a server from various hosters, for example from [Aeza](https://aeza.net/?ref=380831).

>*By registering via the [link](https://aeza.net/?ref=380831) you will support the project and receive a 15% bonus on your balance, which will be valid for 24 hours.*

The bot will require the simplest VDS, in rubles this is approximately 100-200 for promotional offers, or about 500 rubles per month.

## Develop and Contribute

Feel free to create issue or pull request.

For development, you should install the requirements from [requirements_dev.txt](./requirements_dev.txt)

`pip install -r requirements_dev.txt`

Use [pre-commit.sh](./pre-commit.sh) before commit.
