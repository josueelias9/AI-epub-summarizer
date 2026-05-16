'use client'

import { usePathname, useRouter } from 'next/navigation'

const LOCALES = [
    { code: 'en', flag: '🇺🇸', label: 'EN' },
    { code: 'es', flag: '🇪🇸', label: 'ES' }
]

export default function LocaleSwitcher({ lang }: { lang: string }) {
    const pathname = usePathname()
    const router = useRouter()

    function switchLocale(newLang: string) {
        // Replace /en/... with /newLang/...
        const newPath = pathname.replace(/^\/[^/]+/, `/${newLang}`)
        router.push(newPath)
    }

    return (
        <div className='flex items-center gap-1'>
            {LOCALES.map(l => (
                <button
                    key={l.code}
                    onClick={() => switchLocale(l.code)}
                    className={`text-xs px-2 py-1 rounded-md font-medium transition-colors ${
                        l.code === lang
                            ? 'bg-indigo-500 text-white'
                            : 'text-indigo-200 hover:bg-indigo-600 hover:text-white'
                    }`}
                >
                    {l.flag} {l.label}
                </button>
            ))}
        </div>
    )
}
