import type { GameState, TargetCell } from "./state";

type MatchState = {
  isMatch: boolean;
  dimRows: Set<number>;
};

function rowsMatch(row: number[], targetRow: TargetCell[]) {
  if (row.length !== targetRow.length) return false;
  for (let c = 0; c < row.length; c += 1) {
    const expected = targetRow[c];
    if (expected === null) continue;
    if (row[c] !== expected) return false;
  }
  return true;
}

function findMatchingRowIndices(state: GameState) {
  if (state.target.length > state.current.length) return null;
  const indices: number[] = [];
  let searchFrom = 0;
  for (const targetRow of state.target) {
    let found = false;
    for (let i = searchFrom; i < state.current.length; i += 1) {
      if (rowsMatch(state.current[i], targetRow)) {
        indices.push(i);
        searchFrom = i + 1;
        found = true;
        break;
      }
    }
    if (!found) return null;
  }
  return indices;
}

export function evaluateMatchState(state: GameState): MatchState {
  const indices = findMatchingRowIndices(state);
  const isMatch = indices !== null;
  const dimRows = new Set<number>();
  if (indices) {
    const matched = new Set(indices);
    for (let i = 0; i < state.current.length; i += 1) {
      if (!matched.has(i)) dimRows.add(i);
    }
  }
  return { isMatch, dimRows };
}
