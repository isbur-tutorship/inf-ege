import type { GameState } from "./state";

export function normalizeGuess(value: string) {
  return value.toLowerCase().replace(/[^a-z]/g, "");
}

export function getCorrectOrder(state: GameState) {
  return normalizeGuess(state.correctOrder);
}

export function isGuessCorrect(state: GameState, value: string) {
  const normalized = normalizeGuess(value);
  if (!normalized) return false;
  return normalized === getCorrectOrder(state);
}

export function createGuessController(
  state: GameState,
  input: HTMLInputElement,
  status: HTMLDivElement
) {
  const update = () => {
    const normalized = normalizeGuess(input.value);
    if (!normalized) {
      status.textContent = "";
      status.classList.remove("guess__status--win");
      return;
    }

    if (isGuessCorrect(state, input.value)) {
      status.textContent = "Correct";
      status.classList.add("guess__status--win");
    } else {
      status.textContent = "Not yet";
      status.classList.remove("guess__status--win");
    }
  };

  input.addEventListener("input", update);

  return { update };
}
