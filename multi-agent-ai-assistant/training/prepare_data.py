import json

# Load original dataset
with open("dataset/dataset.json") as f:
    data = json.load(f)

formatted = []

for item in data:
    text = f"""### Instruction:
{item['instruction']}

### Input:
{item['input']}

### Response:
{item['output']}"""

    formatted.append({"text": text})

# Save new dataset
with open("dataset/train.json", "w") as f:
    json.dump(formatted, f, indent=4)

print("✅ train.json created successfully!")