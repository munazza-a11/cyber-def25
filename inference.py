import os
import pickle
import pandas as pd

# Define paths as per assignment
INPUT_DIR = '/input/logs'
OUTPUT_FILE = '/output/alerts.csv'
MODEL_PATH = 'model.pkl'

def scan():
    if not os.path.exists(INPUT_DIR):
        print("No input directory found")
        return

    # Load Model
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)

    results = []
    
    # Process files
    for file in os.listdir(INPUT_DIR):
        try:
            path = os.path.join(INPUT_DIR, file)
            # Read CSV (assuming no header, just data)
            data = pd.read_csv(path, header=None)
            predictions = model.predict(data)
            
            # If any row is '1', mark file as malware
            status = 'MALWARE' if 1 in predictions else 'SAFE'
            results.append({'file': file, 'status': status})
            print(f"Scanned {file}: {status}")
        except Exception as e:
            print(f"Skipping {file}: {e}")

    # Save Results
    pd.DataFrame(results).to_csv(OUTPUT_FILE, index=False)
    print(f"Results saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    scan()
