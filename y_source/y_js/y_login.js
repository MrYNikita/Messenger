(() => {

    document.querySelector('#inputSend').onclick = () => {

        const form = document.forms[0];

        fetch('http://localhost:8000/user',{

            method: 'post',
            headers: { 'Content-type': 'application/json'},
            body: JSON.stringify({
                'login': form.elements.login.value,
                'nickname': form.elements.nickname.value,
                'password': form.elements.password.value
            })
        
        }).then(async (response) => {

            let jectUser = await response.json();

            sessionStorage.setItem('y_id', jectUser.id);

            if (response.status == 200) location = `http://localhost:8000/user/authorizate/login/${form.elements.login.value}/password/${form.elements.password.value}`;

        });

    };

})();