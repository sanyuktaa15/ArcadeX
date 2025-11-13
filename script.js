// --- Load Pyodide once ---
let pyodideReadyPromise = loadPyodide();

async function runGame(gamePath) {
  let gameKey = "";

  if (gamePath.includes("car")) gameKey = "car";
  else if (gamePath.includes("rain")) gameKey = "rain";
  else if (gamePath.includes("galaxy")) gameKey = "galaxy";
  else if (gamePath.includes("space")) gameKey = "space";

  // Open a popup or new tab to trigger Flask route
  const gameUrl = `http://127.0.0.1:5000/run/${gameKey}`;
  window.open(gameUrl, "_blank", "width=600,height=400");
}

window.addEventListener("DOMContentLoaded", () => {
  const startBtn = document.getElementById("start-btn");
  const startPage = document.getElementById("start-page");
  const gameSection = document.getElementById("game-section");

  // --- Switch from Start to Menu ---
  startBtn.addEventListener("click", () => {
    console.log("✅ Start button clicked!");
    startPage.classList.add("hidden");
    gameSection.classList.remove("hidden");
  });

  // --- When a game card is clicked ---
  document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('click', () => {
      const gameName = card.querySelector('h3').textContent.trim();
      console.log(`🎮 Clicked on: ${gameName}`);

      // Match game titles to Python files
      if (gameName === "Car Racing") {
        runGame("carracing/car_racing.py");
      } else if (gameName === "Galaxy Fighters") {
        runGame("galaxyfighters/galaxy_fighters.py");
      } else if (gameName === "Rain Dodge") {
        runGame("raindodge/rain_dodge.py");
      } else if (gameName === "Space Invaders") {
        runGame("spaceinvaders/space_invaders.py");
      }
    });
  });
});
