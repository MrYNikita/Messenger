(() => {

    // красивые url
    //window.history.pushState(null,null,'/Im');

    let divChat = document.querySelector('#divChat');
    let divContact = document.querySelector('#divContact');
    let divContactList = divContact.querySelector('#divContactList');

    let jectChatActive = {};

    document.querySelector('#buttonContactFind').onclick = async () => {

        fetch(`http://localhost:8000/user/nickname/${document.querySelector('#divContactFind').querySelector('input').value}`, {

            method: 'get',
            headers: { 'Content-type': 'application/json' },

        }).then(async (response) => {

            let arrayUsers = await response.json();

            arrayUsers = arrayUsers.filter((jectUser) => jectUser.id !== sessionStorage.getItem('y_id') - 0);

            while (divContactList.firstChild) divContactList.removeChild(divContactList.firstChild);

            for (jectUser of arrayUsers) createContact(jectUser);

        });

        function createContact(jectUser) {

            let divContactNew = document.createElement('div');
            let imgContactNew = document.createElement('img');
            let pContactCountNew = document.createElement('p');
            let pContactNicknameNew = document.createElement('p');
            let buttonContactWriteNew = document.createElement('button');
            let buttonContactDeleteNew = document.createElement('button');

            pContactCountNew.innerHTML = 0;
            pContactNicknameNew.innerHTML = jectUser.nickname;
            buttonContactWriteNew.innerText = 'Написать';
            buttonContactDeleteNew.innerText = 'Стереть';
            divContactNew.jectUser = jectUser;

            divContactNew.classList.add('divContact');
            divContactNew.append(imgContactNew, pContactNicknameNew, buttonContactWriteNew, buttonContactDeleteNew, pContactCountNew);
            divContactList.appendChild(divContactNew);

            buttonContactWriteNew.onclick = async () => {

                divChat.querySelector('#h2ChatHeader').innerHTML = divContactNew.jectUser.nickname;

                jectChatActive.id_user_two = jectUser.id;

            };

        };

    };
    document.querySelector('#buttonChatActiveSend').onclick = async () => {

        await fetch(`http://localhost:8000/chat_pair/user/id_user_one/${sessionStorage.getItem('y_id') - 0}/id_user_two/${jectUser.id}`, {

            method: 'get',
            headers: { 'Content-type': 'application/json', },

        }).then(async (response) => {

            if (response.status !== 200) {

                console.log({id_user_one: sessionStorage.getItem('y_id') - 0, id_user_two: jectChatActive.id_user_two});

                await fetch('/chat_pair/',{

                    method: 'post',
                    headers: { 'Content-type': 'application/json' },
                    body: JSON.stringify({ id_user_one: sessionStorage.getItem('y_id') - 0, id_user_two: jectChatActive.id_user_two, }),

                }).then(async (response) => jectChatActive = await response.json());

            }
            else {

                jectChatActive = await response.json();

            };

        });

        await fetch('http://localhost:8000/message/', {

            method: 'post',
            headers: { 'Content-type': 'application/json' },
            body: JSON.stringify({
                text: document.querySelector('#inputChatActive').value,
                id_chat: jectChatActive.id,
                id_member: sessionStorage.getItem('y_id') - 0,
            }),

        });

    };

    function createMessage(jectMessage) {



    };

})();