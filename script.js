// When any game card is clicked, run its corresponding Python game
document.querySelectorAll('.card').forEach(card => {
  card.addEventListener('click', () => {

    // Get the game name from the <h3> tag, convert to lowercase and use hyphen
    const gameName = card.querySelector('h3').textContent.toLowerCase().replace(' ', '-');
    
    // Just for debugging in browser console
    console.log(`Clicked on: ${gameName}`);

    // Send request to Flask backend to run the game
    fetch(`/run/${gameName}`)
      .then(response => response.text())
      .then(msg => {
        console.log(msg);  // log backend response
        alert(msg);        // show message on screen
      })
      .catch(err => console.error('Error:', err));
  });
});
