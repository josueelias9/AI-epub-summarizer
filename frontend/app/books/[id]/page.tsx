'use client'

import { useActionState, useCallback, useEffect, useState } from 'react'
import { useParams, useRouter } from 'next/navigation'
import { BookInfo, ChapterInfo, SlidesResponse } from '@/app/lib/api'
import { listBooks, getChapters, getSlides, getLlmStatus } from '@/app/lib/data'
import {
    deleteBook,
    setChapterInclusion,
    summarizeBookAction,
    toggleAllChaptersAction,
    ToggleAllState
} from '@/app/lib/actions'
import ChapterList from '@/components/ChapterList'
import SlidesViewer from '@/components/SlidesViewer'

export default function BookDetailPage() {
    const { id } = useParams<{ id: string }>()
    const router = useRouter()

    const [book, setBook] = useState<BookInfo | null>(null)
    const [chapters, setChapters] = useState<ChapterInfo[]>([])
    const [loadingChapters, setLoadingChapters] = useState(true)
    const [error, setError] = useState<string | null>(null)

    const [summarizeResult, summarizeDispatch, isSummarizing] = useActionState(
        summarizeBookAction,
        { status: 'idle' as const, message: null }
    )

    const [toggleAllResult, toggleAllDispatch, isTogglingAll] = useActionState(
        toggleAllChaptersAction,
        { status: 'idle' as const, error: null } satisfies ToggleAllState
    )

    const [slidesData, setSlidesData] = useState<SlidesResponse | null>(null)
    const [showSlides, setShowSlides] = useState(false)
    const [loadingSlides, setLoadingSlides] = useState(false)

    const [llmConnected, setLlmConnected] = useState<boolean | null>(null)

    const fetchData = useCallback(async () => {
        if (!id) return
        setLoadingChapters(true)
        setError(null)
        try {
            const [chData, booksData] = await Promise.all([getChapters(id), listBooks()])
            setChapters(chData.chapters)
            const found = booksData.books.find(b => b.id === id) ?? null
            setBook(found)
        } catch (err: unknown) {
            setError(err instanceof Error ? err.message : 'Failed to load data')
        } finally {
            setLoadingChapters(false)
        }
    }, [id])

    useEffect(() => {
        fetchData()
        getLlmStatus()
            .then(s => setLlmConnected(s.connected))
            .catch(() => setLlmConnected(false))
    }, [fetchData])

    useEffect(() => {
        if (summarizeResult.status === 'done') fetchData()
    }, [summarizeResult, fetchData])

    useEffect(() => {
        if (toggleAllResult.status === 'done') fetchData()
    }, [toggleAllResult, fetchData])

    async function handleToggleChapter(number: string, include: boolean) {
        try {
            await setChapterInclusion(id, [number], include)
            setChapters(prev =>
                prev.map(ch =>
                    ch.number === number || ch.number.startsWith(number + '.')
                        ? { ...ch, include }
                        : ch
                )
            )
        } catch (err: unknown) {
            alert(err instanceof Error ? err.message : 'Failed to update chapter')
        }
    }

    async function handleViewSlides() {
        setLoadingSlides(true)
        try {
            const data = await getSlides(id)
            setSlidesData(data)
            setShowSlides(true)
        } catch (err: unknown) {
            alert(err instanceof Error ? err.message : 'Failed to load slides')
        } finally {
            setLoadingSlides(false)
        }
    }

    async function handleDeleteBook() {
        if (!confirm('Delete this book and all its data?')) return
        try {
            await deleteBook(id)
            router.push('/')
        } catch (err: unknown) {
            alert(err instanceof Error ? err.message : 'Delete failed')
        }
    }

    const includedCount = chapters.filter(c => c.include).length
    const summarizedCount = chapters.filter(c => c.has_summary).length

    return (
        <div className='space-y-6'>
            {/* Back */}
            <button
                onClick={() => router.push('/')}
                className='text-sm text-indigo-600 hover:underline'
            >
                ← Back to Library
            </button>

            {/* Book header */}
            {book && (
                <div className='bg-white rounded-2xl shadow p-6 flex items-start justify-between gap-4'>
                    <div>
                        <p className='text-xs text-indigo-500 uppercase tracking-wide font-semibold mb-1'>
                            EPUB
                        </p>
                        <h1 className='text-2xl font-bold text-gray-900'>{book.name}</h1>
                        {book.author && <p className='text-sm text-gray-500 mt-1'>{book.author}</p>}
                        <div className='flex gap-3 mt-3 text-sm text-gray-500'>
                            <span>{chapters.length} chapters</span>
                            <span>·</span>
                            <span>{includedCount} included</span>
                            <span>·</span>
                            <span>{summarizedCount} summarized</span>
                        </div>
                    </div>
                    <button
                        onClick={handleDeleteBook}
                        className='text-red-500 hover:text-red-700 text-sm shrink-0'
                    >
                        🗑️ Delete Book
                    </button>
                </div>
            )}

            {/* LLM warning */}
            {llmConnected === false && (
                <div className='bg-amber-50 border border-amber-200 rounded-xl px-4 py-3 text-sm text-amber-700'>
                    ⚠️ Ollama LLM is not reachable. Summarization will fail until it's connected.
                </div>
            )}

            <div className='grid grid-cols-1 lg:grid-cols-3 gap-6'>
                {/* Chapters */}
                <div className='lg:col-span-2 bg-white rounded-2xl shadow p-6'>
                    <div className='flex items-center justify-between mb-4'>
                        <h2 className='text-base font-bold text-gray-800'>
                            Chapters
                            <span className='ml-2 text-xs font-normal text-gray-400'>
                                Toggle to include/exclude from summary
                            </span>
                        </h2>
                        <div className='flex gap-2'>
                            <form action={toggleAllDispatch}>
                                <input type='hidden' name='book_id' value={id} />
                                <input type='hidden' name='include' value='true' />
                                <input
                                    type='hidden'
                                    name='chapter_numbers'
                                    value={JSON.stringify(chapters.map(c => c.number))}
                                />
                                <button
                                    type='submit'
                                    disabled={
                                        isTogglingAll ||
                                        loadingChapters ||
                                        chapters.every(c => c.include)
                                    }
                                    className='text-xs text-indigo-600 hover:underline disabled:opacity-40 disabled:no-underline'
                                >
                                    Select all
                                </button>
                            </form>
                            <span className='text-gray-300'>|</span>
                            <form action={toggleAllDispatch}>
                                <input type='hidden' name='book_id' value={id} />
                                <input type='hidden' name='include' value='false' />
                                <input
                                    type='hidden'
                                    name='chapter_numbers'
                                    value={JSON.stringify(chapters.map(c => c.number))}
                                />
                                <button
                                    type='submit'
                                    disabled={
                                        isTogglingAll ||
                                        loadingChapters ||
                                        chapters.every(c => !c.include)
                                    }
                                    className='text-xs text-indigo-600 hover:underline disabled:opacity-40 disabled:no-underline'
                                >
                                    Deselect all
                                </button>
                            </form>
                        </div>
                    </div>
                    {loadingChapters ? (
                        <p className='text-sm text-gray-400'>Loading chapters…</p>
                    ) : error ? (
                        <p className='text-sm text-red-500'>{error}</p>
                    ) : (
                        <ChapterList chapters={chapters} onToggle={handleToggleChapter} />
                    )}
                </div>

                {/* Actions */}
                <div className='space-y-4'>
                    <div className='bg-white rounded-2xl shadow p-6 space-y-3'>
                        <h2 className='text-base font-bold text-gray-800'>Actions</h2>

                        <form action={summarizeDispatch}>
                            <input type='hidden' name='book_id' value={id} />
                            <button
                                type='submit'
                                disabled={isSummarizing || includedCount === 0}
                                className='w-full flex items-center justify-center gap-2 bg-indigo-600 hover:bg-indigo-700 disabled:opacity-50 text-white font-semibold py-2.5 rounded-xl transition-colors'
                            >
                                {isSummarizing ? (
                                    <>
                                        <svg
                                            className='animate-spin h-4 w-4'
                                            viewBox='0 0 24 24'
                                            fill='none'
                                        >
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
                                        Summarizing…
                                    </>
                                ) : (
                                    '✨ Generate Summary'
                                )}
                            </button>
                        </form>

                        {summarizeResult.message && (
                            <p
                                className={`text-xs px-3 py-2 rounded-lg ${summarizeResult.status === 'error' ? 'bg-red-50 text-red-600' : 'bg-green-50 text-green-700'}`}
                            >
                                {summarizeResult.message}
                            </p>
                        )}

                        <button
                            onClick={handleViewSlides}
                            disabled={loadingSlides}
                            className='w-full flex items-center justify-center gap-2 bg-white hover:bg-gray-50 border border-gray-200 text-gray-700 font-semibold py-2.5 rounded-xl transition-colors'
                        >
                            {loadingSlides ? 'Loading…' : '🎞️ View as Slides'}
                        </button>
                    </div>

                    <div className='bg-indigo-50 rounded-2xl p-4 text-xs text-indigo-700'>
                        <p className='font-semibold mb-1'>How it works</p>
                        <ol className='list-decimal list-inside space-y-1'>
                            <li>Toggle chapters to include/exclude them</li>
                            <li>
                                Click <strong>Generate Summary</strong> to run AI
                            </li>
                            <li>View results as slides &amp; export to PDF</li>
                        </ol>
                    </div>
                </div>
            </div>

            {showSlides && slidesData && (
                <SlidesViewer
                    slides={slidesData.slides}
                    bookName={slidesData.book_name}
                    onClose={() => setShowSlides(false)}
                />
            )}
        </div>
    )
}
