import type { Level } from "../levels/levels";

type MenuHandlers = {
  onStart: (level: Level) => void;
};

export function mountMenu(root: HTMLElement, levels: Level[], handlers: MenuHandlers) {
  const levelButtons = levels
    .map(
      (level) =>
        `<button class="menu__level" data-level="${level.id}">${level.name}</button>`
    )
    .join("");

  root.innerHTML = `
    <header class="app__header">
      <h1>Logic Grid Puzzle</h1>
      <p>Arrange rows and columns to match the target pattern.</p>
    </header>
    <section class="menu">
      <div class="menu__card">
        <h2>Pick a level</h2>
        <p>Start with the default 4x4 and guess the column order.</p>
        <div class="menu__levels">${levelButtons}</div>
      </div>
    </section>
  `;

  const buttons = Array.from(root.querySelectorAll<HTMLButtonElement>(".menu__level"));
  if (!buttons.length) {
    throw new Error("Missing level buttons.");
  }

  const onClick = (event: Event) => {
    const target = event.currentTarget as HTMLButtonElement;
    const id = target.dataset.level;
    const selected = levels.find((level) => level.id === id);
    if (selected) handlers.onStart(selected);
  };

  buttons.forEach((button) => button.addEventListener("click", onClick));

  return () => {
    buttons.forEach((button) => button.removeEventListener("click", onClick));
  };
}
