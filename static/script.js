// Toggle button 
function toggleDisease(buttonId, inputId) {
  const button = document.getElementById(buttonId);
  const hiddenInput = document.getElementById(inputId);

  button.classList.toggle('selected');
  if (button.classList.contains('selected')) {
    hiddenInput.value = '1'; // Toggled ON
  } else {
    hiddenInput.value = '0'; // Toggled OFF
  }
}

// Form submission
const predictionForm = document.getElementById('predictionForm');
predictionForm.addEventListener('submit', async function(event) {
  event.preventDefault(); // stop normal form submission

  // Collect form data
  const formData = new FormData(predictionForm);

  try {
    // Send POST request to /predict
    const response = await fetch('/predict', {
      method: 'POST',
      body: formData
    });
    const data = await response.json();
    // Receive data in dictionary form. For example: { "cancer": "High Risk", "diabetes": "Low Risk", ... }

    // Map disease keys to display names
    const diseaseNames = {
      cancer: "Cancer",
      diabetes: "Diabetes",
      heart: "Heart Disease",
      liver: "Liver Disease",
      stroke: "Stroke"
    };

    // Build results in HTML
    let html = '<table style="width:100%;">';
    html += '<tr><th>Disease</th><th>Risk</th></tr>';

    for (const disease in data) {
      // Use existing mapping if it exists
      const displayName = diseaseNames[disease] || disease;

      html += `<tr><td>${displayName}</td><td>${data[disease]}</td></tr>`;
    }
    html += '</table>';

    // Insert into modal
    const modalResults = document.getElementById('modalResults');
    modalResults.innerHTML = html;

    // Show the modal
    const modalOverlay = document.getElementById('modalOverlay');
    modalOverlay.classList.remove('hidden');

  } catch (err) {
    console.error('Error during fetch:', err);
    alert('An error occurred while getting predictions.');
  }
});

// Close modal
const closeModalBtn = document.getElementById('closeModal');
closeModalBtn.addEventListener('click', () => {
  document.getElementById('modalOverlay').classList.add('hidden');
});