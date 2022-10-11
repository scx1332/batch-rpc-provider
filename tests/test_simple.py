import logging
import unittest
from batch_rpc_provider import BatchRpcProvider, BatchRpcException


class TestSimple(unittest.IsolatedAsyncioTestCase):
    async def test_error(self):
        try:
            # errors are expected so disable them to avoid confusion
            logging.getLogger("batch_rpc_provider.batch_rpc_provider").setLevel(logging.CRITICAL)
            p = BatchRpcProvider('http://dummy:8545', 10000)
            await p.get_chain_id()
        except BatchRpcException as ex:
            self.assertTrue("aiohttp.ClientConnectorError" in str(ex))
        except Exception as ex:
            self.fail("Unexpected exception: {}".format(ex))

    async def test_polygon_chain_id(self):
        p = BatchRpcProvider('https://polygon-rpc.com', 10000)
        chain_id = await p.get_chain_id()
        self.assertEqual(chain_id, 137)

    async def test_polygon_blocknum(self):
        p = BatchRpcProvider('https://polygon-rpc.com', 10000)
        block_num = await p.get_latest_block()
        self.assertTrue(block_num > 30000000)


if __name__ == '__main__':
    unittest.main()
