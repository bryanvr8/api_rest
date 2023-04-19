// async function logJSONData() {
//     const response = await fetch("http://127.0.0.1:8000/api/?format=json");
//     const jsonData = await response.json();
//     console.log(jsonData);
//   }

let tableCli = document.querySelector('#clientes')

fetch("http://127.0.0.1:8000/api").then((resp) => {
    resp.json().then((todos) => {
        todos.map((dados_cliente) => {
            tableCli.innerHTML += `<td>${dados_cliente.id}</td>
                                   <td> ${dados_cliente.cliente}</td>
                                   <td>${dados_cliente.codigo}</td>
                                   <td>${dados_cliente.descricao}</td>`
        })
    })
})