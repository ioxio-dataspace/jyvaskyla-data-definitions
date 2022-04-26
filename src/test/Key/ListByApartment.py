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


class ListKeysByApartmentRequest(CamelCaseModel):
    apartment_id: str = Field(
        ...,
        title="Apartment ID",
        description="ID uniquely identifying the apartment",
        example="cb7f577e-8602-4374-8215-4ba8aba3903d",
    )


DEFINITION = DataProductDefinition(
    description="List keys by apartment",
    request=ListKeysByApartmentRequest,
    response=KeyListResponse,
    route_description="List keys for an apartment",
    summary="List keys for an apartment",
)
