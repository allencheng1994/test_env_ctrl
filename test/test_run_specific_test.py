import unittest
import sys
import random
from pahtlib import Path
sys.path.append(r"..\src")
from run_sepcific_test import run_test

TEST_PLACE = Path(r".\test_run_specifc_test_sample")


class TestRunScript(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        total_files = TEST_PLACE.rglob('*.record')
        for file in total_files:
            file.unlink()

    @classmethod
    def tearDownClass(cls):
        total_files = TEST_PLACE.rglob('*.record')
        for file in total_files:
            file.unlink()

    def test_run_case_one(self):
        run_test(test_place=TEST_PLACE, case_name='testcase-1')
        expected = True
        record = TEST_PLACE.joinpath(r'testcase-1\result\log.record').exists()
        self.assertEqual(record == expected)

    def test_run_case_random(self):
        case_tag = random.randrange(2, 100, 1)
        casename = 'testcase-' + str(case_tag)
        with self.assertRaises(FileNotFoundError):
            run_test(test_place=TEST_PLACE, case_name=casename)
            expected = True
            record = TEST_PLACE.joinpath(
                casename + r'\result\log.record').exists()
            self.assertEqual(record == expected)


class TestRunAllScriptsUnderProject(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        total_files = TEST_PLACE.rglob('*.record')
        for file in total_files:
            file.unlink()

    @classmethod
    def tearDownClass(cls):
        total_files = TEST_PLACE.rglob('*.record')
        for file in total_files:
            file.unlink()


class TestRunSpecificScriptsByUserDefined(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
