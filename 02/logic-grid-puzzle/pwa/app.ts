type Grid = number[][];

type BeforeInstallPromptEvent = Event & {
  prompt: () => Promise<void>;
  userChoice: Promise<{ outcome: "accepted" | "dismissed"; platform: string }>;
};

const gridSize = { rows: 4, cols: 4 };
let current: Grid = [
  [1, 0, 1, 0],
  [0, 1, 0, 1],
  [1, 0, 0, 1],
  [0, 1, 1, 0],
];
const target: Grid = [
  [0, 1, 1, 0],
  [1, 0, 0, 1],
  [0, 1, 0, 1],
  [1, 0, 1, 0],
];

const grid = document.querySelector<HTMLDivElement>("#grid");
const targetGrid = document.querySelector<HTMLDivElement>("#target");
const shuffleButton = document.querySelector<HTMLButtonElement>("#shuffle");
const installButton = document.querySelector<HTMLButtonElement>("#install");

if (!grid || !targetGrid || !shuffleButton || !installButton) {
  throw new Error("Missing required elements.");
}

function renderGrid(container: HTMLElement, data: Grid) {
  container.innerHTML = "";
  data.forEach((row) => {
    row.forEach((cell) => {
      const div = document.createElement("div");
      div.className = `cell ${cell ? "cell--on" : ""}`;
      div.textContent = cell ? "1" : "0";
      container.appendChild(div);
    });
  });
}

function shuffleRowsAndCols() {
  const rows = [...current];
  rows.sort(() => Math.random() - 0.5);
  const cols = [...Array(gridSize.cols).keys()];
  cols.sort(() => Math.random() - 0.5);

  current = rows.map((row) => cols.map((index) => row[index]));
}

shuffleButton.addEventListener("click", () => {
  shuffleRowsAndCols();
  renderGrid(grid, current);
});

renderGrid(grid, current);
renderGrid(targetGrid, target);

let deferredPrompt: BeforeInstallPromptEvent | null = null;
window.addEventListener("beforeinstallprompt", (event) => {
  event.preventDefault();
  deferredPrompt = event as BeforeInstallPromptEvent;
  installButton.hidden = false;
});

installButton.addEventListener("click", async () => {
  if (!deferredPrompt) return;
  deferredPrompt.prompt();
  await deferredPrompt.userChoice;
  deferredPrompt = null;
  installButton.hidden = true;
});

window.addEventListener("appinstalled", () => {
  installButton.hidden = true;
});

if ("serviceWorker" in navigator && import.meta.env.PROD) {
  window.addEventListener("load", () => {
    navigator.serviceWorker.register("/sw.js");
  });
}
