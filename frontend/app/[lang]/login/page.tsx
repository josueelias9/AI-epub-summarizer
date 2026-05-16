import { notFound } from 'next/navigation'
import { Suspense } from 'react'
import { getDictionary, hasLocale } from '../dictionaries'
import LoginForm from '@/components/login-form'

export default async function LoginPage({ params }: { params: Promise<{ lang: string }> }) {
    const { lang } = await params
    if (!hasLocale(lang)) notFound()
    const dict = await getDictionary(lang)
    const t = dict.loginForm

    return (
        <div className='min-h-[70vh] flex items-center justify-center'>
            <div className='bg-white rounded-2xl shadow-xl w-full max-w-sm mx-4 p-8'>
                <div className='text-center mb-6'>
                    <span className='text-4xl'>📚</span>
                    <h1 className='mt-3 text-2xl font-bold text-gray-900'>{t.title}</h1>
                    <p className='text-sm text-gray-500 mt-1'>{t.subtitle}</p>
                </div>
                <Suspense>
                    <LoginForm />
                </Suspense>
            </div>
        </div>
    )
}
