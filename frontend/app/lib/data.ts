'use server'

import type { BookInfo, ChapterInfo, SlidesResponse } from './api'

const API_URL = `${process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'}/api/v1`

async function handleResponse<T>(res: Response): Promise<T> {
    if (!res.ok) {
        const err = await res.json().catch(() => ({ detail: res.statusText }))
        throw new Error(err.detail ?? res.statusText)
    }
    return res.json() as Promise<T>
}

export async function listBooks(): Promise<{ total: number; books: BookInfo[] }> {
    return fetch(`${API_URL}/epub/books`).then(r => handleResponse(r))
}

export async function getChapters(
    bookId: string
): Promise<{ book_id: string; total: number; chapters: ChapterInfo[] }> {
    return fetch(`${API_URL}/epub/chapters?book_id=${bookId}`).then(r => handleResponse(r))
}

export async function getSlides(bookId: string): Promise<SlidesResponse> {
    return fetch(`${API_URL}/epub/slides/${bookId}`).then(r => handleResponse(r))
}

export async function getLlmStatus(): Promise<{
    connected: boolean
    host: string
    model: string
}> {
    return fetch(`${API_URL}/epub/llm/status`).then(r => handleResponse(r))
}
