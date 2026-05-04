'use client'

import { BookInfo } from '@/lib/api'
import { useRouter } from 'next/navigation'

interface Props {
    book: BookInfo
    onDelete: (id: string) => void
}

export default function BookCard({ book, onDelete }: Props) {
    const router = useRouter()

    return (
        <div className='bg-white rounded-xl shadow hover:shadow-md transition-shadow border border-gray-100 flex flex-col'>
            <button
                onClick={() => router.push(`/books/${book.id}`)}
                className='flex-1 p-5 text-left'
            >
                <p className='text-xs text-indigo-500 font-semibold uppercase tracking-wide mb-1'>
                    EPUB
                </p>
                <h2 className='text-lg font-bold text-gray-800 line-clamp-2 mb-1'>{book.name}</h2>
                {book.author && <p className='text-sm text-gray-500'>{book.author}</p>}
                {book.language && (
                    <span className='mt-2 inline-block text-xs bg-indigo-50 text-indigo-600 px-2 py-0.5 rounded-full'>
                        {book.language}
                    </span>
                )}
            </button>
            <div className='border-t border-gray-100 px-5 py-3 flex justify-between items-center'>
                <button
                    onClick={() => router.push(`/books/${book.id}`)}
                    className='text-sm text-indigo-600 hover:underline font-medium'
                >
                    Open →
                </button>
                <button
                    onClick={() => onDelete(book.id)}
                    className='text-sm text-red-500 hover:text-red-700'
                    title='Delete book'
                >
                    🗑️ Delete
                </button>
            </div>
        </div>
    )
}
