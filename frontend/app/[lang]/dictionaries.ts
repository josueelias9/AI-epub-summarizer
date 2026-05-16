import 'server-only'
import { cache } from 'react'

const dictionaries = {
    en: () => import('./dictionaries/en.json').then(m => m.default),
    es: () => import('./dictionaries/es.json').then(m => m.default)
}

export type Locale = keyof typeof dictionaries
export type Dictionary = Awaited<ReturnType<typeof dictionaries.en>>

export const hasLocale = (locale: string): locale is Locale => locale in dictionaries

export const getDictionary = cache(async (locale: Locale) => dictionaries[locale]())
