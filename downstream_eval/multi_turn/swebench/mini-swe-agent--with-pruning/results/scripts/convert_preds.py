import json

with open("../with-pruner-glm4.6/preds.json") as f:
    preds = json.load(f)

with open("../with-pruner-glm4.6/preds-50.jsonl", "w") as f:
    for item in preds.values():
        f.write(json.dumps(item) + "\n")