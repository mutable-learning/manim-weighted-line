from typing import Any

from manim import config
from manim.constants import DEFAULT_FONT_SIZE, ITALIC, SMALL_BUFF
from manim.mobject.geometry.line import Line
from manim.mobject.text.text_mobject import Text
from manim.utils.color import WHITE


class WeightedLine(Line):
    """A line to display weighted edges in a network graph.

    Parameters
    ----------
    args
        Arguments to be passed to :class:`Line`
    weight
        The weight of the edge to display
    weight_config
        Dict of options to be passed to :class:`Text`
    weight_alpha
        The alpha position on the edge to show the weight
    bg_config
        Dict of options to be passed to :class:`Rectangle`
    add_bg
        Boolean to show a rectangle behind the weight
    kwargs
        Additional arguments to be passed to :class:`Line`

    """

    def __init__(
        self,
        *args: Any,
        weight: str | int | float | None = None,
        weight_config: dict | None = None,
        weight_alpha: float = 0.5,
        bg_config: dict | None = None,
        add_bg: bool = True,
        **kwargs: Any,
    ):
        self.weight = weight
        self.alpha = weight_alpha
        self.add_bg = add_bg
        super().__init__(*args, **kwargs)

        self.weight_config = {
            "color": WHITE,
            "slant": ITALIC,
            "font_size": DEFAULT_FONT_SIZE * 0.5,
        }

        if weight_config:
            self.weight_config.update(weight_config)

        self.bg_config = {
            "color": config.background_color,
            "opacity": 1,
        }
        if bg_config:
            self.bg_config.update(bg_config)

        if self.weight is not None:
            self._add_weight()

    def _add_weight(self):
        """
        Clears any current weight and then displays the weight is not none.

        Use weight_config dict to send options to the Text object.

        Use bg_config dict to send options to the background Rectangle object.

        """

        # Set the new weight if it is present

        point = self.point_from_proportion(self.alpha)
        label = Text(str(self.weight), **self.weight_config)
        label.move_to(point)

        if self.add_bg:
            label.add_background_rectangle(**self.bg_config)
            label.background_rectangle.height += SMALL_BUFF

        self.add(label)
