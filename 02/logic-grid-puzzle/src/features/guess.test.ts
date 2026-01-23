import { describe, expect, it } from "vitest";
import { getCorrectOrder, isGuessCorrect, normalizeGuess } from "./guess";
import type { GameState } from "./state";

const baseState: GameState = {
  current: [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
  ],
  target: [
    [1, 0, null, 1],
  ],
  colLabels: ["w", "x", "y", "z"],
  colOrder: [0, 1, 2, 3],
  correctOrder: "wxyz",
};

describe("column order guess", () => {
  it("uses the declared correct order", () => {
    const state: GameState = { ...baseState, correctOrder: "ywzx" };
    expect(getCorrectOrder(state)).toBe("ywzx");
  });

  it("normalizes input and ignores non-letters", () => {
    expect(normalizeGuess(" W-x y z ")).toBe("wxyz");
  });

  it("accepts correct guess", () => {
    const state: GameState = { ...baseState, correctOrder: "xwzy" };
    expect(isGuessCorrect(state, "xwzy")).toBe(true);
  });

  it("rejects incorrect or empty guess", () => {
    const state: GameState = { ...baseState, correctOrder: "xwzy" };
    expect(isGuessCorrect(state, "xwyz")).toBe(false);
    expect(isGuessCorrect(state, "")).toBe(false);
  });
});
