const form = document.querySelector("form"),
    nextBtn = form.querySelector(".nextBtn"),
    backBtn = form.querySelector(".backBtn"),
    allInput = form.querySelectorAll(".first input"),
    fornecedorSelect = document.getElementById('fornecedor'),
    genesysActions = document.getElementById('genesysActions'),
    avayaActions = document.getElementById('avayaActions');

nextBtn.addEventListener("click", () => {
    allInput.forEach(input => {
        if (input.value != "") {
            form.classList.add('secActive');
        } else {
            form.classList.remove('secActive');
        }
    });
});

backBtn.addEventListener("click", () => form.classList.remove('secActive'));

fornecedorSelect.addEventListener('change', function() {
    var fornecedor = this.value;

    if (fornecedor === 'Genesys') {
        genesysActions.style.display = 'block';
        avayaActions.style.display = 'none';
    } else if (fornecedor === 'Avaya') {
        genesysActions.style.display = 'none';
        avayaActions.style.display = 'block';
    } else {
        genesysActions.style.display = 'none';
        avayaActions.style.display = 'none';
    }
});
