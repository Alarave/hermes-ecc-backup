import os
import sys
import hashlib
import json

STATE_FILE = ".frozen_contracts.json"

def get_file_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def freeze(filepath):
    if not os.path.exists(filepath):
        print(f"Error: File {filepath} tidak ditemukan.")
        sys.exit(1)
    
    file_hash = get_file_hash(filepath)
    state = {}
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            state = json.load(f)
    
    state[filepath] = file_hash
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=4)
        
    print(f"✅ FROZEN: {filepath} (Hash: {file_hash[:8]}...)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python freeze_contract.py <filepath>")
        sys.exit(1)
    freeze(sys.argv[1])
