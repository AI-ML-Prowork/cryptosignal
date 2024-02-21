document.addEventListener("DOMContentLoaded", function () {
    // Fetch cryptocurrency data from the CoinGecko API
    fetch("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1&sparkline=false")
        .then(response => response.json())
        .then(data => {
            // Populate the cryptocurrency table
            populateCryptoTable(data);
        })
        .catch(error => console.error("Error fetching cryptocurrency data:", error));

    function populateCryptoTable(cryptoData) {
        const tableContainer = document.getElementById("crypto-table");

        // Create a table element
        const table = document.createElement("table");
        table.classList.add("crypto-table");

        // Create table header
        const headerRow = table.insertRow(0);
        const headers = ["Name", "Symbol", "Price", "24h Change"];
        headers.forEach(headerText => {
            const th = document.createElement("th");
            th.textContent = headerText;
            headerRow.appendChild(th);
        });

        // Create table rows with cryptocurrency data
        cryptoData.forEach(coin => {
            const row = table.insertRow();
            const cellNames = ["name", "symbol", "current_price", "price_change_percentage_24h"];

            cellNames.forEach(cellName => {
                const cell = row.insertCell();
                cell.textContent = coin[cellName];

                // Apply dark theme and color for price change
                if (cellName === "price_change_percentage_24h") {
                    const priceChange = parseFloat(coin[cellName]);
                    cell.classList.add(priceChange >= 0 ? "positive" : "negative");
                }
            });
        });

        // Append the table to the container
        tableContainer.appendChild(table);
    }
});
