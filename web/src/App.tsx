import { useCallback, useEffect, useRef, useState } from 'react'
import { AgentPanel } from './components/AgentPanel'
import { ShotCard } from './components/ShotCard'
import { SqlPanel } from './components/SqlPanel'
import { Timeline } from './components/Timeline'
import { chat, extractJson, fetchEdl, getFilmShots, getFilms, getShots, getSimilar, getStats } from './lib/api'
import type { AgentEvent, AssemblerResult, Film, LibrarianResult, Shot, Stats, Warning } from './lib/types'

const EXAMPLES = [
  'rainy night, two people, close-up',
  'lonely man walking through an empty street, wide shot',
  'build a 60-second teaser: tension rising to a climax, then release',
]

export default function App() {
  const [stats, setStats] = useState<Stats | null>(null)
  const [films, setFilms] = useState<Film[]>([])
  const [film, setFilm] = useState<string>('')
  const [query, setQuery] = useState('')
  const [results, setResults] = useState<Shot[]>([])
  const [sql, setSql] = useState<string | null>(null)
  const [count, setCount] = useState<number | null>(null)
  const [ms, setMs] = useState<number | null>(null)
  const [events, setEvents] = useState<AgentEvent[]>([])
  const [busy, setBusy] = useState(false)
  const [timeline, setTimeline] = useState<Shot[]>([])
  const [warnings, setWarnings] = useState<Warning[]>([])
  const [edl, setEdl] = useState<string | null>(null)
  const session = useRef<string | null>(null)

  useEffect(() => {
    getStats().then(setStats).catch(() => undefined)
    getFilms().then(setFilms).catch(() => undefined)
  }, [])

  useEffect(() => {
    if (!film) return
    getFilmShots(film).then((s) => {
      setResults(s)
      setSql(null)
      setCount(s.length)
    })
  }, [film])

  const addToTimeline = useCallback((s: Shot) => {
    setTimeline((t) => (t.some((x) => x.shot_id === s.shot_id) ? t : [...t, s]))
  }, [])

  const similar = useCallback(async (s: Shot) => {
    setResults(await getSimilar(s.shot_id))
    setSql(`SELECT ... ORDER BY cosineDistance(embedding, <embedding of ${s.shot_id}>) LIMIT 24`)
    setQuery(`similar to ${s.shot_id}`)
  }, [])

  const ask = useCallback(
    async (text: string) => {
      if (!text.trim() || busy) return
      setBusy(true)
      setEvents([])
      setEdl(null)
      const t0 = performance.now()
      try {
        for await (const ev of chat(text, session.current)) {
          if (ev.type === 'session') session.current = ev.session_id
          setEvents((e) => [...e, ev])
          if (ev.type === 'text' && ev.final && ev.agent === 'EditorAssistant') {
            const lib = extractJson<LibrarianResult>(ev.text)
            if (lib && Array.isArray(lib.shots)) {
              setResults(lib.shots)
              setSql(lib.sql ?? null)
              setCount(lib.count ?? lib.shots.length)
              setMs(Math.round(performance.now() - t0))
            }
            const cut = extractJson<AssemblerResult>(ev.text)
            if (cut && Array.isArray(cut.shot_ids) && cut.timeline) {
              const shots = await getShots(cut.shot_ids)
              setTimeline(shots)
              setWarnings(cut.warnings ?? [])
              setEdl(cut.edl ?? null)
            }
          }
        }
      } catch (e) {
        setEvents((ev) => [...ev, { type: 'error', message: String(e) }])
      } finally {
        setBusy(false)
      }
    },
    [busy],
  )

  const exportEdl = useCallback(async () => {
    const text = edl ?? (await fetchEdl(timeline.map((s) => s.shot_id), 'SHOT MEMORY SEQUENCE'))
    const blob = new Blob([text], { type: 'text/plain' })
    const a = document.createElement('a')
    a.href = URL.createObjectURL(blob)
    a.download = 'shot-memory.edl'
    a.click()
  }, [edl, timeline])

  const move = (id: string, dir: -1 | 1) =>
    setTimeline((t) => {
      const i = t.findIndex((s) => s.shot_id === id)
      const j = i + dir
      if (i < 0 || j < 0 || j >= t.length) return t
      const n = [...t]
      ;[n[i], n[j]] = [n[j], n[i]]
      return n
    })

  return (
    <div className="app">
      <header>
        <div className="brand">
          <span className="logo">▣</span> Shot Memory
        </div>
        <div className="stats">
          {stats && (
            <>
              <b>{stats.films}</b> films · <b>{stats.shots.toLocaleString()}</b> shots · <b>{stats.hours}</b> h
            </>
          )}
        </div>
        <select value={film} onChange={(e) => setFilm(e.target.value)}>
          <option value="">Browse a film…</option>
          {films.map((f) => (
            <option key={f.film_id} value={f.film_id}>
              {f.title} ({f.year}) · {f.shot_count} · {f.status}
            </option>
          ))}
        </select>
      </header>

      <main>
        <section className="work">
          <form
            className="search"
            onSubmit={(e) => {
              e.preventDefault()
              ask(query)
            }}
          >
            <input
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Describe the shots you need, or ask for a cut…"
              disabled={busy}
            />
            <button disabled={busy || !query.trim()}>{busy ? 'Working…' : 'Ask'}</button>
          </form>
          <div className="examples">
            {EXAMPLES.map((x) => (
              <button key={x} className="ghost" onClick={() => { setQuery(x); ask(x) }} disabled={busy}>
                {x}
              </button>
            ))}
          </div>

          <SqlPanel sql={sql} count={count} ms={ms} />

          <div className="grid">
            {results.map((s) => (
              <ShotCard key={s.shot_id} shot={s} onAdd={addToTimeline} onSimilar={similar} />
            ))}
            {!results.length && !busy && <div className="empty">No shots yet. Search above or browse a film.</div>}
          </div>

          <Timeline
            items={timeline}
            warnings={warnings}
            onRemove={(id) => setTimeline((t) => t.filter((s) => s.shot_id !== id))}
            onMove={move}
            onExport={exportEdl}
            onClear={() => {
              setTimeline([])
              setWarnings([])
              setEdl(null)
            }}
          />
        </section>

        <aside>
          <AgentPanel events={events} busy={busy} />
        </aside>
      </main>
    </div>
  )
}
