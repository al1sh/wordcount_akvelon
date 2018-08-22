import unittest
import os
import sys
import shutil
import zipfile

sys.path.append('..')
import wordcount


class BasicTests(unittest.TestCase):
    
    def test_simple_nested_folder(self):
        """Tests txt file lookup inside folder and a nested folder"""
        # script location + temp folder
        temp_folder = os.path.join(sys.path[0], "temp")

        if os.path.isdir(temp_folder):
            shutil.rmtree(temp_folder)

        # create temp folder
        if not os.path.exists(temp_folder):
            os.mkdir(temp_folder)
        
        # create text file test_file.txt inside with one word
        filename = "test_file.txt"
        filepath = os.path.join(temp_folder, filename)
        with open(filepath, "w") as test_file:
            test_file.write("one")
        
        # create subfolder inside
        subfolder = os.path.join(temp_folder, "subfolder")
        os.mkdir(subfolder)

        # create test_file_subfolder.txt inside subfolder
        subfile_name = "test_file_subfolder.txt"
        subfile_path = os.path.join(subfolder, subfile_name)
        with open(subfile_path, "w") as test_file:
            test_file.write("one two")

        word_counter = wordcount.WordCounter()
        result = word_counter.find_in_dir(temp_folder)

        # remove everything inside temp directory
        shutil.rmtree(temp_folder)

        self.assertTupleEqual((result[0]["wordcount"], result[0]["name"], result[0]["path"]),
                              (1, filename, filepath))

        self.assertTupleEqual((result[1]["wordcount"], result[1]["name"], result[1]["path"]),
                              (2, subfile_name, subfile_path))

    @unittest.skip("not completed yet")
    def test_nested_zip(self):
        """Test txt lookup in nested zip """
        
        # script location + temp folder
        temp_folder = os.path.join(sys.path[0], "temp")

        if os.path.isdir(temp_folder):
            shutil.rmtree(temp_folder)

        # create temp folder
        os.mkdir(temp_folder)
        
        # create text file test_file.txt inside with one word
        filename = "test_file.txt"
        filepath = os.path.join(temp_folder, filename)
        with open(filepath, "w") as test_file:
            test_file.write("one")
        
        # create subfolder inside
        subfolder = os.path.join(temp_folder, "subfolder")
        os.mkdir(subfolder)

        # create test_file_subfolder.txt inside subfolder
        subfile_name = "test_file_subfolder.txt"
        subfile_path = os.path.join(subfolder, subfile_name)
        with open(subfile_path, "w") as test_file:
            test_file.write("one two")

        shutil.make_archive(temp_folder, "zip", subfolder, subfolder)

        word_counter = wordcount.WordCounter()
        result = word_counter.find_in_dir(temp_folder)

        # remove everything inside temp directory
        shutil.rmtree(temp_folder)

        self.assertTupleEqual((result[0]["wordcount"], result[0]["name"], result[0]["path"]),
                              (1, filename, filepath))

        self.assertTupleEqual((result[1]["wordcount"], result[1]["name"], result[1]["path"]),
                              (2, subfile_name, subfile_path))



if __name__ == '__main__':
    unittest.main()