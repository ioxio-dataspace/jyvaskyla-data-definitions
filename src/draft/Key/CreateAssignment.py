from converter import CamelCaseModel, DataProductDefinition
from pydantic import Field


class CreateAssignment(CamelCaseModel):
    key_id: str = Field(
        ...,
        title="Key ID",
        description="UID of a key as a hex encoded string without delimiters",
        example="a1b2c3d4e5f6890",
        min_length=1,
        regex=r"^[0-9a-f]+$",
    )
    lock_id: str = Field(
        ...,
        title="Lock ID",
        description="Vendor specific ID for a lock",
        example="12345678",
        min_length=1,
    )


DEFINITION = DataProductDefinition(
    description="Create key assignment",
    request=CreateAssignment,
    response=CreateAssignment,
    route_description="Create assignment",
    summary="Create key assignment",
)
