const API_BASE = process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'
const API_URL = `${API_BASE}/api/v1`

export const staticUrl = (path: string) => `${API_BASE}/static/${path}`

export interface BookInfo {
    id: string
    name: string
    language: string | null
    author: string | null
}

export interface ChapterInfo {
    id: string
    title: string
    number: string
    include: boolean
    has_summary: boolean
    chapter_id: string | null
}

export interface SlideInfo {
    chapter_id: string
    title: string
    number: string
    summary: string | null
    content: string
    images: string[]
    depth: number
}

export interface SlidesResponse {
    book_id: string
    book_name: string
    slides: SlideInfo[]
}

async function handleResponse<T>(res: Response): Promise<T> {
    if (!res.ok) {
        const err = await res.json().catch(() => ({ detail: res.statusText }))
        throw new Error(err.detail ?? res.statusText)
    }
    return res.json() as Promise<T>
}

export const api = {
    books: {
        list: (): Promise<{ total: number; books: BookInfo[] }> =>
            fetch(`${API_URL}/epub/books`).then(r => handleResponse(r)),

        delete: (id: string): Promise<{ book_id: string; success: boolean }> =>
            fetch(`${API_URL}/epub/books/${id}`, { method: 'DELETE' }).then(r => handleResponse(r))
    },

    epub: {
        upload: (
            file: File,
            bookName?: string
        ): Promise<{ book_id: string; book_name: string; total_chapters: number }> => {
            const fd = new FormData()
            fd.append('file', file)
            if (bookName) fd.append('book_name', bookName)
            return fetch(`${API_URL}/epub/upload`, { method: 'POST', body: fd }).then(r =>
                handleResponse(r)
            )
        },

        chapters: (
            bookId: string
        ): Promise<{ book_id: string; total: number; chapters: ChapterInfo[] }> =>
            fetch(`${API_URL}/epub/chapters?book_id=${bookId}`).then(r => handleResponse(r)),

        setInclusion: (
            bookId: string,
            chapterNumbers: string[],
            include: boolean
        ): Promise<{ book_id: string; updated_count: number }> =>
            fetch(`${API_URL}/epub/chapters/include`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ book_id: bookId, chapter_numbers: chapterNumbers, include })
            }).then(r => handleResponse(r)),

        summarize: (bookId: string): Promise<{ book_id: string; chapters_summarized: number }> =>
            fetch(`${API_URL}/epub/summarize`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ book_id: bookId })
            }).then(r => handleResponse(r)),

        slides: (bookId: string): Promise<SlidesResponse> =>
            fetch(`${API_URL}/epub/slides/${bookId}`).then(r => handleResponse(r)),

        llmStatus: (): Promise<{ connected: boolean; host: string; model: string }> =>
            fetch(`${API_URL}/epub/llm/status`).then(r => handleResponse(r))
    }
}
