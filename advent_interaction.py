import os
from pathlib import Path
from dotenv import load_dotenv
from loguru import logger
import httpx

ENV_PATH = Path().parent.joinpath(".env")
ENV_ADVENT_COOKIE = "ADVENT_COOKIE"


def load_advent_cookie() -> str:
    logger.debug(f"Loading env from '{ENV_PATH}'")
    load_dotenv(ENV_PATH)
    return os.environ[ENV_ADVENT_COOKIE]


def _build_problem_url(day: int) -> str:
    return f"https://adventofcode.com/2023/day/{day}/input"


def _build_stored_path(day: int) -> Path:
    return Path(f"data/input_day_{day}.txt")


def _get_input_from_website(day: int) -> Path:
    response = httpx.get(
        _build_problem_url(day),
        headers={
            "Cookie": load_advent_cookie()
        }
    )
    data_path = _build_stored_path(day)
    with open(data_path, "w") as f:
        f.write(response.text)
    return data_path


def get_problem_input(day: int) -> str:
    logger.info("Getting problem input")
    data_path = _build_stored_path(day)
    if not data_path.exists():
        _get_input_from_website(day)
    with open(data_path, "r") as f:
        return f.read()
