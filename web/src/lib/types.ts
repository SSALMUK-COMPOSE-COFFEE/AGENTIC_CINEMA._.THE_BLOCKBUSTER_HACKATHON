export type Shot = {
  shot_id: string
  film_id?: string
  film_title: string
  shot_index?: number
  t_in: number
  t_out: number
  caption: string
  people_count?: number
  time_of_day?: string
  interior?: string
  weather?: string
  shot_size?: string
  camera_move?: string
  emotion?: string
  tension?: number
  dialogue_present?: boolean
  thumbnail_uri: string
  proxy_uri: string
  dist?: number
}

export type Film = {
  film_id: string
  title: string
  year: number
  shot_count: number
  status: string
}

export type Stats = { films: number; shots: number; hours: number }

export type AgentEvent =
  | { type: 'session'; session_id: string }
  | { type: 'tool_call'; agent: string; name: string; args: Record<string, unknown>; t?: number }
  | { type: 'tool_result'; agent: string; name: string; result: unknown; t?: number; ms?: number | null }
  | { type: 'text'; agent: string; text: string; final: boolean; t?: number }
  | { type: 'thinking'; agent: string; t?: number }
  | { type: 'result'; agent: 'Librarian'; data: LibrarianResult; t?: number }
  | { type: 'result'; agent: 'CutAssembler'; data: AssemblerResult; t?: number }
  | { type: 'error'; message: string }
  | { type: 'done' }

export type Warning = {
  pair: [string, string]
  rule: string
  severity: 'low' | 'mid' | 'high'
  explanation: string
  suggested_replacement?: string | null
}

export type TimelineItem = Shot & { rec_in: number; rec_out: number }

export type LibrarianResult = { sql: string; count: number; shots: Shot[] }
export type AssemblerResult = {
  brief: string
  beats: { name: string; shot_ids: string[] }[]
  shot_ids: string[]
  timeline: TimelineItem[]
  edl: string
  total_seconds: number
  warnings: Warning[]
  sequence_id?: string
}
