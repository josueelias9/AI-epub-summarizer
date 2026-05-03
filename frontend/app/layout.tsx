import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
    title: 'EPUB Summarizer',
    description: 'Upload and summarize EPUB books chapter by chapter'
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html lang='en'>
            <body className='min-h-screen bg-gray-50 text-gray-900'>
                <header className='bg-indigo-700 text-white shadow-md no-print'>
                    <div className='max-w-6xl mx-auto px-4 py-4 flex items-center gap-3'>
                        <span className='text-2xl'>📚</span>
                        <a href='/' className='text-xl font-bold tracking-tight hover:opacity-80'>
                            EPUB Summarizer
                        </a>
                    </div>
                </header>
                <main className='max-w-6xl mx-auto px-4 py-8'>{children}</main>
            </body>
        </html>
    )
}
