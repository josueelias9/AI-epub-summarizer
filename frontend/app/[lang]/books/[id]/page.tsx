'use client'

import { useActionState, useCallback, useEffect, useMemo, useState } from 'react'
import { useParams, useRouter } from 'next/navigation'
import { BookInfo, ChapterInfo, SlidesResponse } from '@/app/lib/api'
import { listBooks, getChapters, getSlides, getLlmStatus } from '@/app/lib/data'
import {
    deleteBook,
    setChapterInclusion,
    toggleAllChaptersAction,
    ToggleAllState
} from '@/app/lib/actions'
import ChapterList from '@/components/ChapterList'
import SlidesViewer from '@/components/SlidesViewer'
import { useDictionary } from '../../DictionaryProvider'

const API_URL = `${process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'}/api/v1`

type SummaryJobStatus = {
    job_id: string
    book_id: string
    status: 'queued' | 'processing' | 'completed' | 'failed'
    chapters_total: number
    chapters_summarized: number
    error_message: string | null
}

async function handleResponse<T>(res: Response): Promise<T> {
    if (!res.ok) {
        const err = await res.json().catch(() => ({ detail: res.statusText }))
        throw new Error(err.detail ?? res.statusText)
    }
    return res.json() as Promise<T>
}

// TODO: why these methods are not in the data layer?
async function enqueueSummary(bookId: string): Promise<SummaryJobStatus> {
    return fetch(`${API_URL}/epub/summarize/queue`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ book_id: bookId })
    }).then(r => handleResponse(r))
}

async function getSummaryJobStatus(jobId: string): Promise<SummaryJobStatus> {
    return fetch(`${API_URL}/epub/summarize/jobs/${jobId}`).then(r => handleResponse(r))
}

async function getLatestSummaryJob(bookId: string): Promise<SummaryJobStatus | null> {
    const res = await fetch(`${API_URL}/epub/summarize/jobs/latest/${bookId}`)
    if (res.status === 404) return null
    return handleResponse(res)
}

export default function BookDetailPage() {
    const { id, lang } = useParams<{ id: string; lang: string }>()
    const router = useRouter()
    const dict = useDictionary()
    const t = dict.bookDetail

    const [book, setBook] = useState<BookInfo | null>(null)
    const [chapters, setChapters] = useState<ChapterInfo[]>([])
    const [loadingChapters, setLoadingChapters] = useState(true)
    const [error, setError] = useState<string | null>(null)

    const [summaryJob, setSummaryJob] = useState<SummaryJobStatus | null>(null)
    const [isQueueingSummary, setIsQueueingSummary] = useState(false)
    const [summaryMessage, setSummaryMessage] = useState<{
        status: 'idle' | 'info' | 'success' | 'error'
        message: string | null
    }>({ status: 'idle', message: null })

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
            setError(err instanceof Error ? err.message : t.failedToLoad)
        } finally {
            setLoadingChapters(false)
        }
    }, [id, t.failedToLoad])

    useEffect(() => {
        fetchData()
        getLlmStatus()
            .then(s => setLlmConnected(s.connected))
            .catch(() => setLlmConnected(false))

        if (!id) return
        getLatestSummaryJob(id)
            .then(job => {
                if (!job) return
                setSummaryJob(job)
                if (job.status === 'processing' || job.status === 'queued') {
                    setSummaryMessage({ status: 'info', message: t.summaryBackgroundInfo })
                }
            })
            .catch(() => {
                // Non-fatal: page should still load even if job history endpoint fails.
            })
    }, [fetchData])

    useEffect(() => {
        if (toggleAllResult.status === 'done') fetchData()
    }, [toggleAllResult, fetchData])

    useEffect(() => {
        if (!summaryJob || (summaryJob.status !== 'queued' && summaryJob.status !== 'processing')) {
            return
        }

        const intervalId = setInterval(async () => {
            try {
                const next = await getSummaryJobStatus(summaryJob.job_id)
                setSummaryJob(next)
                if (next.status === 'completed') {
                    setSummaryMessage({
                        status: 'success',
                        message: t.summaryCompleted.replace('{count}', String(next.chapters_summarized))
                    })
                    fetchData()
                }
                if (next.status === 'failed') {
                    setSummaryMessage({
                        status: 'error',
                        message: next.error_message || t.summaryFailed
                    })
                }
            } catch (err: unknown) {
                setSummaryMessage({
                    status: 'error',
                    message: err instanceof Error ? err.message : t.summaryStatusError
                })
            }
        }, 3000)

        return () => clearInterval(intervalId)
    }, [summaryJob, fetchData, t.summaryCompleted, t.summaryFailed, t.summaryStatusError])

    async function handleGenerateSummary() {
        setIsQueueingSummary(true)
        try {
            const queued = await enqueueSummary(id)
            setSummaryJob(queued)
            setSummaryMessage({ status: 'info', message: t.summaryQueued })
        } catch (err: unknown) {
            setSummaryMessage({
                status: 'error',
                message: err instanceof Error ? err.message : t.summaryFailed
            })
        } finally {
            setIsQueueingSummary(false)
        }
    }

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
            alert(err instanceof Error ? err.message : t.failedToUpdate)
        }
    }

    async function handleViewSlides() {
        setLoadingSlides(true)
        try {
            const data = await getSlides(id)
            setSlidesData(data)
            setShowSlides(true)
        } catch (err: unknown) {
            alert(err instanceof Error ? err.message : t.failedToLoadSlides)
        } finally {
            setLoadingSlides(false)
        }
    }

    async function handleDeleteBook() {
        if (!confirm(t.deleteConfirm)) return
        try {
            await deleteBook(id)
            router.push(`/${lang}/library`)
        } catch (err: unknown) {
            alert(err instanceof Error ? err.message : t.deleteFailed)
        }
    }

    const includedCount = chapters.filter(c => c.include).length
    const summarizedCount = chapters.filter(c => c.has_summary).length
    const isSummaryActive = summaryJob?.status === 'queued' || summaryJob?.status === 'processing'

    const summaryStatusLabel = useMemo(() => {
        if (!summaryJob) return ''
        if (summaryJob.status === 'queued') return t.queued
        if (summaryJob.status === 'processing') return t.processing
        if (summaryJob.status === 'completed') return t.completed
        return t.failed
    }, [summaryJob, t])

    const summaryButtonLabel = useMemo(() => {
        if (isQueueingSummary) return t.summaryQueueing
        if (summaryJob?.status === 'queued') return t.summaryQueuedButton
        if (summaryJob?.status === 'processing') return t.summaryProcessingButton
        return t.generateSummary
    }, [isQueueingSummary, summaryJob, t])

    return (
        <div className='space-y-6'>
            {/* Back */}
            <button
                onClick={() => router.push(`/${lang}/library`)}
                className='text-sm text-indigo-600 hover:underline'
            >
                {t.backToLibrary}
            </button>

            {/* Book header */}
            {book && (
                <div className='bg-white rounded-2xl shadow p-6 flex items-start justify-between gap-4'>
                    <div>
                        <p className='text-xs text-indigo-500 uppercase tracking-wide font-semibold mb-1'>
                            {t.epub}
                        </p>
                        <h1 className='text-2xl font-bold text-gray-900'>{book.name}</h1>
                        {book.author && <p className='text-sm text-gray-500 mt-1'>{book.author}</p>}
                        <div className='flex gap-3 mt-3 text-sm text-gray-500'>
                            <span>
                                {chapters.length} {t.chaptersCount}
                            </span>
                            <span>·</span>
                            <span>
                                {includedCount} {t.includedCount}
                            </span>
                            <span>·</span>
                            <span>
                                {summarizedCount} {t.summarizedCount}
                            </span>
                        </div>
                    </div>
                    <button
                        onClick={handleDeleteBook}
                        className='text-red-500 hover:text-red-700 text-sm shrink-0'
                    >
                        {t.deleteBook}
                    </button>
                </div>
            )}

            {/* LLM warning */}
            {llmConnected === false && (
                <div className='bg-amber-50 border border-amber-200 rounded-xl px-4 py-3 text-sm text-amber-700'>
                    {t.llmWarning}
                </div>
            )}

            <div className='grid grid-cols-1 lg:grid-cols-3 gap-6'>
                {/* Chapters */}
                <div className='lg:col-span-2 bg-white rounded-2xl shadow p-6'>
                    <div className='flex items-center justify-between mb-4'>
                        <h2 className='text-base font-bold text-gray-800'>
                            {t.chaptersTitle}
                            <span className='ml-2 text-xs font-normal text-gray-400'>
                                {t.chaptersHint}
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
                                    {t.selectAll}
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
                                    {t.deselectAll}
                                </button>
                            </form>
                        </div>
                    </div>
                    {loadingChapters ? (
                        <p className='text-sm text-gray-400'>{t.loadingChapters}</p>
                    ) : error ? (
                        <p className='text-sm text-red-500'>{error}</p>
                    ) : (
                        <ChapterList chapters={chapters} onToggle={handleToggleChapter} />
                    )}
                </div>

                {/* Actions */}
                <div className='space-y-4'>
                    <div className='bg-white rounded-2xl shadow p-6 space-y-3'>
                        <h2 className='text-base font-bold text-gray-800'>{t.actionsTitle}</h2>

                        <button
                            onClick={handleGenerateSummary}
                            disabled={isSummaryActive || isQueueingSummary || includedCount === 0}
                            className='w-full flex items-center justify-center gap-2 bg-indigo-600 hover:bg-indigo-700 disabled:opacity-50 text-white font-semibold py-2.5 rounded-xl transition-colors'
                        >
                            {(isSummaryActive || isQueueingSummary) && (
                                <svg className='animate-spin h-4 w-4' viewBox='0 0 24 24' fill='none'>
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
                            )}
                            {summaryButtonLabel}
                        </button>

                        {summaryJob && (
                            <div className='text-xs px-3 py-2 rounded-lg bg-blue-50 text-blue-700 border border-blue-100'>
                                <p className='font-semibold'>
                                    {t.summaryJobLabel}: {summaryStatusLabel}
                                </p>
                                <p>
                                    {summaryJob.chapters_summarized}/{summaryJob.chapters_total}{' '}
                                    {t.summaryProgressSuffix}
                                </p>
                            </div>
                        )}

                        {summaryMessage.message && (
                            <p
                                className={`text-xs px-3 py-2 rounded-lg ${summaryMessage.status === 'error' ? 'bg-red-50 text-red-600' : summaryMessage.status === 'success' ? 'bg-green-50 text-green-700' : 'bg-amber-50 text-amber-700'}`}
                            >
                                {summaryMessage.message}
                            </p>
                        )}

                        <button
                            onClick={handleViewSlides}
                            disabled={loadingSlides}
                            className='w-full flex items-center justify-center gap-2 bg-white hover:bg-gray-50 border border-gray-200 text-gray-700 font-semibold py-2.5 rounded-xl transition-colors'
                        >
                            {loadingSlides ? t.loadingSlides : t.viewSlides}
                        </button>
                    </div>

                    <div className='bg-indigo-50 rounded-2xl p-4 text-xs text-indigo-700'>
                        <p className='font-semibold mb-1'>{t.howItWorksTitle}</p>
                        <ol className='list-decimal list-inside space-y-1'>
                            {t.howItWorksSteps.map((step, i) => (
                                <li key={i}>{step}</li>
                            ))}
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
