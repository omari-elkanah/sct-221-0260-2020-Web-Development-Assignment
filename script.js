document.addEventListener("DOMContentLoaded", function() {
    function greetUser() {
        const name = document.getElementById("nameInput").value;
        const greeting = document.getElementById("greeting");
        greeting.textContent = `Hello, ${name}!`;
    }
  
    const greetButton = document.getElementById("greetButton");
    greetButton.addEventListener("click",greetUser);
});