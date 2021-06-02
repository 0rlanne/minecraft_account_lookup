import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Mini_projet",
    version="1",
    license="MIT",
    author="Hoxtry",
    author_email="Sousousasori@gmail.com",
    description="Minecraft user information",
    long_description="little project for get all information about an user (using mijang api and namemc api ",
    url="https://github.com/hoxtry",
    packages=setuptools.find_packages(),
    install_requires = ["requests", "bs4"],
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)