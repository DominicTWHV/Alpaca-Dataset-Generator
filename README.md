# Synthetic Alpaca Dataset Generator
A simple python-based synthetic dataset generator in the Alpaca format powered by OpenAI API.

The configurations are in the main.py file.

# The Alpaca Format:

Example:

```json
[
  {
    "instruction": "Describe a process of making crepes.",
    "input": "",
    "output": "Making crepes is an easy and delicious process! Here are step-by-step instructions on how to make them:\n\n1. Assemble your ingredients. For basic crepes, you'll need: 1 cup all-purpose flour, 2 eggs, 1/2 cup milk, 1/2 cup water, 1/4 teaspoon salt, and 2 tablespoons melted butter.\n\n2. Mix the batter: In a large mixing bowl, whisk together the flour and the eggs. Gradually add the milk and water, stirring constantly to ensure that there are no lumps. Add salt and melted butter, and mix well.\n\n3. Let the batter rest: If you can, let the batter sit for an hour or so. This will help the flour to absorb the liquid and make the crepes more tender.\n\n4. Heat your pan: Preheat a non-stick pan over medium heat. Lightly butter the pan or use cooking spray to prevent the crepes from sticking.\n\n5. Pour the batter: Using a ladle or a measuring cup, pour a small amount of batter (about 1/4 cup) onto the center of the pan. Immediately tilt the pan in a circular motion to spread the batter evenly and thinly over the bottom of the pan.\n\n6. Cook the crepe: Cook the crepe for 1-2 minutes until the bottom is lightly golden. Carefully loosen the edges with a spatula and flip the crepe over to cook the other side for another minute.\n\n7. Remove and repeat: Gently slide the crepe onto a plate, and then repeat the process with the remaining batter. Remember to re-butter the pan between each crepe if necessary.\n\n8. Fill and serve: Fill your cooked crepes with your desired filling, such as fresh fruit, whipped cream, Nutella, or ham and cheese. Roll or fold, and serve immediately. Enjoy!"
  },
  {
    "instruction": "Transform the following sentence using a synonym: The car sped quickly.",
    "input": "",
    "output": "The car accelerated rapidly."
  }
]
```

# Setup:

```bash
git clone https://github.com/DominicTWHV/Alpaca_Dataset_Generator.git
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

---

Configure your settings via:

```bash
nano main.py
```

Configure the system prompt by going into the `instruction.txt` file and editing the contents. 

**Warning: the code uses a specific regex pattern matching, whats provided generally works well for basic generic dataset generation, so unless you know what you are doing, do NOT edit that file, otherwise, when combined with `permit_fail_retry`, you can very much exceed your API limits with no actual usable returns.**

```bash
nano instruction.txt
```

# Running:

```bash
python3 main.py
```
