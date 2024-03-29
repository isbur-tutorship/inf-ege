Первоисточник: https://core.telegram.org/bots/tutorial

# Получи свой токен бота

В нашем случае, токен - это особая последовательность символов, что-то вроде пароля от бота, который позволяет платформе Telegram понять, что твоя программа отвечает за поведение конкретного бота. Каждый бот имеет свой уникальный токен, который всегда можно получить или перевыпустить через бота @BotFather.

Чтобы получить токен, откройте диалог с @BotFather, введите команду /newbot и следуйте предлагаемым шагам до самого конца.

Тебе будет предложено:

 - Выбрать **name** — отображаемое имя бота, может быть любым (в разумных пределах)
 - Выбрать **username** — системный индентификатор бота, должен быть уникальным, нельзя поменять, кроме как создав нового бота. Должно заканчиваться на "bot" и состоять только из латинских символов, цифр и нижних подчёркиваний.

Полученный токен будет похож на это:
```
4839574812:AAFD39kkdpWt3ywyRZergyOLMaJhac60qc
```

> Убедись, что хранишь токен в надёжном месте, относись к нему как к паролю и не делись ни с кем.

# Зарегистрируйся на ![Replit'е](https://replit.com)
Для начала надо зайти на главную страницу ![Replit'а](https://replit.com). В верхнем правом углу будет кнопка "Sign Up" (зарегистрироваться).

![](signup.png)

Можно создать со своими собственными именем пользователя (username), адресом почты (email) и паролем (password). Или можно использовать свой готовый аккаунт Google, Facebook или GitHub.

![](signup2.png)

Как только ты залогинишься, увидишь домашнюю страницу пользователя:

![](signup3.png)

# Создать репл

Чтобы создать репл (проект), зайди на домашнюю страницу пользователя ([https://replit.com/~]) и нажми кнопку "Сreate Repl" в боковом меню.

![](create-repl.gif)

Выбери имя репла и шаблон. В нашем случае это будет Python.

![](create-repl2.gif)

# Запуск репла

В принципе, ты уже можешь писать код. Скопируй следующую строку и вставь в окно редактора кода:
```python
print("Информатика — топчик!")
```
Нажми большую зелёную кнопку "Run" — вуаля! В правом окне отображается результат работы программы.

# Настройка репла

Но мы пришли сюда за чем-то большим: хотим написать своего Telegram-бота! Для этого голого Питона будет недостаточно, нужно кое-что установить. Делается это просто: заходим во вкладку "Shell" и вставляем в поле для в ввода следующее:
```
pip install python-telegram-bot --upgrade
```
Нажми клавишу Enter на клавиатуре!

Так мы устанавливаем дополнительные возможности для Питона. 

# Начинаем писать бота


