'use client'

import { useCallback, useEffect, useState } from 'react'
import { SlideInfo, staticUrl } from '@/lib/api'

interface Props {
    slides: SlideInfo[]
    bookName: string
    onClose: () => void
}

export default function SlidesViewer({ slides, bookName, onClose }: Props) {
    const [current, setCurrent] = useState(0)
    const total = slides.length
    const slide = slides[current]

    const prev = useCallback(() => setCurrent(i => Math.max(0, i - 1)), [])
    const next = useCallback(() => setCurrent(i => Math.min(total - 1, i + 1)), [total])

    useEffect(() => {
        function onKey(e: KeyboardEvent) {
            if (e.key === 'ArrowRight' || e.key === 'ArrowDown') next()
            if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') prev()
            if (e.key === 'Escape') onClose()
        }
        window.addEventListener('keydown', onKey)
        return () => window.removeEventListener('keydown', onKey)
    }, [next, prev, onClose])

    if (!slide) {
        return (
            <div className='fixed inset-0 z-50 bg-gray-900 flex items-center justify-center'>
                <p className='text-white'>No slides available. Generate a summary first.</p>
                <button onClick={onClose} className='ml-4 text-gray-300 underline'>
                    Close
                </button>
            </div>
        )
    }

    const hasContent = slide.summary || slide.content
    const displayText = slide.summary ?? slide.content

    return (
        <>
            {/* Screen view */}
            <div className='no-print fixed inset-0 z-50 bg-gray-900 flex flex-col'>
                {/* Top bar */}
                <div className='flex items-center justify-between px-6 py-3 bg-gray-800 text-white shrink-0'>
                    <span className='font-semibold truncate max-w-xs'>{bookName}</span>
                    <div className='flex items-center gap-3'>
                        <span className='text-sm text-gray-400'>
                            {current + 1} / {total}
                        </span>
                        <button
                            onClick={() => window.print()}
                            className='text-sm bg-indigo-600 hover:bg-indigo-500 px-3 py-1 rounded-lg'
                        >
                            ⬇ PDF
                        </button>
                        <button
                            onClick={onClose}
                            className='text-gray-300 hover:text-white text-xl'
                        >
                            ✕
                        </button>
                    </div>
                </div>

                {/* Slide */}
                <div className='flex-1 overflow-y-auto flex items-start justify-center p-8'>
                    <div className='bg-white rounded-2xl shadow-xl w-full max-w-3xl p-8'>
                        <p className='text-xs text-indigo-500 font-semibold uppercase tracking-widest mb-2'>
                            {slide.number}
                        </p>
                        <h2 className='text-2xl font-bold text-gray-900 mb-4'>{slide.title}</h2>

                        {slide.summary ? (
                            <>
                                <div className='prose prose-sm max-w-none text-gray-700 whitespace-pre-wrap'>
                                    {slide.summary}
                                </div>
                                {!slide.summary && (
                                    <p className='text-gray-400 italic text-sm'>
                                        No summary yet — generate one from the book detail page.
                                    </p>
                                )}
                            </>
                        ) : (
                            <p className='text-gray-400 italic text-sm'>
                                No summary yet — generate one from the book detail page.
                            </p>
                        )}

                        {slide.images.length > 0 && (
                            <div className='mt-6 grid grid-cols-2 gap-4'>
                                {slide.images.map(img => (
                                    // eslint-disable-next-line @next/next/no-img-element
                                    <img
                                        key={img}
                                        src={staticUrl(img)}
                                        alt=''
                                        className='rounded-lg max-h-48 object-contain w-full'
                                    />
                                ))}
                            </div>
                        )}
                    </div>
                </div>

                {/* Navigation */}
                <div className='flex items-center justify-center gap-4 px-6 py-4 bg-gray-800 shrink-0'>
                    <button
                        onClick={prev}
                        disabled={current === 0}
                        className='px-5 py-2 bg-gray-700 hover:bg-gray-600 disabled:opacity-40 text-white rounded-xl text-sm font-medium'
                    >
                        ← Prev
                    </button>
                    {/* Progress dots (max 15 shown) */}
                    <div className='flex gap-1 overflow-hidden max-w-xs'>
                        {slides.slice(Math.max(0, current - 7), current + 8).map((_, i) => {
                            const idx = Math.max(0, current - 7) + i
                            return (
                                <button
                                    key={idx}
                                    onClick={() => setCurrent(idx)}
                                    className={`h-2 rounded-full transition-all ${
                                        idx === current ? 'w-5 bg-indigo-400' : 'w-2 bg-gray-600'
                                    }`}
                                />
                            )
                        })}
                    </div>
                    <button
                        onClick={next}
                        disabled={current === total - 1}
                        className='px-5 py-2 bg-gray-700 hover:bg-gray-600 disabled:opacity-40 text-white rounded-xl text-sm font-medium'
                    >
                        Next →
                    </button>
                </div>
            </div>

            {/* Print view — each slide on its own page */}
            <div className='hidden print:block'>
                {slides.map((s, i) => (
                    <div key={s.chapter_id} className='print-slide p-12'>
                        <p className='text-xs text-gray-400 uppercase tracking-widest mb-2'>
                            {s.number}
                        </p>
                        <h2 className='text-3xl font-bold mb-6'>{s.title}</h2>
                        {s.summary ? (
                            <p className='text-base text-gray-700 whitespace-pre-wrap'>
                                {s.summary}
                            </p>
                        ) : (
                            <p className='text-gray-400 italic'>No summary.</p>
                        )}
                        {s.images.length > 0 && (
                            <div className='mt-6 flex flex-wrap gap-4'>
                                {s.images.map(img => (
                                    // eslint-disable-next-line @next/next/no-img-element
                                    <img
                                        key={img}
                                        src={staticUrl(img)}
                                        alt=''
                                        className='max-h-48 object-contain'
                                    />
                                ))}
                            </div>
                        )}
                    </div>
                ))}
            </div>
        </>
    )
}
