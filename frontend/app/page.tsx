import { redirect } from 'next/navigation'

// The middleware redirects / → /{locale}/ automatically.
// This is a fallback in case the middleware is bypassed.
export default function RootPage() {
    redirect('/en')
}
