// This code runs when the user submits the form
document.querySelector('form').addEventListener('submit', async function(e) {
   e.preventDefault();

   const formData = new FormData(this);

   try {
      // Send the form data to the server using a POST request
      const response = await fetch('{% url "result" %}', {
         method: 'POST',
         body: formData
      });

      // If the response is not OK, throw an error
      if (!response.ok) {
         throw new Error(response.statusText);
      }

      // Get the response data as a Blob
      const blob = await response.blob();

      // Create an object URL from the Blob
      const imageUrl = URL.createObjectURL(blob);

      // Display the output image on the page
      const imgElement = document.createElement('img');
      imgElement.src = imageUrl;
      document.querySelector('body').appendChild(imgElement);

   } catch (err) {
      // If there is an error, display it on the page
      const errorElement = document.createElement('p');
      errorElement.textContent = err.message;
      document.querySelector('body').appendChild(errorElement);
   }
});
