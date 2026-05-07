export const staticUrl = (path: string) =>
    `${process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'}/static/${path}`

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
