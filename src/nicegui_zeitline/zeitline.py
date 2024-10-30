from pathlib import Path
from typing import Any, Callable, Optional, Union

from nicegui.elements.mixins.disableable_element import DisableableElement


class Zeitline(
    DisableableElement,
    component="zeitline.js",
    dependencies=["lib/zeitline/zeitline.bundle.min.js"],
    default_classes="nicegui-zeitline",
):
    # VALUE_PROP: str = 'value'
    LOOPBACK = False

    def __init__(
        self,
        *,
        width: int,
        height: int,
        events: Optional[list[Union[str, tuple[str, str]]]] = None,
    ) -> None:
        """Zeitline

        An interactive polylinear timeline.

        """
        super().__init__()
        self._props["width"] = width
        self._props["height"] = height
        self._props["conf"] = {}
        if events is not None:
            for event in events:
                args = [event] if isinstance(event, str) else [*event]
                self.add_event(*args)

    def add_event(self, date: str, label: str = ""):
        self._props["conf"].setdefault("data", []).append(
            {"date": date, "label": label}
        )
        self.update()

    def set_range(self, start: str, end: str):
        self._props["conf"]["dateRange"] = [start, end]
        self.update()

    def add_interval(self, start: str, end: str, weight: int = 100):
        self._props["conf"].setdefault("intervals", []).append([start, end, weight])
        self.update()
