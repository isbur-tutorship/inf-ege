export type Cell = 0 | 1;
export type Grid = Cell[][];
export type TargetCell = Cell | null;
export type TargetGrid = TargetCell[][];
export type DragKind = "row" | "col";

export type Label = "w" | "x" | "y" | "z";
export type LabelSequence =
  | `${Label}${Label}${Label}`
  | `${Label}${Label}${Label}${Label}`;

export type GameState = {
  current: Grid;
  target: TargetGrid;
  colLabels: Label[];
  colOrder: number[];
  correctOrder: LabelSequence;
};

export function createInitialState(input: {
  current: Grid;
  target: TargetGrid;
  colLabels?: Label[];
  correctOrder: LabelSequence;
}): GameState {
  const columnCount = input.current[0]?.length ?? 0;
  const defaultLabels: Label[] =
    columnCount === 3 ? ["x", "y", "z"] : columnCount === 4 ? ["w", "x", "y", "z"] : [];
  if (!defaultLabels.length) {
    throw new Error("Column count must be 3 or 4 to derive default labels.");
  }

  const colLabels = input.colLabels ?? defaultLabels;
  if (colLabels.some((label) => label.length !== 1)) {
    throw new Error("Column labels must be single characters.");
  }
  const labelSet = new Set(colLabels);
  if (labelSet.size !== colLabels.length) {
    throw new Error("Column labels must be unique.");
  }
  const expectedOrder = Array.from(input.correctOrder);
  if (expectedOrder.length !== colLabels.length) {
    throw new Error("Correct order length must match column labels.");
  }
  if (expectedOrder.some((label) => !labelSet.has(label))) {
    throw new Error("Correct order must use existing column labels.");
  }
  const colOrder = colLabels.map((_, index) => index);
  return {
    current: input.current.map((row) => [...row]),
    target: input.target.map((row) => [...row]),
    colLabels: [...colLabels],
    colOrder,
    correctOrder: input.correctOrder,
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
