
# CSMarketAPI Client

Asynchronous Python client for [CSMarketAPI](https://csmarketapi.com) — typed responses (Pydantic), enums for marketplaces/currencies, and convenient async context managers.

## Highlights

- **Async & Fast:** Use with `async with CSMarketAPI(...)`
- **Typed Models:** All responses are Pydantic models
- **Enums:** For `Market`, `Currency` and `Phase`
- **Modern Python:** 3.13+, type hints everywhere

---

## Installation

```bash
pip install csmarketapi
```

---

## Requirements

- Python 3.13+
- CSMarketAPI API key

---

## Quickstart

```python
import asyncio
from csmarketapi import CSMarketAPI
from csmarketapi.enums import Market, Currency

async def main():
    async with CSMarketAPI("YOUR_API_KEY") as client:
        items = await client.get_items()
        print(f"Loaded {len(items.items)} items.")

asyncio.run(main())
```

---

## Usage Examples

All methods are async and return Pydantic models.

### Listings (Latest)
```python
async with CSMarketAPI("YOUR_API_KEY") as client:
    res = await client.get_listings_latest_aggregated(
        market_hash_name="Chroma 2 Case",
        markets=list(Market),
        currency=Currency.USD,
    )
    print(res.market_hash_name, res.listings[0].market, res.listings[0].ask_price)
```

### Sales (Latest)
```python
async with CSMarketAPI("YOUR_API_KEY") as client:
    res = await client.get_sales_latest_aggregated(
        market_hash_name="Chroma 2 Case",
        markets=[Market.SKINPORT, Market.SKINBARON]
    )
    print(res.sales[0].market, res.sales[0].median_price)
```

### Item Contents
```python
async with CSMarketAPI("YOUR_API_KEY") as client:
    res = await client.get_item_contents(market_hash_name="Kilowatt Case")
    print(res.contents)
```

### Account
```python
async with CSMarketAPI("YOUR_API_KEY") as client:
    account = await client.get_account()
    print(account.plan, account.usage.remaining)
```

---

## Error Handling & Tipps

- Wrap API calls in `try/except` for network errors
- Optional fields may be `None`
- Use `markets=list(Market)` for all markets

---

## License

MIT 

---

