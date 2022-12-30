from fake_useragent import UserAgent
from requests import get, Response
from random import choice


class NitroCode:
    def __init__(
        self, code: str = "random", length: int = 16, valid: bool | None = None
    ) -> None:
        self.valid: bool | None = valid
        self.length: str = length
        if code != "random":
            self.code: str = code
        else:
            self.code: str = "".join(
                choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
                for _ in range(length)
            )

    def check(self, fake_useragent: bool = True) -> bool | float:
        if fake_useragent:
            headers: dict = {"User-Agent": UserAgent().random}
        else:
            headers: dict = {}
        response: Response = get(
            url=f"https://discord.com/api/v10/entitlements/gift-codes/{self.code}",
            headers=headers,
        )
        if response.status_code == 200:
            self.valid: bool = True
        elif response.status_code == 404:
            self.valid: bool = False
        elif response.status_code == 429:
            return response.json().get("retry_after")
        return self.valid

    def write(self) -> None:
        if self.valid == None:
            with open("results/unknown.txt", "a") as unknowns_file:
                unknowns_file.write(f"{self.code}\n")
        elif self.valid == True:
            with open("results/valid.txt", "a") as valids_file:
                valids_file.write(f"{self.code}\n")
        elif self.valid == False:
            with open("results/invalid.txt", "a") as invalids_file:
                invalids_file.write(f"{self.code}\n")
