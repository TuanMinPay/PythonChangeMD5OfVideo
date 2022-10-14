import hashlib

def get_file_md5(file_path):
    with open(file_path, 'rb') as f:
        md5 = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            md5.update(data)
        return md5.hexdigest()

def change_file_md5(file_path):
    with open(file_path, 'a') as f:
        f.write(' ')

def main():
    # Current MD5
    print(f"Current MD5 of the file: {get_file_md5('./resource/IMG_0795.MOV')}")

    # Change the file
    change_file_md5('./resource/IMG_0795.MOV')
    print(f"Changed MD5 of the file: {get_file_md5('./resource/IMG_0795.MOV')}")

    print("\nDone!")

main()