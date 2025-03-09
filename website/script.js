/* 
   script.js
   Handles the toggle button logic for Family and Personal History.
   When clicked, we toggle the 'selected' class to show a color change.
   The button now only scales on hover (via CSS).
   We also update the hidden input value (0 or 1) accordingly.
*/

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