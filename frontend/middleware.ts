import { NextRequest, NextResponse } from 'next/server'
import NextAuth from 'next-auth'
import { authConfig } from './auth.config'
import Negotiator from 'negotiator'
import { match } from '@formatjs/intl-localematcher'
import { locales, defaultLocale } from './lib/i18n-config'

function getLocale(request: NextRequest): string {
    const negotiatorHeaders: Record<string, string> = {}
    request.headers.forEach((value, key) => (negotiatorHeaders[key] = value))
    const languages = new Negotiator({ headers: negotiatorHeaders }).languages()
    try {
        return match(languages, locales as unknown as string[], defaultLocale)
    } catch {
        return defaultLocale
    }
}

const { auth } = NextAuth(authConfig)

export default auth(function middleware(request: NextRequest) {
    const { pathname } = request.nextUrl

    const pathnameHasLocale = locales.some(
        locale => pathname.startsWith(`/${locale}/`) || pathname === `/${locale}`
    )

    if (pathnameHasLocale) return

    const locale = getLocale(request)
    request.nextUrl.pathname = `/${locale}${pathname}`
    return NextResponse.redirect(request.nextUrl)
})

export const config = {
    matcher: ['/((?!api/auth|_next/static|_next/image|favicon.ico|seed).*)']
}
