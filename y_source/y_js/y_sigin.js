(() => {

    document.querySelector('#inputIn').onclick = () => {

        const form = document.forms[0];

        fetch(`http://localhost:8000/user/login/${form.elements.login.value}/password/${form.elements.password.value}`,{

            method: 'get',
            headers: { 'Content-type': 'text/html'},
        
        }).then(async (response) => {

            let jectUser = await response.json();

            sessionStorage.setItem('y_id', jectUser.id);

            location = `http://localhost:8000/user/authorizate/login/${form.elements.login.value}/password/${form.elements.password.value}`;

        }).catch(async (error) => {

        });

    };

})();