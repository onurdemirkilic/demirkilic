document.querySelector('form').addEventListener('submit', function(event) {
  event.preventDefault(); // Sayfanın yeniden yüklenmesini engelle

  const trackingNumber = document.getElementById('trackingNumber').value;
  const resultContainer = document.getElementById('result');
  const loading = document.getElementById('loading');
  const status = document.getElementById('status');
  const statusText = document.getElementById('statusText');

  // Kargo durumunu burada sorgula ve sonucu resultContainer içine ekle
  // Bu örnekte sadece bir bekleme animasyonu gösterip, ardından durumu gösteriyoruz
  resultContainer.classList.remove('hidden');
  loading.classList.remove('hidden');

  setTimeout(function() {
    loading.classList.add('hidden');
    status.classList.remove('hidden');
    statusText.textContent = 'Takip numarası: ' + trackingNumber;
  }, 2000);
});