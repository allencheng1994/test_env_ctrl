import unittest
import sys
from pathlib import Path
sys.path.append(r"..\src")
from create_testing_folder import create_folders

TEST_PLACE = Path('')
TEST_CONFIG_FILE_SAMPLE_FOLDER = Path(r'./test_create_testing_folder_sample')


class TestCreateFolderWithOneTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if Path(TEST_PLACE).exists():
            Path(TEST_PLACE).unlink()
        create_folders(TEST_PLACE, case_num="1")

    @classmethod
    def tearDownClass(cls):
        if Path(TEST_PLACE).exists():
            Path(TEST_PLACE).unlink()

    def setUp(self):
        self.project_folder = Path(TEST_PLACE)
        self.test_case_folder = self.project_folder.joinpath("test_case_1")

    def test_prject_folder_exist(self):
        expected = True
        self.assertEqual(self.project_folder.exists() == expected)

    def test_sample_folder_exist(self):
        expected = True
        self.assertEqual(self.test_case_folder.joinpath(
            "sample").exists() == expected)

    def test_result_folder_exist(self):
        expected = True
        self.assertEqual(self.test_case_folder.joinpath(
            "result").exists() == expected)

    def test_log_folder_exist(self):
        expected = True
        self.assertEqual(self.test_case_folder.joinpath(
            "log").exists() == expected)


class TestCreateFolderWithThreeTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if Path(TEST_PLACE).exists():
            Path(TEST_PLACE).unlink()
        create_folders(TEST_PLACE, case_num="3")

    @classmethod
    def tearDownClass(cls):
        if Path(TEST_PLACE).exists():
            Path(TEST_PLACE).unlink()

    def setUp(self):
        self.project_folder = Path(TEST_PLACE)
        self.test_case_folder_names = [
            'test_case_' + str(i) for i in range(1, 4)]

    def test_prject_folder_exist(self):
        expected = True
        self.assertEqual(self.project_folder.exists() == expected)

    def test_sample_folder_exist(self):
        expected = True
        for test_case_name in self.test_case_folder_names:
            test_case_folder = self.project_folder.joinpath(test_case_name)
            sample_folder = test_case_folder.joinpath("sample")
            self.assertEqual(sample_folder.exists() == expected)

    def test_result_folder_exist(self):
        expected = True
        for test_case_name in self.test_case_folder_names:
            test_case_folder = self.project_folder.joinpath(test_case_name)
            result_folder = test_case_folder.joinpath("result")
            self.assertEqual(result_folder.exists() == expected)

    def test_log_folder_exist(self):
        expected = True
        for test_case_name in self.test_case_folder_names:
            test_case_folder = self.project_folder.joinpath(test_case_name)
            log_folder = test_case_folder.joinpath("log")
            self.assertEqual(log_folder.exists() == expected)


class TestCreateFolderWithUserDefinedTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if Path(TEST_PLACE).exists():
            Path(TEST_PLACE).unlink()
        config_file = TEST_CONFIG_FILE_SAMPLE_FOLDER.joinpath('case_1.txt')
        create_folders(TEST_PLACE, test_cases="user", config_file=config_file)

    @classmethod
    def tearDownClass(cls):
        if Path(TEST_PLACE).exists():
            Path(TEST_PLACE).unlink()


if __name__ == '__main__':
    unittest.main()
