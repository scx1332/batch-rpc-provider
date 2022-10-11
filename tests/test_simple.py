# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package
import asyncio
import platform
import unittest

from batch_rpc_provider import BatchRpcProvider, BatchRpcException
from unittest import IsolatedAsyncioTestCase


class TestSimple(unittest.IsolatedAsyncioTestCase):
    async def test_error(self):
        if 0:
            try:
                p = BatchRpcProvider('http://dummy:8545', 10000)
                await p.get_chain_id()
            except BatchRpcException as ex:
                self.assertTrue("URLError" in str(ex))
            except Exception as ex:
                self.fail("Unexpected exception: {}".format(ex))

    async def test_polygon_chainid(self):
        try:
            p = BatchRpcProvider('https://polygon-rpc.com', 10000)
            self.assertEqual(await p.get_chain_id(), 137)

        except Exception as ex:
            self.fail("Unexpected exception: {}".format(ex))


if __name__ == '__main__':


    unittest.main()
