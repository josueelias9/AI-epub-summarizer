import { Suspense } from 'react'
import LoginForm from '@/components/login-form'

export default function LoginPage() {
    return (
        <div className='min-h-screen flex items-center justify-center bg-gray-50'>
            <div className='bg-white rounded-2xl shadow-xl w-full max-w-sm mx-4 p-8'>
                <div className='text-center mb-6'>
                    <span className='text-4xl'>📚</span>
                    <h1 className='mt-3 text-2xl font-bold text-gray-900'>Sign in</h1>
                    <p className='text-sm text-gray-500 mt-1'>to your EPUB Summarizer</p>
                </div>
                <Suspense>
                    <LoginForm />
                </Suspense>
            </div>
        </div>
    )
}
