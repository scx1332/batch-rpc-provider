import argparse
import asyncio
import platform

from batch_rpc_provider import BatchRpcProvider

import batch_rpc_provider

async def main():
    parser = argparse.ArgumentParser(description='Test params')
    parser.add_argument('--target-url', dest="target_url", type=str, help='Node name', default="https://polygon-rpc.com")


    args = parser.parse_args()

    p = BatchRpcProvider(args.target_url, 100)
    block_no = 35719449
    await p.get_logs(f"0x{block_no:x}", f"0x{block_no:x}", "0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619", ["0x000000000000000000000000a94f5374fce5edbc8e2a8697c15331677e6ebf0b"])

if __name__ == "__main__":
    print(batch_rpc_provider.__version__)
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
