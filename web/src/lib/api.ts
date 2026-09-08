import type { AgentEvent, Film, Shot, Stats } from './types'

const json = async <T,>(res: Response): Promise<T> => {
  if (!res.ok) throw new Error(`${res.status} ${await res.text()}`)
  return res.json() as Promise<T>
}

export const getStats = () => fetch('/api/stats').then(json<Stats>)
export const getFilms = () => fetch('/api/films').then(json<Film[]>)
export const getFilmShots = (filmId: string, offset = 0, limit = 60) =>
  fetch(`/api/films/${filmId}/shots?offset=${offset}&limit=${limit}`).then(json<Shot[]>)
export const getShots = (ids: string[]) =>
  fetch(`/api/shots?${ids.map((i) => `ids=${encodeURIComponent(i)}`).join('&')}`).then(json<Shot[]>)
export const getSimilar = (shotId: string) =>
  fetch(`/api/shots/${encodeURIComponent(shotId)}/similar`).then(json<Shot[]>)

export const buildTimeline = (shotIds: string[]) =>
  fetch('/api/sequences/timeline', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ shot_ids: shotIds }),
  }).then(json<{ edl: string; timeline: (Shot & { rec_in: number; rec_out: number })[]; total_seconds: number }>)

export const fetchEdl = (shotIds: string[], title: string) =>
  fetch('/api/sequences/edl', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ shot_ids: shotIds, title }),
  }).then((r) => r.text())

export async function* chat(message: string, sessionId: string | null): AsyncGenerator<AgentEvent> {
  const res = await fetch('/api/agent/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message, session_id: sessionId }),
  })
  if (!res.ok || !res.body) throw new Error(`${res.status}`)
  const reader = res.body.getReader()
  const decoder = new TextDecoder()
  let buf = ''
  while (true) {
    const { value, done } = await reader.read()
    if (done) break
    buf += decoder.decode(value, { stream: true })
    let idx
    while ((idx = buf.indexOf('\n\n')) >= 0) {
      const chunk = buf.slice(0, idx)
      buf = buf.slice(idx + 2)
      const line = chunk.split('\n').find((l) => l.startsWith('data: '))
      if (line) yield JSON.parse(line.slice(6)) as AgentEvent
    }
  }
}

export const fmt = (s: number) => {
  const h = Math.floor(s / 3600)
  const m = Math.floor((s % 3600) / 60)
  const sec = Math.floor(s % 60)
  const f = Math.round((s % 1) * 24) % 24
  const pad = (n: number) => String(n).padStart(2, '0')
  return `${pad(h)}:${pad(m)}:${pad(sec)}:${pad(f)}`
}
