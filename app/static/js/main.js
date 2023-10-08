let formProduct = document.getElementById("formProduct");
const resultadoElement = document.getElementById("resultado");

/**
 * @param {json} data
 */
function showProduct(data) {
  resultadoElement.innerHTML = "";
  data.forEach((product) => {
    addElement(product);
  });
}

function showError(e) {
  console.error(e);
  resultadoElement.innerHTML = "";
  const pError = document.createElement("p");
  pError.textContent = e;
  resultadoElement.appendChild(pError);
}

formProduct.addEventListener("submit", (e) => {
  e.preventDefault();
  resultadoElement.innerHTML = "";

  let product = encodeURIComponent(document.getElementById("product").value);

  const imgLoad = document.createElement("img");
  imgLoad.classList = "img-load";
  imgLoad.src = "/static/img/loading.gif";
  resultadoElement.appendChild(imgLoad);

  let requestData = {
    product,
  };

  const options = {
    headers: {
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify(requestData),
  };

  fetch("http://127.0.0.1:5000/api", options)
    .then((response) => {
      if (!response.ok) {
        throw new Error("La solicitud no se pudo completar correctamente");
      }
      return response.json();
    })
    .then((data) => {
      console.log(data);
      showProduct(data);
    })
    .catch((e) => showError(e));
});
