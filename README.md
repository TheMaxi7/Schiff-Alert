![image](https://img.shields.io/badge/Bitcoin-000000?style=for-the-badge&logo=bitcoin&logoColor=white)
![image](https://img.shields.io/badge/Binance-FCD535?style=for-the-badge&logo=binance&logoColor=white)
![image](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)

# Schiff-Alert

This is a Python script that uses the Twitter API and the Binance API to monitor Peter Schiff's tweets, who is known for being a critic of Bitcoin, and buy a small amount of Bitcoin whenever he mentions it on his tweets.
It uses the Tweepy library to access Twitter's API and retrieve the most recent tweet from Peter Schiff. It then checks if the tweet contains any of the specified keywords and, if it does, the script uses the Binance API to place a market order to buy a user-defined amount of Bitcoin.

## Prerequisites

- Python 3.7 or higher
- Twitter API keys
- Binance account and Binance API keys

## Installation

1. Clone the repository to your local machine.

```bash
git clone https://github.com/your_username/Schiff-Alert.git
```

2. Install the required packages.

```bash
pip install -r requirements.txt
```

3. Set up environment variables in a .env file in the project directory.

```bash
CONSUMER_KEY=...
CONSUMER_SECRET=...
ACCESS_KEY=...
ACCESS_SECRET=...
CLIENT_ID=...
CLIENT_SECRET=...
BEARER_TOKEN=...
API_KEY_BINANCE=...
API_SECRET_BINANCE=...
```

4. Start the bot by running the `bot.py` script.

```bash
python bot.py
```

## Usage

The bot will automatically check every 60 seconds if Peter Schiff tweets and, in case he does it, searches for the keywords to see if the tweet is about Bitcoin or not. In case it is, it places a market order on Binance for the BTC/USDT pairing.
  
## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Altaro97/Schiff-Alert/blob/main/LICENSE) file for details.

## Disclaimer

- I created this bot purely for entertainment and mainly for the memes. The bot's functionality is not intended to be used as an investing tool, and any resulting profits or losses are not the responsibility of the bot or its creator.
- The purpose of this little project is demonstrating how automation and programming can be used to create fun and interesting projects. The fact that the bot functions as intended does not mean that it should be taken seriously as an investment tool. Any decisions related to investing in Bitcoin or any other asset should be made after careful research and analysis.
- I urge anyone who may come across this bot to approach it with caution and not to use it as a financial advice or tool. The bot's purpose is purely for fun and not meant to be used for any other purpose. 
