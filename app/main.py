"""Генератор приветствий."""


def greeting(name: str) -> str:
    """
    Возвращает текст приветствия.

      Args:
          name: Имя пользователя

      Returns:
          str: Текст приветствия
    """
    capitalized_name = name.title()
    return 'Привет, {capitalized_name}'.format(
        capitalized_name=capitalized_name,
    )
