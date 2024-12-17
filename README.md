# Synthetic Alpaca Dataset Generator
A simple python-based synthetic dataset generator in the Alpaca format powered by OpenAI API.

The configurations are in the main.py file.

# Setup:

```bash
git clone https://github.com/DominicTWHV/Alpaca-Dataset-Generator.git
cd Alpaca-Dataset-Generator
apt install python3 python3-venv python3-pip -y
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
mv example.env .env
```

Then, go into `.env` and insert your API token.
Example:
```bash
nano .env
```

And configure your settings via:
```bash
nano main.py
```

# Running:

```bash
python3 main.py
```