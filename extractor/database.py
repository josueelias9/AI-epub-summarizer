"""
Database configuration and session management
"""
from sqlmodel import SQLModel, create_engine, Session
from models import Book, Chapter, Metadata, ProcessingJob
from config import settings
from datetime import datetime
import os

# Get database URL from settings
DATABASE_URL = settings.database_url

# Create engine
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Set to False in production
    pool_pre_ping=True,  # Verify connections before use
    pool_recycle=300  # Recycle connections every 5 minutes
)

def get_db():
    """Dependency to get database session"""
    with Session(engine) as session:
        yield session

def init_db():
    """Initialize database and create tables"""
    print("Initializing database...")
    SQLModel.metadata.create_all(engine)
    print("Database tables created successfully!")
    
    # Add sample data
    populate_sample_data()

def populate_sample_data():
    """Populate database with sample data"""
    with Session(engine) as db:
        try:
        # Check if we already have data
        existing_books = db.query(Book).count()
        if existing_books > 0:
            print("Sample data already exists, skipping population.")
            return
        
        print("Populating sample data...")
        
        # Sample Book 1
        book1 = Book(
            title="The Art of Programming",
            author="John Doe",
            isbn="978-0123456789",
            description="A comprehensive guide to modern programming practices and methodologies.",
            language="en",
            publisher="Tech Publications",
            publication_date="2024",
            file_path="/path/to/book1.epub",
            file_size=2048576  # 2MB
        )
        db.add(book1)
        db.flush()  # To get the ID
        
        # Chapters for Book 1
        chapters1 = [
            Chapter(
                book_id=book1.id,
                title="Introduction to Programming",
                chapter_number=1,
                content="This chapter introduces basic programming concepts...",
                word_count=1250,
                summary="Introduction to fundamental programming concepts and paradigms.",
                file_name="chapter1.html",
                order_index=1
            ),
            Chapter(
                book_id=book1.id,
                title="Data Structures",
                chapter_number=2,
                content="Understanding various data structures and their applications...",
                word_count=2100,
                summary="Overview of arrays, lists, stacks, queues, and trees.",
                file_name="chapter2.html",
                order_index=2
            ),
            Chapter(
                book_id=book1.id,
                title="Algorithms",
                chapter_number=3,
                content="Exploring different algorithmic approaches and complexity analysis...",
                word_count=1890,
                summary="Introduction to sorting, searching, and optimization algorithms.",
                file_name="chapter3.html",
                order_index=3
            )
        ]
        
        for chapter in chapters1:
            db.add(chapter)
        
        # Metadata for Book 1
        metadata1 = [
            Metadata(book_id=book1.id, key="genre", value="Technology"),
            Metadata(book_id=book1.id, key="difficulty", value="Intermediate"),
            Metadata(book_id=book1.id, key="target_audience", value="Software Developers"),
            Metadata(book_id=book1.id, key="pages", value="342")
        ]
        
        for meta in metadata1:
            db.add(meta)
        
        # Sample Book 2
        book2 = Book(
            title="Modern Web Development",
            author="Jane Smith",
            isbn="978-0987654321",
            description="Learn to build modern web applications with the latest technologies.",
            language="en",
            publisher="Web Dev Press",
            publication_date="2024",
            file_path="/path/to/book2.epub",
            file_size=3145728  # 3MB
        )
        db.add(book2)
        db.flush()
        
        # Chapters for Book 2
        chapters2 = [
            Chapter(
                book_id=book2.id,
                title="HTML5 and CSS3 Fundamentals",
                chapter_number=1,
                content="Modern HTML5 semantic elements and CSS3 features...",
                word_count=1680,
                summary="Building blocks of modern web pages with HTML5 and CSS3.",
                file_name="web_chapter1.html",
                order_index=1
            ),
            Chapter(
                book_id=book2.id,
                title="JavaScript ES6+",
                chapter_number=2,
                content="Modern JavaScript features and best practices...",
                word_count=2340,
                summary="Modern JavaScript syntax, modules, and async programming.",
                file_name="web_chapter2.html",
                order_index=2
            )
        ]
        
        for chapter in chapters2:
            db.add(chapter)
        
        # Metadata for Book 2
        metadata2 = [
            Metadata(book_id=book2.id, key="genre", value="Web Development"),
            Metadata(book_id=book2.id, key="difficulty", value="Beginner"),
            Metadata(book_id=book2.id, key="target_audience", value="Web Developers"),
            Metadata(book_id=book2.id, key="pages", value="287")
        ]
        
        for meta in metadata2:
            db.add(meta)
        
        # Sample Processing Jobs
        job1 = ProcessingJob(
            book_id=book1.id,
            job_type="extraction",
            status="completed",
            progress=100,
            result_data='{"chapters_extracted": 3, "metadata_extracted": 4}',
            completed_at=datetime.utcnow()
        )
        
        job2 = ProcessingJob(
            book_id=book2.id,
            job_type="summarization",
            status="processing",
            progress=65
        )
        
        db.add(job1)
        db.add(job2)
        
        # Commit all changes
        db.commit()
        print("Sample data populated successfully!")
        
        except Exception as e:
            print(f"Error populating sample data: {e}")
            db.rollback()
            raisedef reset_db():
    """Reset database - drop all tables and recreate"""
    print("Resetting database...")
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    populate_sample_data()
    print("Database reset complete!")