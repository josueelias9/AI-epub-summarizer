'use client'

import { useActionState } from 'react'
import { useSearchParams } from 'next/navigation'
import { authenticate } from '@/app/lib/actions'

export default function LoginForm() {
    const searchParams = useSearchParams()
    const callbackUrl = searchParams.get('callbackUrl') || '/'
    const [errorMessage, formAction, isPending] = useActionState(authenticate, undefined)

    return (
        <form action={formAction} className='space-y-4'>
            <input type='hidden' name='redirectTo' value={callbackUrl} />

            <div>
                <label htmlFor='email' className='block text-sm font-medium text-gray-700 mb-1'>
                    Email
                </label>
                <input
                    id='email'
                    name='email'
                    type='email'
                    placeholder='you@example.com'
                    required
                    className='w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500'
                />
            </div>

            <div>
                <label htmlFor='password' className='block text-sm font-medium text-gray-700 mb-1'>
                    Password
                </label>
                <input
                    id='password'
                    name='password'
                    type='password'
                    placeholder='••••••••'
                    required
                    minLength={6}
                    className='w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500'
                />
            </div>

            <button
                type='submit'
                aria-disabled={isPending}
                disabled={isPending}
                className='w-full bg-indigo-600 hover:bg-indigo-700 disabled:opacity-60 text-white font-semibold py-2 rounded-lg transition-colors'
            >
                {isPending ? 'Signing in…' : 'Sign in'}
            </button>

            {errorMessage && <p className='text-sm text-red-600 text-center'>{errorMessage}</p>}
        </form>
    )
}
