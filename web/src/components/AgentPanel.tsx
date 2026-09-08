import type { AgentEvent } from '../lib/types'

const label: Record<string, string> = {
  Librarian: 'Searching archive',
  CutAssembler: 'Assembling cut',
  ContinuityChecker: 'Checking continuity',
  Narrator: 'Explaining',
  EditorAssistant: 'Routing',
}

export function AgentPanel({ events, busy }: { events: AgentEvent[]; busy: boolean }) {
  const items = events.filter(
    (e) => e.type === 'tool_call' || e.type === 'result' || (e.type === 'text' && e.final) || e.type === 'error',
  )
  return (
    <div className="agent-panel">
      <h3>Agent team {busy && <span className="spinner" />}</h3>
      <ol>
        {items.map((e, i) => {
          if (e.type === 'tool_call')
            return (
              <li key={i} className="call">
                <b>{e.agent}</b> → {e.name}
                <code>{JSON.stringify(e.args).slice(0, 160)}</code>
              </li>
            )
          if (e.type === 'text')
            return (
              <li key={i} className={e.final ? 'final' : ''}>
                <b>{label[e.agent] ?? e.agent}</b>
                <p>{e.text.length > 400 ? e.text.slice(0, 400) + '…' : e.text}</p>
              </li>
            )
          if (e.type === 'result')
            return (
              <li key={i} className="result">
                <b>{e.agent}</b> returned{' '}
                {e.agent === 'Librarian' ? `${e.data.count} shots` : `${e.data.shot_ids.length} shots, ${e.data.warnings.length} warnings`}
              </li>
            )
          if (e.type === 'error') return <li key={i} className="error">{e.message}</li>
          return null
        })}
      </ol>
    </div>
  )
}
