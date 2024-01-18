 // Get all elements with class 'toggleButton'
 let toggleButtons = document.querySelectorAll('.toggleButton');
 let deleteButtons = document.querySelectorAll('.deleteButton')
 let showAll = false
 // Loop through each button and add the click event
 toggleButtons.forEach(function(button) {
     button.addEventListener('click', function() {
         // Get the parent row of the clicked button
         var parentRow = button.parentElement.parentElement;

         // Get the next sibling (which is the 'attendees' row)
         var attendeesRow = parentRow.nextElementSibling;

         // Toggle the display of the 'attendees' row
         if (attendeesRow.style.display === 'none' || attendeesRow.style.display === '') {
             attendeesRow.style.display = 'table-row';
         } else {
             attendeesRow.style.display = 'none';
         }
     });
 });

 document.querySelector('.toggleAllButton').addEventListener('click', function() {
     showAll = !showAll
     attendees = document.querySelectorAll('.attendees')

     attendees.forEach((target) => showAll ? target.style.display = 'table-row' : target.style.display = 'none')
 })

 // This does not do anything
 deleteButtons.forEach((button) => {
     button.addEventListener('click', (e) => {
         // let confirm = window.confirm("Are you sure?")
         let csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

         console.log(csrfToken)
         let url = `del/${e.target.id}`
         let options = {
             method : "DELETE",
             headers: {
                 'Content-Type': 'application/json',
                 'X-CSRFToken' : csrfToken,
             }
         }

         fetch(url, options)
         .then(response => {
             if (response.ok) window.location.href = "";
             else console.error('Error: ', response.statusText)
         })
         .catch(error => {
             // Handle network errors or other issues
             console.error('Fetch error:', error);
         });

         console.log(e.target.id)
     })
 })