(() => {

    //window.history.pushState(null,null,'/Im');

    document.querySelector('#buttonContactFind').onclick = () => {

        fetch(`http://localhost:8000/users/${document.querySelector('#divContactFind').querySelector('input').value}`,{

            method: 'get',
            headers: { 'Content-type': 'application/json'},
        
        }).then(async (response) => {

            let res = await response.json();

        });

    };

})();