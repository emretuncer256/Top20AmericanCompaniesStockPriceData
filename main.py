import json
from pathlib import Path

from data_fetcher import fetch_data

companies: dict[str, str] = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Alphabet (Google)": "GOOG",
    "Amazon": "AMZN",
    "NVIDIA": "NVDA",
    "Meta Platforms (Facebook)": "META",
    "Tesla": "TSLA",
    "Berkshire Hathaway": "BRK-B",
    "Eli Lilly": "LLY",
    "Walmart": "WMT",
    "Exxon Mobil Corporation": "XOM",
    "UnitedHealth Group Incorporated": "UNH",
    "CVS Health Corporation": "CVS",
    "McKesson Corporation": "MCK",
    "Chevron Corporation": "CVX",
    "AmerisourceBergen Corp": "ABG.BE",
    "Costco Wholesale Corporation": "COST",
    "Cardinal Health, Inc.": "CAH",
    "The Cigna Group": "CI",
    "Marathon Petroleum Corporation": "MPC"
}
industry = [
    "Electronics industry",
    "Technology and Cloud Computing",
    "Technology and Cloud Computing",
    "Retail and Cloud Computing",
    "Electronics industry and Cloud Computing",
    "Technology",
    "Automotive and Energy",
    "Conglomerate",
    "Pharmaceutical industry",
    "Retail",
    "Petroleum industry",
    "Healthcare",
    "Healthcare",
    "Health",
    "Petroleum industry",
    "Pharmaceutical industry",
    "Retail",
    "Healthcare",
    "Health Insurance",
    "Petroleum industry"
]
START: str = "2016-1-1"
END: str = "2023-12-30"
PATH: Path = Path("data")


def fetch_and_save_companies() -> None:
    prices = dict()

    for company, flag in companies.items():
        data = fetch_data(flag, START, END)
        print(f"{company} fetched.")
        prices[flag] = data

    for f, d in prices.items():
        path = PATH / (f + ".csv")
        d.to_csv(path)
        print(f"{f} saved to: {path}")


def save_metadata() -> None:
    metadata = {
        "start_date": START,
        "end_date": END,
        "companies": companies,
        "industry_types": industry
    }
    with open("metadata.json", "w") as file:
        file.write(json.dumps(metadata, indent=4))


if __name__ == '__main__':
    fetch_and_save_companies()
    save_metadata()
