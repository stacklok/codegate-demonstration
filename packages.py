import hashlib
import invokehttp

def get_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

def http():
    invokehttp.main()

def main():
    file_path = 'new.py'
    sha256 = get_sha256(file_path)
    print(f'SHA-256: {sha256}')