import { notFound } from 'next/navigation'
import { getDictionary, hasLocale } from './dictionaries'
import { DictionaryProvider } from './DictionaryProvider'
import { auth } from '@/auth'
import { signOutAction } from '@/app/lib/actions'
import LocaleSwitcher from '@/components/LocaleSwitcher'
import Link from 'next/link'

export function generateStaticParams() {
    return [{ lang: 'en' }, { lang: 'es' }]
}

export default async function LangLayout({
    children,
    params
}: {
    children: React.ReactNode
    params: Promise<{ lang: string }>
}) {
    const { lang } = await params
    if (!hasLocale(lang)) notFound()

    const [dict, session] = await Promise.all([getDictionary(lang), auth()])

    return (
        <DictionaryProvider dict={dict}>
            <header className='bg-indigo-700 text-white shadow-md no-print'>
                <div className='max-w-6xl mx-auto px-4 py-4 flex items-center justify-between gap-3'>
                    <div className='flex items-center gap-3'>
                        <span className='text-2xl'>📚</span>
                        <Link
                            href={`/${lang}`}
                            className='text-xl font-bold tracking-tight hover:opacity-80'
                        >
                            {dict.nav.title}
                        </Link>
                    </div>
                    <div className='flex items-center gap-3'>
                        <LocaleSwitcher lang={lang} />
                        {session?.user && (
                            <>
                                <span className='text-sm text-indigo-200 hidden sm:block'>
                                    {session.user.email}
                                </span>
                                <form action={signOutAction}>
                                    <button
                                        type='submit'
                                        className='text-sm bg-indigo-800 hover:bg-indigo-900 px-3 py-1.5 rounded-lg transition-colors'
                                    >
                                        {dict.nav.signOut}
                                    </button>
                                </form>
                            </>
                        )}
                    </div>
                </div>
            </header>
            <main className='max-w-6xl mx-auto px-4 py-8'>{children}</main>
        </DictionaryProvider>
    )
}
