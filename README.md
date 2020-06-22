# Курсовая работа
Тестирование веб-приложения PrestaShop

## Как это работает?
1. Изменения пушатся в любую ветку, кроме master.
2. Создаётся Pull Request из ветки с изменениями в master.
3. Jenkins получает сигнал о создании реквеста, подхватывает Jenkinsfile из нужной ветки и запускает pipeline.
4. Запускается PrestaShop с базой и Selenoid из Docker-compose.
5. Собирается образ с тестами на основе образа Python.
6. Запускается контейнер из образа с тестами и прогоняет их.
7. По результатам тестов создаётся Allure-отчёт и прикрепляется к отчёту о билде в Jenkins.
8. Останавливается окружение и удаляются тестовые данные.
