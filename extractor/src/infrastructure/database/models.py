"""
SQLModel ORM models — infrastructure concern only.
These map to the database tables and are separate from domain entities.
"""
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, Text
from typing import Optional, List
from datetime import datetime
