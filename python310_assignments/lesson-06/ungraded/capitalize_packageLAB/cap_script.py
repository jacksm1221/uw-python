#!/usr/bin/env python

"""
A really simple script just to demonstrate packaging
"""
import main
import importlib.metadata

if __name__ == "__main__":
    main.main()


def version(package: str) -> str:
    try:
        return importlib.metadata.version(package)
    except importlib.metadata.PackageNotFoundError:
        return "0.0.0"

__version__ = version(__name__)