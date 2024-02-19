// crypto/static/crypto/crypto_list.js

document.addEventListener('DOMContentLoaded', function() {
    setInterval(updatePrices, 5000);  // Update prices every 5 seconds

    function updatePrices() {
        fetch('/crypto-list/')
            .then(response => response.json())
            .then(data => {
                const cryptocurrencies = data.cryptocurrencies;

                cryptocurrencies.forEach(crypto => {
                    const element = document.getElementById(`price-${crypto.id}`);
                    if (element) {
                        element.innerText = `$${crypto.quote.USD.price.toFixed(2)}`;
                    }
                });
            })
            .catch(error => console.error('Error fetching data:', error));
    }
});
