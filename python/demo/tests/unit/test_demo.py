import unittest
import pprint
from demo.demo import ClientS3


pp = pprint.PrettyPrinter(indent=4)


class TestClientS3(unittest.TestCase):
    def test_put_object(self):
        s3cl = ClientS3()
        response = s3cl.put_object("blarg", "my-bucket", "file.txt")
        # pp.pprint(response['ResponseMetadata'])
        response_status = response['ResponseMetadata']["HTTPStatusCode"]
        self.assertEqual(response_status, 1000)
        # self.assertEqual(
        # repsonse_sha256, "a593942cb7ea9ffcd8ccf2f0fa23c338e23bfecd9a3e508dfc0bcf07501ead08")


if __name__ == "__main__":
    unittest.main()
