"""基于 rich 的美观终端输出工具.

提供全局 ``console`` 实例供各模块统一使用，确保输出风格一致.
"""

from rich.console import Console

console = Console()
