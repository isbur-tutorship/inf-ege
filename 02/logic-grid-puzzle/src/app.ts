import "./styles.css";
import { createInstallPrompt, registerServiceWorker } from "./features/pwa";
import { levels } from "./levels/levels";
import { mountGame } from "./scenes/game";
import { mountMenu } from "./scenes/menu";

const root = document.querySelector<HTMLElement>("#app");
if (!root) {
  throw new Error("Missing app root.");
}

const installPrompt = createInstallPrompt();
let cleanup: (() => void) | null = null;

const showMenu = () => {
  if (cleanup) cleanup();
  cleanup = mountMenu(root, levels, {
    onStart: (level) => showGame(level),
  });
};

const showGame = (level: (typeof levels)[number]) => {
  if (cleanup) cleanup();
  cleanup = mountGame(root, level, {
    onInstallButton: (button) => installPrompt.bindButton(button),
    onBack: () => showMenu(),
  });
};

showMenu();
registerServiceWorker();
