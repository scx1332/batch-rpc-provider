import unittest
from batch_rpc_provider import BatchRpcProvider, BatchRpcException


class TestSimple(unittest.IsolatedAsyncioTestCase):
    async def test_error(self):
        try:
            p = BatchRpcProvider('http://dummy:8545', 10000)
            await p.get_chain_id()
        except BatchRpcException as ex:
            self.assertTrue("aiohttp.ClientConnectorError" in str(ex))
        except Exception as ex:
            self.fail("Unexpected exception: {}".format(ex))

    async def test_polygon_chain_id(self):
        try:
            p = BatchRpcProvider('https://polygon-rpc.com', 10000)
            self.assertEqual(await p.get_chain_id(), 137)
        except Exception as ex:
            self.fail("Unexpected exception: {}".format(ex))


if __name__ == '__main__':
    unittest.main()
