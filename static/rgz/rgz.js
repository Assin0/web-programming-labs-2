function filltovarList() {
    fetch('/rgz/api/tovari/')
    .then(function (data) {
        return data.json();
    })
    .then(function (tovari) {
        let tbody = document.getElementById('tovar-list');
        tbody.innerHTML = '';
        for(let i = 0; i <tovari.length; i++) {
            tr = document.createElement('tr');
            let tdName = document.createElement('td');
            tdName.innerText = tovari[i].name || 'Нет данных';

            let tdCount = document.createElement('td');
            tdCount.innerText = tovari[i].count || 'Нет данных';

            let tdArticle = document.createElement('td');
            tdArticle.innerText = tovari[i].article || 'Нет данных';

            let editButton = document.createElement('button')
            editButton.innerText = 'редактировать';
            editButton.onclick = function() {
                edittovar(i, tovari[i]);
            }

            let delButton = document.createElement('button')
            delButton.innerText = 'удалить';
            delButton.onclick = function() {
                deletetovar(i);
            };

            let tdActions = document.createElement('td');
            tdActions.append(editButton);
            tdActions.append(delButton);
            
            tr.append(tdName);
            tr.append(tdCount);
            tr.append(tdArticle);
            tr.append(tdActions)

            tbody.append(tr);
            }
    })
      
}

function deletetovar(num) {
    if(! confirm('Вы точно хотите удалить данный товар?'))
        return;

    fetch(`/rgz/api/tovari/${num}`, {method: "DELETE"})
    .then(function () {
        filltovarList();
    });
}

function showModal() {
    document.querySelector('div.modal').style.display = 'block';
}
function hideModal() {
    document.querySelector('div.modal').style.display = 'none'
}

function cancel() {
    hideModal();
}

function addtovar() {
    document.getElementById('num').value = '';
    document.getElementById('name').value = '';
    document.getElementById('count').value = '';
    document.getElementById('article').value = '';
    showModal();
}

function sendtovar() {
    const num = document.getElementById('num').value;
    const tovar = {
        name: document.getElementById('name').value,
        count: document.getElementById('count').value,
        article: document.getElementById('article').value,
    }
    const url = `/rgz/api/tovari/${num}`;
    const method = num ? 'PUT' : 'POST';
    fetch(url, {
        method:method,
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(tovar)
    })
    .then(function() {
        filltovarList();
        hideModal();
    });
}


function edittovar(num, tovar) {
    document.getElementById('num').value = num;
    document.getElementById('name').value = tovar.name;
    document.getElementById('count').value = tovar.count;
    document.getElementById('article').value = tovar.article;
    showModal();
}

function fillzakazList() {
    fetch('/rgz/api/zakazi/')
    .then(function (data) {
        return data.json();
    })
    .then(function (zakazi) {
        let tbody = document.getElementById('zakaz-list');
        tbody.innerHTML = '';
        for(let i = 0; i <zakazi.length; i++) {
            tr = document.createElement('tr');
            let tdName = document.createElement('td');
            tdName.innerText = zakazi[i].zname || 'Нет данных';

            let tdStatus = document.createElement('td');
            tdStatus.innerText = zakazi[i].zstatus || 'Нет данных';

            let tdCount = document.createElement('td');
            tdCount.innerText = zakazi[i].zcount || 'Нет данных';

            let tdArticle = document.createElement('td');
            tdArticle.innerText = zakazi[i].zarticle || 'Нет данных';

            let editButton = document.createElement('button')
            editButton.innerText = 'редактировать';
            editButton.onclick = function() {
                editzakaz(i, zakazi[i]);
            }

            let delButton = document.createElement('button')
            delButton.innerText = 'удалить';
            delButton.onclick = function() {
                deletezakaz(i);
            };

            let tdActions = document.createElement('td');
            tdActions.append(editButton);
            tdActions.append(delButton);
            
            tr.append(tdName);
            tr.append(tdCount);
            tr.append(tdArticle);
            tr.append(tdStatus);
            tr.append(tdActions)

            tbody.append(tr);
            }
    })
      
}

function deletezakaz(num) {
    if(! confirm('Вы точно хотите удалить данный заказ?'))
        return;

    fetch(`/rgz/api/zakazi/${num}`, {method: "DELETE"})
    .then(function () {
        fillzakazList();
    });
}

function zshowModal() {
    document.querySelector('div.zmodal').style.display = 'block';
}
function zhideModal() {
    document.querySelector('div.zmodal').style.display = 'none'
}

function zcancel() {
    zhideModal();
}

function addzakaz() {
    document.getElementById('znum').value = '';
    document.getElementById('zname').value = '';
    document.getElementById('zcount').value = '';
    document.getElementById('zarticle').value = '';
    document.getElementById('zstatus').value = '';
    zshowModal();
}

function sendzakaz() {
    const num = document.getElementById('znum').value;
    const zakaz = {
        zname: document.getElementById('zname').value,
        zcount: document.getElementById('zcount').value,
        zarticle: document.getElementById('zarticle').value,
        zstatus: document.getElementById('zstatus').value,
    }
    const url = `/rgz/api/zakazi/${num}`;
    const method = num ? 'PUT' : 'POST';
    fetch(url, {
        method:method,
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(zakaz)
    })
    .then(function() {
        fillzakazList();
        zhideModal();
    });
}


function editzakaz(znum, zakaz) {
    document.getElementById('znum').value = znum;
    document.getElementById('zname').value = zakaz.zname;
    document.getElementById('zcount').value = zakaz.zcount;
    document.getElementById('zarticle').value = zakaz.zarticle;
    document.getElementById('zstatus').value = zakaz.zstatus;
    zshowModal();
}