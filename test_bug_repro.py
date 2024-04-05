from unittest import TestCase

from hashlib import sha512
from os import makedirs
from pathlib import Path
from shutil import copyfile


class ShutilCopier(TestCase):
    def test_bug_repro(self):
        infile = Path("origin") / "file.txt"
        infile_digest = sha512(infile.read_bytes()).hexdigest()

        makedirs("destination", exist_ok=True)
        copyfile("origin/file.txt", "destination/file.txt")

        outfile = Path("destination") / "file.txt"
        outfile_digest = sha512(outfile.read_bytes()).hexdigest()

        self.assertEqual(outfile_digest, infile_digest)
