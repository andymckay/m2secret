import unittest

import m2secret


class TestUnicode(unittest.TestCase):
    key = 'some-key'

    def test_ascii(self):
        secret = m2secret.Secret()
        secret.encrypt('foo', self.key)
        res = secret.serialize()

        reverse = m2secret.Secret()
        reverse.deserialize(res)
        assert reverse.decrypt(self.key) == 'foo'

    def test_unicode(self):
        secret = m2secret.Secret()
        secret.encrypt(u'foo', self.key)
        res = secret.serialize()

        reverse = m2secret.Secret()
        reverse.deserialize(res)
        assert reverse.decrypt(self.key) == 'foo'



if __name__ == '__main__':
    unittest.main()
