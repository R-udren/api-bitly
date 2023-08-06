# Bitly Link Shortener and Click Counter
This Python script working with Bitly API to shorten URLs and count clicks on Bitly links.

## Requirements
* Python 3.6 or higher
* requests
* dotenv

## Installation & Usage
1. Clone repository to your local machine
```bash
git clone https://github.com/R-udren/api-bitly.git
```
2. Go to the program directory
```bash
cd api-bitly
```
3. Install the requirements
```bash
pip install -r requirements.txt
```
4. __After configuration__ launch script
```bash
python bitly_tool.py
```

## Configuration
Before running the script, you need to set up your Bitly API token. Here's how:
1. Go to [Bitly's Documentation](https://dev.bitly.com/docs/getting-started/authentication/) and create an account.
2. Create a new access token.
3. Rename the `EXAMPLE.env` file to `.env`.
4. Open the `.env` file and replace `YOUR_BITLY_TOKEN` with your actual Bitly API token.
