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


const confirmDelete = id =>{
    let deleteObj = document.getElementById('category_delete')
    deleteObj.setAttribute('href', `/delete-budget-category/${id}/`)
}