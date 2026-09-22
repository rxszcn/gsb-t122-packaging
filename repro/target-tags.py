"""为目标环境枚举这条路上，短名表与本机参数各自的表现

跑法：PYTHONPATH=src .venv/bin/python repro/target-tags.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import inspect

from packaging import tags

print("generic_tags:", [str(t) for t in list(tags.generic_tags(interpreter="cpython312", platforms=["any"]))[:2]])
print("compatible_tags 尾部:", [str(t) for t in list(tags.compatible_tags(python_version=(3, 12), interpreter="cpython", platforms=["any"]))[-3:]])
print("sys_tags 签名:", inspect.signature(tags.sys_tags))
print("platform_tags 签名:", inspect.signature(tags.platform_tags))
print("短名表:", tags.INTERPRETER_SHORT_NAMES)
