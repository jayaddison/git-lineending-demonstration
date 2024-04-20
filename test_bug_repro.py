from unittest import TestCase

from hashlib import sha512
from pathlib import Path


class SHA512Test(TestCase):
    def test_bug_repro(self):
        file = Path("origin") / "file.txt"
        digest = sha512(file.read_bytes()).hexdigest()

        self.assertEqual("8d47d372496b4eb8a324a1e481a195c6506757dfabefe1b032a945a1f2c28f7797440bf9252614c6b533774b6dad304df81df4379cffc32a58d8bd58e8ed91e6", digest)
