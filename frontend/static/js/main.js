document.addEventListener("DOMContentLoaded", function() {
    const ctx = document.getElementById('salesChart').getContext('2d');
    
    // Gradient for chart
    const gradient = ctx.createLinearGradient(0, 0, 0, 200);
    gradient.addColorStop(0, 'rgba(138, 43, 226, 0.4)');
    gradient.addColorStop(1, 'rgba(138, 43, 226, 0.0)');

    const salesChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
            datasets: [{
                label: 'Ventas ($)',
                data: [12000, 19000, 30000, 25000, 42000, 50000],
                borderColor: '#8a2be2',
                borderWidth: 3,
                backgroundColor: gradient,
                fill: true,
                tension: 0.4,
                pointBackgroundColor: '#00d2ff',
                pointBorderColor: '#fff',
                pointHoverRadius: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false }
            },
            scales: {
                y: {
                    grid: { color: 'rgba(255, 255, 255, 0.05)' },
                    ticks: { color: '#94a3b8' }
                },
                x: {
                    grid: { display: false },
                    ticks: { color: '#94a3b8' }
                }
            }
        }
    });
});
