'use server'

import { AuthError } from 'next-auth'
import { signIn, signOut } from '@/auth'

const API_URL = `${process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'}/api/v1`

async function handleResponse<T>(res: Response): Promise<T> {
    if (!res.ok) {
        const err = await res.json().catch(() => ({ detail: res.statusText }))
        throw new Error(err.detail ?? res.statusText)
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
