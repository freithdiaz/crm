document.addEventListener("DOMContentLoaded", function() {
    loadDeals();
});

async function loadDeals() {
    try {
        const response = await fetch("/api/deals/");
        const deals = await response.json();
        renderDeals(deals);
    } catch (error) {
        console.error("Error cargando tratos:", error);
    }
}

function renderDeals(deals) {
    // Clear columns
    const columns = ["Prospecto", "Contactado", "Calificado", "Propuesta", "Ganado"];
    columns.forEach(col => {
        document.getElementById(`body-${col}`).innerHTML = "";
        document.getElementById(`count-${col}`).innerText = "0";
    });

    const counts = { Prospecto: 0, Contactado: 0, Calificado: 0, Propuesta: 0, Ganado: 0 };

    deals.forEach(deal => {
        const colBody = document.getElementById(`body-${deal.stage}`);
        if(!colBody) return; // Ignore if stage isn't mapped to column

        counts[deal.stage]++;
        const card = document.createElement("div");
        card.className = "deal-card glass hover-glow";
        card.id = `deal-${deal.id}`;
        card.draggable = true;
        card.ondragstart = drag;

        card.innerHTML = `
            <div class="deal-card-header">
                <h6>${deal.title}</h6>
            </div>
            <div class="deal-card-body">
                <span class="amount">$${deal.amount.toLocaleString()}</span>
                <div class="probability-bar">
                    <div class="progress" style="width: ${deal.probability}%"></div>
                </div>
            </div>
        `;
        colBody.appendChild(card);
    });

    // Update counts
    columns.forEach(col => {
        document.getElementById(`count-${col}`).innerText = counts[col];
    });
}

// Drag & Drop Handlers
function drag(event) {
    event.dataTransfer.setData("text", event.target.id);
}

window.allowDrop = function(event) {
    event.preventDefault();
}

window.drop = async function(event) {
    event.preventDefault();
    const cardId = event.dataTransfer.getData("text");
    const targetCol = event.currentTarget.id; // Get the Column ID (Prospecto, etc)
    const dealId = cardId.replace("deal-", "");

    const colBody = document.getElementById(`body-${targetCol}`);
    const card = document.getElementById(cardId);

    if (colBody && card) {
         colBody.appendChild(card); // Move Visually
         await updateDealStage(dealId, targetCol);
         loadDeals(); // Refresh to update counts correctly if needed
    }
}

async function updateDealStage(dealId, newStage) {
    try {
        await fetch(`/api/deals/${dealId}/stage`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ stage: newStage })
        });
    } catch (error) {
        console.error("Error actualizando etapa:", error);
    }
}
