from model import NGramModel

def load(path):
    with open(path) as f:
        return [line.split() for line in f if line.strip()]

def main():
    model = NGramModel(n=3)
    model.train(load("data/sequences.txt"))

    print("Crop Health Sequence Monitor")
    print("Enter observations separated by spaces (e.g. aphids leaf_curl). Type 'quit' to exit.")
    while True:
        text = input("\nObserved so far: ").strip()
        if text == "quit":
            break
        preds = model.predict(text.split())
        if not preds:
            print("No prediction available for this sequence.")
            continue
        print("Likely next:")
        for item, prob in preds:
            print(f"  {item}  ({prob:.0%})")

if __name__ == "__main__":
    main()
