(() => {

    // красивые url
    //window.history.pushState(null,null,'/Im');

    let divContact = document.querySelector('#divContact');
    let divContactList = divContact.querySelector('#divContactList')

    document.querySelector('#buttonContactFind').onclick = () => {

        fetch(`http://localhost:8000/user/nickname/${document.querySelector('#divContactFind').querySelector('input').value}`,{

            method: 'get',
            headers: { 'Content-type': 'application/json'},
        
        }).then(async (response) => {

            let arrayUsers = await response.json();

            arrayUsers = arrayUsers.filter((jectUser) => jectUser.id !== sessionStorage.getItem('y_id') - 0);

            while (divContactList.firstChild) divContactList.removeChild(divContactList.firstChild);

            for (jectUser of arrayUsers) createContact(jectUser);

        });

        function createContact(jectUser) {

            let pContactNew = document.createElement('p');
            let divContactNew = document.createElement('div');
            let imgContactNew = document.createElement('img');
            let buttonContactWriteNew = document.createElement('button');
            let buttonContactDeleteNew = document.createElement('button');

            pContactNew.innerHTML = jectUser.nickname;
            buttonContactWriteNew.innerText = 'Написать';
            buttonContactDeleteNew.innerText = 'Стереть';

            divContactNew.classList.add('divContact');
            divContactNew.append(imgContactNew,pContactNew,buttonContactWriteNew,buttonContactDeleteNew);
            divContactList.appendChild(divContactNew);

        };

    };

})();