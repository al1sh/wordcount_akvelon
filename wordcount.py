import os
import sys
import shutil
import zipfile


class WordCounter:
    def __init__(self):
        self.result = []

    def find_in_dir(self, path):
        """Searches given path for txt files including its subdirectories and zip archives"""

        for dirpath, directories, filenames in os.walk(path):

                for filename in filenames:

                    name_and_extension = filename.split(".")
                    extension = name_and_extension[-1]

                    if extension == "txt":
                        # print(os.path.join(dirpath, filename))
                        with open(os.path.join(dirpath, filename)) as txt_file:
                            words = txt_file.read().split()
                            self.result.append({"name": filename,
                                                "path": os.path.join(dirpath, filename),
                                                "wordcount": len(words)})

                    elif extension == "zip":
                        folder_name = filename.split(".")[0]
                        path_to_folder = os.path.join(dirpath, folder_name)

                        try:
                            # open zip file
                            zfile = zipfile.ZipFile(os.path.join(dirpath, filename))

                            # create new folder with contents from zip file
                            zfile.extractall(path_to_folder)
                            zfile.close()

                        # Exit with error if zip file can't be extracted
                        except Exception as e:
                            sys.exit(str(e))

                        # search inside extracted zip folder
                        self.find_in_dir(path_to_folder)

                        # remove the temp folder
                        shutil.rmtree(path_to_folder)
        return self.result


        

def main():
    path = input("Please select path\n")
    # path = "C:\\Users\\Akvelon\\Desktop\\wordcount\\tests\\test_folder"
    # path = "/home/user/PycharmProjects/txt_zip/tests/test_folder/"

    try:
        os.chdir(path)

    # Exception if path does not exist or no read permissions
    except Exception as e:
        sys.exit(str(e))

    word_counter = WordCounter()
    result = word_counter.find_in_dir(path)

    for textfile in result:
        print("Name: {}\n\t Path: {}\n\t Word Count: {}\n\n".
              format(textfile["name"], textfile["path"], textfile["wordcount"]))

   
if __name__ == "__main__":
    main()