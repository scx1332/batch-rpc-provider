import asyncio
import logging
import argparse
import platform

import batch_rpc_provider
from batch_rpc_provider import BatchRpcProvider, BatchRpcException, check_address_availability

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

NULL_ADDR = "0x0000000000000000000000000000000000000000"
POLYGON_GENESIS_ADDR = "0x0000000000000000000000000000000000001010"

CHAIN_ID_MAINNET = 1
CHAIN_ID_RINKEBY = 4
CHAIN_ID_GOERLI = 5
CHAIN_ID_POLYGON = 137
CHAIN_ID_MUMBAI = 80001


async def check_history_availability(p: BatchRpcProvider):
    latest_block = await p.get_latest_block()

    chain_id = await p.get_chain_id()

    def get_addr_to_check():
        if chain_id == CHAIN_ID_MAINNET:
            return NULL_ADDR
        if chain_id == CHAIN_ID_RINKEBY:
            return NULL_ADDR
        if chain_id == CHAIN_ID_GOERLI:
            return NULL_ADDR
        if chain_id == CHAIN_ID_POLYGON:
            return POLYGON_GENESIS_ADDR
        if chain_id == CHAIN_ID_MUMBAI:
            return POLYGON_GENESIS_ADDR
        raise Exception(f"Unrecognized chain id {chain_id}")

    check_balance_addr = get_addr_to_check()

    min_succeeded_block = await check_address_availability(p, check_balance_addr)
    # logger.info(f"Seems like history is available from {min_succeeded_block}. History depth: {latest_block - min_succeeded_block}")
    return min_succeeded_block, latest_block - min_succeeded_block

async def main():
    parser = argparse.ArgumentParser(description='Test params')
    parser.add_argument('--target-url', dest="target_url", type=str, help='Node name', default="https://polygon-rpc.com")

    args = parser.parse_args()
    p = BatchRpcProvider(args.target_url, 1)
    res = await check_history_availability(p)
    print("Oldest block: {}, archive depth: {}".format(res[0], res[1]))


if __name__ == "__main__":
    print(batch_rpc_provider.__version__)
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
