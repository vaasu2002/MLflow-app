from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
SHORT_DESCRIPTION = "Write a short description of the project"
REPO_NAME = "REPO_NAME"
AUTHOR_USER_NAME = "vaasu2002"
SRC_REPO = "learning"
AUTHOR_EMAIL = "vaasu.bisht2021@vitbhopal.ac.in"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description=SHORT_DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email=AUTHOR_EMAIL,
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.6",
    install_requires=LIST_OF_REQUIREMENTS
)