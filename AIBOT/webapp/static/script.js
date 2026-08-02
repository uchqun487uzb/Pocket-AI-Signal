const button = document.getElementById("signalButton");
const pair = document.getElementById("pair");
const signalType = document.getElementById("signalType");
const pairName = document.getElementById("pairName");
const percent = document.querySelector(".percent");
const historyList = document.getElementById("historyList");

document.querySelectorAll(".time").forEach(btn => {
    btn.onclick = () => {
        document.querySelectorAll(".time").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
    };
});

button.onclick = async () => {

    button.innerHTML = "⏳ AI hisoblanmoqda...";

    const timeframe =
        document.querySelector(".time.active").innerText;

    try {

        const res = await fetch(
            `/signal?symbol=${encodeURIComponent(pair.value)}&timeframe=${timeframe}`
        );

        const data = await res.json();

        signalType.innerHTML = data.signal;
        pairName.innerHTML = pair.options[pair.selectedIndex].text;
        percent.innerHTML = data.confidence + "%";

        if (data.signal == "BUY") {
            signalType.style.color = "#00ff66";
        } else if (data.signal == "SELL") {
            signalType.style.color = "#ff4444";
        } else {
            signalType.style.color = "#ffffff";
        }

        const row = document.createElement("p");
        row.innerHTML =
            pair.options[pair.selectedIndex].text +
            " | " +
            timeframe +
            " | " +
            data.signal +
            " | " +
            data.confidence + "%";

        historyList.prepend(row);

    } catch (e) {

        alert("Signalni olishda xatolik!");

        console.log(e);

    }

    button.innerHTML = "🚀 AI SIGNAL";

};
