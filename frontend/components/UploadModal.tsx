'use client'

import { useState, useRef } from 'react'
import { uploadEpub } from '@/app/lib/actions'

interface Props {
    onUploaded: (bookId: string, bookName: string) => void
    onClose: () => void
}

export default function UploadModal({ onUploaded, onClose }: Props) {
    const [file, setFile] = useState<File | null>(null)
    const [bookName, setBookName] = useState('')
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState<string | null>(null)
    const inputRef = useRef<HTMLInputElement>(null)
    // TODO: I think this can be simplified by using the new useFormState or useActionState.
    async function handleSubmit(e: React.FormEvent) {
        e.preventDefault()
        if (!file) return
        setLoading(true)
        setError(null)
        try {
            const fd = new FormData()
            fd.append('file', file)
            if (bookName) fd.append('book_name', bookName)
            const res = await uploadEpub(fd)
            onUploaded(res.book_id, res.book_name)
        } catch (err: unknown) {
            setError(err instanceof Error ? err.message : 'Upload failed')
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className='fixed inset-0 z-50 flex items-center justify-center bg-black/50'>
            <div className='bg-white rounded-2xl shadow-xl w-full max-w-md mx-4 p-6'>
                <div className='flex items-center justify-between mb-4'>
                    <h2 className='text-lg font-bold text-gray-800'>Upload EPUB</h2>
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
                                <p className='text-sm text-gray-500'>
                                    Click to select an <strong>.epub</strong> file
                                </p>
                            </>
                        )}
                    </div>

                    <div>
                        <label className='block text-sm font-medium text-gray-700 mb-1'>
                            Book name <span className='text-gray-400'>(optional)</span>
                        </label>
                        <input
                            type='text'
                            value={bookName}
                            onChange={e => setBookName(e.target.value)}
                            placeholder='Leave blank to use EPUB metadata'
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
                        disabled={!file || loading}
                        className='w-full bg-indigo-600 hover:bg-indigo-700 disabled:opacity-50 text-white font-semibold py-2 rounded-xl transition-colors'
                    >
                        {loading ? 'Uploading & Extracting…' : 'Upload & Extract'}
                    </button>
                </form>
            </div>
        </div>
    )
}
