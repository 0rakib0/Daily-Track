// function myFunc(e){
//     console.log(e)
// }

document.getElementById('hello').addEventListener('click', (e) => {
    const id = e.currentTarget.getAttribute('data-bank-id'); // Call getAttribute with the attribute name

    console.log(id);
});
