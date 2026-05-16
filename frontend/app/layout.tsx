import type { Metadata } from 'next'
import './globals.css'
import { auth } from '@/auth'
import { signOutAction } from '@/app/lib/actions'

export const metadata: Metadata = {
    title: 'EPUB Summarizer',
    description: 'Upload and summarize EPUB books chapter by chapter'
}

export default async function RootLayout({ children }: { children: React.ReactNode }) {
    const session = await auth()

    return (
        <html lang='en'>
            <body className='min-h-screen bg-gray-50 text-gray-900'>
                <header className='bg-indigo-700 text-white shadow-md no-print'>
                    <div className='max-w-6xl mx-auto px-4 py-4 flex items-center justify-between gap-3'>
                        <div className='flex items-center gap-3'>
                            <span className='text-2xl'>📚</span>
                            <a
                                href='/'
                                className='text-xl font-bold tracking-tight hover:opacity-80'
                            >
                                EPUB Summarizer
                            </a>
                        </div>
                        {session?.user && (
                            <div className='flex items-center gap-4'>
                                <span className='text-sm text-indigo-200 hidden sm:block'>
                                    {session.user.email}
                                </span>
                                <form action={signOutAction}>
                                    <button
                                        type='submit'
                                        className='text-sm bg-indigo-800 hover:bg-indigo-900 px-3 py-1.5 rounded-lg transition-colors'
                                    >
                                        Sign out
                                    </button>
                                </form>
                            </div>
                        )}
                    </div>
                </header>
                <main className='max-w-6xl mx-auto px-4 py-8'>{children}</main>
            </body>
        </html>
    )
}
