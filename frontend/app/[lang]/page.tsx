import { notFound } from 'next/navigation'
import { getDictionary, hasLocale } from './dictionaries'
import Link from 'next/link'

export default async function LandingPage({ params }: { params: Promise<{ lang: string }> }) {
    const { lang } = await params
    if (!hasLocale(lang)) notFound()
    const { landing: t } = await getDictionary(lang)

    return (
        <div className='flex flex-col gap-24 pb-24'>
            {/* Hero */}
            <section className='text-center pt-16 pb-8 flex flex-col items-center gap-6'>
                <div className='inline-flex items-center gap-2 bg-indigo-50 text-indigo-700 text-sm font-medium px-4 py-1.5 rounded-full border border-indigo-200'>
                    <span>✨</span> {t.badge}
                </div>
                <h1 className='text-5xl sm:text-6xl font-extrabold text-gray-900 leading-tight tracking-tight max-w-2xl'>
                    {t.heroLine1} <span className='text-indigo-600'>{t.heroHighlight}</span>
                </h1>
                <p className='text-lg text-gray-500 max-w-xl'>{t.subtitle}</p>
                <div className='flex flex-col sm:flex-row gap-3 mt-2'>
                    <Link
                        href={`/${lang}/library`}
                        className='bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-8 py-3 rounded-xl shadow-md transition-colors text-base'
                    >
                        {t.goToLibrary}
                    </Link>
                    <Link
                        href={`/${lang}/login`}
                        className='border border-gray-300 hover:border-indigo-400 text-gray-700 hover:text-indigo-600 font-semibold px-8 py-3 rounded-xl transition-colors text-base'
                    >
                        {t.signIn}
                    </Link>
                </div>
            </section>

            {/* Features */}
            <section className='grid grid-cols-1 sm:grid-cols-2 gap-6 max-w-3xl mx-auto w-full'>
                {t.features.map(f => (
                    <div
                        key={f.title}
                        className='bg-white border border-gray-200 rounded-2xl p-6 shadow-sm flex flex-col gap-3 hover:shadow-md transition-shadow'
                    >
                        <span className='text-3xl'>{f.icon}</span>
                        <h3 className='font-bold text-gray-900 text-lg'>{f.title}</h3>
                        <p className='text-gray-500 text-sm leading-relaxed'>{f.description}</p>
                    </div>
                ))}
            </section>

            {/* How it works */}
            <section className='text-center flex flex-col items-center gap-10'>
                <h2 className='text-3xl font-bold text-gray-900'>{t.howItWorks}</h2>
                <ol className='flex flex-col sm:flex-row gap-6 sm:gap-4 max-w-3xl w-full'>
                    {t.steps.map(({ step, label, desc }) => (
                        <li
                            key={step}
                            className='flex-1 bg-indigo-50 border border-indigo-100 rounded-2xl p-6 flex flex-col items-center gap-2 text-center'
                        >
                            <span className='w-10 h-10 rounded-full bg-indigo-600 text-white font-bold text-lg flex items-center justify-center'>
                                {step}
                            </span>
                            <span className='font-semibold text-gray-900'>{label}</span>
                            <span className='text-sm text-gray-500'>{desc}</span>
                        </li>
                    ))}
                </ol>
            </section>

            {/* CTA */}
            <section className='text-center flex flex-col items-center gap-4'>
                <h2 className='text-2xl font-bold text-gray-900'>{t.ctaTitle}</h2>
                <p className='text-gray-500'>{t.ctaSubtitle}</p>
                <Link
                    href={`/${lang}/library`}
                    className='bg-indigo-600 hover:bg-indigo-700 text-white font-semibold px-10 py-3 rounded-xl shadow-md transition-colors text-base mt-2'
                >
                    {t.ctaButton}
                </Link>
            </section>
        </div>
    )
}
