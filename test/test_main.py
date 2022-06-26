from pathlib import Path
import unittest
import os
import shutil

FILE = Path(__file__).resolve()
PROJECT_DIR = Path(FILE).parents[1]

TEST_PLACE = Path(__file__).parent.joinpath("test_main")


class TestCreateFolderWithDefaultFour(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if TEST_PLACE.exists():
            shutil.rmtree(TEST_PLACE)
        TEST_PLACE.mkdir()

        os.chdir(TEST_PLACE)
        cmd = "python3 " + str(PROJECT_DIR.joinpath("main.py").resolve()) + " init 4"
        os.system(cmd)

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


class TestCreateFolderWithThreeTestCaseTwoStruct(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if TEST_PLACE.exists():
            shutil.rmtree(TEST_PLACE)
        TEST_PLACE.mkdir()

        os.chdir(TEST_PLACE)
        cmd = (
            "python3 "
            + str(PROJECT_DIR.joinpath("main.py").resolve())
            + " init -c "
            + str(
                PROJECT_DIR
                / "test"
                / "test_create_testing_folder_sample"
                / "config_2.json"
            )
        )
        os.system(cmd)

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
