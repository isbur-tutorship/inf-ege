import { defineConfig } from "vite";

export default defineConfig({
  root: "src",
  base: "/inf-ege/02/logic-grid-puzzle/",
  build: {
    outDir: "../dist",
    emptyOutDir: true,
  },
  test: {
    environment: "happy-dom",
  },
});
