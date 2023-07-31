import os
import shutil
import argparse
import zipfile
import tarfile

def normalize(name):
    trans_dict = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Е': 'E', 'Є': 'Ye',
        'Ж': 'Zh', 'З': 'Z', 'И': 'Y', 'І': 'I', 'Ї': 'Yi', 'Й': 'Y', 'К': 'K', 'Л': 'L',
        'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'Kh'
    }
    
    normalized_name = ''
    for char in name:
        if char.upper() in trans_dict:
            normalized_name += trans_dict[char.upper()]
        else:
            normalized_name += char
    return normalized_name

def sort_folder(path):
    os.makedirs(os.path.join(path, 'images'), exist_ok=True)
    os.makedirs(os.path.join(path, 'documents'), exist_ok=True)
    os.makedirs(os.path.join(path, 'audio'), exist_ok=True)
    os.makedirs(os.path.join(path, 'video'), exist_ok=True)
    os.makedirs(os.path.join(path, 'archives'), exist_ok=True)

    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path) and item not in ['images', 'documents', 'audio', 'video', 'archives']:
            sort_folder(item_path)
            continue

        extension = item.split('.')[-1].upper()

        if extension in ['JPEG', 'PNG', 'JPG', 'SVG']:
            shutil.move(item_path, os.path.join(path, 'images', normalize(item)))
        elif extension in ['AVI', 'MP4', 'MOV', 'MKV']:
            shutil.move(item_path, os.path.join(path, 'video', normalize(item)))
        elif extension in ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']:
            shutil.move(item_path, os.path.join(path, 'documents', normalize(item)))
        elif extension in ['MP3', 'OGG', 'WAV', 'AMR']:
            shutil.move(item_path, os.path.join(path, 'audio', normalize(item)))
        elif extension in ['ZIP', 'RAR', 'TAR', 'GZ']:
            extract_archive(item_path, os.path.join(path, 'archives'))

def extract_archive(archive_path, extract_path):
    extension = os.path.splitext(archive_path)[1].lower()

    if extension == '.zip':
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
    elif extension in ['.tar', '.tar.gz', '.tgz']:
        with tarfile.open(archive_path, 'r:*') as tar_ref:
            tar_ref.extractall(extract_path)

def main():
    parser = argparse.ArgumentParser(description='Sort files in a directory by type.')
    parser.add_argument('directory', type=str, help='Path to the directory to sort')

    args = parser.parse_args()
    directory = args.directory

    sort_folder(directory)

if __name__ == '__main__':
    main()