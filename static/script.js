/* 
   script.js
   1) Toggle button logic for family/personal history
   2) Intercept form submission -> fetch predictions
   3) Show results in a modal
*/

// ========== 1) Toggle Button Logic ==========
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

// ========== 2) Intercept Form Submission ==========
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
    // data should look like:
    // { "cancer": "High Risk", "diabetes": "Low Risk", ... }

    // Build results HTML
    let html = '<table style="width:100%;">';
    html += '<tr><th>Disease</th><th>Risk</th></tr>';
    for (const disease in data) {
      html += `<tr><td>${disease.toUpperCase()}</td><td>${data[disease]}</td></tr>`;
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

// ========== 3) Close Modal Logic ==========
const closeModalBtn = document.getElementById('closeModal');
closeModalBtn.addEventListener('click', () => {
  document.getElementById('modalOverlay').classList.add('hidden');
});