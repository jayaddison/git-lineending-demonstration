from unittest import TestCase

from hashlib import sha512
from pathlib import Path
from shutil import copytree


class ShutilCopier(TestCase):
    def test_bug_repro(self):
        infile = Path("origin") / "file.txt"
        infile_digest = sha512(infile.read_bytes()).hexdigest()

        copytree("origin", "destination")

        outfile = Path("destination") / "file.txt"
        outfile_digest = sha512(outfile.read_bytes()).hexdigest()

        self.assertEqual(outfile_digest, infile_digest)
