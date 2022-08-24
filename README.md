# Installation

`git clone https://github.com/XCV0/AircraftsNotifications`

# Arguments

- Имя программы которое вы используете(Поддержка: dump1090, virtualradar)
- Тип уведомления(Поддержка: звук, текст в консоли)
- IP Адрес на котором открыта прогрмма(Обычно это 127.0.0.1, указывать обязательно)
- Порт (Указывать обязательно, если это virtualradar указать любое значение)

# Launch example

`python main.py dump1090 sound 127.0.0.1 8080`

`python main.py virtualradar 127.0.0.1 0`
