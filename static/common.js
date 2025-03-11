const update = id => {
    const url = `/update-to-complate/${id}/`;  // URL with the ID inserted

    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    })
        .then(response => {
            // Check if the response status is OK (status code 200)
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            // return response.json();  // Parse the response body as JSON if status is OK
            location.reload();
        })
        .then(data => {
            console.log(data);
            // Do something with the response data, such as updating the UI
        })
        .catch(error => {
            console.error('Error:', error);
        });
};

const taskUpdate = id => {
    const url = `/task-update-to-complate/${id}/`;  // URL with the ID inserted

    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    })
        .then(response => {
            // Check if the response status is OK (status code 200)
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            // return response.json();  // Parse the response body as JSON if status is OK
            location.reload();
        })
        .then(data => {
            console.log(data);
            // Do something with the response data, such as updating the UI
        })
        .catch(error => {
            console.error('Error:', error);
        });
};






const deleteConfirmation = (id, item) => {
    let deleteObj = document.getElementById('delete')
    if (item === 'budget') {
        deleteObj.setAttribute('href', `/delete-budget/${id}/`)
    } else if (item === 'mail') {
        deleteObj.setAttribute('href', `/delete-mail/${id}/`)
    }else if(item === 'budget_cat'){
        deleteObj.setAttribute('href', `/delete-budget-category/${id}/`)
    }else if(item === 'note'){
        deleteObj.setAttribute('href', `/delete-note/${id}/`)
    }else if(item === 'task'){
        deleteObj.setAttribute('href', `/delete-task/${id}/`)
    }
}