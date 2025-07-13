#!/usr/bin/python3
""" The p[ackage initilization file
"""
from .engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
