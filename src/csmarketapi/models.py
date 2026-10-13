from __future__ import annotations

import datetime
from typing import Any

from pydantic import BaseModel

from .enums import Market, Phase


class ListingsLatestAggregated(BaseModel):
    class Listing(BaseModel):
        market: Market
        market_link: str
        mean_price: float | None = None
        ask_price: float | None = None
        max_price: float | None = None
        median_price: float | None = None
        bid_price: float | None = None
        listings: int
        bid_volume: int | None = None
        volume_24h: int | None = None
        available: bool | None = None
        phase: Phase | None = None
        timestamp: datetime.datetime

    market_hash_name: str
    listings: list[Listing]


class ListingsHistoryAggregated(BaseModel):

    class Link(BaseModel):
        market_link: str

    class Observation(BaseModel):
        mean_price: float | None = None
        ask_price: float | None = None
        max_price: float | None = None
        median_price: float | None = None
        bid_price: float | None = None
        listings: int
        bid_volume: int | None = None
        volume_24h: int | None = None
        available: bool | None = None
        phase: Phase | None = None
        fetched_at: datetime.datetime

    markets: dict[Market, Link]
    series: dict[Market, list[Observation]]


class SalesLatestAggregated(BaseModel):

    class Sale(BaseModel):
        id: int
        market: str
        mean_price: float | None = None
        min_price: float | None = None
        max_price: float | None = None
        median_price: float | None = None
        volume: int | None = None
        day: datetime.date

    market_hash_name: str
    sales: list[Sale]


class SalesHistoryAggregated(BaseModel):

    class Item(BaseModel):
        class Sale(BaseModel):
            id: int
            market: str
            mean_price: float | None = None
            min_price: float | None = None
            max_price: float | None = None
            median_price: float | None = None
            volume: int | None = None

        day: datetime.date
        sales: list[Sale]

    items: list[Item]


class Items(BaseModel):
    class Item(BaseModel):
        market_hash_name: str
        item_type: str | None = None
        weapon: str | None = None
        wear: str | None = None
        collection: str | None = None
        rarity: int | None = None
        icon_url: str | None = None
        min_float: float | None = None
        max_float: float | None = None
        is_stattrak: bool = False
        is_souvenir: bool = False

    items: list[Item]


class ItemContents(BaseModel):
    class Content(BaseModel):
        name: str
        icon_url: str | None = None
        rarity: str | None = None
        rarity_color: str | None = None
        is_rare: bool

    market_hash_name: str
    contents: list[Content]


class PlayerCountsLatest(BaseModel):
    timestamp: datetime.datetime
    count: int


class PlayerCountsHistory(BaseModel):
    class Item(BaseModel):
        timestamp: datetime.datetime
        count: int

    items: list[Item]


class Markets(BaseModel):
    class Market(BaseModel):
        market: str
        url: str
        currency: str
        active: bool

    items: list[Market]


class Account(BaseModel):
    class Usage(BaseModel):
        used: int
        used_percent: float
        limit: int
        remaining: int
        resets_in_days: int
        quota_unlimited: bool = False
        usage_billing_enabled: bool = False
        usage_budget_cents: int | None = None
        usage_overage_credits: int = 0
        usage_overage_limit: int = 0
        usage_billing_paused: bool = False
        discount_percent: int = 0
        list_price_cents: int = 999
        price_cents: int = 999
        savings_cents: int = 0

    email: str | None
    name: str
    plan: str
    quota_unlimited: bool
    usage: Usage
