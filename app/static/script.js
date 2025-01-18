// Sample data for topics and perspectives
const topics = [
    { id: 1, title: "Should AI be used in schools?", perspectives: ["Pro", "Con", "Neutral"] },
    { id: 2, title: "Is climate change the most urgent issue?", perspectives: ["Pro", "Con", "Neutral"] },
    { id: 3, title: "Should the voting age be lowered?", perspectives: ["Pro", "Con", "Neutral"] }

];

// Function to randomly assign a perspective (Pro, Con, Neutral)
function assignPerspective(topicId) {
    const topic = topics.find(t => t.id === topicId);
    const randomIndex = Math.floor(Math.random() * topic.perspectives.length);
    const assignedPerspective = topic.perspectives[randomIndex];
    
    return assignedPerspective;
}

// Event listener for the debate button (on the topic page)
document.addEventListener("DOMContentLoaded", () => {
    const debateButtons = document.querySelectorAll('.debate-btn');
    
    debateButtons.forEach(button => {
        button.addEventListener("click", (e) => {
            const topicId = parseInt(e.target.dataset.topicId);
            const perspective = assignPerspective(topicId);
            
            // Display perspective to the user
            const perspectiveDisplay = document.getElementById('perspective-display');
            perspectiveDisplay.textContent = `You are assigned the perspective: ${perspective}`;
        });
    });
});

// Event listener for submitting an argument
document.getElementById("submit-argument").addEventListener("click", () => {
    const argumentContent = document.getElementById("argument-input").value;
    if (argumentContent) {
        // Here you could send the argument to the backend (e.g., via AJAX)
        alert("Your argument has been submitted!");
    } else {
        alert("Please enter an argument.");
    }
});
