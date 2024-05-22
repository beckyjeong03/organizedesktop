import os
import shutil

def main():
    path = '/mnt/c/Users/becky/Downloads'
    files = os.listdir(path)
    
    

    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            filename, extension = os.path.splitext(file)
            extension = extension[1:]  

            if not os.path.exists(path + '/' + extension):
                os.makedirs(path + '/' + extension)

            new_file_path = os.path.join(path, extension, file)
            
            if os.path.exists(new_file_path):
                base_filename = filename
                counter = 1
                while os.path.exists(os.path.join(path, extension, f"{base_filename}_{counter}{extension}")):
                    counter += 1
                new_file_path = os.path.join(path, extension, f"{base_filename}_{counter}{extension}")
            
            shutil.move(os.path.join(path, file), new_file_path)
            print(f"Moved '{file}' to '{new_file_path}'")

if __name__ == "__main__":
    main()
