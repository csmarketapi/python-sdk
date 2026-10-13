import os

import dotenv
import pytest
import pytest_asyncio
from csmarketapi import CSMarketAPI
from csmarketapi.enums import Market


@pytest.fixture(scope="session", autouse=True)
def load_env():
    dotenv.load_dotenv()


@pytest_asyncio.fixture
async def client(load_env):
    api_key = os.getenv("API_KEY")
    if not api_key:
        pytest.skip("API_KEY environment variable is required for tests")
    return CSMarketAPI(api_key)


@pytest.mark.asyncio
async def test_get_listings_latest_aggregated(client: CSMarketAPI):
    await client.get_listings_latest_aggregated(
        market_hash_name="Chroma 2 Case",
        markets=list(Market),
    )


@pytest.mark.asyncio
async def test_get_listings_history_aggregated(client: CSMarketAPI):
    await client.get_listings_history_aggregated(
        market_hash_name="Chroma 2 Case",
        markets=list(Market),
    )


@pytest.mark.asyncio
async def test_get_sales_latest_aggregated(client: CSMarketAPI):
    await client.get_sales_latest_aggregated(
        market_hash_name="Chroma 2 Case",
        markets=list(Market),
    )


@pytest.mark.asyncio
async def test_get_sales_history_aggregated(client: CSMarketAPI):
    await client.get_sales_history_aggregated(
        market_hash_name="Chroma 2 Case",
        markets=list(Market),
    )


@pytest.mark.asyncio
async def test_get_items(client: CSMarketAPI):
    await client.get_items()


@pytest.mark.asyncio
async def test_get_item_contents(client: CSMarketAPI):
    await client.get_item_contents(market_hash_name="Chroma 2 Case")


@pytest.mark.asyncio
async def test_get_player_counts_latest(client: CSMarketAPI):
    await client.get_player_counts_latest()


@pytest.mark.asyncio
async def test_get_player_counts_history(client: CSMarketAPI):
    await client.get_player_counts_history()


@pytest.mark.asyncio
async def test_get_markets(client: CSMarketAPI):
    await client.get_markets()


@pytest.mark.asyncio
async def test_get_account(client: CSMarketAPI):
    await client.get_account()
