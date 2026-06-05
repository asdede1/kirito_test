const form = document.getElementById('add-passenger-form');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Собираем данные из полей, которые мы только что пометили ID в HTML
    const passengerData = {
        main_id: parseInt(document.getElementById('main_id').value),
        name: document.getElementById('name').value,
        ticket: parseInt(document.getElementById('ticket').value),
        place: parseInt(document.getElementById('place').value)
    };

    console.log("Данные подготовлены к отправке:", passengerData);

    try {
        const response = await fetch('http://127.0.0.1:8000/pas', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(passengerData)
        });

        if (response.ok) {
            const result = await response.json();
            // ИСПРАВЛЕНО: добавили обратные кавычки ` ` чтобы работал вывод id
            alert(`Успех! Пассажир сохранен. cl_id: ${result.cl_id}`);
            form.reset(); // Очищаем форму
        } else {
            const error = await response.json();
            alert("Ошибка сервера: " + JSON.stringify(error.detail));
        }
    } catch (err) {
        alert("Не удалось соединиться с сервером. Проверь FastAPI!");
    }
});
