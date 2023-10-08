function addElement({ asin, image, name, price, url }) {
  const resultadoElement = document.getElementById("resultado");
  const cartProduct = document.createElement("a");
  const nameProduct = document.createElement("p");
  nameProduct.textContent = name;

  const imageProduct = document.createElement("img");
  imageProduct.classList.add("img-product");
  imageProduct.src = image;
  const priceProduct = document.createElement("div");
  priceProduct.classList = "price";
  priceProduct.textContent = price ? `US$${price}` : "No tiene precio";

  const priceOverlay = document.createElement("div");
  priceOverlay.classList = "price-overlay";
  priceOverlay.appendChild(imageProduct);
  priceOverlay.appendChild(priceProduct);

  cartProduct.classList.add("cart");
  cartProduct.href = url;
  cartProduct.target = "_blank";
  cartProduct.appendChild(nameProduct);
  cartProduct.appendChild(priceOverlay);

  resultadoElement.appendChild(cartProduct);
}
