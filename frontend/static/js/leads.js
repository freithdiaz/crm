document.addEventListener("DOMContentLoaded", function() {
    const tableBody = document.getElementById("leadsTableBody");
    const modal = document.getElementById("aiModal");
    const modalText = document.getElementById("aiSummaryText");
    const closeBtn = document.querySelector(".close-modal");

    // Fetch leads
    async function loadLeads() {
        try {
            const response = await fetch("/api/leads/");
            const leads = await response.json();
            renderTable(leads);
        } catch (error) {
            console.error("Error cargando leads:", error);
            tableBody.innerHTML = `<tr><td colspan="6" style="color:red">Error cargando datos.</td></tr>`;
        }
    }

    function renderTable(leads) {
        if (leads.length === 0) {
            tableBody.innerHTML = `<tr><td colspan="6" style="text-align:center">No hay leads registrados.</td></tr>`;
            return;
        }

        tableBody.innerHTML = leads.map(lead => `
            <tr>
                <td><strong>${lead.name}</strong></td>
                <td>${lead.company}</td>
                <td>${lead.email}</td>
                <td><span class="status-badge ${lead.status.toLowerCase()}">${lead.status}</span></td>
                <td>$${lead.value.toLocaleString()}</td>
                <td>
                    <button class="action-btn ai" onclick="viewSummary(${lead.id})"><i class="fa-solid fa-bolt"></i> AI</button>
                    <button class="action-btn edit"><i class="fa-solid fa-pencil"></i></button>
                </td>
            </tr>
        `).join("");
    }

    // View AI Summary Window
    window.viewSummary = async function(id) {
        modalText.innerHTML = "Generando resumen inteligente...";
        modal.style.display = "block";
        try {
            const response = await fetch(`/api/leads/${id}/ai-summary`);
            const data = await response.json();
            modalText.innerHTML = data.summary.replace(/\n/g, "<br>");
        } catch (error) {
            modalText.innerHTML = "Error al generar resumen.";
        }
    }

    // Close Modal
    if(closeBtn) {
        closeBtn.onclick = () => modal.style.display = "none";
    }
    window.onclick = (e) => { if (e.target === modal) modal.style.display = "none"; }

    loadLeads();
});
