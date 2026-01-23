export type Cell = 0 | 1;
export type Grid = Cell[][];
export type TargetCell = Cell | null;
export type TargetGrid = TargetCell[][];
export type DragKind = "row" | "col";

export type GameState = {
  current: Grid;
  target: TargetGrid;
  colLabels: string[];
  colOrder: number[];
};

export function createInitialState(input: {
  current: Grid;
  target: TargetGrid;
  colLabels: string[];
}): GameState {
  const colOrder = input.colLabels.map((_, index) => index);
  return {
    current: input.current.map((row) => [...row]),
    target: input.target.map((row) => [...row]),
    colLabels: [...input.colLabels],
    colOrder,
  };
}

export function swapRows(state: GameState, first: number, second: number) {
  const copy = [...state.current];
  [copy[first], copy[second]] = [copy[second], copy[first]];
  state.current = copy;
}

export function swapCols(state: GameState, first: number, second: number) {
  state.current = state.current.map((row) => {
    const copy = [...row];
    [copy[first], copy[second]] = [copy[second], copy[first]];
    return copy;
  });
  const orderCopy = [...state.colOrder];
  [orderCopy[first], orderCopy[second]] = [orderCopy[second], orderCopy[first]];
  state.colOrder = orderCopy;
}

export function shuffleRowsAndCols(state: GameState) {
  const rows = [...state.current];
  rows.sort(() => Math.random() - 0.5);
  const cols = [...Array(state.current[0]?.length ?? 0).keys()];
  cols.sort(() => Math.random() - 0.5);

  state.current = rows.map((row) => cols.map((index) => row[index]));
  state.colOrder = cols.map((index) => state.colOrder[index]);
}
