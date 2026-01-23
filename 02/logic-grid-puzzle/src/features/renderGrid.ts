import type { DragKind, TargetCell } from "./state";

type RenderOptions = {
  showHeaders?: boolean;
  colLabels?: string[];
  columnOrder?: number[];
  dimRows?: Set<number>;
  headerHandler?: (element: HTMLElement, kind: DragKind, index: number) => void;
};

export function renderGrid(
  container: HTMLElement,
  data: Array<TargetCell[]>,
  options: RenderOptions = {}
) {
  const showHeaders = options.showHeaders ?? true;
  const colLabels = options.colLabels ?? [];
  const columnOrder = options.columnOrder ?? colLabels.map((_, index) => index);
  const dimmedRows = options.dimRows ?? new Set<number>();
  const rows = data.length;
  const cols = data[0]?.length ?? 0;
  container.innerHTML = "";
  const headerOffset = showHeaders ? 1 : 0;
  container.style.setProperty("--grid-cols", String(cols + headerOffset));
  container.style.setProperty("--grid-rows", String(rows + headerOffset));

  const startIndex = showHeaders ? -1 : 0;
  for (let rowIndex = startIndex; rowIndex < rows; rowIndex += 1) {
    for (let colIndex = startIndex; colIndex < cols; colIndex += 1) {
      if (showHeaders && rowIndex === -1 && colIndex === -1) {
        const corner = document.createElement("div");
        corner.className = "corner";
        container.appendChild(corner);
        continue;
      }

      if (showHeaders && rowIndex === -1) {
        const header = document.createElement("div");
        header.className = "header header--col";
        const labelIndex = columnOrder[colIndex] ?? colIndex;
        header.textContent = colLabels[labelIndex] ?? String(labelIndex + 1);
        if (options.headerHandler) {
          options.headerHandler(header, "col", colIndex);
        }
        container.appendChild(header);
        continue;
      }

      if (showHeaders && colIndex === -1) {
        const header = document.createElement("div");
        header.className = "header header--row";
        if (dimmedRows.has(rowIndex)) header.classList.add("header--dim");
        header.textContent = "";
        if (options.headerHandler) {
          options.headerHandler(header, "row", rowIndex);
        }
        container.appendChild(header);
        continue;
      }

      const cell = data[rowIndex][colIndex];
      const div = document.createElement("div");
      const dimClass = dimmedRows.has(rowIndex) ? " cell--dim" : "";
      if (cell === null) {
        div.className = `cell cell--blank${dimClass}`;
        div.textContent = "";
      } else {
        div.className = `cell ${cell ? "cell--on" : ""}${dimClass}`;
        div.textContent = cell ? "1" : "0";
      }
      container.appendChild(div);
    }
  }
}
