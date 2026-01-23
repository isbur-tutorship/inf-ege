import { attachHeaderDrag } from "../features/drag";
import { createGuessController } from "../features/guess";
import { evaluateMatchState } from "../features/match";
import { renderGrid } from "../features/renderGrid";
import { createInitialState, shuffleRowsAndCols } from "../features/state";
import type { Level } from "../levels/levels";

type GameHandlers = {
  onInstallButton: (button: HTMLButtonElement) => void;
  onBack: () => void;
};

export function mountGame(root: HTMLElement, level: Level, handlers: GameHandlers) {
  root.innerHTML = `
    <header class="app__header">
      <div class="app__title">
        <h1>Logic Grid Puzzle</h1>
        <button id="back" class="button--ghost" type="button">Back</button>
      </div>
      <p>Drag rows/columns to match the target pattern.</p>
    </header>
    <section class="board">
      <div class="board__label">Current</div>
      <div id="grid" class="grid" aria-label="Current grid"></div>
    </section>
    <section class="board">
      <div class="board__label">Target</div>
      <div id="target" class="grid grid--target" aria-label="Target grid"></div>
    </section>
    <div class="actions">
      <button id="shuffle">Shuffle</button>
      <button id="install" class="button--install" hidden>Install</button>
    </div>
    <section class="guess">
      <label for="guess-input">Column order guess (w,x,y,z)</label>
      <div class="guess__row">
        <input
          id="guess-input"
          type="text"
          autocomplete="off"
          placeholder="e.g. wxyz"
        />
        <div id="guess-status" class="guess__status" aria-live="polite"></div>
      </div>
    </section>
  `;

  const grid = root.querySelector<HTMLDivElement>("#grid");
  const targetGrid = root.querySelector<HTMLDivElement>("#target");
  const shuffleButton = root.querySelector<HTMLButtonElement>("#shuffle");
  const installButton = root.querySelector<HTMLButtonElement>("#install");
  const backButton = root.querySelector<HTMLButtonElement>("#back");
  const guessInput = root.querySelector<HTMLInputElement>("#guess-input");
  const guessStatus = root.querySelector<HTMLDivElement>("#guess-status");

  if (
    !grid ||
    !targetGrid ||
    !shuffleButton ||
    !installButton ||
    !backButton ||
    !guessInput ||
    !guessStatus
  ) {
    throw new Error("Missing required elements.");
  }

  const state = createInitialState(level);
  const guessController = createGuessController(state, guessInput, guessStatus);
  let lastMatch = false;

  const applyMatchState = (isMatch: boolean) => {
    grid.classList.toggle("grid--match", isMatch);
    if (isMatch && !lastMatch) {
      grid.classList.add("grid--match-pulse");
      window.setTimeout(() => grid.classList.remove("grid--match-pulse"), 700);
    }
    lastMatch = isMatch;
  };

  const renderCurrentGrid = () => {
    const match = evaluateMatchState(state);
    renderGrid(grid, state.current, {
      showHeaders: true,
      colLabels: state.colLabels,
      columnOrder: state.colOrder,
      dimRows: match.dimRows,
      headerHandler: (element, kind, index) => {
        attachHeaderDrag(element, kind, index, state, () => {
          renderCurrentGrid();
          guessController.update();
        });
      },
    });
    applyMatchState(match.isMatch);
  };

  const onShuffle = () => {
    shuffleRowsAndCols(state);
    renderCurrentGrid();
    guessController.update();
  };

  shuffleButton.addEventListener("click", onShuffle);
  backButton.addEventListener("click", handlers.onBack);

  renderCurrentGrid();
  renderGrid(targetGrid, state.target, { showHeaders: false });
  guessController.update();
  handlers.onInstallButton(installButton);

  return () => {
    shuffleButton.removeEventListener("click", onShuffle);
    backButton.removeEventListener("click", handlers.onBack);
  };
}
