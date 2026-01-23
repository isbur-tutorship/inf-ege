import { describe, expect, it } from "vitest";
import { mountGame } from "./game";
import { levels } from "../levels/levels";

describe("game scene", () => {
  it("marks column order guess as correct or incorrect", () => {
    const root = document.createElement("main");
    const cleanup = mountGame(root, levels[0], {
      onInstallButton: () => {},
      onBack: () => {},
    });

    const input = root.querySelector<HTMLInputElement>("#guess-input");
    const status = root.querySelector<HTMLDivElement>("#guess-status");
    if (!input || !status) {
      throw new Error("Missing guess elements.");
    }

    input.value = "wxyz";
    input.dispatchEvent(new Event("input", { bubbles: true }));
    expect(status.textContent).toBe("Correct");

    input.value = "wyxz";
    input.dispatchEvent(new Event("input", { bubbles: true }));
    expect(status.textContent).toBe("Not yet");

    cleanup();
  });
});
