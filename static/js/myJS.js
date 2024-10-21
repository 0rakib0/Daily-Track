function updateUrl(e){
    let deleteObj = document.getElementById('delete-bank')
    deleteObj.setAttribute('href', `/delete-bank/${e}/`)
    console.log("==================")
    console.log(deleteObj.getAttribute('href'))
}

