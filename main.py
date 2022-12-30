from scripts.install import *

install_requirements(check_requirements())
from scripts.miscellaneous import *
from scripts.classes import *
from colorama import Fore
from time import sleep


def main() -> None:
    ensure_files()
    CONFIG: dict = get_config()
    clear_screen()
    while True:
        nitro_code: NitroCode = NitroCode(
            length=CONFIG["generation_settings"]["code_length"]
        )
        results: bool | float | int = nitro_code.check(
            fake_useragent=CONFIG["checking_settings"]["use_random_user_agent"]
        )
        if results == True:
            if CONFIG["display_settings"]["use_color_on_check"]:
                print(f"{Fore.GREEN}Valid code: {nitro_code.code}{Fore.WHITE}")
            else:
                print(f"Valid code: {nitro_code.code}")
            nitro_code.write()
        elif results == False:
            if CONFIG["display_settings"]["use_color_on_check"]:
                print(f"{Fore.RED}Invalid code: {nitro_code.code}{Fore.WHITE}")
            else:
                print(f"Invalid code: {nitro_code.code}")
            nitro_code.write()
        elif isinstance(results, float | int):
            if not CONFIG["checking_settings"]["sleep_on_ratelimit"]:
                if CONFIG["display_settings"]["use_color_on_rate_limit"]:
                    print(f"{Fore.MAGENTA}Ratelimited!{Fore.WHITE}")
                else:
                    print(f"Ratelimited!")
            else:
                if CONFIG["checking_settings"]["sleep_double_time_on_ratelimit"]:
                    sleep_time: float = results * 2
                else:
                    sleep_time: float = results
                if CONFIG["display_settings"]["use_color_on_rate_limit"]:
                    print(
                        f"{Fore.MAGENTA}Ratelimited! Waiting {sleep_time} seconds...{Fore.WHITE}"
                    )
                else:
                    print(f"Ratelimited! Waiting {sleep_time} seconds...")
                sleep(sleep_time)


if __name__ == "__main__":
    main()
