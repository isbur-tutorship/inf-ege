type BeforeInstallPromptEvent = Event & {
  prompt: () => Promise<void>;
  userChoice: Promise<{ outcome: "accepted" | "dismissed"; platform: string }>;
};

export function createInstallPrompt() {
  let deferredPrompt: BeforeInstallPromptEvent | null = null;
  let installButton: HTMLButtonElement | null = null;

  const onClick = async () => {
    if (!deferredPrompt || !installButton) return;
    deferredPrompt.prompt();
    await deferredPrompt.userChoice;
    deferredPrompt = null;
    installButton.hidden = true;
  };

  const handleBeforeInstallPrompt = (event: Event) => {
    event.preventDefault();
    deferredPrompt = event as BeforeInstallPromptEvent;
    if (installButton) installButton.hidden = false;
  };

  const handleAppInstalled = () => {
    if (installButton) installButton.hidden = true;
  };

  window.addEventListener("beforeinstallprompt", handleBeforeInstallPrompt);
  window.addEventListener("appinstalled", handleAppInstalled);

  const bindButton = (button: HTMLButtonElement) => {
    if (installButton) {
      installButton.removeEventListener("click", onClick);
    }
    installButton = button;
    installButton.hidden = deferredPrompt ? false : true;
    installButton.addEventListener("click", onClick);
  };

  return { bindButton };
}

export function registerServiceWorker() {
  if ("serviceWorker" in navigator && import.meta.env.PROD) {
    window.addEventListener("load", () => {
      navigator.serviceWorker.register("/sw.js");
    });
  }
}
