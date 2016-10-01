from unittest import TestCase

from cleanpath import clean


class TestCleanpath(TestCase):
    def test_clean(self):
        tcases = [
            ('/a/b/c/:/a/b/c:/a/b/c/', '/a/b/c'),
            ('../a/b:/a/b:../a/b', '/a/b'),
            ('/a:/b:/c:/b:/a/:a', '/a:/b:/c'),
            ('/has/path with spaces/bin:/a/b:/a', '/has/path with spaces/bin:/a/b:/a')
        ]
        for tcase in tcases:
            messy, expect = tcase
            got = clean(messy)
            if expect != got:
                self.fail('Expected ' + expect + ', got ' + got)
