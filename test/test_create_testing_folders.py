import unittest
import sys
from pathlib import Path
import shutil

FILE = Path(__file__).resolve()
PROJECT_DIR = Path(FILE).parents[1]

sys.path.append(str(PROJECT_DIR / "src"))
from create_testing_folder import (
    create_folders_with_config,
    create_folders_with_default,
)

TEST_PLACE = Path(__file__).parent.joinpath("testplace")
TEST_CONFIG_FILE_SAMPLE_FOLDER = Path(__file__).parent.joinpath(
    "test_create_testing_folder_sample"
)


class TestCreateFolderWithDefaultOne(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if TEST_PLACE.exists():
            shutil.rmtree(TEST_PLACE)

        TEST_PLACE.mkdir()
        create_folders_with_default(
            TEST_PLACE,
        )

    @classmethod
    def tearDownClass(cls):
        if TEST_PLACE.exists():
            shutil.rmtree(TEST_PLACE)

    def setUp(self):
        self.project_folder = TEST_PLACE
        self.test_case_folder = self.project_folder.joinpath("testcase_1")

    def test_prject_folder_exist(self):
        expected = True
        self.assertEqual(self.project_folder.exists(), expected)

    def test_sample_folder_exist(self):
        expected = True
        self.assertEqual(self.test_case_folder.joinpath("sample").exists(), expected)

    def test_result_folder_exist(self):
        expected = True
        self.assertEqual(self.test_case_folder.joinpath("result").exists(), expected)

    def test_log_folder_exist(self):
        expected = True
        self.assertEqual(self.test_case_folder.joinpath("log").exists(), expected)


class TestCreateFolderWithDefaultFour(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if TEST_PLACE.exists():
            shutil.rmtree(TEST_PLACE)

        TEST_PLACE.mkdir()
        create_folders_with_default(
            TEST_PLACE, 4
        )

    @classmethod
    def tearDownClass(cls):
        if TEST_PLACE.exists():
            shutil.rmtree(TEST_PLACE)

    def setUp(self):
        self.project_folder = TEST_PLACE
        folders = ["testcase_" + str(i + 1) for i in range(4)]
        self.test_case_folder = [
            self.project_folder.joinpath(folder) for folder in folders
        ]

    def test_project_folder_exist(self):
        expected = True
        self.assertEqual(self.project_folder.exists(), expected)

    def test_testcase_folder_exist(self):
        expected = True
        for i in range(4):
            with self.subTest(i=i):
                self.assertEqual(self.test_case_folder[i].exists(), expected)

    def test_sample_folder_exist(self):
        expected = True
        for i in range(4):
            with self.subTest(i=i):
                self.assertEqual(
                    self.test_case_folder[i].joinpath("sample").exists(), expected
                )

    def test_result_folder_exist(self):
        expected = True
        for i in range(4):
            with self.subTest(i=i):
                self.assertEqual(
                    self.test_case_folder[i].joinpath("result").exists(), expected
                )

    def test_log_folder_exist(self):
        expected = True
        for i in range(4):
            with self.subTest(i=i):
                self.assertEqual(
                    self.test_case_folder[i].joinpath("log").exists(), expected
                )

class TestCreateFolderWithOneTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if TEST_PLACE.exists():
            shutil.rmtree(TEST_PLACE)

        TEST_PLACE.mkdir()
        create_folders_with_config(
            TEST_PLACE,
            config_file=TEST_CONFIG_FILE_SAMPLE_FOLDER.joinpath("config_1.json"),
        )

    @classmethod
    def tearDownClass(cls):
        if TEST_PLACE.exists():
            shutil.rmtree(TEST_PLACE)

    def setUp(self):
        self.project_folder = TEST_PLACE
        self.test_case_folder = self.project_folder.joinpath("testcase_1")

    def test_prject_folder_exist(self):
        expected = True
        self.assertEqual(self.project_folder.exists(), expected)

    def test_sample_folder_exist(self):
        expected = True
        self.assertEqual(self.test_case_folder.joinpath("sample").exists(), expected)

    def test_result_folder_exist(self):
        expected = True
        self.assertEqual(self.test_case_folder.joinpath("result").exists(), expected)

    def test_log_folder_exist(self):
        expected = True
        self.assertEqual(self.test_case_folder.joinpath("log").exists(), expected)


class TestCreateFolderWithThreeTestCaseOneStruct(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if TEST_PLACE.exists():
            shutil.rmtree(TEST_PLACE)

        TEST_PLACE.mkdir()
        create_folders_with_config(
            TEST_PLACE,
            config_file=TEST_CONFIG_FILE_SAMPLE_FOLDER.joinpath("config_2.json"),
        )

    @classmethod
    def tearDownClass(cls):
        if TEST_PLACE.exists():
            shutil.rmtree(TEST_PLACE)

    def setUp(self):
        self.project_folder = TEST_PLACE
        folders = ["testcase_" + str(i + 1) for i in range(3)]
        self.test_case_folder = [
            self.project_folder.joinpath(folder) for folder in folders
        ]

    def test_project_folder_exist(self):
        expected = True
        self.assertEqual(self.project_folder.exists(), expected)

    def test_testcase_folder_exist(self):
        expected = True
        for i in range(3):
            with self.subTest(i=i):
                self.assertEqual(self.test_case_folder[i].exists(), expected)

    def test_sample_folder_exist(self):
        expected = True
        for i in range(3):
            with self.subTest(i=i):
                self.assertEqual(
                    self.test_case_folder[i].joinpath("sample").exists(), expected
                )

    def test_result_folder_exist(self):
        expected = True
        for i in range(3):
            with self.subTest(i=i):
                self.assertEqual(
                    self.test_case_folder[i].joinpath("result").exists(), expected
                )

    def test_log_folder_exist(self):
        expected = True
        for i in range(3):
            with self.subTest(i=i):
                self.assertEqual(
                    self.test_case_folder[i].joinpath("log").exists(), expected
                )


class TestCreateFolderWithThreeTestCaseTwoStruct(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if TEST_PLACE.exists():
            shutil.rmtree(TEST_PLACE)

        TEST_PLACE.mkdir()
        create_folders_with_config(
            TEST_PLACE,
            config_file=TEST_CONFIG_FILE_SAMPLE_FOLDER.joinpath("config_2.json"),
        )

    @classmethod
    def tearDownClass(cls):
        if TEST_PLACE.exists():
            shutil.rmtree(TEST_PLACE)

    def setUp(self):
        self.project_folder = TEST_PLACE
        folders = ["testcase_" + str(i + 1) for i in range(6)]
        self.test_case_folder = [
            self.project_folder.joinpath(folder) for folder in folders
        ]

    def test_project_folder_exist(self):
        expected = True
        self.assertEqual(self.project_folder.exists(), expected)

    def test_testcase_folder_exist(self):
        expected = True
        for i in range(6):
            with self.subTest(i=i):
                self.assertEqual(self.test_case_folder[i].exists(), expected)

    def test_sample_folder_exist(self):
        expected = True
        for i in range(6):
            with self.subTest(i=i):
                self.assertEqual(
                    self.test_case_folder[i].joinpath("sample").exists(), expected
                )

    def test_result_folder_exist(self):
        expected = True
        for i in range(6):
            with self.subTest(i=i):
                self.assertEqual(
                    self.test_case_folder[i].joinpath("result").exists(), expected
                )

    def test_log_folder_exist(self):
        expected = True
        for i in range(6):
            with self.subTest(i=i):
                self.assertEqual(
                    self.test_case_folder[i].joinpath("log").exists(), expected
                )

    def test_sub_log_folder_unexist(self):
        expected = False
        for i in range(3):
            with self.subTest(i=i):
                self.assertEqual(
                    self.test_case_folder[i]
                    .joinpath("log")
                    .joinpath("situation_1")
                    .exists(),
                    expected,
                )
            with self.subTest(i=i):
                self.assertEqual(
                    self.test_case_folder[i]
                    .joinpath("log")
                    .joinpath("situation_2")
                    .exists(),
                    expected,
                )

    def test_sub_log_folder_exist(self):
        expected = True
        for i in range(3, 6):
            with self.subTest(i=i):
                self.assertEqual(
                    self.test_case_folder[i]
                    .joinpath("log")
                    .joinpath("situation_1")
                    .exists(),
                    expected,
                )
            with self.subTest(i=i):
                self.assertEqual(
                    self.test_case_folder[i]
                    .joinpath("log")
                    .joinpath("situation_2")
                    .exists(),
                    expected,
                )


if __name__ == "__main__":
    unittest.main()
