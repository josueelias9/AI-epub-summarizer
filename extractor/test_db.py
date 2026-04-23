#!/usr/bin/env python3
"""
Database connection test script
"""
import sys
import os
from sqlmodel import create_engine, text
from config import settings

def test_database_connection():
    """Test the database connection"""
    print("Testing database connection...")
    print(f"Connecting to: {settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")
    print(f"User: {settings.DB_USER}")
    
    try:
        # Create engine
        engine = create_engine(settings.database_url)
        
        # Test connection
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version()"))
            version = result.fetchone()[0]
            print(f"✅ Connected successfully!")
            print(f"PostgreSQL version: {version}")
            
            # Test if tables exist
            result = connection.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
            """))
            tables = result.fetchall()
            
            if tables:
                print(f"📊 Found {len(tables)} tables:")
                for table in tables:
                    print(f"  - {table[0]}")
            else:
                print("📋 No tables found. Database is empty.")
                
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print("\nTroubleshooting:")
        print("1. Check if PostgreSQL container is running:")
        print("   docker ps | grep postgres")
        print("2. Check environment variables:")
        print(f"   DB_HOST={settings.DB_HOST}")
        print(f"   DB_PORT={settings.DB_PORT}")
        print(f"   POSTGRES_USER={settings.DB_USER}")
        print(f"   POSTGRES_DB={settings.DB_NAME}")
        print("3. Check if the database exists in PostgreSQL")
        sys.exit(1)

if __name__ == "__main__":
    test_database_connection()