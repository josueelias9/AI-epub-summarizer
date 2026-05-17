import type { NextAuthConfig } from 'next-auth'
import { locales, defaultLocale } from './lib/i18n-config'

export const authConfig = {
    trustHost: true,
    pages: {
        signIn: '/login'
    },
    providers: [
        // added later in auth.ts since it requires bcrypt which is only compatible with Node.js
        // while this file is also used in non-Node.js environments
    ],
    callbacks: {
        authorized({ auth, request: { nextUrl } }) {
            const isLoggedIn = !!auth?.user
            const pathname = nextUrl.pathname

            // Detect locale from path, fall back to default
            const firstSegment = pathname.split('/')[1]
            const locale = (locales as readonly string[]).includes(firstSegment)
                ? firstSegment
                : defaultLocale

            const isAuthPage = pathname.includes('/login')
            const isSeedRoute = pathname.startsWith('/seed')
            const isPublicHome = pathname === '/' || pathname === `/${locale}`

            if (isSeedRoute || isPublicHome) return true

            if (isAuthPage) {
                if (isLoggedIn) return Response.redirect(new URL(`/${locale}`, nextUrl))
                return true
            }

            if (!isLoggedIn) return Response.redirect(new URL(`/${locale}/login`, nextUrl))
            return true
        }
    }
} satisfies NextAuthConfig
