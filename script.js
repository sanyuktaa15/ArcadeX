// When "PRESS START" is clicked, show the game section
document.getElementById("start-btn").addEventListener("click", function() {
  document.getElementById("start-page").classList.add("hidden");
  document.getElementById("game-section").classList.remove("hidden");
});
