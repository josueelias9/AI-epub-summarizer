'use client'

import { ChapterInfo } from '@/app/lib/api'
import { useDictionary } from '@/app/[lang]/DictionaryProvider'

interface Props {
    chapters: ChapterInfo[]
    onToggle: (number: string, include: boolean) => void
}

function depthOf(number: string) {
    return number.split('.').length
}

export default function ChapterList({ chapters, onToggle }: Props) {
    const t = useDictionary().chapterList
    if (chapters.length === 0) {
        return <p className='text-sm text-gray-400'>{t.noChapters}</p>
    }

    return (
        <ul className='space-y-1'>
            {chapters.map(ch => {
                const depth = depthOf(ch.number)
                const indent = (depth - 1) * 16
                return (
                    <li
                        key={ch.id}
                        style={{ paddingLeft: `${indent}px` }}
                        className='flex items-center gap-3 py-1.5 px-2 rounded-lg hover:bg-gray-50 group'
                    >
                        <input
                            type='checkbox'
                            checked={ch.include}
                            onChange={e => onToggle(ch.number, e.target.checked)}
                            className='h-4 w-4 rounded text-indigo-600 focus:ring-indigo-500 cursor-pointer'
                        />
                        <span
                            className={`text-sm flex-1 ${ch.include ? 'text-gray-800' : 'text-gray-400 line-through'}`}
                        >
                            <span className='text-xs text-gray-400 mr-1'>{ch.number}</span>
                            {ch.title}
                        </span>
                        {ch.has_summary && (
                            <span className='text-xs bg-green-100 text-green-700 px-1.5 py-0.5 rounded-full opacity-0 group-hover:opacity-100 transition-opacity'>
                                {t.summarizedBadge}
                            </span>
                        )}
                    </li>
                )
            })}
        </ul>
    )
}
