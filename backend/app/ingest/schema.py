from enum import Enum

from pydantic import BaseModel, Field


class TimeOfDay(str, Enum):
    unknown = "unknown"
    day = "day"
    night = "night"
    dawn = "dawn"
    dusk = "dusk"


class Interior(str, Enum):
    unknown = "unknown"
    interior = "interior"
    exterior = "exterior"


class ShotSize(str, Enum):
    unknown = "unknown"
    ecu = "ecu"
    cu = "cu"
    mcu = "mcu"
    ms = "ms"
    mls = "mls"
    ls = "ls"
    els = "els"


class CameraMove(str, Enum):
    unknown = "unknown"
    static = "static"
    pan = "pan"
    tilt = "tilt"
    dolly = "dolly"
    handheld = "handheld"
    zoom = "zoom"
    crane = "crane"


class ShotMeta(BaseModel):
    caption: str = Field(description="Two or three sentences an editor would write in a shot log: who, where, what happens, how it is framed and lit.")
    people_count: int = Field(ge=0)
    time_of_day: TimeOfDay
    interior: Interior
    weather: str = Field(description="Visible weather or 'none' if indoors or not applicable.")
    shot_size: ShotSize
    camera_move: CameraMove
    emotion: str = Field(description="Dominant emotional tone in one or two words.")
    tension: int = Field(ge=1, le=5, description="1 calm to 5 peak tension.")
    dialogue_present: bool
    dominant_colors: list[str]
    objects: list[str] = Field(description="Notable props, vehicles, animals, set pieces.")
    characters: list[str] = Field(description="Short visual descriptors of each person on screen, e.g. 'woman in trench coat'.")
