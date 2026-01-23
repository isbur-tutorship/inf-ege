import type { Grid, TargetGrid, Label, LabelSequence } from "../features/state";

export type Level = {
  id: string;
  name: string;
  current: Grid;
  target: TargetGrid;
  colLabels?: Label[];
  correctOrder: LabelSequence;
  remark?: string;
};

export const levels: Level[] = [
  {
    id: "reshuege-15097",
    name: "01",
    current: [
      [1, 0, 0],
      [1, 1, 0]
    ],
    target: [
      [0, 0, null],
      [1, null, null] 
    ],
    correctOrder: "yzx"
  },  
  {
    id: "reshuege-19051",
    name: "02",
    current: [
      [1, 0, 0, 1],
      [1, 0, 1, 1],
      [1, 1, 1, 0]
    ],
    target: [
      [0, 1, 1, 0],
      [0, null, null, null],
      [null, 1, 0, 1] 
    ],
    correctOrder: "xwzy"
  },
];
