import type { Grid, TargetGrid } from "../features/state";

export type Level = {
  id: string;
  name: string;
  current: Grid;
  target: TargetGrid;
  colLabels: string[];
};

export const levels: Level[] = [
  {
    id: "default-4x4",
    name: "Default 4x4",
    current: [
      [1, 0, 1, 0],
      [0, 1, 0, 1],
      [1, 0, 0, 1],
      [0, 1, 1, 0],
    ],
    target: [
      [0, 1, 1, 0],
      [1, 0, null, 1],
      [0, 1, 0, 1],
    ],
    colLabels: ["w", "x", "я", "z"],
  },
];
