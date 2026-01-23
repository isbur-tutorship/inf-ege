import type { DragKind, GameState } from "./state";
import { swapCols, swapRows } from "./state";

let dragSource: { kind: DragKind; index: number } | null = null;
let dragImage: HTMLElement | null = null;

function buildDragImage(state: GameState, kind: DragKind, index: number) {
  const ghost = document.createElement("div");
  ghost.className = `drag-ghost drag-ghost--${kind}`;

  if (kind === "row") {
    state.current[index].forEach((cell) => {
      const div = document.createElement("div");
      div.className = `cell ${cell ? "cell--on" : ""}`;
      div.textContent = cell ? "1" : "0";
      ghost.appendChild(div);
    });
  } else {
    state.current.forEach((row) => {
      const cell = row[index];
      const div = document.createElement("div");
      div.className = `cell ${cell ? "cell--on" : ""}`;
      div.textContent = cell ? "1" : "0";
      ghost.appendChild(div);
    });
  }

  document.body.appendChild(ghost);
  return ghost;
}

export function attachHeaderDrag(
  element: HTMLElement,
  kind: DragKind,
  index: number,
  state: GameState,
  onSwap: () => void
) {
  element.draggable = true;

  element.addEventListener("dragstart", (event) => {
    dragSource = { kind, index };
    element.classList.add("header--dragging");
    if (dragImage) {
      dragImage.remove();
      dragImage = null;
    }
    dragImage = buildDragImage(state, kind, index);
    if (event.dataTransfer) {
      event.dataTransfer.effectAllowed = "move";
      event.dataTransfer.setData("text/plain", `${kind}:${index}`);
      if (dragImage) {
        event.dataTransfer.setDragImage(
          dragImage,
          Math.floor(dragImage.offsetWidth / 2),
          Math.floor(dragImage.offsetHeight / 2)
        );
      }
    }
  });

  element.addEventListener("dragend", () => {
    dragSource = null;
    element.classList.remove("header--dragging");
    if (dragImage) {
      dragImage.remove();
      dragImage = null;
    }
  });

  element.addEventListener("dragover", (event) => {
    if (!dragSource || dragSource.kind !== kind) return;
    event.preventDefault();
    if (event.dataTransfer) event.dataTransfer.dropEffect = "move";
  });

  element.addEventListener("drop", (event) => {
    event.preventDefault();
    if (!dragSource || dragSource.kind !== kind || dragSource.index === index) return;
    if (kind === "row") {
      swapRows(state, dragSource.index, index);
    } else {
      swapCols(state, dragSource.index, index);
    }
    onSwap();
  });
}
