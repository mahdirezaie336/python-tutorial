import os
import shutil
import unittest
from datetime import datetime
from random import randint
import sh

SRC_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_PATH = os.path.dirname(SRC_PATH)
TEST_PATH = os.path.join(SRC_PATH, 'test')
ORG_PATH = os.path.join(TEST_PATH, 'organized')


class TestMediaOrganizer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.chdir(TEST_PATH)

        with open('../organize.py', 'rb') as a:
            data = a.read()
            with open('organize.py', 'wb') as b:
                b.write(data)

    @staticmethod
    def _set_mtimes(media_dir, mtimes):
        # set modification times
        for path, mtime in mtimes.items():
            dt = datetime(mtime, randint(1, 12), randint(3, 26), randint(0, 23), randint(0, 59), randint(0, 59))
            os.utime(os.path.join(media_dir, path), (dt.timestamp(), dt.timestamp()))

    def _test(self, media_dir, mtimes, expected_structure):
        self._set_mtimes(media_dir, mtimes)

        # run organize.py on input dir
        shutil.rmtree(ORG_PATH, ignore_errors=True)

        os.system("python3 organize.py " + media_dir + " " + ORG_PATH)

        # test output dir
        self.assertTrue(os.path.isdir(ORG_PATH))
        self.assertListEqual(sorted(sh.find('.', _cwd=ORG_PATH).splitlines()), expected_structure)

    def test_sample_1(self):
        media_dir = os.path.join(TEST_PATH, 'test_sample_1')
        mtimes = {
            'image.jpg': 2013,
            'video.mov': 2013,
        }
        expected_structure = [
            '.',
            './2013',
            './2013/photos',
            './2013/photos/image.jpg',
            './2013/videos',
            './2013/videos/video.mov',
        ]

        self._test(media_dir, mtimes, expected_structure)

    def test_sample_2(self):
        media_dir = os.path.join(TEST_PATH, 'test_sample_2')
        mtimes = {
            'Gallery/b/c/img.jpg': 1998,
            'DCIM/linux.png': 2020,
        }
        expected_structure = [
            '.',
            './1998',
            './1998/photos',
            './1998/photos/img.jpg',
            './2020',
            './2020/photos',
            './2020/photos/linux.png',
        ]

        self._test(media_dir, mtimes, expected_structure)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(ORG_PATH, ignore_errors=True)
