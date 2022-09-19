from setuptools import setup, find_packages
from audit_tools import __VERSION__

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="coinfabrik-audit-tools",
    description="Internal tools made by Coinfabrik audit team",
    url="https://gitlab.com/coinfabrik-private/audit-tools",
    author="Coinfabrik audits team",
    version=__VERSION__,
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    license="mit",
    long_description=long_description,
    entry_points={
        "console_scripts": [
            "estimate-sol = estimate_sol.estimate_script:run",
        ],
    },
)