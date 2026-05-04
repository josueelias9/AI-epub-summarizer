'use client'

import { useCallback, useEffect, useState } from 'react'
import { api, BookInfo } from '@/lib/api'
import BookCard from '@/components/BookCard'
import UploadModal from '@/components/UploadModal'
import { useRouter } from 'next/navigation'

export default function HomePage() {
    const router = useRouter()
    const [books, setBooks] = useState<BookInfo[]>([])
    const [loading, setLoading] = useState(true)
    const [showUpload, setShowUpload] = useState(false)
    const [error, setError] = useState<string | null>(null)

    const fetchBooks = useCallback(async () => {
        setLoading(true)
        setError(null)
        try {
            const data = await api.books.list()
            setBooks(data.books)
        } catch (err: unknown) {
            setError(err instanceof Error ? err.message : 'Failed to load books')
        } finally {
            setLoading(false)
        }
    }, [])

    useEffect(() => {
        fetchBooks()
    }, [fetchBooks])

    async function handleDelete(id: string) {
        if (!confirm('Delete this book and all its data?')) return
        try {
            await api.books.delete(id)
            setBooks(prev => prev.filter(b => b.id !== id))
        } catch (err: unknown) {
            alert(err instanceof Error ? err.message : 'Delete failed')
        }
    }

    function handleUploaded(bookId: string, bookName: string) {
        setShowUpload(false)
        router.push(`/books/${bookId}`)
    }

    return (
        <div>
            <div className='flex items-center justify-between mb-6'>
                <div>
                    <h1 className='text-2xl font-bold text-gray-900'>Your Library</h1>
                    <p className='text-sm text-gray-500 mt-0.5'>
                        Upload an EPUB to summarize it chapter by chapter
                    </p>
                </div>
                <button
                    onClick={() => setShowUpload(true)}
                    className='bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-4 py-2 rounded-xl shadow transition-colors'
                >
                    + Upload EPUB
                </button>
            </div>

            {loading && (
                <div className='flex items-center justify-center py-20 text-gray-400'>
                    <svg className='animate-spin h-6 w-6 mr-2' viewBox='0 0 24 24' fill='none'>
                        <circle
                            className='opacity-25'
                            cx='12'
                            cy='12'
                            r='10'
                            stroke='currentColor'
                            strokeWidth='4'
                        />
                        <path
                            className='opacity-75'
                            fill='currentColor'
                            d='M4 12a8 8 0 018-8v8H4z'
                        />
                    </svg>
                    Loading…
                </div>
            )}

            {!loading && error && (
                <div className='bg-red-50 border border-red-200 rounded-xl p-4 text-sm text-red-700'>
                    {error}{' '}
                    <button onClick={fetchBooks} className='underline ml-1'>
                        Retry
                    </button>
                </div>
            )}

            {!loading && !error && books.length === 0 && (
                <div className='text-center py-20'>
                    <p className='text-5xl mb-4'>📚</p>
                    <p className='text-gray-500 mb-4'>
                        No books yet. Upload your first EPUB to get started.
                    </p>
                    <button
                        onClick={() => setShowUpload(true)}
                        className='bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-6 py-2 rounded-xl transition-colors'
                    >
                        Upload EPUB
                    </button>
                </div>
            )}

            {!loading && !error && books.length > 0 && (
                <div className='grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4'>
                    {books.map(book => (
                        <BookCard key={book.id} book={book} onDelete={handleDelete} />
                    ))}
                </div>
            )}

            {showUpload && (
                <UploadModal onUploaded={handleUploaded} onClose={() => setShowUpload(false)} />
            )}
        </div>
    )
}
