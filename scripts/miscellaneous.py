from os.path import isfile, isdir, exists
from json import load, dumps, decoder
from os import name, system, mkdir


def clear_screen() -> None:
    if name == "nt":
        system("cls")
    else:
        system("clear")


def repair_config(config_filename: str = "config.json") -> None:
    with open(config_filename, "w") as config_file:
        config_file.write(
            dumps(
                {
                    "generation_settings": {"code_length": 16},
                    "checking_settings": {
                        "sleep_double_time_on_ratelimit": False,
                        "sleep_on_ratelimit": True,
                        "use_random_user_agent": True,
                    },
                    "display_settings": {
                        "use_color_on_check": True,
                        "use_color_on_input": True,
                        "use_color_on_rate_limit": True,
                        "display_code_with_url": False,
                    },
                },
                indent=4,
            )
        )


def get_config() -> dict:
    try:
        with open("config.json", "r") as config_file:
            config: dict = load(config_file)
    except (FileNotFoundError, decoder.JSONDecodeError):
        repair_config("config.json")
        return get_config()
    else:
        return config


def ensure_files() -> None:
    if not exists("results") or not isdir("results"):
        mkdir("results")
        open("invalid.txt", "w").close()
        open("valid.txt", "w").close()
        return
    if not exists("results/invalid.txt") or not isfile("results/invalid.txt"):
        open("invalid.txt", "w").close()
    if not exists("results/valid.txt") or not isfile("results/valid.txt"):
        open("valid.txt", "w").close()
