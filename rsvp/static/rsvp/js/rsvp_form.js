let num_attendees = 0
function handleKeyDown(event){
    if (event.key === 'Enter'){
        renderAttendeeInputs(event.target.value)
        event.preventDefault()
    }
}
function renderAttendeeInputs(){
    num_attendees++
    const container = document.querySelector('.attendee_container')
    document.querySelector("#hidden_num_attendees").value = num_attendees
    // Create and append a new input
    let div = document.createElement('div');
        div.classList.add("attendee_input")
        div.classList.add("input")

        let input = document.createElement('input');
        input.type = 'text';  
        input.name = 'attendee_' + num_attendees;
        input.placeholder = "Guest's name";
        input.required = true
        let button = document.createElement('button');
        button.type = 'button'
        button.innerHTML = 'Delete'
        button.onclick = (e) => {
            num_attendees--
            document.querySelector("#hidden_num_attendees").value = num_attendees
            div.remove()
        }
        div.appendChild(input)
        div.appendChild(button)
        container.appendChild(div);
    }