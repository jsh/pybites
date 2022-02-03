"""Bite 130. Analyze some basic Car Data."""

from cars import get_models, most_prolific_automaker


def test_most_prolific_automaker_1999() -> None:
    """Most prolific automaker of 1999."""
    assert most_prolific_automaker(1999) == "Dodge"


def test_most_prolific_automaker_2008() -> None:
    """Most prolific automaker of 2008."""
    assert most_prolific_automaker(2008) == "Toyota"


def test_most_prolific_automaker_2013() -> None:
    """Most prolific automaker of 2013."""
    assert most_prolific_automaker(2013) == "Hyundai"


def test_get_models_volkswagen() -> None:
    """VW models for 2008."""
    models = get_models("Volkswagen", 2008)
    # sets are unordered
    assert len(models) == 2
    assert "Jetta" in models
    assert "Rabbit" in models


def test_get_models_nissan() -> None:
    """Nissan models 2000."""
    assert get_models("Nissan", 2000) == {"Pathfinder"}


def test_get_models_open() -> None:
    """Try to get missing models."""
    # not in data set
    assert get_models("Opel", 2008) == set()


def test_get_models_mercedes() -> None:
    """Mercedes models 2007."""
    models = get_models("Mercedes-Benz", 2007)
    assert len(models) == 3
    assert "SL-Class" in models
    assert "GL-Class" in models
    assert "CL-Class" in models
