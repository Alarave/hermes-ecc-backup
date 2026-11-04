import os
import sys
import hashlib
import json

STATE_FILE = ".frozen_contracts.json"

def get_file_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def verify(filepath):
    if not os.path.exists(STATE_FILE):
        print(f"Error: Tidak ada kontrak yang dibekukan ({STATE_FILE} missing).")
        sys.exit(1)
        
    with open(STATE_FILE, 'r') as f:
        state = json.load(f)
        
    if filepath not in state:
        print(f"⚠️ Warning: {filepath} tidak ada dalam daftar frozen contracts.")
        sys.exit(0)
        
    if not os.path.exists(filepath):
        print(f"❌ REJECTED: File {filepath} telah dihapus!")
        sys.exit(1)
        
    current_hash = get_file_hash(filepath)
    expected_hash = state[filepath]
    
    if current_hash != expected_hash:
        print(f"❌ REJECTED: Kontrak {filepath} telah diubah tanpa izin (Hash mismatch).")
        sys.exit(1)
        
    print(f"✅ VERIFIED: Kontrak {filepath} utuh.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python verify_frozen_contract.py <filepath>")
        sys.exit(1)
    verify(sys.argv[1])
