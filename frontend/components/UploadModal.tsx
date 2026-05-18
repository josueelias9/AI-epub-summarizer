'use client'

import { useState, useRef } from 'react'
import { useDictionary } from '@/app/[lang]/DictionaryProvider'

const API_URL = `${process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'}/api/v1`

interface Props {
    onUploaded: (bookId: string, bookName: string) => void
    onClose: () => void
}

export default function UploadModal({ onUploaded, onClose }: Props) {
    const t = useDictionary().uploadModal
    const [file, setFile] = useState<File | null>(null)
    const [bookName, setBookName] = useState('')
    const [isPending, setIsPending] = useState(false)
    const [error, setError] = useState<string | null>(null)
    const inputRef = useRef<HTMLInputElement>(null)
    // This can't be a server action because it needs to handle file uploads, which require streaming the request body. Server actions currently don't support streaming, so we have to handle the upload on the client side and then call the server API.
    async function handleSubmit(e: React.FormEvent) {
        e.preventDefault()
        if (!file) return
        setIsPending(true)
        setError(null)
        try {
            const formData = new FormData()
            formData.append('file', file)
            if (bookName.trim()) formData.append('book_name', bookName.trim())
                // TODO: why not in actions.ts file? it's repeated
            const res = await fetch(`${API_URL}/epub/upload`, { method: 'POST', body: formData })
            if (!res.ok) {
                const err = await res.json().catch(() => ({ detail: res.statusText }))
                const detail = Array.isArray(err.detail)
                    ? err.detail.map((e: { msg?: string }) => e.msg ?? JSON.stringify(e)).join(', ')
                    : (err.detail ?? res.statusText)
                throw new Error(detail)
            }
            const data = await res.json()
            onUploaded(data.book_id, data.book_name)
        } catch (err: unknown) {
            setError(err instanceof Error ? err.message : 'Upload failed')
        } finally {
            setIsPending(false)
        }
    }

    return (
        <div className='fixed inset-0 z-50 flex items-center justify-center bg-black/50'>
            <div className='bg-white rounded-2xl shadow-xl w-full max-w-md mx-4 p-6'>
                <div className='flex items-center justify-between mb-4'>
                    <h2 className='text-lg font-bold text-gray-800'>{t.title}</h2>
                    <button
                        onClick={onClose}
                        className='text-gray-400 hover:text-gray-600 text-xl leading-none'
                    >
                        ✕
                    </button>
                </div>

                <form onSubmit={handleSubmit} className='space-y-4'>
                    <div
                        onClick={() => inputRef.current?.click()}
                        className='border-2 border-dashed border-indigo-200 rounded-xl p-6 text-center cursor-pointer hover:bg-indigo-50 transition-colors'
                    >
                        <input
                            ref={inputRef}
                            type='file'
                            accept='.epub'
                            className='hidden'
                            onChange={e => setFile(e.target.files?.[0] ?? null)}
                        />
                        {file ? (
                            <p className='text-sm font-medium text-indigo-700'>{file.name}</p>
                        ) : (
                            <>
                                <p className='text-3xl mb-2'>📂</p>
                                <p className='text-sm text-gray-500'>{t.selectFile}</p>
                            </>
                        )}
                    </div>
                    <div>
                        <label className='block text-sm font-medium text-gray-700 mb-1'>
                            {t.bookNameLabel}{' '}
                            <span className='text-gray-400'>{t.bookNameOptional}</span>
                        </label>
                        <input
                            type='text'
                            value={bookName}
                            onChange={e => setBookName(e.target.value)}
                            placeholder={t.bookNamePlaceholder}
                            className='w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500'
                        />
                    </div>
                    {error && (
                        <p className='text-sm text-red-600 bg-red-50 rounded-lg px-3 py-2'>
                            {error}
                        </p>
                    )}
                    <button
                        type='submit'
                        disabled={!file || isPending}
                        className='w-full bg-indigo-600 hover:bg-indigo-700 disabled:opacity-50 text-white font-semibold py-2 rounded-xl transition-colors'
                    >
                        {isPending ? t.uploading : t.uploadButton}
                    </button>
                </form>
            </div>
        </div>
    )
}
