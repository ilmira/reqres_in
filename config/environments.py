from dataclasses import dataclass
from enum import Enum


class Environment(str, Enum):
    DEV = "dev"
    STAGE = "stage"

    def __str__(self):
        return {
            self.DEV: "Dev",
            self.STAGE: "Stage"
        }[self]


@dataclass
class EnvironmentConfig:
    reqres_url: str

    def __str__(self):
        return f"- Reqres API: {self.reqres_url}"


environments = {
    Environment.DEV: EnvironmentConfig(
        reqres_url="https://reqres.in/api"
    ),
    Environment.STAGE: EnvironmentConfig(
        reqres_url="https://reqres.in/api"
    )
}
