from typing import List

from converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class KeyEntry(CamelCaseModel):
    key_id: str = Field(
        ...,
        title="Key ID",
        description="UID of a key as a hex encoded string without delimiters",
        example="a1b2c3d4e5f6890",
        min_length=1,
        regex=r"^[0-9a-f]+$",
    )


class KeyListResponse(CamelCaseModel):
    keys: List[KeyEntry] = Field([], example=[KeyEntry(key_id="a1b2c3d4e5f6890")])


class ListKeysByPersonRequest(CamelCaseModel):
    person_id: str = Field(
        ...,
        title="Person ID",
        description="ID uniquely identifying the person",
        example="34bd224c-9b4d-4c70-b04e-3fec52064867",
    )


DEFINITION = DataProductDefinition(
    description="List keys by person",
    request=ListKeysByPersonRequest,
    response=KeyListResponse,
    route_description="List keys for a person",
    summary="List keys for a person",
)
