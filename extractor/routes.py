"""
API routes for EPUB Structure Extractor
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select, func
from typing import List, Optional
from datetime import datetime

from database import get_db
from app.models import Book, Chapter, Metadata, ProcessingJob

router = APIRouter()

# Response models with additional computed fields
class BookResponse(Book):
    chapter_count: Optional[int] = None

# Request models for creation
class BookCreateRequest(Book):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# Books endpoints
@router.get("/books", response_model=List[BookResponse])
async def get_books(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """Get all books with pagination"""
    books = db.exec(select(Book).offset(skip).limit(limit)).all()
    
    # Add chapter count to each book
    result = []
    for book in books:
        chapter_count = db.exec(select(func.count(Chapter.id)).where(Chapter.book_id == book.id)).first()
        book_dict = book.dict()
        book_dict["chapter_count"] = chapter_count
        result.append(BookResponse(**book_dict))
    
    return result

@router.get("/books/{book_id}", response_model=BookResponse)
async def get_book(book_id: int, db: Session = Depends(get_db)):
    """Get a specific book by ID"""
    book = db.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # Add chapter count
    chapter_count = db.exec(select(func.count(Chapter.id)).where(Chapter.book_id == book.id)).first()
    book_dict = book.dict()
    book_dict["chapter_count"] = chapter_count
    
    return BookResponse(**book_dict)

@router.post("/books", response_model=BookResponse)
async def create_book(book_data: BookCreateRequest, db: Session = Depends(get_db)):
    """Create a new book"""
    new_book = Book(**book_data.dict(exclude_unset=True))
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    
    book_dict = new_book.dict()
    book_dict["chapter_count"] = 0
    return BookResponse(**book_dict)

@router.delete("/books/{book_id}")
async def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Delete a book and all its related data"""
    book = db.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    
    return {"message": f"Book '{book.title}' deleted successfully"}

# Chapters endpoints
@router.get("/books/{book_id}/chapters", response_model=List[Chapter])
async def get_book_chapters(book_id: int, db: Session = Depends(get_db)):
    """Get all chapters for a specific book"""
    # Verify book exists
    book = db.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    chapters = db.exec(select(Chapter).where(Chapter.book_id == book_id).order_by(Chapter.order_index)).all()
    return chapters

@router.get("/chapters/{chapter_id}", response_model=Chapter)
async def get_chapter(chapter_id: int, db: Session = Depends(get_db)):
    """Get a specific chapter by ID"""
    chapter = db.get(Chapter, chapter_id)
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")
    
    return chapter

# Metadata endpoints
@router.get("/books/{book_id}/metadata", response_model=List[Metadata])
async def get_book_metadata(book_id: int, db: Session = Depends(get_db)):
    """Get all metadata for a specific book"""
    # Verify book exists
    book = db.get(Book, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    metadata = db.exec(select(Metadata).where(Metadata.book_id == book_id)).all()
    return metadata

# Processing Jobs endpoints
@router.get("/jobs", response_model=List[ProcessingJob])
async def get_processing_jobs(
    status: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    """Get all processing jobs, optionally filtered by status"""
    query = select(ProcessingJob)
    
    if status:
        query = query.where(ProcessingJob.status == status)
    
    jobs = db.exec(query.order_by(ProcessingJob.created_at.desc())).all()
    return jobs

@router.get("/jobs/{job_id}", response_model=ProcessingJob)
async def get_processing_job(job_id: int, db: Session = Depends(get_db)):
    """Get a specific processing job by ID"""
    job = db.get(ProcessingJob, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Processing job not found")
    
    return job

# Statistics endpoints
@router.get("/stats")
async def get_statistics(db: Session = Depends(get_db)):
    """Get general statistics about the database"""
    stats = {
        "total_books": db.exec(select(func.count(Book.id))).first(),
        "total_chapters": db.exec(select(func.count(Chapter.id))).first(),
        "total_processing_jobs": db.exec(select(func.count(ProcessingJob.id))).first(),
        "jobs_by_status": {}
    }
    
    # Get job counts by status
    job_stats = db.exec(
        select(ProcessingJob.status, func.count(ProcessingJob.id))
        .group_by(ProcessingJob.status)
    ).all()
    
    for status, count in job_stats:
        stats["jobs_by_status"][status] = count
    
    # Get total word count
    total_words = db.exec(select(func.sum(Chapter.word_count))).first() or 0
    stats["total_words"] = total_words
    
    return stats

# Search endpoints
@router.get("/search/books", response_model=List[BookResponse])
async def search_books(
    q: str = Query(..., min_length=1),
    db: Session = Depends(get_db)
):
    """Search books by title, author, or description"""
    books = db.exec(select(Book).where(
        (Book.title.contains(q)) |
        (Book.author.contains(q)) |
        (Book.description.contains(q))
    )).all()
    
    # Add chapter count to each book
    result = []
    for book in books:
        chapter_count = db.exec(select(func.count(Chapter.id)).where(Chapter.book_id == book.id)).first()
        book_dict = book.dict()
        book_dict["chapter_count"] = chapter_count
        result.append(BookResponse(**book_dict))
    
    return result

@router.get("/search/chapters", response_model=List[Chapter])
async def search_chapters(
    q: str = Query(..., min_length=1),
    book_id: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    """Search chapters by title or content"""
    query = select(Chapter).where(
        (Chapter.title.contains(q)) |
        (Chapter.content.contains(q)) |
        (Chapter.summary.contains(q))
    )
    
    if book_id:
        query = query.where(Chapter.book_id == book_id)
    
    chapters = db.exec(query).all()
    return chapters