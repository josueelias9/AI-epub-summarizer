'use server'

import { AuthError } from 'next-auth'
import { signIn, signOut } from '@/auth'

const API_URL = `${process.env.NEXT_PRIVATE_API_URL ?? 'http://localhost:8000'}/api/v1`

async function handleResponse<T>(res: Response): Promise<T> {
    if (!res.ok) {
        const err = await res.json().catch(() => ({ detail: res.statusText }))
        const detail = Array.isArray(err.detail)
            ? err.detail.map((e: { msg?: string }) => e.msg ?? JSON.stringify(e)).join(', ')
            : (err.detail ?? res.statusText)
        throw new Error(detail)
    }
    return res.json() as Promise<T>
}

export async function deleteBook(id: string): Promise<{ book_id: string; success: boolean }> {
    return fetch(`${API_URL}/epub/books/${id}`, { method: 'DELETE' }).then(r => handleResponse(r))
}

export async function uploadEpub(
    formData: FormData
): Promise<{ book_id: string; book_name: string; total_chapters: number }> {
    return fetch(`${API_URL}/epub/upload`, { method: 'POST', body: formData }).then(r =>
        handleResponse(r)
    )
}

export type UploadState = {
    error: string | null
    book_id?: string
    book_name?: string
}

export async function uploadEpubAction(
    _prevState: UploadState | null,
    formData: FormData
): Promise<UploadState> {
    try {
        const res = await fetch(`${API_URL}/epub/upload`, {
            method: 'POST',
            body: formData
        }).then(r =>
            handleResponse<{ book_id: string; book_name: string; total_chapters: number }>(r)
        )
        return { error: null, book_id: res.book_id, book_name: res.book_name }
    } catch (err: unknown) {
        return { error: err instanceof Error ? err.message : 'Upload failed' }
    }
}

export async function setChapterInclusion(
    bookId: string,
    chapterNumbers: string[],
    include: boolean
): Promise<{ book_id: string; updated_count: number }> {
    return fetch(`${API_URL}/epub/chapters/include`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ book_id: bookId, chapter_numbers: chapterNumbers, include })
    }).then(r => handleResponse(r))
}

export async function summarizeBook(
    bookId: string
): Promise<{ book_id: string; chapters_summarized: number }> {
    return fetch(`${API_URL}/epub/summarize`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ book_id: bookId })
    }).then(r => handleResponse(r))
}

export type SummarizeState = { status: 'idle' | 'done' | 'error'; message: string | null }

export async function summarizeBookAction(
    _prev: SummarizeState,
    formData: FormData
): Promise<SummarizeState> {
    const bookId = formData.get('book_id') as string
    try {
        const res = await fetch(`${API_URL}/epub/summarize`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ book_id: bookId })
        }).then(r => handleResponse<{ book_id: string; chapters_summarized: number }>(r))
        return { status: 'done', message: `Summarized ${res.chapters_summarized} chapters.` }
    } catch (err: unknown) {
        return {
            status: 'error',
            message: err instanceof Error ? err.message : 'Summarization failed'
        }
    }
}

export async function authenticate(
    prevState: string | undefined,
    formData: FormData
): Promise<string | undefined> {
    try {
        await signIn('credentials', formData)
    } catch (error) {
        if (error instanceof AuthError) {
            switch (error.type) {
                case 'CredentialsSignin':
                    return 'Invalid credentials.'
                default:
                    return 'Something went wrong.'
            }
        }
        throw error // NEXT_REDIRECT must be rethrown
    }
}

export async function logout() {
    await signOut({ redirectTo: '/login' })
}
