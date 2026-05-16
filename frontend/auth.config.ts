import type { NextAuthConfig } from 'next-auth'

export const authConfig = {
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
            const isAuthPage = nextUrl.pathname.startsWith('/login')
            const isSeedRoute = nextUrl.pathname.startsWith('/seed')
            const isPublic = nextUrl.pathname === '/'

            if (isSeedRoute || isPublic) return true

            if (isAuthPage) {
                if (isLoggedIn) return Response.redirect(new URL('/', nextUrl))
                return true
            }

            if (!isLoggedIn) return false // NextAuth redirects to /login
            return true
        }
    }
} satisfies NextAuthConfig
