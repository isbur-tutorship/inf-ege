import type { GameState } from "./state";

function normalizeGuess(value: string) {
  return value.toLowerCase().replace(/[^a-z]/g, "");
}

export function createGuessController(
  state: GameState,
  input: HTMLInputElement,
  status: HTMLDivElement
) {
  const update = () => {
    const normalized = normalizeGuess(input.value);
    const expected = state.colOrder.map((index) => state.colLabels[index]).join("");
    if (!normalized) {
      status.textContent = "";
      status.classList.remove("guess__status--win");
      return;
    }

    if (normalized === expected) {
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
