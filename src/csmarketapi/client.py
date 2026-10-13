import httpx

from .enums import Currency, Market, Phase
from .models import (
    Account,
    ItemContents,
    Items,
    ListingsHistoryAggregated,
    ListingsLatestAggregated,
    Markets,
    PlayerCountsHistory,
    PlayerCountsLatest,
    SalesHistoryAggregated,
    SalesLatestAggregated,
)


class CSMarketAPI:
    def __init__(self, api_key: str):
        self.client = httpx.AsyncClient(
            base_url="https://api.csmarketapi.com",
            params={
                "key": api_key,
            },
            follow_redirects=True,
        )

    async def __aenter__(self) -> "CSMarketAPI":
        return self

    async def __aexit__(
        self,
        exc_type: type[Exception] | None,
        exc_value: Exception | None,
        traceback: any,
    ) -> None:
        await self.close()

    async def close(self) -> None:
        await self.client.aclose()
        self.client = None

    async def get_listings_latest_aggregated(
        self,
        market_hash_name: str,
        markets: list[Market] | None = None,
        currency: Currency = Currency.USD,
        phase: Phase | None = None,
    ) -> ListingsLatestAggregated:
        r = await self.client.get(
            "/v2/listings/latest/aggregate",
            params={
                "market_hash_name": market_hash_name,
                **(
                    {"markets": [market.value for market in markets]}
                    if markets is not None
                    else {}
                ),
                "currency": currency.value,
                **({"phase": phase.value} if phase is not None else {}),
            },
        )
        r.raise_for_status()
        return ListingsLatestAggregated(**r.json())

    async def get_listings_history_aggregated(
        self,
        market_hash_name: str,
        markets: list[Market] | None = None,
        currency: Currency = Currency.USD,
        since: str | None = None,
        phase: Phase | None = None,
    ) -> ListingsHistoryAggregated:
        r = await self.client.get(
            "/v2/listings/history/aggregate",
            params={
                "market_hash_name": market_hash_name,
                **(
                    {"markets": [market.value for market in markets]}
                    if markets is not None
                    else {}
                ),
                "currency": currency.value,
                **({"since": since} if since is not None else {}),
                **({"phase": phase.value} if phase is not None else {}),
            },
        )
        r.raise_for_status()
        return ListingsHistoryAggregated(**r.json())

    async def get_sales_latest_aggregated(
        self,
        market_hash_name: str,
        markets: list[Market] | None = None,
        currency: Currency = Currency.USD,
    ) -> SalesLatestAggregated:
        r = await self.client.get(
            "/v2/sales/latest/aggregate",
            params={
                "market_hash_name": market_hash_name,
                **(
                    {"markets": [market.value for market in markets]}
                    if markets is not None
                    else {}
                ),
                "currency": currency.value,
            },
        )
        r.raise_for_status()
        return SalesLatestAggregated(**r.json())

    async def get_sales_history_aggregated(
        self,
        market_hash_name: str,
        markets: list[Market] | None = None,
        start: str | None = None,
        end: str | None = None,
        currency: Currency = Currency.USD,
    ) -> SalesHistoryAggregated:
        r = await self.client.get(
            "/v2/sales/history/aggregate",
            params={
                "market_hash_name": market_hash_name,
                **(
                    {"markets": [market.value for market in markets]}
                    if markets is not None
                    else {}
                ),
                **({"start": start} if start is not None else {}),
                **({"end": end} if end is not None else {}),
                "currency": currency.value,
            },
        )
        r.raise_for_status()

        return SalesHistoryAggregated(items=r.json())

    async def get_items(
        self,
        q: str | None = None,
        unlisted: bool = False,
    ) -> Items:
        r = await self.client.get(
            "/v2/items/",
            params={
                **({"q": q} if q is not None else {}),
                "unlisted": unlisted,
            },
        )
        r.raise_for_status()
        return Items(items=r.json())

    async def get_item_contents(self, market_hash_name: str) -> ItemContents:
        r = await self.client.get(
            "/v2/items/contents",
            params={
                "market_hash_name": market_hash_name,
            },
        )
        r.raise_for_status()
        return ItemContents(**r.json())

    async def get_markets(self) -> Markets:
        r = await self.client.get("/v2/markets/")
        r.raise_for_status()
        return Markets(items=r.json())

    async def get_account(self) -> Account:
        r = await self.client.get("/v2/account")
        r.raise_for_status()
        return Account(**r.json())

    async def get_player_counts_latest(self) -> PlayerCountsLatest:
        r = await self.client.get("/v2/player_counts/latest")
        r.raise_for_status()
        return PlayerCountsLatest(**r.json())

    async def get_player_counts_history(
        self,
        start: str | None = None,
        end: str | None = None,
    ) -> PlayerCountsHistory:
        r = await self.client.get(
            "/v2/player_counts/history",
            params={
                **({"start": start} if start is not None else {}),
                **({"end": end} if end is not None else {}),
            },
        )
        r.raise_for_status()
        return PlayerCountsHistory(items=r.json())
